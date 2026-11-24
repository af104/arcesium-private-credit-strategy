# Private Credit Market and Fund Operations Tech Market Sizing (as of late 2026)

Notes for an Excel revenue scenario model of Arcesium selling into private credit managers. Each figure is labeled with its data year and whether it is REPORTED (survey or filing data) or ESTIMATE/FORECAST. "Derived" means my own arithmetic on sourced numbers.

## 1. Global private credit AUM: current size and projections

### Takeaway
Reported global private credit AUM was about $3.5T at end-2024 (ACC/AIMA definition, broad). Narrower Preqin-style "private debt fund" definitions put it at roughly $1.7-2.0T. Forecasts for 2029-2030 cluster around $2.6T (Preqin 2024 forecast, narrow) to $4.5T (BlackRock, and Preqin's 2025 report). Pick one definition and use it consistently in the model, because the gap between definitions is wider than the growth assumptions.

### Cited Findings
- **$3.5T global private credit AUM at end-2024, up 17% from end-2023** (REPORTED, 2024 data). From ACC (AIMA) and Houlihan Lokey, *Financing the Economy 2025*, released Dec 2025., [Investment Executive](https://www.investmentexecutive.com/news/research-and-markets/global-private-credit-market-reaches-us3-5-trillion-aum-threshold-report/); [ACC report page](https://acc.aima.org/compass/insights/private-credit/financing-the-economy-2025.html)
- Same ACC report (2024 data, REPORTED):
  - ACC membership is 250 managers holding over $2T of private credit assets.
  - The survey covered 49 managers with $2.1T AUM.
  - 2024 deployment was about $592.8B, up 78% from $333.4B in 2023.
  - The top 20% of managers deployed about 85% of capital.
  - The US accounts for 65% of AUM and 54% of deployment.
  - Corporate lending is 60% of investments. Asset-backed lending was 16% of 2024 deployment.
  - 80% of committed capital sits in closed-ended structures rather than semi-liquid ones.
  - Investor mix is 76% institutional, 24% HNW.
 , [Investment Executive](https://www.investmentexecutive.com/news/research-and-markets/global-private-credit-market-reaches-us3-5-trillion-aum-threshold-report/)
- **Preqin (Sep 2024 FORECAST):**
  - Private debt AUM reaches **$2.64T by 2029**, a 9.88% CAGR from end-2023 to 2029.
  - Direct lending grows at a 10.18% CAGR to **$1.33T by 2029**.
 , [Alternative Credit Investor](https://alternativecreditinvestor.com/2024/09/18/private-debt-aum-to-hit-2-64tn-by-2029/)
- **Preqin "Private Markets in 2030" (Oct 2025 FORECAST):** direct lending and other private credit strategies "projected to reach $4.5 trillion by 2030." Total alternatives are forecast at about $32T by 2030., [BusinessWire (Preqin release, 16 Oct 2025)](https://www.businesswire.com/news/home/20251016075672/en/Preqin-Releases-Private-Markets-in-2030-Report); [Alternative Credit Investor](https://alternativecreditinvestor.com/2025/10/16/global-alts-aum-to-hit-32tn-by-2030/)
- **BlackRock (Apr 2025 FORECAST):** "We see scope for private credit AUM to reach $4.5tn by 2030" (Q2 2025 Global Credit Quarterly)., [Alternative Credit Investor](https://alternativecreditinvestor.com/2025/04/07/blackrock-predicts-private-credit-aum-will-reach-4-5tn-by-2030/). BlackRock also published a Jan 2026 private credit primer, which I did not fetch: [PDF](https://www.blackrock.com/gls-download/literature/market-commentary/private-credit-primer-january-2026.pdf)
- **Forbes (Nov 2024, as cited by Arcesium):** private credit "projected to reach $2.8 trillion by 2028" (FORECAST, secondary citation)., [Arcesium blog](https://www.arcesium.com/blog/empowering-private-credit-operations-expanding-market)
- **US direct lending is about $1T** (REPORTED, PitchBook LCD/LSEG as of 30 Sep 2025). Semi-liquid wealth-channel vehicles "command almost a third" of it., [Morgan Stanley IM, Private Credit 2026 Outlook](https://www.morganstanley.com/im/es-es/intermediary-investor/insights/outlooks/private-credit-2026-outlook.html)
- **Credit AUM at the 8 large listed alternatives managers** (REPORTED, 2024): $2.33T, up 21.5%. This includes public and liquid credit, so it is not purely private.

  | Manager | 2024 credit AUM |
  |---|---|
  | Apollo | $616B |
  | Blackstone Credit & Insurance | $376B |
  | Ares | $349B |
  | Brookfield | $317B |
  | KKR | $276B |
  | Carlyle | $192B |
  | Blue Owl | $136B |
  | TPG Angelo Gordon | $72B |

 , [Preqin News](https://www.preqin.com/news/credit-aum-at-listed-alternatives-managers-rises-21-5-to-usd2-33tn-in-2024)
- **IMF:**
  - The Apr 2024 GFSR sized private credit at about **$2.1T (2023 data)**. This is widely reported as "$2 trillion" and I took it from secondary coverage, not the GFSR itself., [Crowdfund Insider](https://www.crowdfundinsider.com/2024/04/223642-2-trillion-private-credit-market-may-increase-financial-vulnerabilities-due-to-limited-oversight-report/); [IMF GFSR Apr 2024 infographic](https://www.imf.org/-/media/files/publications/gfsr/2024/april/english/infographic.pdf.md)
  - The Oct 2025 GFSR says US and European banks have about **$4.5T** of exposure to hedge funds, private credit and other NBFIs, roughly 9% of loan books. No standalone private credit figure is given., [Hedgeweek](https://www.hedgeweek.com/imf-flags-4-5tn-bank-exposure-to-hedge-funds-and-private-credit/)

### Inferences
- Suggested model base case, all derived:
  - **Broad ACC definition:** $3.5T (2024) growing at about 10-12%/yr gives roughly $4.2-4.4T for 2026E and $5.6-6.2T for 2030E.
  - **Narrow fund-AUM definition:** about $2.0T (2024), heading to $2.6-2.8T by 2028-29 per Preqin and Forbes.
  - BlackRock's and Preqin's 2025 figure of $4.5T by 2030 sits between the two. It works as a mid case if the base is about $2.5-3T today.
- The 17% growth in 2024 (ACC) and the 78% jump in deployment suggest near-term growth above the ~10% Preqin CAGR. A 12-15% upside scenario is defensible.

### Gaps
- I did not verify a Morgan Stanley global forecast. Figures circulating ($2.6T by 2029, $5T) could not be confirmed from a primary MS source.
- I did not find PitchBook's latest global private debt AUM figure. The [H1 2025 PitchBook Global Private Debt Report PDF](https://pitchbook.brightspotcdn.com/a7/b9/cea7abbf0976b65c715b477a159f/h1-2025-global-private-debt-report.pdf) exists but was not read.
- I did not retrieve a standalone private credit size from the IMF Oct 2025 GFSR.

## 2. Number of managers/funds, AUM tiers, fundraising, concentration

### Takeaway
I found no public source with a clean count of private credit managers by AUM tier. Available proxies:
- ACC has 250 member managers with more than $2T.
- Preqin shows 1,345 private debt funds in market.
- 136 managers run evergreen private credit vehicles.

The market is highly concentrated: the top 20 managers hold about 36% of dry powder and over 80% of evergreen AUM, and the top 20% of managers did about 85% of deployment.

### Cited Findings
- **1,345 private debt funds in market**, seeking a combined $490.4B (REPORTED, Preqin, early 2025)., [Preqin News](https://www.preqin.com/news/credit-aum-at-listed-alternatives-managers-rises-21-5-to-usd2-33tn-in-2024)
- **Private debt fundraising** (REPORTED, Preqin): $217.9B in 2024 vs $216.8B in 2023., [Preqin News](https://www.preqin.com/news/credit-aum-at-listed-alternatives-managers-rises-21-5-to-usd2-33tn-in-2024)
- **PitchBook (2024 data, REPORTED):**
  - Private debt fundraising topped $200B for the fifth straight year.
  - The number of funds closed fell more than 50% year on year.
  - More than 80% of closed funds were larger than their predecessors.
  - Megafund capital was $86.6B.
  - Emerging managers (3 or fewer funds) took only 6% of capital, down from 10.1% in 2023.
  - Direct lending was 60.7% of capital raised.
 , [Alternative Credit Investor](https://alternativecreditinvestor.com/2025/03/19/largest-managers-and-funds-increasingly-dominate-private-credit/)
- **Dry powder concentration** (REPORTED, Preqin/S&P, end-2024): the **top 20 managers hold 36%** of global private credit dry powder ($138B of $385B), and 17 of the 20 are US-based., [Alternative Credit Investor](https://alternativecreditinvestor.com/2025/01/07/more-than-one-third-of-dry-powder-is-held-by-top-20-private-credit-managers/); [S&P Global MI](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2025/1/top-20-private-credit-managers-hold-more-than-one-third-of-dry-powder-86886642)
- **Evergreen managers** (REPORTED, With Intelligence, Mar 2025): 136 managers run evergreen private credit. The top 5 hold $254B (over half), and the top 20 hold over 80%., [With Intelligence](https://www.withintelligence.com/insights/private-credit-funds-surpasses-500bn/)
- **ACC (2024 data):** the top 20% of surveyed managers deployed about 85% of capital ($503B), and there are 250 ACC member managers with more than $2T., [Investment Executive](https://www.investmentexecutive.com/news/research-and-markets/global-private-credit-market-reaches-us3-5-trillion-aum-threshold-report/)
- **H1 2026 fundraising:** five managers (Barings, Churchill, Crescent, Blackstone and others) raised about $64B. This is a secondary, lower-quality source and I have not verified it., [Angel Investors Network](https://angelinvestorsnetwork.com/market-analysis/private-credit-h1-2026-largest-fundraises-barings-churchill-crescent-blackstone)

### Inferences
- Illustrative tier model, an ESTIMATE to be validated with Preqin/PitchBook data. It is built from: 250 ACC members holding more than $2T, 8 listed mega-managers holding about $2.3T of credit, and 136 evergreen managers. These suggest a power-law distribution.

  | Tier | Approx. managers | Approx. share of AUM |
  |---|---|---|
  | $50B+ | ~15-25 | ~55-65% |
  | $10-50B | ~40-60 | ~20-25% |
  | $1-10B | ~200-300 | ~10-15% |
  | <$1B | ~1,000+ (mostly emerging) | <5% |

- For a vendor like Arcesium, the reachable "sweet spot" is likely the roughly 50-300 managers in the $5-50B range. The top 20 often build in-house or already run multi-vendor stacks.

### Gaps
- I found no public breakdown of manager counts by AUM tier, globally or for the US. This needs Preqin Pro or PitchBook data.
- I found no reliable total count of private credit managers. Preqin tracks thousands of private debt fund managers, but I found no citable 2025 number.

## 3. Growth drivers and operational pain points

### Takeaway
Growth is coming from wealth and evergreen vehicles (more than $500B evergreen AUM; non-traded BDCs at $170B), asset-based finance, insurance capital and bank disintermediation. Ops pain centers on Excel, loan lifecycle complexity (PIK, amendments, restructurings), fragmented books of record, more frequent NAVs and investor reporting demands. All of these point to daily or monthly NAV and data-platform needs, which favors Arcesium-type platforms.

### Cited Findings
- **Evergreen private credit AUM was $503B, up 27%** from $395B in H1 2024 (REPORTED, With Intelligence, Mar 2025):
  - Perpetual non-traded BDCs reached $170B in H2 2024, up 33% in six months.
  - BCRED alone was above $70B at year-end 2024.
  - Private institutional evergreen funds passed $100B.
 , [With Intelligence](https://www.withintelligence.com/insights/private-credit-funds-surpasses-500bn/)
- **Morningstar:** evergreen funds reached $534.6B, with AUM up 25% in 2025 (REPORTED; covers all evergreen private-market funds, not only credit)., [WealthManagement.com](https://www.wealthmanagement.com/alternative-investments/morningstar-evergreen-fund-aum-grew-by-25-in-2025)
- **Semi-liquid wealth vehicles are almost one third of the ~$1T US direct lending market**, and private credit CLOs took 20% of institutional CLO flows (Morgan Stanley IM 2026 outlook)., [Morgan Stanley IM](https://www.morganstanley.com/im/es-es/intermediary-investor/insights/outlooks/private-credit-2026-outlook.html)
- **Asset-backed lending was 16% of 2024 deployment**, and HNW investors supply 24% of capital (ACC 2025)., [Investment Executive](https://www.investmentexecutive.com/news/research-and-markets/global-private-credit-market-reaches-us3-5-trillion-aum-threshold-report/)
- Preqin's 2030 report cites newer, more liquid structures, bank disintermediation and new borrower supply as drivers. Preqin also frames US private credit as a potential "$34tn" addressable market through product expansion (headline only, not read)., [BusinessWire](https://www.businesswire.com/news/home/20251016075672/en/Preqin-Releases-Private-Markets-in-2030-Report); [Preqin News](https://www.preqin.com/news/product-expansion-makes-us-private-credit-a-potential-usd34tn-market)
- **Headwind:** non-traded BDC fundraising fell in Q4 2025, and 2026 coverage cites retail BDC redemption pressure., [Blue Vault](https://bluevaultpartners.com/nontraded-bdc-fundraising-falls-returns-rally-in-q4-2025/); [Angel Investors Network](https://angelinvestorsnetwork.com/market-analysis/private-credit-h1-2026-largest-fundraises-barings-churchill-crescent-blackstone)
- **Ops pain points:**
  - **Lumonic 2025 survey of 150 private credit firms:** most still run on Excel. Only 5% have integrated AI into underwriting or loan management, and only 10% use third-party tools for underwriting or portfolio management. Respondents prefer all-in-one solutions., [Lumonic](https://www.lumonic.com/content/the-state-of-private-credit-technology)
  - **CSC "Future Private Capital CFO 2025"** (300 GPs and 200 LPs, cross-asset):
    - 51% of GPs plan to expand outsourcing, and 63% plan to expand their tech frameworks.
    - 44% of LPs lack investment-level reporting, and 74% want daily or on-demand performance reporting.
    - Investor portals are the top LP frustration with GPs (35%).
    - 39% of GPs rank talent as their top concern.
   , [BusinessWire](https://www.businesswire.com/news/home/20250430162117/en)
  - **Arcesium's own framing:** manual loan accounting for drawdowns, prepayments and rollovers; PIK, restructurings and defaults; strategy diversity (direct lending vs ABF); split investment and accounting books of record; slow NAV/P&L., [Arcesium blog](https://www.arcesium.com/blog/empowering-private-credit-operations-expanding-market)

### Inferences
- The evergreen/BDC segment (about $500B+, growing 25-30%/yr in 2024-25) needs daily or monthly NAV, investor-level accounting and regulatory reporting. That makes it the highest-intensity buyer of middle and back office tech, and a natural priority segment for the model.
- ABF's share of deployment (16%) and its data complexity (loan-tape level) support a per-asset or data-volume pricing upsell.

### Gaps
- I found no hard figure on the share of private credit managers still primarily on spreadsheets. Lumonic says "majority" without a percentage.
- Insurance-capital share of private credit AUM was not retrieved.

## 4. Size and growth of the fund admin / investment ops software market and private markets software

### Takeaway
Credible analyst sizing of private-markets ops software is scarce in public sources. A useful proxy: the private markets data, analytics and software sector has an estimated $18B TAM by 2030 (Asymmetrix). Vendor scale benchmarks: Clearwater's ARR is $841M, Allvue's is over $200M, and Preqin sold for $3.5B. Generic "market research" sites (Grand View and similar) exist but are low quality.

### Cited Findings
- **Private markets data and analytics sector TAM is about $18B by 2030** (ESTIMATE, Asymmetrix newsletter, May 2025; no current size or CAGR given)., [Asymmetrix](https://asymmetrixintelligence.substack.com/p/whats-next-in-the-18bn-private-markets)
- **Allvue Systems** (REPORTED by Reuters sources, Aug 2026):
  - ARR is **over $200M**, growing more than 15%/yr, with margins above 30%.
  - Vista is exploring a sale at up to **$3B** including debt. It sought about $1.7B in its 2021 IPO attempt.
 , [Reuters via WHBL](https://whbl.com/2026/08/21/buyout-firm-vista-explores-3-billion-sale-of-private-markets-data-provider-allvue-sources-say/)
- **BlackRock completed its acquisition of Preqin** for £2.55B ($3.5B) in Mar 2025., [Reuters via WHBL](https://whbl.com/2026/08/21/buyout-firm-vista-explores-3-billion-sale-of-private-markets-data-provider-allvue-sources-say/)
- **Fund admin scale:** the 12 largest administrators added $2.5T of AUA and about 3,000 funds, and hired more than 2,000 staff, in the year to mid-2025 (The Drawdown Fund Admin Report 2025)., [The Drawdown](https://the-drawdown.com/article/fund-admin-report-2025-busy-bees)
- **Generic market-research estimates** exist (GMI fund accounting software; Market Research Future investment fund administration services; TBRC alternative investment software) but were not read, and I consider them low reliability., [GMI](https://gminsights.com/industry-analysis/fund-accounting-software-market/market-size); [MRFR](https://www.marketresearchfuture.com/reports/investment-fund-administration-services-market-67104); [GII/TBRC](https://www.giiresearch.com/report/tbrc1888060-alternative-investment-software-global-market.html)
- A BCA Research report, "Private market software: how big, how fragile" (Jun 2026), exists but is paywalled and not read., [BCA](https://www.bcaresearch.com/reports/private-market-software-how-big-how-fragile-15-06-2026/219796)

### Inferences
- Bottom-up cross-check, derived: if private credit is about $3.5-4T AUM and total tech plus outsourced ops spend runs about 3-6 bps of AUM (see Section 5), the private credit ops wallet is about **$1.0-2.4B per year**. Pure software is likely a third to half of that, about $0.4-1.0B. Treat this as a model assumption, not a sourced figure.

### Gaps
- I found no Celent, Aite-Novarica, Coalition or Burgiss estimate of private credit or private markets ops software spend in public sources.
- I found no published CAGR for fund administration services from a reputable source.

## 5. Pricing, contract values and vendor ARR proxies

### Takeaway
Public benchmarks for institutional middle-office SaaS pricing are thin. The best proxies are vendor ARR divided by client count:
- Clearwater: about $336K ARR per client on average, with 152 clients above $1M.
- Small-fund admin quotes: about $75-200K/yr for $50-250M funds, and $200-500K+ above $250M.

For Arcesium-scale platforms at $5-50B managers, low-seven-figure ACVs are plausible, but that is an inference.

### Cited Findings
- **Clearwater Analytics (CWAN), FY2025 REPORTED (Feb 2026 release):**
  - ARR was **$841M** at 31 Dec 2025, up 77% (boosted by the Enfusion and Beacon acquisitions).
  - FY revenue was $731.4M, and Q4 revenue was $217.5M (+72%).
  - It has over **2,500 clients**, with **152 above $1M ARR**.
  - Gross retention is 98% and net retention 109%.
  - CWAN agreed to an all-cash take-private at $24.55/share, expected to close Q2 2026, and gave no 2026 guidance.
 , [BusinessWire](https://www.businesswire.com/news/home/20260218581398/en/)
  - Derived: average ARR per client is about $336K or less ($841M / 2,500+).
- **Allvue:** ARR over $200M (Aug 2026, Reuters sources). Client count was not in the Reuters piece. A low-quality profile site claims "500+ clients," which would imply about $400K average ARR (unverified, derived)., [Reuters via WHBL](https://whbl.com/2026/08/21/buyout-firm-vista-explores-3-billion-sale-of-private-markets-data-provider-allvue-sources-say/); [yespress (unverified)](https://yespress.io/allvue-systems)
- **SS&C:** the FY2025 10-K is available (fund admin segment / GlobeOp) but its per-client metrics were not extracted., [SEC 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1402436/000119312526076745/ssnc-20251231.htm)
- **Small-fund admin pricing (VC Beast benchmark, Jul-Sep 2026, small VC-oriented funds):**
  - AngelList's published price is 0.10% of fund size plus $10K/yr (Institutional), or 0.15% plus $20K (Full Service).
  - Observed quote bands are about $25-75K/yr ($10-50M funds), $75-200K+ ($50-250M) and $200-500K+ (above $250M).
  - Caveat: the benchmark has a disclosed conflict (shared ownership with Archstone) and covers no private credit specifics.
 , [VC Beast](https://vcbeast.com/fund-admin-pricing-benchmark)

### Inferences
- **Arcesium ACV assumptions for the model** (ESTIMATES, derived from the proxies above):

  | Client tier | ACV range |
  |---|---|
  | $1-10B managers | ~$250K-750K |
  | $10-50B | ~$0.75-2.5M |
  | $50B+ | ~$2-5M+ (multi-product) |

  These are consistent with Clearwater's mix of a $336K average and 152 clients above $1M.
- Expressed as bps, $1M on a $10B book is 1 bp. Software-only pricing for large credit managers is likely in the **0.5-2 bps** range, and full outsourced fund admin is likely in the several-bps range. Neither range is sourced; both need validation.

### Gaps
- I found no public bps-of-AUM benchmark for institutional private credit fund administration or middle-office software.
- Arcesium's own revenue and client count were not found publicly.
- SS&C per-client data was not extracted.

## 6. Outsourcing rates

### Takeaway
Cross-asset private-funds surveys show outsourcing is near-universal at some level: 94% of North American private fund managers use third-party administrators for European funds. Outsourcing intent keeps rising (51% of GPs plan to expand it). I found no private-credit-specific outsourcing rate.

### Cited Findings
- **Ocorian survey (Oct 2024; North American PE, private debt, RE, VC and infra managers with $1.59T AUM; refers to European fund administration):**
  - 94% use third-party administrators to some extent, and 6% are fully in-house.
  - 42% use several third-party providers, and 17% use just one.
 , [Ocorian](https://www.ocorian.com/news-press-releases/outsourcing-takes-bigger-role-north-american-fund-managers)
- **CSC 2025:** 51% of GPs plan to expand outsourcing, and 70% of LPs view reputable global service providers positively., [BusinessWire](https://www.businesswire.com/news/home/20250430162117/en)
- Other relevant but unread sources:
  - [Gen II Mood Index on operating models](https://content.gen2fund.com/story/core-alternative-managers-mood-index-2024/page/6)
  - [Apex on outsourcing in private markets](https://www.apexgroup.com/insights/the-growing-role-of-outsourcing-in-private-markets/)
  - [Gen II on private credit fund admin](https://gen2fund.com/news/why-fund-administration-is-becoming-a-competitive-advantage-in-private-credit/)

### Inferences
- Model assumption: about 80-95% of private credit managers outsource at least fund accounting or investor services, while a smaller share, perhaps 30-50%, outsource middle-office loan ops and portfolio monitoring. That second figure is an ESTIMATE, not sourced. It implies software and co-sourcing vendors like Arcesium compete with, and partner with, administrators rather than replacing in-house teams.

### Gaps
- I found no private-credit-specific outsourcing rate (fund admin or middle office) from EY, ACC or Coalition. The EY Global Alternative Fund Survey 2025 likely has this but was not retrieved.
