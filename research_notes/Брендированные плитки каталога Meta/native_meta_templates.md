# Meta's own tools for branding catalog product tiles (Advantage+ catalog ads / hotel ads)

Research date: 2026-11-12.

**How the sources were read.** In this session, facebook.com, developers.facebook.com, confect.io, thebrandmove.com, dynamicproductads.com and holostenko.ua were all blocked by the network proxy (HTTP 403 or no DNS).
- **Meta Help Center articles (high confidence).** Their full text came from Meta's own help-article tool (Facebook Ads MCP). Quotes from them are the verbatim current article text. They are cited by their facebook.com/business/help URL.
- **developers.facebook.com pages (medium confidence).** The pages themselves could not be opened. Facts about them come only from web-search result summaries and snippets of those pages.
- **Third-party blogs (low to medium confidence).** These are also known only through search snippets.

---

## 1. Commerce Manager "Image templates": layers, fields, conditional display, ratios, launch date, hotel availability

### Takeaway
Image templates are a layer-based design canvas in Commerce Manager. The layers are:
- Product (required)
- Catalog field
- Image
- Text
- Sticker
- Background

Conditional display is available on catalog field, image and text layers. Templates come in 1:1, 4:5 and 9:16. You apply a template in Ads Manager, but you cannot create or edit one there, and there is no API for managing templates.

The feature has limited availability and is switched on per business. Meta's developer docs reportedly describe it as available to businesses with a *product catalog*. The catalog-field examples Meta gives are commerce fields (title, brand, price, sale price, custom labels). I found no source saying image templates work with a **hotel**-vertical catalog or expose hotel fields such as star_rating or address.city. Treat hotel support as unconfirmed and likely absent.

