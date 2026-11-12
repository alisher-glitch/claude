# Links, trip dates and UTM in Meta hotel catalog ads (single image, carousel, collection + Instant Experience, app deep links)

Research date: 2026-11-12. Method caveat: developers.facebook.com, facebook.com/business/help, support.marinsoftware.com and hospitalitynet.org could not be fetched directly from this session (network policy). Meta Business Help Center text was retrieved verbatim through Meta's own Ads MCP help-article tool (help-center text current as of Nov 2026; it mentions "starting in March 2026" changes). Developer-doc content (template tags, template_url_spec) comes from search-engine extracts of those Meta pages, not full-page reads, so exact wording there should be re-checked by whoever has access. Livin context: catalog `url` = livin.kz/go redirect (for attribution) with `?startDate=...&endDate=...` appended from the feed.

## 1. Hotel URL template tags: where they work, defaults, past dates

### Takeaway
Meta's hotel template tags (`{{hotel.hotel_id}}`, `{{trip.checkin_date date_format:Y-m-d}}`, `{{trip.checkout_date ...}}`, filters like `| urlencode`) are meant for the ad-level `template_url_spec` (web/ios/android) set through the Marketing API. If no check-in date is known for the person, `trip.checkin_date` defaults to **the next day**. If `template_url_spec` is missing or cannot be rendered, Meta uses the catalog item's `url`. I found no documented behaviour for past dates and no documented `trip.length_of_stay` tag.

