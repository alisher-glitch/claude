# Branded/overlaid Meta catalog tiles: performance evidence and policy/legal risk (KZ focus)

Research date: 2026-11-12. Method note: only WebSearch could be used. WebFetch failed because confect.io, dataiads.io and adilet.zan.kz are outside this session's network allowlist, so the findings below rely on search-result excerpts. The exact wording of statutes and vendor pages has **not** been read from the primary pages. Anything legally decisive must be checked against adilet.zan.kz.

Labels used: **[VENDOR]** = published by a company that sells overlay or design tooling. **[META]** = Meta's own documentation. **[3P]** = third-party blog or agency, no product stake shown. **[LAW]** = statute text, usually from an unofficial aggregator.

---

## Q1. Do branded frames, price overlays or rating overlays outperform plain product photos in Meta catalog/dynamic ads (CTR, CVR, ROAS), especially in travel/hotels?

### Takeaway
I found no independent, controlled evidence (Meta-published, academic, or neutral third-party) that overlays beat plain catalog images on Meta. Almost every quantified "lift" comes from vendors that sell overlay tools: Confect, Marpipe, Canned Banners and Amadeus/TravelClick. These are self-selected wins with weak or undisclosed controls. The more credible pattern is "it depends". Overlays often lift CTR, but the CVR/ROAS effect is mixed and sometimes negative, and it varies by product, brand type and offer type. Meta itself publishes no lift numbers for its native "dynamic overlays" feature.

