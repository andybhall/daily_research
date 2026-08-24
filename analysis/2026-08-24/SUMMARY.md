# Hobbyist AI-behavior watchdogs — probes, 2026-08-24 (frontier 6, collector archives)

## Top find — SpeechMap.ai (xlr8harder)
Verified from the site today: **375 models**, **795,000 responses analyzed**,
**March 2023 → August 2026**, four outcome codes — Complete / Evasive / Denial / Error —
across political arguments, satire, religion, history, and rights advocacy. Per-model and
per-topic compliance/refusal rates are browsable (e.g., "argue for traditional gender roles"
61% compliance vs 92.6% with genders reversed; outlawing Judaism 10.5% vs witchcraft 68.5%).
**Partial probe:** the site exposes structured per-model/per-topic results, but bulk data
requires contacting the project (no public API/export disclosed).

## Runner-up — Leaked system-prompt archives (YeeKal/leaked-system-prompts, mirror leaked-system-prompts.com)
**Cloned and analyzed today** (metadata only, no prompt text reproduced): **116 system-prompt
files across 20+ vendors** — Anthropic (24), OpenAI (18), xAI (13), Perplexity (6), Google (6),
Discord (5), Cursor (4), Microsoft/Devin (3), DeepSeek/GitHub (2)… Version panel by filename year:
**2022: 3 · 2023: 17 · 2024: 36 · 2025: 49 · 2026: 10** — the hidden "constitutions" configuring
frontier AI, tracked as they change. Sibling archives: asgeirtj/system_prompts_leaks,
elder-plinius/CL4R1T4S. Breakdown in `system_prompts_by_vendor.csv`.

## Runner-up — TrackingAI.org (Maxim Lott)
Runs Political Compass (and IQ) tests against ~19+ LLMs, re-polling as models change, to track
political bias over time. Inspired by David Rozado's LLM-political-preference work (which is the
claimed academic version).
