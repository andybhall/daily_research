# Frontier-3 × AI (optimized persuasion) — probe log, 2026-08-21

Constrained on probing: the strongest AI-persuasion datasets are GitHub-deposited, and
this environment blocks external GitHub (raw.githubusercontent 404 on the data paths;
codeload 403). No Zenodo/OSF/HuggingFace mirror surfaced. Figures below are verified from
the papers fetched this run, not a live data pull.

## Top find — Talk2AI (arXiv 2604.04354)
Verified from the arXiv paper: **3,080 conversations / 30,800 turns**, **770 profiled
Italian adults across 4 weekly sessions (Spring 2025)**, within-subject: each person
conversed with one of GPT-4o / Claude 3.7 Sonnet / DeepSeek-V3 / Mistral Large on
climate change, math anxiety, and health misinformation; each session records opinion
change, conviction stability, perceived humanness, behavioral intentions, plus
sociodemographics + psychometrics. Deposited on GitHub (MassimoStel/Talk2AI).
**Could not probe:** external GitHub blocked here (raw 404 / codeload 403; likely LFS).

## Runner-up — Levers of Political Persuasion (Science 2025, DOI 10.1126/science.aea3884)
Verified: **19 LLMs, 707 political issues, 76,977 responses from 42,357 people,
466,769 fact-checked LLM claims**; persuasiveness driven more by post-training (+51%)
and prompting (+27%) than scale or personalization. Public code + OSF pre-registration.
Constructed experiment + Science-published (heavily-cited-incoming).

## Runner-up — AI election-information audits
States United (ChatGPT + Google AI Overview; 497 responses Sep–Oct 2025 → 402 Jan–Feb
2026; error 6.9%/8.2% → 0%), Reuters Institute (2024 UK election), CDT (disability voting).
AI as political-information intermediary; underlying question-response data mostly unpublished.
