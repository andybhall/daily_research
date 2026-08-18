# Frontier-10 × AI (dataverse trawl) — probe log, 2026-08-18

A constrained day: the best political-AI deposits are either **curated incident
databases** or **access-restricted**, and the genuinely-incidental corpora are
**already claimed**. Honest probe record below (no fabricated figures).

## Top find — Political Deepfakes Incident Database (PDID)
Verified via the AAAI paper + GRAIL Lab project page (both fetched today):
**939 images + 502 videos, 2018→present**, with researcher-coded fields — target,
presented-as-real/fake, external verification, harms, propagation metrics, sharer,
and manipulation architecture/modality.
**Could not probe:** hosted on Airtable; open-access is "pending consideration of
ethical risks" — no public CSV/API confirmed today. Figures are from fetched pages.

## Runner-up — Gen-Review (LLM penetration of peer review)
Harvard Dataverse `doi:10.7910/DVN/PYDPEZ`. **Verified via the Dataverse API today**
(`genreview_dataverse_metadata.json`): a single file `gen_review.db`,
**1,614,589,952 bytes (~1.6 GB)**, `application/octet-stream`, license **CC BY 4.0**.
**Partial probe only:** a bounded range GET (first 1.5 MB, HTTP 206) could not yield
the SQLite schema (sqlite_master pages lie beyond the first 1.5 MB; the full 1.6 GB
exceeds a polite pull). Existence/size/format/license confirmed; internal fields/counts not.

## Runner-up — Human–AI political conversations
"Talking Politics with AI" (arXiv 2607.00551) classifies **4.30M** human-AI chats:
**3.9% contain political content**, mostly practical (info-seeking, drafting) rather
than opinion. Incidental real usage; underlying corpora (WildChat/LMSYS/ShareLM) are
already claimed, so this is a pointer to an on-agenda subset, not a fresh deposit.
