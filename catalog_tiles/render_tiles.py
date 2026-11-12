#!/usr/bin/env python3
"""Брендированные плитки отелей для каталога Meta в стиле карточки приложения Livin.

Читает CSV-фид отелей Meta, для каждого отеля рисует квадратную плитку 1080x1080
(фото, звёздность, тип и город, название, цена «от») и пишет новый фид, где
плитка стоит первой картинкой (image[0].url), а исходные фото сдвинуты на одну
позицию.

Имя файла плитки содержит хеш её содержимого: если фото, название, звёзды и цена
не менялись, файл и ссылка остаются прежними и Meta не скачивает картинку заново.
Уже нарисованные плитки повторно не рисуются.

Пример:
    python3 render_tiles.py \
        --feed hotels.csv \
        --out-dir tiles/ \
        --base-url https://d260djxm8uty7r.cloudfront.net/feeds/meta/tiles/ \
        --out-feed hotels_branded.csv

Зависимости: Python 3.9+, Pillow (pip install pillow).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

# Меняйте при любом изменении макета: все плитки перерисуются и получат новые ссылки.
TEMPLATE_VERSION = "v1"

# --- Макет (пиксели на холсте 1080x1080) -------------------------------------
SIZE = 1080
PAD = 40
PHOTO_BOX = (PAD, PAD, SIZE - PAD, 790)
PHOTO_RADIUS = 56

# Цвета сняты с экрана «Избранное» приложения Livin.
WHITE = (255, 255, 255)
TEXT_DARK = (28, 33, 45)       # «Отель, Астана»
BLUE = (30, 136, 229)          # название отеля, значок места
GRAY = (115, 123, 138)         # цена
ORANGE = (255, 153, 0)         # звёзды
PILL_BG = (255, 255, 255, 215)  # полупрозрачная плашка поверх фото

FONT_DIR_CANDIDATES = [
    "/usr/share/fonts/opentype/inter",
    "/usr/share/fonts/truetype/inter",
    "/Library/Fonts",
    str(Path(__file__).parent / "fonts"),
]


def find_font(names: list[str], override: str | None) -> str:
    if override:
        return override
    for d in FONT_DIR_CANDIDATES:
        for n in names:
            p = Path(d) / n
            if p.exists():
                return str(p)
    sys.exit(f"Не найден шрифт {names}. Укажите путь через --font-semibold/--font-medium "
             "(нужен шрифт с кириллицей, казахскими буквами и знаком ₸, например Inter).")


# --- Данные фида ---------------------------------------------------------------
@dataclass
class Hotel:
    hotel_id: str
    name: str
    city: str
    kind: str
    stars: int
    price_kzt: int | None
    photo_url: str


PRICE_RE = re.compile(r"^\s*([\d\s.,]+)\s*([A-Za-z]{3})?\s*$")


def parse_price(raw: str) -> tuple[int | None, str | None]:
    """'15259.00 KZT' -> (15259, 'KZT'); пусто/0 -> (None, cur)."""
    if not raw:
        return None, None
    m = PRICE_RE.match(raw)
    if not m:
        return None, None
    num = m.group(1).replace(" ", "").replace(",", ".")
    try:
        val = float(num)
    except ValueError:
        return None, None
    cur = (m.group(2) or "").upper() or None
    if val <= 0:
        return None, cur
    return int(val), cur


def parse_stars(raw: str) -> int:
    try:
        v = int(float(raw))
    except (TypeError, ValueError):
        return 0
    return v if 1 <= v <= 5 else 0


def image_columns(header: list[str]) -> dict[int, list[str]]:
    """Группирует колонки вида image[3].url / image[3].tag[0] по индексу."""
    groups: dict[int, list[str]] = {}
    for col in header:
        m = re.match(r"^image\[(\d+)\]\.(.+)$", col)
        if m:
            groups.setdefault(int(m.group(1)), []).append(col)
    return groups


# --- Рисование -------------------------------------------------------------------
def rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    # Рисуем в 4x и уменьшаем — сглаженные углы.
    k = 4
    big = Image.new("L", (size[0] * k, size[1] * k), 0)
    ImageDraw.Draw(big).rounded_rectangle((0, 0, size[0] * k - 1, size[1] * k - 1),
                                          radius * k, fill=255)
    return big.resize(size, Image.LANCZOS)


def star_polygon(cx: float, cy: float, r: float) -> list[tuple[float, float]]:
    import math
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    return pts


def draw_aa(canvas: Image.Image, box: tuple[int, int, int, int], painter) -> None:
    """Рисует фигуру со сглаживанием: в 4x на прозрачном слое и вклеивает."""
    k = 4
    w, h = box[2] - box[0], box[3] - box[1]
    layer = Image.new("RGBA", (w * k, h * k), (0, 0, 0, 0))
    painter(ImageDraw.Draw(layer), k)
    layer = layer.resize((w, h), Image.LANCZOS)
    canvas.alpha_composite(layer, (box[0], box[1]))


def pin_painter(color):
    def paint(d: ImageDraw.ImageDraw, k: int):
        # Капля-указатель 30x40: круг + треугольник, белая точка внутри.
        d.ellipse((0, 0, 30 * k, 30 * k), fill=color)
        d.polygon([(3 * k, 21 * k), (27 * k, 21 * k), (15 * k, 40 * k)], fill=color)
        d.ellipse((10 * k, 10 * k, 20 * k, 20 * k), fill=WHITE)
    return paint


def fit_text(draw: ImageDraw.ImageDraw, text: str, font, max_w: int) -> str:
    if draw.textlength(text, font=font) <= max_w:
        return text
    while text and draw.textlength(text + "…", font=font) > max_w:
        text = text[:-1]
    return text.rstrip() + "…"


def fmt_kzt(v: int) -> str:
    return f"{v:,}".replace(",", " ")  # 82711 -> "82 711"


class Renderer:
    def __init__(self, font_semibold: str, font_medium: str, logo: Image.Image | None,
                 show_price: bool):
        self.f_title = ImageFont.truetype(font_semibold, 56)
        self.f_place = ImageFont.truetype(font_medium, 40)
        self.f_price = ImageFont.truetype(font_semibold, 42)
        self.f_price_sub = ImageFont.truetype(font_medium, 40)
        self.logo = logo
        self.show_price = show_price
        self.mask = rounded_mask((PHOTO_BOX[2] - PHOTO_BOX[0], PHOTO_BOX[3] - PHOTO_BOX[1]),
                                 PHOTO_RADIUS)

    def render(self, h: Hotel, photo: Image.Image) -> Image.Image:
        canvas = Image.new("RGBA", (SIZE, SIZE), WHITE + (255,))

        # 1. Фото с закруглёнными углами, обрезка по центру.
        pw, ph = PHOTO_BOX[2] - PHOTO_BOX[0], PHOTO_BOX[3] - PHOTO_BOX[1]
        photo = ImageOps.fit(ImageOps.exif_transpose(photo).convert("RGB"), (pw, ph),
                             Image.LANCZOS, centering=(0.5, 0.5))
        canvas.paste(photo, PHOTO_BOX[:2], self.mask)

        # 2. Плашка звёздности (вместо рейтинга в приложении): N оранжевых звёзд.
        if h.stars:
            r, gap, padx, pill_h = 24, 8, 26, 84
            pill_w = padx * 2 + h.stars * (2 * r) + (h.stars - 1) * gap
            x0, y0 = PHOTO_BOX[0] + 36, PHOTO_BOX[1] + 36

            def paint_pill(d, k, n=h.stars):
                d.rounded_rectangle((0, 0, pill_w * k - 1, pill_h * k - 1), pill_h * k // 2,
                                    fill=PILL_BG)
                for i in range(n):
                    cx = (padx + r + i * (2 * r + gap)) * k
                    d.polygon(star_polygon(cx, pill_h * k / 2 + k, r * k), fill=ORANGE)
            draw_aa(canvas, (x0, y0, x0 + pill_w, y0 + pill_h), paint_pill)

        # 3. Логотип Livin в правом верхнем углу (вместо сердечка).
        if self.logo is not None:
            lw, lh = self.logo.size
            lx = PHOTO_BOX[2] - 32 - lw
            canvas.alpha_composite(self.logo, (lx, PHOTO_BOX[1] + 32))

        d = ImageDraw.Draw(canvas)
        text_x = PAD + 4
        max_w = SIZE - PAD - text_x

        # 4. Значок места + «Отель, Астана».
        y = PHOTO_BOX[3] + 30
        draw_aa(canvas, (text_x, y + 4, text_x + 30, y + 44), pin_painter(BLUE))
        place = ", ".join(p for p in (h.kind, h.city) if p)
        d.text((text_x + 44, y), fit_text(d, place, self.f_place, max_w - 44),
               font=self.f_place, fill=TEXT_DARK)

        # 5. Название отеля.
        y += 62
        d.text((text_x, y), fit_text(d, h.name, self.f_title, max_w), font=self.f_title,
               fill=BLUE)

        # 6. Цена «от ₸82 711 за ночь». Нет цены — строку не рисуем.
        if self.show_price and h.price_kzt:
            y += 84
            main = f"от ₸{fmt_kzt(h.price_kzt)}"
            d.text((text_x, y), main, font=self.f_price, fill=GRAY)
            d.text((text_x + d.textlength(main + " ", font=self.f_price), y + 2), "за ночь",
                   font=self.f_price_sub, fill=GRAY)

        return canvas.convert("RGB")


# --- Загрузка фото ----------------------------------------------------------------
def load_photo(url: str, cache_dir: Path, timeout: int, retries: int) -> Image.Image:
    if not re.match(r"^https?://", url):  # локальный путь — для тестов
        return Image.open(url)
    key = hashlib.sha1(url.encode()).hexdigest()
    cached = cache_dir / key
    if cached.exists():
        return Image.open(cached)
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "livin-tile-renderer/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
            img = Image.open(io.BytesIO(data))
            img.load()
            cached.write_bytes(data)
            return img
        except Exception as e:  # noqa: BLE001 — логируем любую ошибку загрузки
            last_err = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"не скачалось фото {url}: {last_err}")


# --- Основной цикл ------------------------------------------------------------------
def content_key(h: Hotel, show_price: bool, logo_hash: str) -> str:
    parts = [TEMPLATE_VERSION, logo_hash, h.photo_url, h.name, h.city, h.kind, str(h.stars),
             str(h.price_kzt if show_price else "")]
    return hashlib.sha1("\x1f".join(parts).encode()).hexdigest()[:12]


def safe_id(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]", "_", s)[:120]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--feed", required=True, help="входной CSV-фид отелей Meta")
    ap.add_argument("--out-dir", required=True, help="куда класть плитки")
    ap.add_argument("--base-url", required=True,
                    help="публичный URL папки с плитками (с / на конце)")
    ap.add_argument("--out-feed", required=True, help="выходной CSV с плиткой в image[0]")
    ap.add_argument("--cache-dir", default=".photo_cache", help="кэш скачанных фото")
    ap.add_argument("--logo", help="PNG логотипа Livin (прозрачный фон), ставится справа сверху")
    ap.add_argument("--logo-height", type=int, default=64)
    ap.add_argument("--no-price", action="store_true",
                    help="не рисовать цену (меньше перерисовок и повторных загрузок в Meta)")
    ap.add_argument("--price-step", type=int, default=0,
                    help="округлять цену ВНИЗ до шага, напр. 1000: «от ₸82 000» вместо 82 711; "
                         "реже меняется картинка, «от» остаётся правдой")
    ap.add_argument("--kind", default="",
                    help="одна подпись типа для всех строк, если в фиде нет колонки типа. "
                         "По умолчанию пусто: в каталоге есть квартиры и гостевые дома, "
                         "«Отель» на них было бы неправдой — лучше --col-kind")
    ap.add_argument("--col-id", default="hotel_id")
    ap.add_argument("--col-name", default="name")
    ap.add_argument("--col-city", default="address.city")
    ap.add_argument("--col-stars", default="star_rating")
    ap.add_argument("--col-price", default="base_price")
    ap.add_argument("--col-kind", default="", help="колонка с типом жилья, если есть")
    ap.add_argument("--max-images", type=int, default=20, help="лимит Meta на число фото")
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--retries", type=int, default=3)
    ap.add_argument("--limit", type=int, default=0, help="обработать только первые N строк")
    ap.add_argument("--font-semibold")
    ap.add_argument("--font-medium")
    args = ap.parse_args()

    out_dir, cache_dir = Path(args.out_dir), Path(args.cache_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)
    base_url = args.base_url if args.base_url.endswith("/") else args.base_url + "/"

    logo, logo_hash = None, ""
    if args.logo:
        raw = Path(args.logo).read_bytes()
        logo_hash = hashlib.sha1(raw).hexdigest()[:8]
        logo = Image.open(io.BytesIO(raw)).convert("RGBA")
        logo = logo.resize((round(logo.width * args.logo_height / logo.height), args.logo_height),
                           Image.LANCZOS)

    renderer = Renderer(
        find_font(["Inter-SemiBold.otf", "Inter-SemiBold.ttf"], args.font_semibold),
        find_font(["Inter-Medium.otf", "Inter-Medium.ttf"], args.font_medium),
        logo, show_price=not args.no_price)

    with open(args.feed, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        header = list(reader.fieldnames or [])
        rows = list(reader)
    if args.limit:
        rows = rows[: args.limit]

    for col in (args.col_id, args.col_name, "image[0].url"):
        if col not in header:
            sys.exit(f"В фиде нет колонки {col!r}. Колонки: {header}")

    stats = {"rows": len(rows), "rendered": 0, "reused": 0, "failed": 0, "no_price": 0,
             "non_kzt_price": 0}
    tile_for_row: dict[int, str] = {}
    jobs = []

    for i, row in enumerate(rows):
        price, cur = parse_price(row.get(args.col_price, ""))
        if price is not None and cur not in (None, "KZT"):
            stats["non_kzt_price"] += 1
            price = None
        if price is None:
            stats["no_price"] += 1
        elif args.price_step > 1:
            price = (price // args.price_step) * args.price_step
        h = Hotel(
            hotel_id=row[args.col_id],
            name=row.get(args.col_name, "").strip(),
            city=row.get(args.col_city, "").strip(),
            kind=(row.get(args.col_kind, "").strip() if args.col_kind else args.kind),
            stars=parse_stars(row.get(args.col_stars, "")),
            price_kzt=price,
            photo_url=row["image[0].url"].strip(),
        )
        if not h.photo_url:
            stats["failed"] += 1
            continue
        fname = f"{safe_id(h.hotel_id)}_{content_key(h, not args.no_price, logo_hash)}.jpg"
        tile_for_row[i] = fname
        if (out_dir / fname).exists():
            stats["reused"] += 1
        else:
            jobs.append((i, h, fname))

    def work(job):
        i, h, fname = job
        photo = load_photo(h.photo_url, cache_dir, args.timeout, args.retries)
        tile = renderer.render(h, photo)
        tmp = out_dir / (fname + ".tmp")
        tile.save(tmp, "JPEG", quality=88, optimize=True, progressive=True)
        os.replace(tmp, out_dir / fname)  # атомарно: Meta не увидит недописанный файл
        return i

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(work, j): j for j in jobs}
        for fut in as_completed(futs):
            i, h, _ = futs[fut]
            try:
                fut.result()
                stats["rendered"] += 1
            except Exception as e:  # noqa: BLE001
                stats["failed"] += 1
                tile_for_row.pop(i, None)  # без плитки строка уйдёт с исходными фото
                print(f"[warn] {h.hotel_id}: {e}", file=sys.stderr)
    elapsed = time.time() - t0

    # Новый фид: плитка -> image[0], исходные фото сдвигаются на +1.
    groups = image_columns(header)
    suffixes = sorted({c.split("].", 1)[1] for cols in groups.values() for c in cols})
    max_idx = min(max(groups) + 1 if groups else 0, args.max_images - 1)
    img_cols = [f"image[{n}].{s}" for n in range(max_idx + 1) for s in suffixes]
    other_cols = [c for c in header if c not in {c2 for cols in groups.values() for c2 in cols}]
    first_img_pos = next((k for k, c in enumerate(header) if c.startswith("image[")), len(header))
    new_header = (other_cols[:first_img_pos] + img_cols + other_cols[first_img_pos:])

    with open(args.out_feed, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=new_header, extrasaction="ignore")
        w.writeheader()
        for i, row in enumerate(rows):
            out = {c: row.get(c, "") for c in other_cols}
            shift = 1 if i in tile_for_row else 0
            for n in range(max_idx + 1):
                src = n - shift
                for s in suffixes:
                    out[f"image[{n}].{s}"] = row.get(f"image[{src}].{s}", "") if src >= 0 else ""
            if shift:
                out["image[0].url"] = base_url + tile_for_row[i]
            w.writerow(out)

    per = (elapsed / stats["rendered"] * 1000) if stats["rendered"] else 0
    print(f"строк: {stats['rows']} | нарисовано: {stats['rendered']} | без изменений: "
          f"{stats['reused']} | ошибок: {stats['failed']} | без цены: {stats['no_price']} "
          f"(из них не в KZT: {stats['non_kzt_price']}) | {elapsed:.1f} c, ~{per:.0f} мс/плитку")


if __name__ == "__main__":
    main()