### Cited Findings
- `trip.checkin_date` is the check-in date Meta collected for the person from the advertiser's hotel events. **If no check-in date was collected, it defaults to the next day** (tomorrow), not today. — [Meta: Hotel Ads – Template Tags](https://developers.facebook.com/docs/marketing-api/hotel-ads/template-tags) (via search extract)
- The tags only work if the advertiser sends the required details in its hotel events (pixel/SDK: Search, ViewContent, InitiateCheckout, Purchase, with `checkin_date`/`checkout_date` as recommended parameters). — [Meta: Hotel Ads – Template Tags](https://developers.facebook.com/docs/marketing-api/hotel-ads/template-tags); [Meta Help: Standard pixel parameters for hotel ads](https://www.facebook.com/business/help/661142797646824)
- `date.today` and similar date tags use UTC unless a time zone is set. — [Meta: Hotel Ads – Template Tags](https://developers.facebook.com/docs/marketing-api/hotel-ads/template-tags) (via search extract)
- Meta's Travel Ads docs give a `template_url_spec` example with `ios` and `web` objects. Both build the URL from `hotel.hotel_id` plus `startDate={{trip.checkin_date date_format:Y-m-d | urlencode}}` and a matching `endDate` from `trip.checkout_date`. The iOS one uses a custom `example://` scheme. — [Meta: Travel Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/travel-ads) (via search extract)
- "Use the template_url_spec field to specify the URL that appears after someone clicks the ad. If you don't provide it, or we can't derive it when we render an ad, we display the URL from the catalog." — [Meta: Travel Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/travel-ads) (via search extract)
- Precedence in the hotel catalog docs: ad-level URLs override feed URLs. For deep links the order is ad-level `template_url_spec`, then the feed's `applink` object, then the website's App Links meta tags. — [Meta: Hotel Ads – Catalog & Feed](https://developers.facebook.com/docs/marketing-api/hotel-ads/catalog/) (via search extract)
- `length_of_stay` is documented as a **catalog feed field** for date-specific room prices (number of nights; pricing keyed on `checkin_date` + `length_of_stay`). Date-specific prices can be set for up to 180 days from feed upload. I found no `trip.length_of_stay` URL tag. — [Meta: Hotel Ads – Catalog & Feed](https://developers.facebook.com/docs/marketing-api/hotel-ads/catalog/); [Meta: Date-Specific Prices](https://developers.facebook.com/docs/marketing-api/dynamic-ads-for-hotels/dynamic-pricing/v2.12)
- Hotel-chain playbook: target people with a check-in date in the next 0–10 days, and stop showing ads once the check-in date has passed (booking-window audience rule). This is the documented way to avoid stale dates. — [Meta: Travel Roadmap – Hotel Chain](https://developers.facebook.com/docs/marketing-api/travel-ads-smb/hotel-chain)
- Ads Manager (UI): with the Sales objective and a catalog, "you'll only see the URL parameters field. The website URL field is not supported." — [Meta Help: Specifications for dynamic URL parameters](https://www.facebook.com/business/help/2360940870872492)
- Ads Manager: "people who click or tap on a product in your ad are sent to its product link from your catalog. The website URL doesn't override product links." The website URL is used only for the profile/end card in a carousel. To override, choose "Override catalog deep links" (website) or enter an iOS/Android deep link. — [Meta Help: Create Meta Advantage+ catalog ads](https://www.facebook.com/business/help/1132465490107046)
- Parameters in the URL parameters field are appended to the destination URL unless they duplicate one already there. On a duplicate, the URL-parameters value wins: `utm_source=1` in the URL plus `utm_source=2` in URL parameters gives `utm_source=2`. Don't leave keys empty (`background=&foo=bar`). — [Meta Help: Add URL parameters to your Meta ads](https://www.facebook.com/business/help/1016122818401732)
- Third party (Marin) lists the accepted feed/event check-in formats as YYYYMMDD, YYYY-MM-DD and YYYY-MM-DDThh:mmTZD. — [Marin Support: Facebook Travel Ads](https://support.marinsoftware.com/en_US/facebook/facebook-travel-ads) (search extract only)

### Inferences
- In Ads Manager there is no "Website URL" box for catalog sales ads, so `trip.*` tags would have to go in the URL parameters field (for example `startDate={{trip.checkin_date date_format:Y-m-d}}`) or in `template_url_spec` via the API. Meta's help pages only list `ad.*`, `campaign.*`, `placement` etc. as URL-parameters tags. Whether `trip.*` renders in that field is **not documented** and needs a live test.
- For Livin: the feed URL already carries static `startDate`/`endDate`. If Meta also appends `startDate` through the URL parameters field, Meta's duplicate rule means **Meta's value overrides the feed's**. The person would then see Meta's personalised date, or tomorrow when Meta has no date. If the livin.kz/go redirect does not forward query parameters to the final page, both are lost.
- Past dates: no source says Meta rolls a past `trip.checkin_date` forward. A retargeted user whose search date has passed may get a past date, so the landing page/redirect should validate dates and roll forward or fall back. The booking-window "stop after check-in" audience rule is the documented mitigation.

### Gaps
- Full text of the Template Tags reference (all `trip.*` tags, whether `checkout_date` has its own default, for example check-in + 1 night) could not be read. Developers.facebook.com was blocked.
- No source on whether `trip.*` tags are expanded inside the Ads Manager URL parameters field (as opposed to `template_url_spec`).
- No source on past-date handling.

## 2. Collection, Instant Experience storefront and Instagram

### Takeaway
In a catalog collection ad, tapping the cover opens a full-screen Instant Experience (IE), and tapping a product tile opens the **product link from the catalog** (or an override). Meta's help states in its exact wording: **"Dynamic URL parameters are not supported for ads in collection format on Instagram placements."** It does not say whether this covers `trip.*` hotel tags. Since Jun 2025, IE opens no longer count as landing page views.

### Cited Findings
- Exact note from Meta Help: "Note: Dynamic URL parameters are not supported for ads in collection format on Instagram placements." Supported dynamic parameters listed: `{{ad.id}}`, `{{adset.id}}`, `{{campaign.id}}`, `{{ad.name}}`, `{{adset.name}}`, `{{campaign.name}}`, `{{placement}}`, `{{site_source_name}}`, `{{media_type}}` (Advantage+ catalog ads only). Name-based values are frozen at first publish. — [Meta Help: Specifications for dynamic URL parameters](https://www.facebook.com/business/help/2360940870872492)
- Collection format: "When someone taps on the cover image or video, a full-screen Instant Experience will open… When someone taps on the smaller product images, product detail pages provided by you will open." Collection is mobile-only. Placements include FB Feed/Marketplace/Stories/Reels and IG Feed/Stories/Reels/Explore home. The Lookbook IE template doesn't work on Instagram, and Digital Circular doesn't work on IG Reels. — [Meta Help: Supported objectives and placements for collection ads](https://www.facebook.com/business/help/2445340345521914)
- "Starting in March 2026, all single media and Advantage+ catalog collection ads on Facebook Feed will no longer display a URL in the ad footer." — [Meta Help: Create Meta Advantage+ catalog ads](https://www.facebook.com/business/help/1132465490107046)
- "A URL parameter is only applicable to the first product page… if they click out of the product page from the ad experience and come back… organically later on, the URL parameter will be lost." — [Meta Help: Add URL parameters to your Meta ads](https://www.facebook.com/business/help/1016122818401732)
- Meta changed collection-ad reporting so that opening the Instant Experience is **no longer counted as a landing page view**. Before, IE entry counted as an LPV even without a website visit. Effective June 2025. — [Cendyn: Meta Collection Ads reporting – LPV changes explained](https://www.cendyn.com/blog/metas-collection-ads-reporting-update-lpvs) (search extract; also republished on [Hospitality Net](https://www.hospitalitynet.org/opinion/4127929/meta-collection-ads-reporting-landing-page-view-lpv-changes-explained))
- Collection with a catalog needs a product set plus a matching Instant Experience. The flow is feed, then IE, then product link to the site or app. — [Meta: Collection Ads (Marketing API)](https://developers.facebook.com/docs/marketing-api/creative/collection-ads) (search extract)

### Inferences
- What the person lands on, by format (catalog sales ad, Ads Manager):
  - **Single image, carousel product card, collection grid tile, product tap inside the IE storefront:** the catalog item `url` (for Livin, livin.kz/go?…&startDate&endDate) plus the ad's URL parameters, unless "Override catalog deep links" or `template_url_spec` is set. The landing page opens in the FB/IG in-app browser.
  - **Carousel end/profile card:** the ad's Website URL.
  - **Collection cover tap:** no website, only the IE. The site is reached on a second tap (a product or CTA inside the IE).
- "Dynamic URL parameters" in the Instagram collection note most likely means the `{{…}}` macros in the URL parameters field. Hotel `trip.*` tags use the same `{{ }}` templating, so the safe assumption is they **may also fail on Instagram collection**, until tested. Static UTMs (no braces) are unaffected by that note. Static parameters baked into the feed URL (such as Livin's `startDate`/`endDate`) don't depend on Meta templating and should survive.
- Since the IE is an extra hop, clicks on the cover that only open the IE inflate "link clicks" relative to sessions. Website sessions and LPVs come only from the second tap. Expect a larger click-to-session gap for collection than for carousel or single image.

### Gaps
- No Meta source says whether `template_url_spec` (with `trip.*`) is used for product taps inside an IE storefront, or whether the IE uses the raw catalog `url`.
- No Meta source says whether the Instagram-collection restriction also strips static URL parameters, or only leaves `{{…}}` unexpanded or removed. No forum reports found.

## 3. App deep links (catalog applink, template_url_spec ios/android, collection/IE, deferred)

### Takeaway
Catalog items can carry `applink.ios_url` / `applink.android_url`, among others. If the app isn't installed, the link falls back to the website or app store. Ad-level deep links (Ads Manager "iOS/Android deep link" or API `template_url_spec.ios/android`) override catalog applinks. Universal Links / Android App Links are recommended. Deferred deep linking is for app-install campaigns and needs the Facebook SDK (iOS SDK 18.0.3 or later for iOS 14.5+).

### Cited Findings
- Catalog fields: `applink.ios_url`: "A deep link to your app on iOS… if installed. If the app isn't installed, the link redirects to your website or the App Store." `applink.android_url` works the same way, with Google Play. — [Meta Help: Catalog data specifications (other products)](https://www.facebook.com/business/help/1471103771472267)
- "Meta currently supports… Apple's universal links and Android App Links (recommended)." You can set them in Ads Manager (deep link field at ad level; "for ads with product media, you can enter the product.url template in the deep link field"), in the catalog app-link fields, or via "template links for dynamic ads" in the Marketing API. Custom URL schemes and Facebook App Links are also supported. — [Meta Help: Use app deep links as your destination](https://www.facebook.com/business/help/1627795160837067)
- Deep links re-engage installed users (Traffic/Engagement objectives). Deferred deep links send non-installers to the store and then to the content on first open. They are used for app-install ads and need the FB SDK. "Your app must use the Facebook SDK for iOS on version 18.0.3 or above to use deferred deep linking in campaigns targeting iOS 14.5+ users." — [Meta Help: Use app deep links as your destination](https://www.facebook.com/business/help/1627795160837067)
- In the Ads Manager catalog flow you can enter an app link under "iOS deep link" or "Android deep link" to override product links. — [Meta Help: Create Meta Advantage+ catalog ads](https://www.facebook.com/business/help/1132465490107046)
- Dynamic URL parameters "also work with any mobile app deep links". For App Promotion: "add your dynamic URL parameters to the end of your deferred deep link. There is no separate URL parameters field." — [Meta Help: Specifications for dynamic URL parameters](https://www.facebook.com/business/help/2360940870872492)
- Deep-link precedence for hotel ads: ad `template_url_spec`, then feed `applink`, then website App Links meta tags. — [Meta: Hotel Ads – Catalog & Feed](https://developers.facebook.com/docs/marketing-api/hotel-ads/catalog/) (search extract)
- Branch: Meta's deferred deep linking for ads relies on a browser-based flow, so a Branch Ad Link is needed. Meta shows a "Leave Facebook" interstitial when users exit the in-app browser from paid media. — [Branch: Meta Ads deferred deep linking](https://help.branch.io/marketer-hub/docs/meta-ads-deferred-deep-linking) (search extract)

### Inferences
- For Livin, the safest app route is to make livin.kz URLs Universal Links / App Links. The same catalog `url` (with dates) then opens the app if installed and the in-app browser otherwise. Separate custom-scheme `applink` fields would need their own date parameters, because `startDate`/`endDate` in the web `url` aren't copied to `applink.*`.
- Universal Links often don't trigger from inside the FB/IG in-app browser on iOS. This is general platform behaviour and is not sourced here, so the web fallback through livin.kz/go should be expected for most taps.
- I found no documentation of IE-specific deep-link behaviour. Assume product taps in the IE follow the same product link or applink rules as feed tiles.

### Gaps
- No Meta source covers deep-link behaviour specifically inside an Instant Experience storefront.

## 4. Known issues from forums (dates missing, UTM stripped, IE breaking attribution)

### Takeaway
I found no Reddit or Stack Overflow threads on hotel `trip.*` dates missing or wrong in Meta ads. Documented and agency-reported issues are general. UTMs are lost after the first page or on redirects. GA4 ignores `fbclid`, so UTMs are required. IE no longer counts as LPV. Tags are not expanded in Ads Manager previews.

### Cited Findings
- Meta itself: URL parameters apply only to the first landing page and are lost if the user leaves and returns organically. — [Meta Help: Add URL parameters to your Meta ads](https://www.facebook.com/business/help/1016122818401732)
- Adding URL parameters in Ads Manager "will override any parameters you have set elsewhere, such as in Instagram's default URL parameters". Meta may auto-add source, medium=paid and ad/campaign/adset IDs (since Jan 1, 2024). — [Meta Help: Add URL parameters to your Meta ads](https://www.facebook.com/business/help/1016122818401732)
- GA4 doesn't read `fbclid` for channel attribution, so without UTMs, Meta traffic may show as referral. Redirect hops commonly drop query strings unless they are re-appended. — [utmguard: Platform click ID conflicts](https://www.utmguard.com/blog/platform-click-id-conflicts); [Twinslytics: UTMs break at redirects](https://twinslytics.com/blog-why-utm-parameters-break-at-checkout-redirects-and-how-to-fi) (third-party, general)
- The Ads Manager preview doesn't substitute tokens, so `{{…}}` appears literally in previews. Name tokens lock at publish. — [Admanage: UTM parameters for Meta ads (2026)](https://admanage.ai/blog/utm-parameters-for-facebook-ads); [Meta Help 2360940870872492](https://www.facebook.com/business/help/2360940870872492)
- An LPV reporting glitch on Meta ran Jan 6–14, 2026 (resolved Jan 13). — [Aimerce: What was going on with LPV](https://www.aimerce.ai/blogs/what-the-heck-was-going-on-with-lpv-on-meta-ads) (search extract)
- Hotel-agency example of poor Facebook hotel-ad landing setups (generic homepage instead of hotel or dates). — [Direct Your Bookings: Facebook Hotel Ads (bad) example](https://www.directyourbookings.com/blog/marketing/facebook-hotel-ads-bad-example/) (title only; not read)

### Inferences
- Likely failure points for Livin: (a) livin.kz/go not forwarding `utm_*`, `fbclid` and `startDate`/`endDate` to the final URL; (b) duplicate `startDate` from feed and URL params (Meta's wins); (c) Instagram collection placements dropping `{{…}}` UTMs; (d) the IE hop making clicks exceed sessions.

### Gaps
- No primary forum evidence (Reddit/SO) was found for hotel date-tag bugs. Absence of reports is not proof the bugs don't exist. The search coverage of Reddit was weak.

## 5. Best practice for UTMs in catalog ads and the attribution impact of IE

### Takeaway
Put UTMs in the ad-level URL parameters field, not in the catalog. Use static `utm_source`/`utm_medium` and dynamic IDs (`{{campaign.id}}`, `{{adset.id}}`, `{{ad.id}}`, `{{placement}}`, `{{site_source_name}}`). Keep a static fallback, because dynamic tags are documented as unsupported for collection on Instagram. Have the redirect pass through every query parameter and `fbclid`. Treat IE "clicks" as non-site traffic and compare sessions against outbound clicks or LPVs.

### Cited Findings
- Meta's example: `utm_campaign={{campaign.name}}&utm_content={{ad.name}}`. Spaces are encoded as `%20`. Changing URL parameters after publishing can re-trigger the learning phase. — [Meta Help: Specifications for dynamic URL parameters](https://www.facebook.com/business/help/2360940870872492)
- With catalog sales ads, only the URL parameters field is available, not the Website URL. — [Meta Help 2360940870872492](https://www.facebook.com/business/help/2360940870872492)
- IE entries no longer count as LPVs (since June 2025), so collection LPVs now reflect only real site loads. — [Cendyn](https://www.cendyn.com/blog/metas-collection-ads-reporting-update-lpvs)

### Inferences
- Recommended for Livin (inference): use static `utm_source=meta&utm_medium=paid_social` plus `utm_campaign={{campaign.id}}&utm_content={{ad.id}}&utm_term={{placement}}`, and also encode the format statically per ad (for example `fmt=collection`), because there is no Meta macro for format. Test an Instagram collection ad to see whether `{{…}}` arrives. For dates, prefer the feed's static `startDate`/`endDate` plus server-side roll-forward over relying on `trip.*`. Add `trip.*` through the API `template_url_spec` only after testing.
- IE attribution impact: one extra tap and an in-app session. Meta's own conversion attribution (pixel/CAPI with `fbclid`/`fbc`) is unaffected if the final page receives `fbclid`. Last-click analytics (GA4/PostHog) depend on the redirect keeping the parameters.

### Gaps
- No Meta or third-party benchmark found for click loss between the IE and the site for hotel catalogs.
