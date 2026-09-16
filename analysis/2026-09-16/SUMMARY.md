# Probe — Board AI-oversight disclosures in proxy statements (EDGAR)

**Source:** SEC EDGAR full-text search API (https://efts.sec.gov/LATEST/search-index),
form type DEF 14A. Pulled 2026-09-16, no auth (UA identifies the bot).

## Computed this run
Number of DEF 14A (proxy) filings containing the exact phrase
**"oversight of artificial intelligence"**, by year:

| year | filings |
|---|---|
| 2020 | 0 |
| 2021 | 0 |
| 2022 | 0 |
| 2023 | 1 |
| 2024 | 3 |
| 2025 | 23 |
| 2026 | 57 |

Stricter variant **"board oversight of artificial intelligence"**: 13 filings in 2026.

The board-level oversight of AI, essentially absent through 2022, is now an explicit,
fast-spreading proxy-disclosure item. (`proxy_ai_oversight_by_year.csv`.)

## Context (fetched this run, cited in memo)
- ISS-Corporate / Harvard corpgov: disclosure of directors' **AI expertise** rose from
  **26% of the Fortune 100 in 2024 to 44% in 2025**.
- Denominator: ~1,432 DEF 14As merely *mentioning* AI in 2026 (this hunt's 08-17 probe);
  today's figure is the governance-structure subset — boards saying they *oversee* AI.

## Distinctness (not a ledger collision)
- 08-17 Found = AI shareholder **resolutions + proxy votes** (demand side).
- 08-27 Found = 10-K **risk-factor** AI disclosures (risk side).
- This = the **board/committee oversight structure + director AI-expertise** (governance
  side) — a third, distinct leg, same EDGAR plumbing.

## Honest limits
- Phrase-based FTS counts are a lower bound (companies phrase oversight many ways);
  a full build would classify board/committee charters and director-skills matrices.
- 2026 proxy season is largely but not fully complete.

## Files
- `proxy_ai_oversight_by_year.csv` — chart source.
