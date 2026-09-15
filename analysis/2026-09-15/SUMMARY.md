# Probe — AI-attributed layoffs (corporate self-disclosures)

**Sources fetched this run:** DisplaceIndex AI-layoffs tracker
(https://displaceindex.com/trends/ai-layoffs-tracker/), Founder Reports tracker
(https://founderreports.com/ai-layoffs-tracker/). Magnitude figures also attributed
to Challenger, Gray & Christmas (via https://thehill.com/policy/technology/5870898).

## Verified aggregates (read off the trackers this run)
- **DisplaceIndex:** 377,084 AI-attributed job cuts across **57 companies / 50 events**,
  Sept 2023 → Sept 2026. Inclusion rule: a named company, a specific job-cut number,
  and AI/automation "explicitly cited as the primary reason." Auto-scans Bloomberg/
  Reuters/WSJ/TechCrunch/CNBC every 6h.
- **Founder Reports:** 31 companies; ~173,568 cuts; same strict self-attribution rule
  (CEO memo / SEC filing / earnings call / shareholder letter).
- **Challenger:** AI cited in **101,743 US job cuts through June 2026** (~2× the 54,836
  in all of 2025); AI the **#1 stated layoff reason for 4 straight months** (Mar–Jun 2026).

## Computed this run (my extraction — event level only)
I parsed the DisplaceIndex page into **47 distinct company-events** (company, sector,
month). **Reliable:** the company / sector / date fields.
- **Events by sector:** Technology 22, Finance 9, Logistics 4, Education 4, Creative 4,
  Customer service 2, Manufacturing 1, Retail 1 (`ai_layoffs_by_sector.csv`).
- **Events by year:** 2023 ×4, 2024 ×13, 2025 ×16, 2026 ×14 (through Sept)
  (`ai_layoffs_events_by_year.csv`).
- Named examples: Microsoft, Meta, Salesforce, IBM, Oracle, Cisco, Intuit, GitLab,
  PayPal, Coinbase, Klarna, Snap, Pinterest.

## Honesty note
The **per-event job counts** in my parse are unreliable — the page interleaves a running
cumulative total that mis-paired against companies (e.g. it yields "Coinbase 62,242,"
impossible for a ~4k-employee firm). So I do **not** report parsed job magnitudes;
those come only from the trackers' own stated totals above. A clean company-level
job-count panel must be built from the underlying disclosures (SEC 8-Ks, earnings-call
transcripts, WARN notices) — the build step, not claimed here.

## Files
- `ai_layoffs_events.csv` — 47 extracted events (job column NOT reliable; kept for provenance).
- `ai_layoffs_by_sector.csv` — event counts by sector (chart source).
- `ai_layoffs_events_by_year.csv` — event counts by year.
