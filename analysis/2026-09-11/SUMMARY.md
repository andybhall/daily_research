# Probe — AI model-card safety disclosures (Hugging Face)

**Source:** Hugging Face public API + raw model-card READMEs
(https://huggingface.co/api/models, https://huggingface.co/<id>/raw/main/README.md).
Pulled 2026-09-11, no auth, polite (0.05s spacing, 200 kB cap/card).

## What I pulled
- The 60 most-downloaded `text-generation` models (metadata + cardData).
- Their model-card READMEs (57 of 60 fetched; 3 had no fetchable README).

## Computed this run (`hf_modelcards.csv`)
Heading-level section presence across the 60 cards (regex over markdown headings,
after stripping YAML front-matter):
- **Evaluation / benchmark section: 36/60 (60%)**
- **Intended-use / Uses section: 26/60 (43%)**
- **Bias / Risks / Limitations section: 11/60 (18%)**
- **Training-data / dataset section: 9/60 (15%)**
- **Safety / responsible / harm section: 2/60 (3%)**
- Gated: 3/60. Median card length: **1,073 words**.
- Licenses: apache-2.0 39, mit 11, other 4, none 3, llama3.x 2.
- Card creation span: **2022-03-02 → 2026-08-19**.

**Takeaway (not available from the landing page):** the most-used open models
document *capability* (evals 60%) far more than *safety* (3%) or *risk* (18%).
The disclosure gap is the finding. Caveat: heading-keyword detection under-counts
disclosures made under non-standard headings or in linked docs; treat as a lower
bound and a reproducible baseline.

## Context (fetched this run, cited in memo)
- Extends the 2024 snapshot that ~85% of 64,116 HF cards with risk-related sections
  lacked substantive risk info (AI Transparency Atlas lineage, arXiv 2512.12443).
- EU AI Act Article 50 machine-readable disclosure duties enforceable from
  2026-08-02.

## Files
- `hf_modelcards.csv` — per-model section flags, downloads, license, gated, created.
- `sections_chart.csv` — section-presence shares (chart source).
