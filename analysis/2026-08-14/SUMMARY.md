# Collector/hobbyist AI-hoard probes — 2026-08-14

## Top find — L1B3RT4S jailbreak hoard (elder-plinius), metadata only
Cloned today from https://github.com/elder-plinius/L1B3RT4S (analysis of **structure and
git history only — no prompt content reproduced**).

- **39 vendor-specific jailbreak files** (one per AI org: OpenAI, Anthropic, Google, Meta,
  Mistral, DeepSeek, xAI, Midjourney, Cohere, NVIDIA, Amazon, Microsoft, Alibaba, Moonshot, …).
- **253 commits**, spanning **2024-04-08 → 2026-02-17** (~22 months) — a longitudinal panel of the
  jailbreak-vs-guardrail commons. Commit cadence in `l1b3rt4s_commits_by_month.csv`;
  vendor list in `l1b3rt4s_vendor_files.txt`.

## Runner-up — Civitai community model archive (API)
Pulled top-100 most-downloaded models via https://civitai.com/api/v1/models today.
- Types: Checkpoint 65, LORA 17, TextualInversion 13. Base models: SD 1.5 (60), SDXL 1.0 (24),
  Pony (24), Illustrious (18), Flux.1 D (7) — the open-model lineage is visible.
- Downloads: max 2,296,900 (Realistic Vision V6.0) · median 278,840.
- **Creator economy:** 25,139,497 "buzz" tips recorded across the sample; 67 distinct creators.
- **Licensing choices** (allowCommercialUse: Image/RentCivit/Rent/Sell combos) and the `poi`
  real-person-likeness flag are captured per model — the under-worked angle vs. prior
  NSFW/deepfake-prevalence papers. Breakdown in `civitai_top_models_breakdown.csv`.
