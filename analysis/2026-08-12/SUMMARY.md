# Hugging Face Hub live-probe results — 2026-08-12

**Source:** HF Hub public API (no auth), pulled today —
`https://huggingface.co/api/models?sort=downloads&direction=-1&limit=1000&full=true`
plus the 500 most-recently-created models. Each record: id, author, downloads,
likes, gated, createdAt, lastModified, library_name, pipeline_tag, tags[] (incl.
`license:*`), siblings[].

**Top-1000 models by downloads:**
- downloads: max 240,250,376 · median 802,470 · p10 397,290; likes median 139; 45 gated.
- tasks: text-generation (233), image-text-to-text (157), ASR (81), sentence-similarity (62).
- licenses: apache-2.0 (518), mit (185), other (92), gemma (16), cc-by-nc-4.0 (16).
- **Corporate concentration:** 319 distinct authors; 102 publish >1 of the top models;
  leaders Qwen (117), Google (44), Nvidia (37), Microsoft (36), Meta/facebook (35).
- creation years of top models: 2022:233, 2023:128, 2024:198, 2025:212, 2026:229.

**Accumulation rate:** the 500 newest public models were created within a ~2.4-hour
window at pull time → **~205 new public models per hour**. This is incidental
platform exhaust piling up continuously. Full breakdowns in
`hf_top1000_breakdowns.csv`.
