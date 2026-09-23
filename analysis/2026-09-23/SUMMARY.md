# Probe — Decensored / "abliterated" open-model ecosystem (Hugging Face)

**Source:** Hugging Face public API (https://huggingface.co/api/models?search=abliterated
/ search=uncensored). Pulled 2026-09-23, no auth. Context: arXiv 2609.05241 ("Uncensored
Open-weight Models: Redistribution as the Persistence Layer"); the "Heretic" abliteration
tool recurs across model names.

## Computed this run
- The searches for **"abliterated"** and **"uncensored"** each return the API cap
  (>1,000 models) — a large, active ecosystem.
- Deduping the top-500-by-downloads of each query = **963 distinct decensored models**,
  with **~37,991,202 combined downloads** (`decensored_top_publishers.csv`).
- **Top publishers by total downloads** (a handful of hobbyists dominate):
  HauhauCS 7.22M (24 models), DavidAU 5.56M (38), huihui-ai 4.34M (53),
  mradermacher 3.88M (**324** such models), JonathanColetti 2.34M (2),
  0bserverx 1.68M (3), orcarouter 1.19M (12), llmfan46 0.99M (35), bartowski 0.71M (41).
- Most-downloaded single models exceed **2M downloads** each (e.g.
  huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF 2.24M; JonathanColetti/Qwen3.8-27B-
  Uncensored 2.33M). Base models: Qwen3, Gemma-4, DeepSeek-V4.

## Why it's a distinct object
The **supply side** of guardrail circumvention — safety-refusal directions removed from
open *weights* and redistributed — as opposed to the ledger's jailbreak-*prompt* hoards
(L1B3RT4S 08-14; leaked system prompts 08-24). A hobbyist-published adoption panel:
model × publisher × base-model × downloads × time. On-agenda for the open-weights /
AI-safety-control governance debate.

## Files
- `decensored_top_publishers.csv` — top-8 publishers by downloads (chart source).
