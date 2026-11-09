# 2026-11-06 — Voter Prompts: how real voters use AI to decide their vote

**Object:** A released dataset of real voters' conversations with four major LLMs as they
decided how to vote in their 2026 Senate race — the demand side (how people actually prompt AI
about elections), distinct from the supply-side MIT audit logged 09-07.

## Verified this run (bahelgason.com/voter-prompts/ + methods page, fetched 2026-11-06 catch-up)
- Authors: Beth Anne Helgason, Maddison Linker, Rishi Gurudevan (Yale SOM). Released 3 Nov 2026.
- Two preregistered studies (AsPredicted #317878, #319077), 16–27 Oct 2026, 35 Senate-race states.
  Study 1 (all voters, CloudResearch): 1,455 participants / 1,372 chats; Study 2 (undecided,
  Prolific): 975 / 896. Combined 2,430 participants; ~2,268 coded chats.
- Models: GPT-5.6, Claude Sonnet 5.5, Gemini 3.8 Flash (both studies), Grok 4.3 (Study 1). Chats
  ran via OpenRouter; each user message coded 3x by Claude Opus 5.5 against a codebook (majority).
- Released on Hugging Face (bahelgason/voter-prompts): chats with identifying details removed +
  codebook + coding outputs (approach codes, evidence quotes, turn-level codes, reply behaviors).
- Findings: 61% asked basic ballot facts; 36% asked for help choosing. Unprompted candidate
  recommendation: only Grok regularly (14%, 8/59); ChatGPT 2/74; Claude & Gemini never. After the
  user shared views: ChatGPT 79% (n=91), Grok 66%, Gemini 53%, Claude 40% (n=80). After the user
  answered the bot's priority question: ChatGPT 88% (21/24) vs Claude 7% (1/15). Median user sent
  2 messages; median first message 12 words.

## Why it clears
Revealed behavior under real election stakes (survey-framed) — how voters actually use AI to
decide (a4); but survey-elicited, point-in-time, not incidental exhaust (b2); brand-new, released
"to help eval builders," no outside analysis yet (c4, unclaimed); panel-able by chat x model x
voter x turn x code x race, ~2,268 chats (d3); bullseye Representation + Information (AI advising
votes) (e5). **Score 18/25.**

## Honest caveats
- Survey-elicited, not in-the-wild exhaust; the authors note only the AI companies hold the full
  real-world transcripts and urge them to share privacy-protected versions.
- Modest N (~2,268 chats); Hugging Face license not stated on the page (access = HF link).
