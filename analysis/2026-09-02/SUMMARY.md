# Institutional records × AI — probes, 2026-09-02 (frontier 5)

## Top find — State AI legislation corpus (NCSL AI Legislation Database)
Verified this run: US states introduced **1,208 AI bills in 2025 (all 50 states) and enacted 145**;
by mid-2026, **1,561 AI bills across 45 states, with 84 laws enacted (27 states) in Jan–Jun 2026**
alone. NCSL's AI Legislation Database tracks enacted + pending bills since 2024, updated monthly,
tagged by topic (gov use, private-sector use, healthcare, hiring/discrimination, deepfakes, studies).
Panel = state × bill × topic × session × status. **Partial probe:** figures from NCSL/MultiState
trackers; full bill text is pullable via LegiScan (API-key gated), so no clean live pull today.

## Runner-up — Federal Register AI rulemaking (PROBED, open API)
Federal Register documents mentioning "artificial intelligence" by year:
57 (2019) · 189 (2023) · **309 (2024)** · **182 (2025)** · 224 (2026, partial). The 2024→2025 drop
tracks the change in administration/AI-EO regime. 2025 by type: **30 final rules, 33 proposed rules,
28 presidential documents (EOs), 91 notices** — real AI policymaking exhaust, panel-able by agency
× type × year. Yearly counts in `federal_register_ai_by_year.csv`.

## Runner-up — Congressional AI hearings corpus
28 congressional hearings on AI analyzed (Chamber of Progress) + Schumer's 9 A.I. Insight Forums
(closed-door, 150+ experts, no transcripts) + public hearing transcripts (TechPolicy.Press).
Legislative AI deliberation; adjacent to the C-QUERI congressional-hearing-Q&A seed.
