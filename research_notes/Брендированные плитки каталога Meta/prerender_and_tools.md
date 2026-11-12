# Pre-rendering branded hotel images into a Meta catalog feed: in-house vs third-party (research notes, 2026-11-12)

Method note: research was done 2026-11-12. WebFetch could not reach any target host in this session (developers.facebook.com, developers.secure.facebook.com, confect.io, channable.com, cropink.com and img.vision all failed DNS: they are outside the session's network allowlist). **All findings below come from web-search result summaries of the cited pages, not from full-page reads.** Verify exact wording on the source before you quote it in a client-facing document. Source dates are given where the search results showed them.

Context: Livin.kz, 9,093 hotels, nightly in-house CSV feed, prices in KZT.

---

## (a) Meta hotel-catalog image fields, specs, ingestion and caching; risks of regenerating images daily

### Takeaway
Meta takes up to 20 images per hotel as `image[i].url` / `image[i].tag` (minimum 500×500, JPG/GIF/PNG; 1024×1024 recommended for carousel). Meta's documented fetch logic **does not re-download an image when the URL stays the same but the content changes**. A new URL makes the item "Outdated" and schedules a re-fetch. Meta also throttles items whose URL changes while the content does not, and it warns against timestamp-style URL changes. Image fetches are scheduled lazily: only items with pixel/app events, or items selected for ad recommendation, get fetched. Regenerating all 9k images every night with new URLs is therefore costly and can backfire.

### Cited Findings
**Feed fields**
- Nested fields like `image` can be sent as JSON-encoded values or as flattened CSV columns in JSON-path syntax, e.g. `image[0].url`. — [Meta Hotel Ads – Catalog & Feed](https://developers.facebook.com/docs/marketing-api/hotel-ads/catalog) (as summarised in search results)
- Each image object has `url` and `tag`. Up to **20 images per hotel** are allowed, and at least one is required. — [Marin Software – Facebook Travel Ads](https://marinsoftware.helpjuice.com/facebook/facebook-travel-ads) (third-party; consistent with Meta's docs)
- `hotel_id` is required (string, max 100 chars). `base_price` is per-night, with an ISO currency code after a space (e.g. "199.00 EUR"). A separate Meta reference types it as an integer, which conflicts with the feed docs. — [Meta Hotel Ads – Catalog](https://developers.facebook.com/documentation/ads-commerce/marketing-api/hotel-ads/catalog); [Product Catalog Hotels reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/product-catalog/hotels)
- Meta's hotel-catalog migration guide (to the "enhanced catalog" infrastructure) says field names such as `hotel_id`, `name` and `price` did not change. — [Meta hotel catalog migration guide](https://developers.facebook.com/documentation/ads-commerce/catalog/guides/hotel-catalog-migration)

**Image specs (hotel catalog docs)**
- Formats: JPG, GIF or PNG. — [Meta Hotel Ads – Catalog & Feed](https://developers.facebook.com/docs/marketing-api/hotel-ads/catalog)
- Minimum is 500×500 px for carousel/collection and for single-image ads (single image displays at 1.91:1). Recommended is 1024×1024 for carousel/collection and 1200×628 for single image. — same source
- File size: no hotel-specific limit was found. Destination-catalog docs say each image can be up to **4 MB**. Secondary guides cite **8 MB** for generic catalog images, which was not verified. — [Meta Destination Ads – Catalog](https://developers.facebook.com/docs/marketing-api/destination-ads/catalog); 8 MB claim appeared only in third-party guides
- Meta has introduced automatic image resizing/cropping for Advantage+ catalog ads. Branded tiles with edge-to-edge text can be cropped. — [Swipe Insight: Meta introduces automatic image resizing for Advantage+ catalog ads](https://web.swipeinsight.app/posts/meta-introduces-automatic-image-resizing-for-advantage-catalog-ads-12109) (date not shown)

**Native overlays (the alternative to baking price into the image)**
- Hotel catalog ads support native overlays for **price, strikethrough and % off**, filled from the feed's price/sale_price. Strikethrough and % off are **hotel-only**. Overlay shapes are pill, circle and triangle. — [Meta Travel Ads docs](https://developers.facebook.com/docs/marketing-api/travel-ads); [Hotel template tags](https://developers.secure.facebook.com/docs/marketing-api/dynamic-ads-for-hotels/template-tags)

**Fetch/caching logic (Meta developer blog, 5 Jan 2021: the only primary source found)**
- If the image URL is unchanged but the image behind it changes, **Meta does not re-fetch**. — [Meta for Developers blog: Product catalog image fetching logic (2021-01-05)](https://developers.facebook.com/blog/post/2021/01/05/product-catalog-image-fetching-logic/)
- When an item's image URL changes, the item becomes **"Outdated"** and is rescheduled for a re-fetch. — same
- Fetching is **throttled for items that change the image URL without changing the image content**. Per the search summary, Meta also advises **against adding a timestamp to the URL**, which "has a high chance of stopping rescheduled fetches for those items." — same
- After a feed upload, Meta does **not** schedule image fetches for every item. Items are queued only when they have a pixel/app event or are pulled in for ad recommendation. — same
- Statuses include "Fetch Failed", "Partial Fetch" and "Not Fetched". If the main image fails, neither the main nor the additional images update. After consecutive failures, fetches for that item are **blocked for 12 hours**. Failures cover HTTP errors (503/403/404), advertiser-side throttling and blocking of Facebook's crawler. — same
- Caveat: no newer Meta documentation confirming or replacing these 2021 rules was found. The search tool also flagged the source as possibly outdated.

**Processing time / known issues**
- No official Meta propagation time was found for image updates. GoDataFeed (vendor) estimates **4–24 hours** after re-submission. — [GoDataFeed disapproval codes (Meta)](https://www.godatafeed.com/disapproval/meta-product-image-contains-placeholder-or-no-image-graphic)
- Bot protection (Fastly/Cloudflare/WAF) commonly returns 403 to `facebookexternalhit`. One host reports a 30 req/domain/min limit that returns 429, and the crawler caches 429 responses. — [Railway: Fastly blocking Meta crawler](https://station.railway.com/questions/fastly-bot-protection-blocking-facebook-a2b85d7c); [Ayrshare: Meta media crawler blocked](https://www.ayrshare.com/docs/help-center/technical-support/meta-media-crawler-blocked.md)
- Catalog API batch uploads have their own per-catalog rate limit (error 80014). This is separate from image fetching. — [Zeotap: Meta Product Catalog destination](https://composable-docs.zeotap.com/destinations/advertising/meta-catalog)
- Placeholder or "no image" graphics are disapproved. — [GoDataFeed](https://www.godatafeed.com/disapproval/meta-product-image-contains-placeholder-or-no-image-graphic)

### Inferences
- **Do not overwrite files in place.** Meta will keep serving the old cached tile, and price/branding will go stale.
- **Do not put the date or a timestamp in the URL every night.** It forces a re-fetch of all 9,093 items, risks throttling (and Meta explicitly discourages timestamps), and with lazy fetching many hotels could sit "Outdated" or show old images. Use a **content-hash URL** instead (e.g. `/tiles/{hotel_id}_{sha1(template_version+price_bucket+photo_id)[:10]}.jpg`). The URL then changes only when the rendered pixels actually change.
- **Keep the nightly KZT price out of the tile, or bucket it** (e.g. "от 25 000 ₸" rounded, or a weekly price band). Then rely on Meta's native hotel price/strikethrough/% overlays for live prices. Otherwise ~9k images change daily and lag reality by 4–24h or more, which risks showing a price that differs from the landing page.
- Keep the original hotel photo as `image[1..n]` and the branded tile as `image[0]`. Use a 1:1 1024×1024 or 1080×1080 JPG well under 4 MB, with a text-safe margin because of Meta's auto-cropping.
- Serve tiles from a CDN without bot challenges for `facebookexternalhit`. Expect a burst of thousands of GETs after a template change, so the host must not answer them with 429.
- Roll a template change out to everything at once only in a planned window. A failure blocks fetches for that item for 12h.

### Gaps
- No current (2025–2026) Meta Business Help page on catalog image caching was retrievable. Whether the 2021 rules still apply exactly is unverified.
- No official timing for processing ~9k image updates was found. Whether "Outdated" items keep serving the old image in delivery in the meantime is unconfirmed.
- The hotel-specific maximum file size was not confirmed. The exact allowed `image[].tag` values were not retrieved.

---

## (b) How in-house generation is typically built

### Takeaway
The common stacks are (1) raster compositing (Sharp/libvips, Pillow, ImageMagick), the fastest option, (2) JSX/HTML→SVG→PNG (Satori + resvg/Sharp, or Takumi), and (3) a headless browser (Puppeteer/Playwright), the most flexible and slowest. At 9k tiles, any of them finishes a full render in minutes to under an hour on one machine. Incremental rendering by content hash brings nightly work down to only the changed items.

### Cited Findings
- Sharp's docs publish benchmarks (sharp v0.35.0 / libvips v8.18.2 on AWS EC2) showing Sharp well ahead of ImageMagick, GraphicsMagick and Jimp on throughput. — [sharp performance](https://sharp.pixelplumbing.com/performance)
- A case study of a Satori pipeline reports ~900 ms/image with resvg, falling to **~200 ms/image** after switching rasterisation to Sharp. — [besthub.dev: Satori + resvg/Sharp backend image generation](https://www.besthub.dev/articles/using-satori-and-resvg-or-sharp-for-efficient-backend-image-generation-architecture-implementation-and-optimizations-2e9170b1e67d)
- One author claims Satori is "~5× quicker than headless Chrome" (not a controlled benchmark). — same
- A developer reports **p95 ≈ 1.4 s per image** for a Puppeteer card service. — [dev.to: OG images with Satori and resvg](https://dev.to/raxxostudios/generate-open-graph-images-on-the-fly-with-satori-and-resvg-3mke)
- Takumi (Rust) rasterises directly to PNG/JPEG/WebP without an SVG step. Its own docs claim it is 2–10× faster than Satori. — [Nuxt SEO: Takumi renderer](https://nuxtseo.com/docs/og-image/renderers/takumi)
- No published benchmark compares libvips, Puppeteer and Satori head-to-head. — (search result)

### Inferences
- Throughput estimates for 9,093 tiles (not measured; extrapolated from the figures above):
  - Satori+Sharp at 200 ms is about 30 min single-threaded, or under 5 min with 8 workers.
  - Puppeteer at about 1–1.4 s with a reused browser is about 2.5–3.5 h single-threaded, or about 20–30 min with 8 pages in parallel.
  - Pure Sharp/Pillow compositing (photo + logo PNG + pre-rendered text) is likely tens of ms per image, so minutes in total.
- Storage is small: about 9k × 150–300 KB JPG ≈ 1.5–3 GB per template version. That fits on S3/R2/any object store behind a CDN. Use immutable content-hash filenames with `Cache-Control: public, max-age=31536000, immutable`.
- A typical pipeline:
  1. The nightly feed job computes a render key per hotel (template version, photo URL, name, star rating, rating, price bucket).
  2. It diffs against the previous run and renders only changed keys.
  3. It uploads the new tiles.
  4. It writes the new URL into `image[0].url` (with `image[0].tag` e.g. "branded"), keeping the original photos as `image[1..]`.
  5. It garbage-collects old objects after about 30 days, since Meta may still reference them.
- Cyrillic/Kazakh text and the ₸ glyph need an embedded font that has those glyphs (Satori requires explicit font buffers). Test the rendering of "₸" and of Kazakh letters (әғқңөұүһі).

### Gaps
- No public engineering blog from an OTA was found that describes its catalog-tile renderer. No GitHub project dedicated to Meta hotel-feed tiles was found (search budget exhausted).

---

## (c) Third-party tool landscape

### Takeaway
Most tools work as "feed in → enriched feed out with new hosted image URLs" or push directly into the Meta catalog. Nearly all of them market to e-commerce product catalogs. **None of the sources found confirms native support for Meta *hotel* catalogs** except Hunch (travel case studies: G Adventures, flight/hotel claims) and Smartly (TUI case study). Published pricing is inconsistent across aggregators.

### Cited Findings
- **Confect**: Overlays prices, discounts and other info on Meta catalog/DPA images, and creates "Confect catalogs" (feed automations). Pricing conflicts between sources: G2 lists $299/$499/$999 per month (Local/Pro/Global), while Software Advice/SoftwareSuggest list from $149. It has a travel example (icelolly.com with the agency Journey Further), but no hotel-feed documentation was found. — [Capterra: Confect](https://www.capterra.com/p/236315/Confect/); [G2: Confect](https://www.g2.com/products/confect/reviews); [Confect: icelolly & Journey Further](https://confect.io/catalog-ad-of-the-week/icelolly-journey-further); [Confect academy: catalogs](https://academy.confect.io/articles/read/intoduction-to-feed-automations)
- **Hunch**: A creative studio with templates (or imported PSDs) connected to a catalog, which then launches ads on Facebook/Instagram/Snapchat, with up to 20 templates per catalog. It markets flight offers and hotel info/deals and has a G Adventures travel case study. A third-party review says pricing has a per-spend component; no published price was found. — [Hunch product](https://blog.hunchads.com/product); [Hunch: G Adventures](https://www.hunchads.com/customers/g-adventures-nl); [Hunch: dynamic travel ads mini case studies](https://content.hunchads.com/dynamic-travel-ads-3-mini-case-studies?hsLang=en); [admanage.ai Hunch review](https://admanage.ai/blog/hunch-ads-review)
- **Cropink**: Connects via an XML feed, Shopify or the Meta catalog, publishes directly to Meta, and lets you download the enriched feed for TikTok/Pinterest. It has hundreds of templates and a Figma plugin. Pricing is by product count, but its own pages conflict: "free for first 100 products", "free up to 25 products" and "from $39/mo". A third-party figure of €2,500/mo looks inconsistent. No hotel-feed mention was found. — [Cropink](https://cropink.com); [Cropink: alternative to Meta overlays](https://cropink.com/alternative-to-meta-overlays-for-product-ads); [G2: Cropink](https://www.g2.com/products/cropink)
- **Bannerbear** (generic image API, DIY feed): Reported 2026 plans are $49/mo for 1,000 credits, $149/mo for 10,000 and $299/mo for 50,000. One image at standard scale is 1 credit. A V5 help page shows $50/$150 instead. — [Bannerbear pricing](https://www.bannerbear.com/pricing); [Bannerbear: API credits](https://www.bannerbear.com/v5/help/articles/545-what-are-api-credits/)
- **Placid** (generic image API): Tiers are Basic (500 credits), Pro (2,500), Business (25,000) and VIP (100,000). One image is 1 credit and there are no overages. Prices conflict across sources ($19–$39 entry). — [Bannerbear vs Placid (2026, competitor blog)](https://www.bannerbear.com/blog/bannerbear-vs-placid/); [Templated: Placid alternatives](https://templated.io/blog/top-placid-alternatives-for-image-generation/)
- **Channable**: Its Image Editor templates are applied via Image Rules, which fill dynamic fields per item and output a PNG stored and hosted by Channable. It requires a Core plan plus a Creatives plan. One third-party estimate puts a full stack at €200+/mo. A Perfect Stay (travel) success story exists, but its content was not retrieved. — [Channable help: The Image Editor](https://helpcenter.channable.com/manage-improve-product-data/creatives-create-and-edit-images/the-image-editor); [Channable: Perfect Stay](https://channable.com/success-stories/perfect-stay); [Pricefy: Channable alternatives](https://www.pricefy.io/channable-alternatives)
- **Productsup**: Image Designer builds templates once and applies them across feeds (also offered as "dynamic image creation / richmedia"). Pricing is custom; one third-party lists from €49/mo. — [Productsup Image Designer](https://productsup.com/blog/productsup-image-designer/); [Productsup richmedia](https://www.productsup.com/platform/richmedia/)
- **DataFeedWatch**: A feed manager; no dedicated image-template product was found. A third party lists plans from $39/mo, while Software Advice says pricing is on request. — [Software Advice: DataFeedWatch](https://www.softwareadvice.com/catalog-management/datafeedwatch-profile/)
- **Feedonomics**: Pricing is custom by SKU count and channels, often estimated at $2,000+/mo (secondhand). It integrates with Marpipe for DPA creative. — [G2: Feedonomics pricing](https://www.g2.com/products/feedonomics/pricing); [Marpipe blog: Feedonomics review](https://marpipe.com/blog/feedonomics-reviewed-2025-product-feed-management-tools)
- **Marpipe**: Third-party pricing figures conflict: $199 Startup / $999 Enterprise, or $399/mo. G2 says the vendor publishes no pricing. — [Quickads: Marpipe pricing](https://www.quickads.ai/blog/marpipe-pricing-for-e-commerce-brands); [PricingSaaS: Marpipe](https://pricingsaas.com/companies/marpipe)
- **Smartly**: No public pricing; it is enterprise and reportedly scales with ad spend (a competitor's claim). It has a travel case study in which Smartly AI personalised ads for TUI, reporting +15% purchases. — [Marpipe: Smartly alternatives](https://marpipe.com/blog/smartly-alternatives); [Smartly: TUI case](https://smartly.io/resources/smartly-ai-enhances-ads-personalization-for-tui-and-delivers-15-more-purchases)
- **Creatopy**: No pricing or hotel-feed information was found in this search.

**Evidence of big travel players**
- Meta's dynamic ads for travel case studies exist for Airbnb (3× ROAS, −47% CPA, 238M people reached) and BookingBuddy (2× revenue). The summaries do not say whether the images were branded/pre-rendered. — [Airbnb case](https://www.casestudies.com/company/facebook/case-study/reaching-travelers-with-facebook-and-instagram-dynamic-ads-for-travel-for-broad-audiences); [BookingBuddy case](https://www.casestudies.com/company/facebook/case-study/driving-online-travel-bookings-with-facebook-dynamic-ads)
- Booking.com's dynamic-ads case study is on **Snapchat**, pulling property images from its catalog. — [Booking.com Snapchat case](https://www.casestudies.com/company/snapchat/case-study/bookingcom-uses-dynamic-ads-for-remarketing-to-drive-incremental-bookings)
- Barceló Hotel Group automated Meta Advantage+ catalog ads with the agency Jakala (content not retrieved). — [Jakala: Barceló](https://www.jakala.com/insights/barcelo-hotel-group-boosting-bookings-with-an-automated-meta-advantage)
- An ad-library aggregator lists Booking.com ads, which could be used to inspect its tiles visually. — [AdManage ad library: Booking.com](https://admanage.ai/ad-library/booking.com)
- CIS: no sources were found on Aviasales, Ostrovok or Freedom Travel using branded catalog tiles. Meta is designated "extremist" and banned in Russia, which limits Russian OTAs' Meta catalog activity. — [Sostav.ru (banner text)](https://www.sostav.ru/blogs/283857/65707)

### Inferences
- For a hotel catalog, the e-commerce-first tools (Confect, Cropink, Marpipe) may not ingest Meta *hotel* catalogs natively. Check whether they can take a generic CSV/XML and return a CSV with new image URLs that you then map into `image[0].url` of the hotel feed. Channable, Productsup and Bannerbear/Placid fit this "feed → hosted image URL" pattern most naturally.
- Cost for 9,093 tiles:
  - API tools like Bannerbear: about $149/mo (10k credits) if only changed tiles are re-rendered; a full nightly re-render (~275k/mo) exceeds every listed plan.
  - Feed platforms (Channable, Productsup): likely €200–€2,000+/mo.
  - In-house: a few dollars per month of compute and storage, plus developer time.
- Because Livin already generates the CSV nightly in-house, in-house rendering with content-hash URLs is likely the lowest-friction, lowest-cost route. Vendors mainly add a visual template editor for marketers.
- The only confirmed evidence of large OTAs using *pre-rendered branded* tiles is indirect. Their ad-library creatives would need to be inspected visually (e.g. the Meta Ad Library, which is not accessible here).

### Gaps
- No vendor documentation explicitly confirmed Meta hotel-catalog (`hotel` vertical) support for Confect, Cropink, Marpipe, Channable or Productsup.
- No G2/Capterra review scores or Reddit (r/FacebookAds, r/PPC) threads were retrieved (search budget and fetch blocks).
- Creatopy pricing and features were not found. Exact current pricing pages could not be fetched; all prices are from aggregators and conflict.
- There was no direct evidence for Booking, Expedia, Trip.com or CIS OTAs (Aviasales, Ostrovok, Freedom Travel) using branded tiles on Meta.