### Cited Findings
**Aggregate vendor data (Confect) [VENDOR]**
- Confect: across 268 companies tested June–Dec 2023 (minimum 1M impressions each), the *median* company saw +31.3% ROAS, +23.4% CTR and −25.3% CPA on Confect-designed catalog ads vs. its normal catalog ads. — [Confect by the numbers](https://confect.io/about-confect). Caveats: vendor-run, the sample consists of Confect customers (selection bias), and the comparison is "designed template vs. default", not one overlay element in isolation. The split methodology was not visible in the excerpt.
- In Confect's template data, adding extra product images to the design *decreased* average ROAS by about 1%. Confect therefore reports some design elements as neutral or negative. — [Confect: Catalog Ads designs cheat sheet](https://confect.io/tactics/catalog-ads-designs-the-big-cheat-sheet) (via search summary)
- A third-party write-up of a Confect study (~6.5 billion impressions) reports:
  - a "free shipping" overlay gave **+11% ROAS for multi-brand stores** but **−38% ROAS for DTC brands**
  - visible star ratings gave +5–15% CTR "across verticals" (lightly documented).
  — [dataiads: catalog ads visual signals / Andromeda](https://www.dataiads.io/en/blog/catalog-ads-visual-signals-andromeda) (secondary report of vendor data; not verified at source)

**Individual vendor cases [VENDOR]**
- Arena Sports (Confect) tested 3 arms: a default catalog ad; product image + price + sale text; and two product images with **no price**. The no-price, two-image design won, with +34% ROAS and +18% CTR vs. the default. The price overlay arm was *not* the winner. — [Confect case: Arena Sports](https://confect.io/cases/arena-sports-increased-catalog-ads-roas-by-34-with-confect)
- Other Confect cases report large wins: Hummel/Oui Oui +93% ROAS, −54% CPA, +85% CVR; ROImonks +97% ROAS and +70% CTR (original vs. backup templates run in parallel); Vero Moda +60% sales; Rock Luggage +35% ROAS; Frederik and Louisa +102% ROAS; Jennifer Behr +76% ROAS. — [Hummel](https://confect.io/cases/hummel-increased-roas-by-93-with-confect), [ROImonks](https://confect.io/cases/roimonks-increased-roas-by-60-percent-with-confect), [Vero Moda](https://confect.io/blog/vero-moda-increased-catalog-ads-performance-by-60-with-confect), [Rock Luggage](https://confect.io/cases/how-incubeta-and-rock-luggage-increased-roas-by-35-with-confect), [Frederik and Louisa](https://confect.io/cases/how-inevo-and-frederik-and-louisa-achieved-a-102-percent-increase-in-roas-with-catalog-ads), [Jennifer Behr](https://confect.io/cases/maison-mrkt-increased-roas-76-percent-jennifer-behr-confect). These are selected success stories, and most do not isolate the overlay as the variable.
- Marpipe reports A/B tests where promo overlays beat plain catalog ads for Into The AM and Lane Bryant, and cites Vera Bradley +20% CTR. — [Marpipe: promo overlays](https://www.marpipe.com/blog/how-to-scale-catalog-ads-with-promo-overlaysed); [casestudies.com: Vera Bradley/Marpipe](https://www.casestudies.com/company/marpipe/case-study/vera-bradley-boosts-ctr-20-with-marpipe)
- Confect's own price guide says testing price display is advisable. It claims, without citing data, that *small shops typically get worse results by showing prices*. — [Confect: prices in dynamic product ads](https://confect.io/blog/showing-prices-in-dynamic-product-ads)

**Travel/hotel-specific (all vendor, mostly not Meta catalog)**
- Canned Banners, US hotel chain retargeting with live nightly rates in dynamic banners: CTR +137% and click-to-conversion +90% vs. ads without pricing. This was display retargeting, not confirmed as Meta, and is an old vendor blog. — [Canned Banners case study](http://www.cannedbanners.com/blog/case-study-dynamic-hotel-retargeting-with-pricing-and-availability/)
- Amadeus/TravelClick "Dynamic Rate Ads":
  - Brussels luxury hotel (search ads): CTR +52%, clicks +46%, CPC −17%, cost per booking −21%
  - six Australian luxury properties (social ads vs. manual remarketing): cost per booking −56%, ROAS 2.6x higher
  — [TravelClick: Dynamic Rate Ads](https://www.travelclick.com/insight/new-product-launch-dynamic-rate-ads/) [VENDOR]
- TikTok (not Meta), dynamic travel/catalog ads:
  - Accor: −46% cost per booking and 1.8x bookings vs. standard web-conversion campaigns
  - Address Hotels: 7x month-over-month ROAS (period comparison, no control)
  These compare catalog vs. non-catalog formats, not overlay vs. plain. — [TikTok: Accor](https://ads.tiktok.com/business/en-US/inspiration/accor-dynamic-travel-ads); [TikTok: Address Hotels](https://ads.tiktok.com/business/en/inspiration/address-hotels-resorts-case-study)
- StitcherAds, mobile travel app dynamic ads: 9x average ROAS and −13% cost per booking vs. target (no overlay isolation). — [StitcherAds case](https://stitcherads.com/case-studies/mobile-travel-app/) [VENDOR]
- Attribution caution for hotels: a hotel-marketing source says ROAS should be judged by total brand.com lift over time, not tracked campaign revenue. In one example Expedia reported 17:1 ROAS where the hotel's own estimate was about 4:1. — [Gourmet Marketing](https://www.gourmetmarketing.net/blog/the-true-cost-of-expedia-travel-ads-how-hotels-sacrifice-direct-revenue); [Hospitality Net case](https://www.hospitalitynet.org/news/4124326.html)

**Meta's own position [META]**
- In 2025 Meta added "dynamic overlays" (previously "labels") to Advantage+ catalog ads. They pull price, % reduction, free delivery and current price from the feed. Coverage dates the rollout or rename to around April–May 2025. No Meta lift data was published with the launch. — [Search Engine Land](https://searchengineland.com/meta-dynamic-overlays-advantage-catalog-ads-454657); [Social Media Today](https://www.socialmediatoday.com/news/facebook-advantage-plus-catalog-ads-overlay-offers/746337/); [ads-up.fr (05/05/2025)](https://ads-up.fr/en/meta-rolls-out-dynamic-overlays-for-advantage-catalogue-ads-campaigns/); [Social Samosa](https://www.socialsamosa.com/news-2/meta-adds-dynamic-overlays-advantage-catalog-ads-9025086)

### Inferences
- The defensible claim is "designed templates *can* lift CTR/ROAS for some advertisers; the effect is heterogeneous and must be tested". "Branded tiles outperform plain photos" is not supported as a general rule.
- Two vendor data points cut *against* price/promo overlays: the Arena Sports winner had no price, and free shipping gave −38% ROAS for DTC brands. A brand selling direct, like a hotel/apartment brand, should not assume a price overlay helps CVR. CTR gains from price can come with lower CVR.
- For travel, price-in-creative lifts come from older display/search vendor work with live rates. They do not translate directly to Meta catalog tiles, and they depend on the price being accurate in real time. Stale prices undermine both performance and compliance.
- The right method is a Meta A/B test (split audiences), comparing plain vs. frame vs. frame+price, with Advantage+ creative/dynamic media enhancements held constant. The KPI should be cost per paid booking, not CTR.

### Gaps
- No Meta-published case study or lift study isolating overlays was found.
- No independent, academic or agency study with a disclosed control design was found.
- No Reddit r/FacebookAds or r/PPC practitioner threads surfaced in search.
- No Meta hotel-catalog (Advantage+ catalog ads for travel) result isolating an overlay was found.
- Hunch and Cropink case studies did not surface.

---

## Q2. Is there evidence of negative effects: overlays reducing performance, conflicts with Advantage+ creative, or auto-crop cutting overlays?

### Takeaway
Negative effects are documented anecdotally and in vendor data, not in controlled studies:
- some overlay types lowered ROAS for some segments
- overlays may "feel cheap" on premium products
- price overlays may raise CTR while lowering CVR
- Meta's automated creative features (crop, dynamic media, enhancements) can alter or replace the designed tile.

Meta's own catalog image guidance advises against text, price and promo overlays baked into the feed image.

### Cited Findings
- Free-shipping overlay: −38% ROAS for DTC brands (Confect data via third party). — [dataiads](https://www.dataiads.io/en/blog/catalog-ads-visual-signals-andromeda) [VENDOR data, 3P report]
- Some products perform better without overlays, especially premium or lifestyle items where overlays "may feel cheap". Price overlays "often increase CTR but may decrease conversion". — [ROASPIG: catalog sales overlays](https://roaspig.com/blog/effective-catalog-sales-overlays/); [ROASPIG: creative customizations](https://roaspig.com/blog/catalog-ad-creative-customizations/) [3P/VENDOR]
- Advantage+ creative can crop images for different aspect ratios, adjust brightness and contrast, and add text overlays when it predicts a lift. Auto-cropping can hurt legibility. Sources disagree on whether enhancements are on or off by default, so check in Ads Manager. — [adlibrary: Advantage+ creative changes](https://adlibrary.com/posts/advantage-plus-creative-changes); [Apogee: Advantage+ controls](https://www.apogee.ad/en/features/advantage-plus/); [Interest Explorer](https://interestexplorer.io/advantage-plus-creative/) [3P]
- "Dynamic media" in Advantage+ catalog ads lets Meta choose catalog images *or videos* per viewer. This can bypass a designed image tile. — [Sprinklr help: Meta Advantage+ Creative](https://www.sprinklr.com/help/articles/facebook-advanced-capabilities/meta-advantage-creative/64f6f8fb9445bf586cdcc23e) [3P]
- One vendor's testing guide says to *always disable Dynamic Media Enhancements before overlay testing*. Otherwise Meta's substitutions contaminate the test. — [BigAtom help](https://support.bigatom.ai/en/articles/12751473-how-to-run-an-experiment-with-the-overlay-feature) [VENDOR]
- Meta's catalog image spec advises against text overlaying the product, CTAs, promo codes, watermarks and time-sensitive info such as temporary price drops. Images must be JPEG/PNG, ≤8 MB, minimum 500×500 px, with 1024×1024 recommended. — [Meta Business Help: Product image specifications for catalogues](https://en-gb.facebook.com/business/help/686259348512056) [META]
- Third-party guides say overlay-heavy images can get reduced delivery or policy flags. A claimed "20% text" limit is **not** confirmed on Meta pages, and another guide says the 20% rule is retired. — [Flow/pansyer](https://flow.pansyer.com/blog/meta-catalog-image-requirements-sizes-ratios-rejection-fixes); [adsuploader specs](https://adsuploader.com/blog/meta-catalog-ads-specs) [3P]

### Inferences
- Baking frames or prices into `image_link` goes against Meta's catalog image guidance. The cleaner architecture is a clean feed image plus overlays added at render time, either through Meta's native dynamic overlays or a template tool. Those also update when the price changes.
- With Advantage+ crop and dynamic media on, a designed square tile can be cropped (to 4:5 or 9:16) or replaced by another asset. Keep critical text inside a safe zone, and disable the relevant enhancements during tests.

### Gaps
- I found no quantified study of auto-crop damage to overlays.
- I could not confirm the current (late 2026) defaults for each Advantage+ creative enhancement in catalog ads.

---

## Q3. What do Meta's Advertising Standards say about prices, "from" prices, strike-through prices, competitor comparisons, catalog image content and hotel catalogs?

### Takeaway
Meta has broad "deceptive/misleading practices" rules that cover deceptive pricing. Ad, Page and landing page are reviewed together. I found **no** Meta rule that specifically governs strike-through prices, "from" prices or comparative ads naming a competitor. Risk on Meta's side is therefore enforcement under general deception rules and third-party IP rules. Local law (Q5) is stricter on comparisons.

### Cited Findings
- The Advertising Standards prohibit ads promoting products, services or offers "through deceptive or misleading practices". — [Meta Advertising Standards intro](https://transparency.meta.com/policies/ad-standards/) [META]
- The Prohibited Commercial Practices policy names **deceptive pricing** as an example of a banned practice. — [Meta: Prohibited Commercial Practices](https://transparency.meta.com/policies/ad-standards/deceptive-content/prohibited-commercial-practices/) [META]
- For eCommerce, Meta may review the Page, the ad content and the landing page together, and rejects misleading practices. It does not disclose what its systems check. — [Meta Business Help: Unacceptable Business Practices](https://www.facebook.com/business/help/2895682587380674) [META]
- Third-party interpretations:
  - "Free" bait pricing with mandatory shipping or subscription charges is flagged.
  - A "70% off" against a price never actually charged is flagged; show the discount against a real prior selling price.
  - Claims must be verifiable on the landing page.
  — [adsuploader: Meta ad guidelines 2026](https://adsuploader.com/blog/meta-ad-guidelines); [wittelsbach.ai](https://www.wittelsbach.ai/blog/facebook-ad-rejected-for-misleading-claims/); [gorevity](https://gorevity.com/best-practices-for-creating-ads-that-align-with-metas-guidelines/) [3P]
- Competitors and IP: ads may not contain content that infringes third-party IP, including trademarks. Rights holders can report via the IP Help Center or Brand Rights Protection. Meta's own marks have separate brand-usage and endorsement rules. — [Meta: Third-party infringement](https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/third-party-infringement/); [Meta: Copyrights and Trademarks](https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/copyright-and-trademarks); [Meta: Brand usage](https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/brand-usage/) [META]
- Catalog image guidance (see Q2): no price drops, promo codes or watermarks on the product image. — [Meta help 686259348512056](https://en-gb.facebook.com/business/help/686259348512056) [META]

### Inferences
- Practical rules for a hotel/apartment catalog:
  - (a) the price on the tile must match the price on the landing page for the same dates and occupancy, so "from X ₸" must be actually bookable at X
  - (b) a strike-through needs a genuine prior price
  - (c) don't use competitor names or logos on tiles (trademark complaints plus KZ law)
  - (d) keep feed images clean and render overlays dynamically, so price changes propagate
- Static price text baked into images goes stale as nightly rates change. That is the most likely path to a "deceptive pricing" rejection or a consumer complaint.

### Gaps
- I did not find Meta's verbatim rules on strike-through or reference pricing, "from" pricing, or comparative advertising.
- I did not find the hotel-catalog-specific commerce or ad policy text. The fields relevant to Meta hotel catalogs, such as `base_price`/`sale_price`, were not verified.

---

## Q4. AI-generated imagery in ads: Meta's "AI info" labels, when disclosure is required, status in 2026

### Takeaway
As of late 2026:
- **Automatic labels:** Meta applies "AI info" labels to ads made with its own gen-AI tools. Placement escalates next to "Sponsored" when a photorealistic AI human is introduced.
- **Third-party detection:** Per secondary sources, an update dated June 1, 2026 says Meta will detect third-party gen-AI via industry signals (C2PA/IPTC) and label it. The extent of the rollout is unclear.
- **Mandatory advertiser self-disclosure:** Required only for social-issue, electoral and political ads containing photorealistic digitally created or altered media.
- **Conflicting claims:** Some SEO/vendor blogs claim universal mandatory disclosure since 2026. Those claims are unverified and contradicted by other sources.

For a hotel advertiser, the real risk is *misrepresentation*: AI imagery that depicts a property, room or view differently from reality falls under deception rules and consumer law. Labelling is not the main issue.

### Cited Findings
- Labels on ads using Meta's gen-AI tools:
  - minor edits without a photorealistic human: no label
  - significant alterations: a lower-prominence label in the three-dot menu
  - photorealistic AI-generated human: a label placed next to "Sponsored"
  — [Bizcommunity](https://www.bizcommunity.com/article/metas-ai-transparency-effort-introduces-ad-content-labels-709732a); [Social Media Today](https://www.socialmediatoday.com/news/meta-updates-ai-content-disclosure-tags/739221/); [getcoai](https://getcoai.com/news/meta-enhances-transparency-with-new-labeling-requirements-for-ai-generated-ads) [3P press on Meta announcement]
- Mandatory disclosure for political, election and social-issue ads with photorealistic, digitally created or altered images, video or realistic audio. Basic edits such as cropping and sharpening are exempt. Announced Nov 2023 and in effect since 2024. — [TechCrunch 2023-11-08](https://techcrunch.com/2023/11/08/meta-will-start-requiring-disclosures-for-political-ads-manipulated-with-ai/); [Social Media Today](https://www.socialmediatoday.com/news/metas-new-disclosure-requirements-for-digitally-altered-ad-content-are-now/704266/)
- Meta's gen-AI ad tools are disallowed for "potentially sensitive topics", including housing, employment, health, pharma and **financial services**. — [Social Media Today](https://www.socialmediatoday.com/news/meta-outlines-new-rules-on-the-use-of-ai-generated-content-in-political-ads/699227/)
- 2026 status, all secondary sources:
  - Third-party AI detection via C2PA metadata, with Meta's newsroom post reportedly updated June 1, 2026 ("will begin"). — [rx-designer](https://rx-designer.com/insights/ai-generated-ads-disclosure-google-meta/); [ugcvids.ai](https://ugcvids.ai/blog/meta-ai-generated-creative-ad-policy-2026); [adplay.ai](https://adplay.ai/blog/made-with-ai-label-meta-ads)
  - Ordinary commercial ads with third-party AI need no manual disclosure. — [ugcvids.ai](https://ugcvids.ai/blog/meta-ai-generated-creative-ad-policy-2026); [fireplaceugc](https://fireplaceugc.com/blog/ai-ad-disclosure-rules)
  - **Contradicted by** claims that disclosure is now required for all AI-generated or significantly edited ads. — [adgenz.ai](https://www.adgenz.ai/blog/meta-ai-ad-disclosure-label-2026-guide)
  - Meta reportedly says not all ads using its features show the label yet. — [digitalapplied](https://www.digitalapplied.com/blog/ai-content-labeling-rules-advertisers-2026-reference)
- EU AI Act Art. 50 transparency duties and California's AI Transparency Act core requirements reportedly apply from Aug 2, 2026. These are not directly applicable to KZ-targeted ads. — [adplay.ai](https://adplay.ai/blog/made-with-ai-label-meta-ads)

### Inferences
- AI-generated lifestyle backgrounds are low risk if they are clearly illustrative. AI renders of rooms, views or amenities that don't exist are high risk under Meta's deception rules and under KZ "недостоверная реклама".
- If gen-AI is used for frames or backgrounds, assume an "AI info" label may appear, especially if C2PA metadata is present. Test whether the label affects CTR.

### Gaps
- I could not read Meta's primary 2026 newsroom or help-center text. The June 1, 2026 detection rollout and its scope are unverified.
- I found no KZ-specific rule on AI-generated imagery in advertising.

---

## Q5. Kazakhstan law (Закон РК «О рекламе» № 508-II of 19.12.2003 and related)

### Takeaway
KZ law is materially stricter than Meta's policies on **comparisons**. Per the aggregator text of Art. 7, advertising that "содержит сравнение рекламируемых товаров (работ, услуг) с товарами (работами, услугами) других физических или юридических лиц" counts as **недобросовестная** (unfair). That is a near-blanket ban on comparative ads, not just a ban on *incorrect* comparisons as in Russian law.

Other rules:
- Prices in ads for goods or services sold in KZ must be in **tenge**.
- Недостоверная реклама covers untrue claims about product characteristics, availability and payment terms.
- The law was amended in 2026 (editions dated 16.01.2026 and 16.03.2026; the current consolidated text is "по состоянию на 17.05.2026"). The content of these amendments is not confirmed.
- Financial-product advertising (relevant to cashback/bank-partner promos) is now governed by ARDFM requirements adopted Aug 2026. If an ad mentions cost, these require full disclosure of the rate, ГЭСВ, fees and commissions.

### Cited Findings
- The law is in force with amendments as of 17.05.2026. Art. 6 sets general requirements; Art. 7 is "Виды ненадлежащей рекламы" (недобросовестная, недостоверная, неэтичная, скрытая). — [prg.kz](https://prg.kz/document/?doc_id=1045608); [adilet (official, not fetched)](https://www.adilet.zan.kz/rus/docs/Z030000508_) [LAW]
- Art. 7 ch. 1 p. 1: недобросовестная реклама "содержит сравнение рекламируемых товаров (работ, услуг) с товарами (работами, услугами) других физических или юридических лиц". — [zakon.uchet.kz](https://zakon.uchet.kz/rus/docs/Z030000508_); [kodeksy-kz.com Art. 7](https://kodeksy-kz.com/ka/o_reklame/7.htm) [LAW, unofficial aggregators]
- Popular summary: недобросовестная = comparing with competitors, disparaging their reputation, copying their trademarks. Недостоверная = misleading the consumer about **price**, properties, composition, shelf life and other information. — [Alatau City Bank business article](https://alataucitybank.kz/business/osim/articles/zakon-o-reklame-chto-nuzhno-znat-predprinimatelyam-kazakhstana) [3P]
- Недостоверная реклама covers untrue information about product characteristics (nature, composition, method and date of manufacture, purpose, consumer properties, conditions of use), among others. — [Law text PDF (eurasiamsu.ru mirror)](https://eurasiamsu.ru/wp-content/uploads/2022/11/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD-%D0%BE-%D0%A0%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%B5.pdf) [LAW, older mirror]. A search-based check could not confirm the explicit "price" wording in the KZ Art. 7 list; that wording is confirmed only in the Russian ФЗ «О рекламе» Art. 5. This is an open point.
- Price in tenge: "указание цены (тарифов, расценок, ставок) осуществляется в тенге" for goods and services sold in KZ. — [kodeksy-kz.com Art. 6](https://kodeksy-kz.com/ka/o_reklame/6.htm); [online.zakon.kz](https://online.zakon.kz/Document/?doc_id=2045608) [LAW]
- Language: the general rule is Kazakh, with Russian and other languages optional. There is an exception for periodicals, internet resources and news agencies. Sources disagree on how this applies to online ads, so get legal advice. — [kodeksy-kz.com Art. 6](https://kodeksy-kz.com/ka/o_reklame/6.htm); [Mindbox](https://mindbox.ru/journal/experts/prodvizhenie-na-rynke-kazahstana/); [airpress.kz on the language law 2026](https://airpress.kz/social/zakon-o-yazykah-v-kazahstane/) [3P]
- Online advertising is also governed by the Закон «Об онлайн-платформах и онлайн-рекламе». Online ads must be clearly identifiable and labelled per the authorized body's procedure. — [Mindbox](https://mindbox.ru/journal/experts/prodvizhenie-na-rynke-kazahstana/); [Alatau City Bank](https://alataucitybank.kz/business/osim/articles/zakon-o-reklame-chto-nuzhno-znat-predprinimatelyam-kazakhstana) [3P]
- 2026 changes:
  - Amendment editions dated 16.01.2026 and 16.03.2026 (content not disclosed in the sources).
  - A reported ban from 2026 on state symbols in advertising.
  - The 2026 MRP is 4,325 ₸, which matters because fines are expressed in MRP.
  — [prg.kz](https://prg.kz/document/?doc_id=1045608); [aequitas.kz Q&A](https://www.aequitas.kz/press-center/publications/10-voprosov-yuristu-po-reklame-v-kazakhstane) [3P/LAW index]
- Financial products: an ARDFM resolution of 3 Aug 2026 approved "Требования к управлению финансовыми продуктами", including advertising and promotion requirements. If an ad states the product's cost, all related payments must be disclosed: the reward rate, ГЭСВ, tariffs, commissions and other costs. Ads must not mislead. Earlier reporting described this as a draft. — [zakon.kz](https://www.zakon.kz/pravo/6528067-trebovaniya-k-upravleniyu-finansovymi-produktami-utverdili-v-kazakhstane.html); [bes.media](https://bes.media/amp/kak-banki-i-mfo-budut-prodavat-kredity-i-strahovki-razbiraem-novye-pravila/); [kapital.kz](https://kapital.kz/finance/149236/v-kazahstane-vnedryat-novye-trebovaniya-k-upravleniyu-finansovymi-produktami.html)

### Inferences
- **Competitor comparisons on tiles** (for example "cheaper than Booking/Airbnb", or competitor price vs. ours) carry high legal risk in KZ under Art. 7 p. 1. This holds even if true, because the statutory text as quoted bans comparison itself. They also carry trademark risk on Meta. Recommendation: don't do it.
- **Prices on tiles:**
  - must be in ₸
  - must match the actual bookable price on the landing page
  - "от X ₸" must be genuinely available
  - a strike-through needs a real prior price
  Otherwise the ad risks being недостоверная, plus Meta "deceptive pricing" enforcement. Dynamic overlays sourced from a live feed are safer than static baked prices.
- **Cashback/bank-partner promos:** if a tile advertises a bank card or installment terms or rates, ARDFM's 2026 disclosure requirements likely reach the bank. Disclosure obligations would likely flow to co-marketing creative too, which suits a catalog tile poorly. Merchant-funded cashback (the hotel's own discount) is a different, consumer-promo matter. This is an inference; get a KZ lawyer to confirm.
- **AI imagery** depicting non-existent property features → недостоверная реклама risk (characteristics/consumer properties).

### Gaps
- I could not read the official adilet.zan.kz text, so the exact current wording of Art. 6, Art. 7 and the 2026 amendments is unverified.
- Whether the current Art. 7 list explicitly mentions "цена" is unverified.
- No specific KZ rules on cashback advertising, on "скидка"/reference-price substantiation, or on AI-generated imagery were found.
- No KZ enforcement cases (АЗРК/МКИ) involving Meta catalog ads were found.
- Fine amounts under the КоАП were not researched.
