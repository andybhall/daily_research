# AI Hallucination Cases DB (Charlotin) — live probe, 2026-08-19

**Source:** full CSV export pulled today from
`https://www.damiencharlotin.com/hallucinations/hallucinations/download.csv`
(the site 403s generic fetchers; a browser User-Agent returns it). 18 fields:
Case Name, Court, State(s), Date, Party(ies), AI Tool, Hallucination Items,
Outcome, Monetary Penalty, Professional Sanction, Alleged, Vendor Disputed(+expl.),
Pointer, Source, Details, Legal Field (primary/secondary).

| Metric | Value |
|---|---|
| Cases | 1,934 |
| Distinct jurisdictions (State(s) tokens) | 41 |
| Cases with a monetary penalty recorded | 351 |

**Explosive growth — cases by year:** 2023: 16 · 2024: 59 · **2025: 845** · **2026: 1,013**.
**Top AI tools blamed:** ChatGPT (118), Claude (11), Perplexity (5), Copilot (5), Grok (4)
— though most entries are "Implied" (1,296) or "Unidentified" (402).
**Top courts:** S.D.N.Y. (48), E.D. Michigan (31), W.D. Washington (30), N.D. Illinois (29),
C.D. California (29). **Top legal fields:** contract (445), administrative (251),
civil rights (194), employment (172), tort (168).

Panel structure = court × jurisdiction × AI tool × legal field × time × outcome/penalty.
Breakdowns in `ai_hallucination_by_year.csv`, `ai_hallucination_by_tool.csv`; full pull in
`ai_hallucination_cases.csv`.
