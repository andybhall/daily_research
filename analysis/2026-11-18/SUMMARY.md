# World Bank AI-Procurement Contracts — live probe (2026-11-18)

**Source:** World Bank Data Catalog, "AI Procurement Contracts" (dataset 0067129), CC-BY 4.0.
Download: https://datacatalogfiles.worldbank.org/ddh-published/0067129/DR0096198/AI_Procurement_Contracts.xlsx
Landing: https://datacatalog.worldbank.org/search/dataset/0067129/ai-procurement-contracts

Pulled the full Excel (3.0 MB) this run and parsed it with a stdlib xlsx reader (no pandas/openpyxl available).

## What it is
The AI-related subset (one row per procurement notice) of ~6.1M government procurement
contracts that the WDR-2026 team classified with an LLM. 22 columns incl. `notice_id`,
`source`, `notice_date`, `country_code/country_name`, `bid_title` (the tender text),
LLM classification fields (`task_result`, `input_result`, `user_result`,
`autonomy_result` + per-field `*_confidence`), `model`, `batch_id`, `income_group`,
`tool_category`.

## Figures computed this run
- **17,685 AI-related contracts**, notice dates **2003 → 2025** (23 years).
- **Sources:** Open Contracting 10,211 · EU TED 4,866 · World Bank 2,608.
- **Classifier `model` = `deepseek` for 100% of rows** — contradicts the catalog page,
  which says GPT-5 classified the 6.1M universe. (Provenance flag; could only be seen by
  pulling the file.) `batch_id` = `wdr_batch_20260207…` confirms it was built for WDR-2026.
- **1,342 distinct country/region codes; 102 countries with ≥20 contracts** (max 1,665
  = Netherlands; median 2). Top: Netherlands 1,665, UK 1,376, Austria 669, Czechia 668,
  Ireland 631 (EU-heavy, because TED is a source).
- **Income group:** High 14,428 (82%) · Upper-mid 1,437 · Lower-mid 1,391 · Low 429.
- **tool_category (12+):** Predictive Analytics & Decision Support 5,512 · Remote Sensing
  & Geospatial 2,099 · Environmental Monitoring 1,604 · Speech & Document Processing 1,236
  · **Surveillance & Biometric Identification 1,159** · AI Infrastructure & Compute 1,081 …
- **task_result:** Predictive 11,925 · Optimization 1,938 · Generative 1,341 · Not-specified 2,481.
- **autonomy_result:** 99.4% Not-specified (only 48 Autonomous / 43 human-in-loop / 18 human-on-loop) — the autonomy field is sparse.

## Caveat on the year series
Raw year counts jump 2024 (801) → 2025 (5,386); this reflects source-ingestion timing
(TED/OCP batch coverage), not a clean 7x one-year jump. The steady signal is 2017→2023
(544 → 1,680). Treat the series as coverage-dependent.

## Files
- `data/AI_Procurement_Contracts.xlsx` — the pulled file.
- `year_growth.csv`, `tool_category.csv`, `income_group.csv`, `task_result.csv` — computed breakdowns.
