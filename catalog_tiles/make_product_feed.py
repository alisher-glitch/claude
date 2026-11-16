#!/usr/bin/env python3
"""Делает из отельного фида Meta (hotels.csv) товарный фид (products.csv).

Зачем: формат «Подборка» с витриной Instant Experience и источник «Products» в Ads Manager
не принимают каталог вертикали hotels — им нужен обычный товарный (ecommerce) каталог.
Тот же набор отелей отдаём вторым фидом в формате товаров.

    python3 make_product_feed.py --feed hotels.csv --out products.csv

Отели без цены пропускаются: у товара цена обязательна.
"""
from __future__ import annotations

import argparse
import csv
import re

FIELDS = ["id", "title", "description", "availability", "condition", "price", "link",
          "image_link", "additional_image_link", "brand",
          "custom_label_0", "custom_label_1", "custom_label_2", "custom_label_3",
          "ios_url", "ios_app_store_id", "ios_app_name",
          "android_url", "android_package", "android_app_name"]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--feed", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--brand-fallback", default="Livin")
    args = ap.parse_args()

    with open(args.feed, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    kept = skipped = 0
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            m = re.match(r"^\s*([\d.]+)\s+([A-Z]{3})\s*$", r.get("base_price", ""))
            if not m or float(m.group(1)) <= 0 or not r.get("image[0].url"):
                skipped += 1
                continue
            extra = [r[f"image[{i}].url"] for i in range(1, 10) if r.get(f"image[{i}].url")]
            w.writerow({
                "id": r["hotel_id"],                      # тот же id, что в событиях (content_ids)
                "title": r["name"][:200],
                "description": r.get("description") or r["name"],
                "availability": "in stock",
                "condition": "new",
                "price": f"{float(m.group(1)):.2f} {m.group(2)}",
                "link": r["url"],
                "image_link": r["image[0].url"],          # брендированная плитка
                "additional_image_link": ",".join(extra),
                "brand": r.get("brand") or args.brand_fallback,
                "custom_label_0": r.get("address.city", ""),
                "custom_label_1": r.get("address.country", ""),
                "custom_label_2": r.get("star_rating", ""),
                "custom_label_3": r.get("category", ""),
                "ios_url": r.get("applink.ios_url", ""),
                "ios_app_store_id": r.get("applink.ios_app_store_id", ""),
                "ios_app_name": r.get("applink.ios_app_name", ""),
                "android_url": r.get("applink.android_url", ""),
                "android_package": r.get("applink.android_package", ""),
                "android_app_name": r.get("applink.android_app_name", ""),
            })
            kept += 1
    print(f"товаров: {kept} | пропущено без цены/фото: {skipped}")


if __name__ == "__main__":
    main()