### Cited Findings
- **Where you build them.** Commerce Manager → select catalog → "Image templates" on the left → "+ Create". You can start from a blank canvas or a starter template. Design starts in 1:1. — [Create image templates for ads using product media (Meta Help 947145298422088)](https://www.facebook.com/business/help/947145298422088)
- **Layer types (verbatim list)** — [Meta Help 947145298422088](https://www.facebook.com/business/help/947145298422088)
  - **Product layer (required).** Shows a product image from the catalog. You can choose the image index: "0 represents the main image (image_link attribute) and 1–3 are the additional images (additional_image_link)". Optional *background removal* makes the background transparent. Optional *crop to fit* overrides the catalog's image-cropping settings. You can add several product layers to show multiple images.
  - **Catalog field.** "pull product attributes from your catalog, such as title, brand, description, price, current price (sale price) or custom labels."
  - **Image layer.** Your own JPG or PNG, such as a logo or graphic.
  - **Text layer.** Custom text with color, opacity, font, size, alignment, style and position.
  - **Sticker layer.** A circle, rectangle or square with its own color and text.
  - **Background layer.** A color that always sits behind everything else and cannot be moved.
- **Layer order and deletion.** Layers are reordered by drag-and-drop, and the top of the list renders in front. The product layer cannot be deleted unless there is more than one. — [Meta Help 947145298422088](https://www.facebook.com/business/help/947145298422088)
- **Conditional display.** "turn on conditional display in its layer settings. set a rule based on a product attribute (such as price) and the layer will only show when the condition is met. conditional display is available for catalog field, image and text layers." It is not listed for sticker, product or background layers. — [Meta Help 947145298422088](https://www.facebook.com/business/help/947145298422088)
- **Preview.** You can preview the template against a chosen product set or product from dropdowns under the canvas. — [Meta Help 947145298422088](https://www.facebook.com/business/help/947145298422088)
- **Aspect ratios.** 1:1 is the base. Separate 4:5 (feed) and 9:16 (stories and reels) versions are created by copying the 1:1 design and adjusting it. "creating templates in all ratios maximises the placements that your templates can be delivered to." — [Meta Help 947145298422088](https://www.facebook.com/business/help/947145298422088)
- **Priority over cropping settings.** Image templates take priority over the catalog's Commerce Manager cropping settings. — [Product image specifications for catalogs (Meta Help 686259348512056)](https://www.facebook.com/business/help/686259348512056)
- **Developer docs (via search summary).**
  - Templates are "a saved, reusable design layered on top of your product images at delivery time".
  - They are created and edited only in Commerce Manager. In Ads Manager you can apply one but not create or edit it.
  - "There is no API for creating, editing, deleting, or listing templates."
  - The feature "is limited to businesses with a product catalog and is enabled by Meta for the owning business… limited availability".
  - The page was reportedly updated on 2026-08-17.
  - Listed errors include "template does not exist" and "templates not enabled for the catalog that owns this template".
  - Source: [Marketing API – Advantage+ catalog ads – Image templates](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-catalog-ads/image-templates). I could not open this page directly.
- **Availability varies by account.** Third-party blogs say the feature is "not yet enabled on every account" and "still rolling out". One says that if the menu item is missing, you should contact your Meta rep. — [thebrandmove](https://www.thebrandmove.com/en/blog/meta-image-templates/), [barbarosozturk](https://barbarosozturk.com/blog/metas-new-image-templates-no-need-for-third-party-apps/), [Confect video templates](https://confect.io/blog/meta-video-catalog-ad-templates) (search snippets only).
- **Confect's guide (2026-07-15).**
  - It describes a layer builder: background, product image, price, headline, logo.
  - Its ratios are 1:1, 4:5 and 9:16. Templates "only work on Catalog Ads".
  - Image number 0 is the primary image. Price can be paired with the catalog's current price.
  - It says templates are different from the old frames and overlays.
  - Source: [Confect – Meta Catalog Ad Templates](https://confect.io/blog/meta-catalog-ads-templates) (search snippet).
- **Related tool: product video creator.** Commerce Manager also has a "product video creator", which is being rolled out gradually.
  - It uses video templates in 9:16 and 4:5. Text overlays can pull each product's price or title from the catalog.
  - It produces videos for up to 25% of a catalog, with a cap of 10,000 products.
  - Source: [Create product videos with video templates (Meta Help 1074724715095990)](https://www.facebook.com/business/help/1074724715095990)
- **Hotel feed fields that a template would need.** The hotel catalog has its own schema:
  - name
  - address object (with city)
  - star_rating, from 1 to 5 in half-point steps
  - base_price
  - sale_price, which must be lower than base_price
  - Source: [Hotel Ads – Catalog & Feed (v3.1)](https://developers.facebook.com/docs/marketing-api/dynamic-ads-for-hotels/catalog/v3.1) and [Hotel ads – Catalogs and feed (current)](https://developers.secure.facebook.com/documentation/ads-commerce/marketing-api/hotel-ads/catalog) (search summaries).
  - API-created hotel catalogs use vertical=hotels. — [Hotel ads catalog docs](https://developers.facebook.com/docs/marketing-api/hotel-ads/catalog/) (search summary)

### Inferences
- **Hotel catalogs probably cannot use image templates.** Meta's help text lists only commerce-vertical field names (title, brand, description, price, current price, custom labels). The developer docs reportedly limit the feature to "businesses with a product catalog". So hotel-vertical catalogs (vertical=hotels) are probably not eligible, or at least are not documented as eligible. Even where the feature is enabled, it is unconfirmed whether hotel fields (star_rating, address.city, base_price) would appear as catalog-field layers.
- **Most likely field mapping, if a hotel catalog could use templates.** price → base_price, sale price → sale_price, plus custom_label_0–4. This is not confirmed.
- **Launch date.** I found no dated Meta announcement. Third-party coverage clusters in 2026, the Confect guide is dated 2026-07-15 and the developer doc was updated 2026-08-17. The frames article says frames are "being replaced by image templates". Together these point to a broad rollout in 2026, with an earlier limited beta possible.

### Gaps
- No exact launch or GA date for image templates.
- No official statement either way on hotel, flight or destination catalog support. To settle it, check in Commerce Manager whether a hotel catalog shows the "Image templates" tab.
- Conditional display operators (>, <, =, contains?) and which attributes can be used in rules are not documented beyond the example "such as price".
- Fonts available, custom font upload, and limits on layer count were not found.

---

## 2. Format support: single image, carousel, collection, Instant Experience, Stories/Reels

### Takeaway
Meta's current help text is explicit: image templates support **single image and carousel only, not collection**. Stories and Reels are reached through a 9:16 template version, with "image touch-ups" kept on. No source says templates apply to collection covers or to Instant Experience (storefront) product grids.

### Cited Findings
- "image templates support single image and carousel formats only, not collection." — [Meta Help 947145298422088](https://www.facebook.com/business/help/947145298422088)
- **Steps to apply a template in Ads Manager.**
  1. Create a Sales campaign with product data on and a catalog selected.
  2. At ad level, choose products from the catalog as the creative source.
  3. Under "Image template", click "Choose template".
  - Source: [Meta Help 947145298422088](https://www.facebook.com/business/help/947145298422088)
- **Advantage+ creative settings Meta recommends with templates.** — [Meta Help 947145298422088](https://www.facebook.com/business/help/947145298422088)
  - Turn **off** background generation, which would replace the template.
  - Turn **off** dynamic overlays, unless you want them drawn on top of the template.
  - Keep **image touch-ups on** "so that 4:5 and 9:16 templates can deliver to all eligible placements."
- **Ratio choice in carousel and collection.** In carousel ads, images may be resized to 1:1 or 4:5 to match the first card. In collection ads, if the first 3 images share a ratio, the 4th may be resized to match. Meta names image templates as one way to control this. — [How aspect ratios of product images may be adjusted (Meta Help 856291093299815)](https://www.facebook.com/business/help/856291093299815)
- **Travel ads formats.** Travel ads "look identical to other single or carousel ads", and Meta "recommend[s] using carousel as default over single image". — [Create an ad template for travel ads (Meta Help 1294482487347184)](https://www.facebook.com/business/help/1294482487347184)
- **Storefront Instant Experience.** It needs the collection ad format and "an ecommerce catalog". It is available with the Traffic and Sales objectives. — [About Instant Experience templates (Meta Help 1454940661230823)](https://www.facebook.com/business/help/1454940661230823)
- **Collection ad structure.** The collection needs at least 4 products or images. "the first image or video from your instant experience will become the cover image… the rest… smaller images at the bottom". The storefront can order products dynamically or in a fixed order. Collection may now be chosen under "format display options" in ad creative. — [Choose products to show in a collection ad (Meta Help 1591426100917979)](https://www.facebook.com/business/help/1591426100917979)
- **Threads.** Advantage+ catalog ads on Threads support only images and image carousels. — [Threads Advantage+ Catalog Ads (dev docs)](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/threads-ads/creation/advantage-catalog-ads) (search summary)

### Inferences
- **Collection tiles and storefront grids get no template.** Templates are excluded from collection, and the storefront requires collection. So the thumbnails under a collection cover and the product grid inside an Instant Experience storefront render raw catalog images, after Commerce Manager cropping. No native template applies.
- **Hotel storefront.** The storefront template requires an "ecommerce catalog". A hotel-vertical catalog therefore may not be able to drive a storefront at all. This is unverified.

### Gaps
- No newer source (2026) saying collection support has been added.
- No Meta doc on how hotel catalogs behave in collection or storefront.

---

## 3. Older or other mechanisms: frames, dynamic overlays, Advantage+ "add overlays", and API fields

### Takeaway
There are three native mechanisms besides image templates:
- **Catalog frames.** One static 1:1 PNG over every product. They are not shown on Instagram and are being retired in favor of image templates. Meta's help article says "early 2027". One third-party snippet says "after October 30, 2026".
- **Dynamic overlays.** A price, strikethrough, % off or free-shipping badge, shown on **Facebook Feed only**. Launched around April–May 2025, replacing the older "catalog info labels".
- **Travel or hotel overlays in the Marketing API (`image_overlay_spec`).** For hotels these support price, strikethrough and % off, filled from the hotel feed's price and sale price. This is the only mechanism with documented **hotel-specific** support.

`template_url_spec` is a link and deep-link field, not a visual one. `image_layer_specs` is reportedly limited-access.

### Cited Findings
**Frames**
- **Retirement notice.** "frames for product images are being replaced by image templates. frames will no longer be available starting in early 2027, so we recommend switching to image templates now." — [Add a frame to product images (Meta Help 517601898571657)](https://www.facebook.com/business/help/517601898571657)
- **Conflicting date.** A third-party snippet says frames "will no longer be available after October 30, 2026". — search-result summary citing [thebrandmove](https://www.thebrandmove.com/en/blog/meta-image-templates/) / [barbarosozturk](https://barbarosozturk.com/blog/metas-new-image-templates-no-need-for-third-party-apps/). The Meta article text above is more authoritative.
- **Frame specs.**
  - Not available on Instagram placements.
  - Path: Ads Manager → ad creative → Creative tools → Edit creative → Add a frame → Custom → upload.
  - Image must be 1:1, under 1 MB and at least 1080×1080. A transparent background with no text is recommended.
  - Opacity, size and position can be adjusted.
  - Source: [Meta Help 517601898571657](https://www.facebook.com/business/help/517601898571657)

**Dynamic overlays**
- **What they are and where they show.** "show product data from your catalog such as prices or discounts in a label on your ad media. dynamic overlays only show on facebook feed." They are available with single image or video, and with carousel. Turn them on via Advantage+ creative → "Add dynamic overlays". — [Add dynamic overlays in Advantage+ catalog ads (Meta Help 626735652348813)](https://www.facebook.com/business/help/626735652348813)
- **Options.** — [Meta Help 626735652348813](https://www.facebook.com/business/help/626735652348813)
  - Price
  - Strikethrough price
  - Percentage off
  - Free shipping, which requires shipping cost 0.0
- **Styling.** — [Meta Help 626735652348813](https://www.facebook.com/business/help/626735652348813)
  - Shape: rectangle, pill, circle or triangle
  - Position, color, font, text color and opacity
  - Character limits: rectangle 13, pill 13, triangle 6, circle 6. For strikethrough, keep each price to 6 or fewer characters.
  - "Always show" overrides Advantage+ automation on Facebook Feed.
  - From March 2026, Facebook Feed includes the Facebook Friends tab.
  - With background generation, Meta auto-styles the overlay.
- **Launch timing.** It was rolled out in about April–May 2025 and renamed from the former "catalog info labels".
  - ads-up.fr article dated 2025-05-05: [ads-up.fr](https://ads-up.fr/en/publications/social-ads/meta-rolls-out-dynamic-overlays-for-advantage-catalogue-ads-campaigns/)
  - Initially delivered to Facebook Feed only: [Social Media Today](https://www.socialmediatoday.com/news/facebook-advantage-plus-catalog-ads-overlay-offers/746337/), [Search Engine Land](https://searchengineland.com/meta-dynamic-overlays-advantage-catalog-ads-454657)
  - "Labels became dynamic overlays in April 2025": [adsuploader](https://adsuploader.com/blog/facebook-catalog-ad-overlays)
  - All of the above are search snippets.

**Travel and hotel overlays in the API**
- **Overlay types by catalog.** The Travel Ads developer doc says supported overlay types are "price, strikethrough and % off. The strikethrough and % off overlays are available for hotels only". Hotel catalogs get price, strikethrough and % off. Destination and flight catalogs get price only. — [Travel Ads (dev docs)](https://developers.facebook.com/documentation/ads-commerce/marketing-api/travel-ads) (search summary)
- **Example in that doc.** "Price Overlay with Strikethrough for a Hotel Ad" uses `image_overlay_spec`, with `overlay_template` set to a pill style. It uses the text tags `{{hotel.price round}}` and `{{hotel.sale_price round}}`, and pricing comes from the feed's price and sale price columns. — [Travel Ads (dev docs)](https://developers.facebook.com/documentation/ads-commerce/marketing-api/travel-ads) (search summary)
- **Help Center article.** Meta has an article titled "How do I add an overlay to my travel ads?" — [Meta Help 1492206750869184](https://www.facebook.com/business/help/1492206750869184). Only the title was found; its text was not retrieved.
- **`image_layer_specs`.** It is described as the Marketing API counterpart that Meta makes "available on a limited basis". — [soku.ai](https://soku.ai/blog/meta-catalog-ads) (third-party search snippet)
- **`template_url_spec`.** It sets the ad-level booking or deep-link URL and takes the highest precedence over feed App Links and website App Link tags. It is not an image field. — [Hotel Ads catalog docs](https://developers.facebook.com/docs/marketing-api/hotel-ads/catalog/) (search summary)

### Inferences
- **For a hotel catalog today.**
  - The native visual branding options with hotel-specific documentation are the API `image_overlay_spec` (price, strikethrough, % off) and possibly the Ads Manager overlay for travel ads (Help 1492206750869184).
  - Frames probably also work with hotel catalogs, since they are just a static PNG, but they are deprecated and do not show on Instagram.
  - Image templates are documented for "product catalogs" only.
- **Dynamic overlays are commerce-oriented.** "Free shipping" and shipping cost are commerce concepts, so it is unclear whether the Ads Manager toggle appears for hotel catalogs. It is also Facebook Feed only.

### Gaps
- Full `image_overlay_spec` schema (text_type values, positions, theme colors, fonts) could not be retrieved because developers.facebook.com was blocked.
- Whether dynamic overlays show for hotel catalogs in Ads Manager is unconfirmed.
- Exact retirement date for frames: "early 2027" (Meta) vs "Oct 30, 2026" (third party) is unresolved.

---

## 4. Hotel ads template tags (text)

### Takeaway
Hotel ads take dynamic text through `{{hotel.*}}` and `{{trip.*}}` tags in primary text, headline and link description. Confirmed tags found are:
- `{{hotel.name}}`
- `{{hotel.description}}`
- `{{hotel.brand}}`
- `{{hotel.city}}`
- `{{hotel.price}}` and `{{hotel.sale_price}}`, with a `round` modifier
- `{{trip.checkin_date}}`

The full official list, including star rating, country, length of stay and checkout date, could not be retrieved.

### Cited Findings
- **Hotel chain guide.** Recommends `{{hotel.name}}`, `{{hotel.description}}`, `{{hotel.brand}}` and `{{trip.checkin_date}}` for dynamic creative. — [Hotel Chain (dev docs)](https://developers.facebook.com/docs/marketing-api/travel-ads-smb/hotel-chain) (search summary)
- **Travel Ads doc.**
  - Has separate sections: "Template Tags for Hotels / Destinations / Flights".
  - The example uses `{{hotel.name}}`, `{{hotel.city}}`, `{{hotel.price round}}` and `{{hotel.sale_price round}}`.
  - Source: [Travel Ads (dev docs)](https://developers.facebook.com/documentation/ads-commerce/marketing-api/travel-ads) (search summary)
- **Check-in date from pixel events.** A check-in date passed in pixel events can be used in the ad through template tags. — [Hotel Ads – Events](https://developers.facebook.com/documentation/ads-commerce/marketing-api/hotel-ads/events) (search summary)
- **Date-specific prices.** Once supplied, these prices can be used through hotel template tags. — [Hotel Ads – Date-Specific Prices](https://developers.facebook.com/docs/marketing-api/dynamic-ads-for-hotels/dynamic-pricing/v2.12) (search summary)
- **Ads Manager wording.** "in the text, headline and feed link description sections, you can select different template tags… the hotel field may include city, country, base price and more depending on which parameters you implemented for your pixel events." — [Meta Help 1294482487347184](https://www.facebook.com/business/help/1294482487347184)
- **length_of_stay field.** The feed field `length_of_stay` (number of nights) is required when adding room information. — [Hotel catalog docs](https://developers.facebook.com/docs/marketing-api/hotel-ads/catalog/) (search summary)

### Inferences
- **Text-only placement.** These tags fill ad text fields, and the price ones also fill `image_overlay_spec` text. They do not draw onto the image except through the overlay spec.
- **Probable additional tags.** Likely tags include `{{hotel.country}}`, `{{hotel.star_rating}}`, `{{trip.checkout_date}}` and `{{trip.length_of_stay}}`, but none of these are confirmed.

### Gaps
- The complete official tag list ("Template Tags for Hotels" on developers.facebook.com/documentation/ads-commerce/marketing-api/travel-ads) needs direct access.

---

## 5. Known limitations, bugs and complaints

### Takeaway
I found no Reddit or forum threads specific to hotel catalogs. The documented and third-party-reported limitations are:
- Limited, per-business availability with no API.
- No collection support.
- Frames do not show on Instagram.
- Dynamic overlays show on Facebook Feed only.
- Advantage+ creative enhancements can override templates.
- A template cannot be edited once linked to an ad.
- Product-set mismatches cause templates not to show.

### Cited Findings
- Limited availability, enabled per business, with no API for template management. — [Image templates dev docs](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-catalog-ads/image-templates) (search summary)
- Meta itself advises turning off background generation, which replaces the template, and dynamic overlays, which draw on top. — [Meta Help 947145298422088](https://www.facebook.com/business/help/947145298422088)
- **Third-party reports.**
  - "Advantage+ Creative enhancements, especially image touch-ups and background generation, override template designs."
  - Product-set mismatch: the template lives on set A while the ad runs on set B.
  - Video templates do not serve in carousels.
  - Source: search summary of [Confect](https://confect.io/blog/meta-catalog-ads-templates) / [dynamicproductads.com](https://dynamicproductads.com/meta-catalog-ads-templates-review-and-alternatives/) and others.
- A template "once linked to an ad, you can't edit it directly" (third-party). Also: "we found no public Meta help article for Templates". The second claim is now outdated, since Help 947145298422088 exists. — search summary of [dynamicproductads.com](https://dynamicproductads.com/meta-catalog-ads-templates-review-and-alternatives/), [thebrandmove](https://www.thebrandmove.com/en/blog/meta-image-templates/)
- "Travel ads" no longer appears as a separate campaign type. It now sits inside Advantage+ catalog ads with a Sales objective, which can confuse users. — [adsuploader – Facebook Travel Ads](https://adsuploader.com/blog/facebook-travel-ads) (search snippet)
- Frames do not show on Instagram. — [Meta Help 517601898571657](https://www.facebook.com/business/help/517601898571657)
- Dynamic overlays show on Facebook Feed only. — [Meta Help 626735652348813](https://www.facebook.com/business/help/626735652348813)

### Inferences
- **Native coverage for a hotel advertiser.** The native stack likely cannot put a branded frame, star rating and city onto hotel tiles consistently across Instagram, Stories/Reels and collection. Hotel overlays cover only price, strikethrough and % off. Image templates (the only rich option) are documented for product catalogs only. This is why third-party template tools (Confect, Hunch, CustomPix and others) that render pre-branded images into the feed are still relevant.

### Gaps
- No Reddit r/FacebookAds or r/PPC threads were retrieved. Reddit did not appear in the search results, so forum sentiment is not covered.

---

## 6. Collection cover and Instant Experience storefront: how product tiles render

### Takeaway
In a collection ad, the cover is the first image or video of the Instant Experience. Below it are at least 3 smaller product tiles. The storefront shows a product grid ordered dynamically or manually. Image templates are explicitly not supported in collection, so tiles show raw catalog images. They are subject only to the catalog's cropping settings and ratio auto-adjustment.

### Cited Findings
- Cover = first image or video. The remaining items become smaller images at the bottom, with at least 4 products or images in total. — [Meta Help 1591426100917979](https://www.facebook.com/business/help/1591426100917979)
- The storefront requires the collection format and an ecommerce catalog. It shows products in a grid. — [Meta Help 1454940661230823](https://www.facebook.com/business/help/1454940661230823)
- The catalog's image-cropping settings apply to carousel and collection ads. The three options are:
  - Fill frame (the default)
  - Show entire image
  - Crop and resize to fit
  - Source: [Meta Help 686259348512056](https://www.facebook.com/business/help/686259348512056)
- In collection, if the first 3 images share a ratio (1:1 or 4:5), the 4th may be resized to match. — [Meta Help 856291093299815](https://www.facebook.com/business/help/856291093299815)
- Image templates do not support collection. — [Meta Help 947145298422088](https://www.facebook.com/business/help/947145298422088)

### Inferences
- **Only path to branded tiles in collection or storefront.** Feed images must be pre-branded, either baked into image_link or additional_image_link by an external tool, or done through a feed rule or partner. No native template applies there. A custom cover image or video can be branded freely because it is a normal uploaded asset.

### Gaps
- No documentation found on whether hotel-vertical catalogs can power collection or storefront at all. The storefront text says "ecommerce catalog".
