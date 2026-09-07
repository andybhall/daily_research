# Probe — LLM Election Data 2024 (Cen et al., MIT)

**Source:** https://huggingface.co/datasets/sarahcen/llm-election-data-2024
(paper: https://arxiv.org/abs/2509.18446). Pulled 2026-09-07 via the HF API +
`resolve/` file downloads. No auth. License: MIT.

## What I pulled
- Full file manifest via the datasets API (92,000 entries; aggregates kept in
  `manifest_summary.json` — the raw 18 MB manifest was not committed).
- 3 sample question CSVs (endo/election process, exo/election integrity,
  exo/predictions) for `claude-3-5-sonnet`.

## Computed this run (not from the landing page)
- **91,998** raw question CSV files under `raw_data/<model>/<condition>/<topic>/…`.
- **8 model configurations** in the public release, each with **12,638**
  question-runs: claude-3-5-sonnet, claude-3-haiku, claude-3-opus (10,152),
  claude-sonnet-with-internet, gemini-1.0-pro, gemini-1.0-pro-with-internet,
  gpt-3.5-turbo, gpt-4-turbo (6,018). (The paper describes up to 12 models; the
  open deposit covers these 8.)
- **605 distinct base-question templates**, split into 3 conditions:
  `baseline` (capability controls: GSM8K, medQA, natural-QA), `endo` (voter-facing:
  election process, issues, candidates), `exo` (predictions, exit polls, election
  integrity, candidates, events, analysis).
- Distinct questions by topic (`questions_by_topic.csv`): exit polls 164, LLM
  policies & self-reflection 113, predictions 110, election issues 69, candidates 58,
  endo issues 17, election process 16, endo candidates 12, election integrity 6.
- **Panel depth:** each daily-frequency question CSV holds **112 near-daily
  snapshots**, min date **2024-07-23**, max **2024-11-12** (through ~a week past
  Election Day). Timestamps to the nanosecond.
- **19 fields/record:** model, date, question, type, category, subcategory,
  query_type, frequency, base_q_template, variation_type, answer, prompt_type,
  response, timestamp, placeholders, pre_prompt_q, + 3 hashes.
- **Steering built in:** questions carry a partisan pre-prompt (`prompt_type`,
  e.g. "I am a Republican. {}") and placeholder variations (e.g. `{'state': 'South
  Carolina'}`) — supports within-question partisan- and framing-sensitivity tests.

## Files
- `manifest_summary.json` — per-model / per-condition / per-topic file counts.
- `questions_by_topic.csv` — distinct questions per topic (chart source).
- `sample_endo_election_process.csv`, `sample_exo_election_integrity.csv`,
  `sample_exo_predictions.csv` — 112-row time series, one per question.
