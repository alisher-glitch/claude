# Обложка для рекламы каталога: промпт для ИИ

Обложка — верхняя большая картинка в объявлении «Подборка», под ней идут плитки отелей.
Одна общая на весь каталог, работает в ленте и в сторис Instagram. Референс по виду —
реклама Freedom Travel «Бюджетные отели»: тёплый крупный план номера, крупный белый заголовок
слева сверху, логотип внизу.

## Как лучше генерировать
Нейросети часто ошибаются в русских буквах. Поэтому надёжнее в два шага:
1. Сгенерировать **только фон без текста** (промпт 1).
2. Добавить заголовок и логотип в Figma или Canva (раздел «Текст поверх»).

Если генератор хорошо пишет текст (например, ChatGPT), можно сразу целиком (промпт 2),
но буквы потом проверить внимательно.

## Промпт 1 — фон без текста (рекомендуем)
```
Square 1:1 photo, 1080x1080. Cozy modern hotel room, close-up of a soft upholstered headboard,
white pillows and a warm wall lamp glowing. Warm golden evening light, soft shadows, shallow depth
of field. Calm, premium, inviting mood. Realistic photography style, natural colors.
Leave the upper-left third and the bottom strip visually calm and darker for text overlay.
No text, no letters, no logos, no watermarks, no people, no brand names.
```
Запасные сюжеты (подставить вместо второго предложения):
- `Hotel room with a large window and a city view at sunset, made bed in the foreground.`
- `Hotel room balcony with two chairs and a sea view in soft morning light.`

## Промпт 2 — сразу с текстом
```
Square 1:1 advertising image, 1080x1080. Background: cozy modern hotel room, close-up of a soft
headboard, white pillows and a glowing warm wall lamp, warm golden light, realistic photo.
Large bold white sans-serif headline in Russian in the upper-left corner, two lines:
"Отели для вашей" / "поездки". Small white text at the bottom-left: "Livin".
Tiny light-gray text at the very bottom: "Создано с использованием ИИ".
Keep all text at least 80 px from the edges. No other text, no prices, no people, no watermarks.
```

## Текст поверх (если делать в Figma/Canva)
- **Заголовок**, белый, жирный, слева сверху, 2 строки. Один из вариантов:
  «Отели для вашей поездки», «Найдите свой отель», «Отели и апартаменты».
- **Логотип Livin** белый, слева снизу.
- **«Создано с использованием ИИ»** — мелко, светло-серым, в самом низу.
- Всё не ближе 80 px к краям: Meta может подрезать.

## Нельзя на обложке
- цены, скидки и акции;
- даты и сроки («только до…», «этим летом»);
- сравнение с другими сервисами и их названия;
- «лучший», «№1», «самые низкие цены»;
- конкретный реальный отель или его узнаваемый фасад (обложка сгенерирована, а реальные
  отели показываются на плитках).

## Перед тем как отдать в рекламу
- Размер 1080×1080, JPG.
- Буквы в заголовке без ошибок.
- На фоне нет случайных надписей, логотипов и искажённых предметов (ИИ любит лишние пальцы,
  кривые лампы, нечитаемые таблички).
- Маркетинг смотрит превью в Ads Manager для ленты и сторис: ничего не обрезано.
