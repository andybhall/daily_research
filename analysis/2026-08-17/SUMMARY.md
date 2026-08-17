# Markets & governance × AI — probes, 2026-08-17

## Top find — AI shareholder resolutions / AI in corporate governance
**Probe (SEC EDGAR full-text search API, efts.sec.gov, pulled today):** count of annual
proxy statements (Form DEF 14A) mentioning "artificial intelligence":

| Year | DEF 14A filings mentioning "artificial intelligence" |
|---|---|
| 2019 | 154 |
| 2021 | 331 |
| 2023 | 457 |
| 2024 | 794 |
| 2025 | 1,152 |
| 2026 | 1,432 |

A ~9× rise 2019→2026 — AI has swept into the proxy. The exact AI *shareholder-proposal*
language is far rarer (`"report on artificial intelligence"` returns 0–2/yr), so the
proposal-level panel must be assembled from EDGAR full-text + Form N-PX fund votes +
advocacy trackers (Open MIC, FTI, Harvard corpgov). Curated figures this run: 15 AI
resolutions in the 2024–25 proxy years, 12 of them at Alphabet/Amazon/Apple/Meta/Microsoft,
avg ~30% support, with AI-misinformation proposals hitting 53.6% (Meta) and 45.7% (Alphabet)
among independent shareholders. Yearly counts in `edgar_ai_in_proxies_by_year.csv`.

## Runner-up — Manifold Markets AI questions
**Probe (Manifold public API, pulled today):** term="artificial intelligence" → **838 markets**,
43% resolved, **30,459,821 mana total volume**, 2.09M liquidity, 379 distinct creators.
Created by year: 2023:346, 2024:232, 2025:139, 2026:102. Dominated by BINARY (610) and
MULTIPLE_CHOICE (192); AGI-timeline questions are ubiquitous ("Will we get AGI before 2029/2030?").
Bulk dumps of markets/bets/comments available since Dec 2021. Breakdown in `manifold_ai_markets.csv`.
