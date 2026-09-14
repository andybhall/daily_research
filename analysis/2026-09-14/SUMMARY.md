# Probe — Canada's Algorithmic Impact Assessment (AIA) registry

**Source:** open.canada.ca CKAN API (`package_search?q="Algorithmic Impact Assessment"`)
+ individual AIA JSON resources. Pulled 2026-09-14, no auth, open licence.
Registry landing: https://open.canada.ca/data/en/dataset?q=algorithmic+impact+assessment

## What I pulled
- CKAN package search (40 matches; **30 are individual published AIAs**, the rest are
  the AIA tool/template).
- 10 individual AIA JSON resources, to confirm the questionnaire structure.

## Computed this run
- **30 published AIAs**, growing over time (metadata_created): 2020 ×2, 2021 ×2,
  2022 ×6, 2023 ×1, 2024 ×7, 2025 ×8, 2026 ×4.
- **By department** (`aia_by_department.csv`): Immigration/IRCC **7**, Employment &
  Social Development/ESDC **7**, Border Services/CBSA **4**, Veterans Affairs **3**,
  Treasury Board **2**, RCMP **2**, Public Services & Procurement **2**, Other
  (Transport/ISED/PHAC) **3**. The register is concentrated in **immigration,
  benefits, and border** — the highest-stakes automated decisions on individuals.
- **Structure:** each AIA JSON is a flat questionnaire of **~79 coded fields**:
  projectDetails* (respondent name, job, department, project phase, description),
  riskProfile1–4, aboutSystem/aboutAlgorithm, decisionSector, and impact1–14, with
  answers coded `item{choice}-{points}` (e.g. `riskProfile3 = item1-4`). Example:
  Veterans Affairs "Mental Health Benefit" AIA, respondent + branch named, eligibility
  determination self-described as "no impact on rights/freedoms."
- **Formats available across the 30:** PDF 76, JSON 32, HTML 6, CSV 3, XLS 2, DOCX 2.

## Honest limits
- The official **impact level (I–IV)** and raw/mitigation totals aren't a single JSON
  field; they're computed from the item-point scoring logic. I verified the coded
  questionnaire answers are present (so the panel is reconstructable) but did not
  recompute official levels this run — that's the build step, not a claim here.

## Nearest work (fetched this run)
- "Bureaucratic Silences: What the Canadian AI Register Reveals, Omits, and Obscures"
  (arXiv 2604.15514) — a qualitative critique; no quantitative multi-AIA panel.

## Files
- `aia_manifest.json` — 30 AIAs (title, department, created date, formats) + by-year.
- `aia_by_department.csv` — department breakdown (chart source).
