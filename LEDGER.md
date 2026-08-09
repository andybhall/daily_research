# LEDGER

The single source of truth for the Daily Dataset Hunt. **Every run reads this file
first.** A candidate that matches anything in **Found** or **Rejected** is dead on
arrival — do not surface it, do not re-litigate it.

- **Status values:** `seed` (surfaced in prior sessions, seeded here so the daily
  run never re-proposes it) · `new` (surfaced by a daily run, un-triaged) ·
  `spec'd` (promoted, has a project spec) · `building` · `published`.
- **Layers:** `information` · `representation` · `governance` (see the agenda at the
  bottom).
- Append-only in spirit: entries move status but are not deleted, so collisions
  stay detectable forever.

---

## Found

| Dataset | URL | Layer | Status |
|---------|-----|-------|--------|
| Congress Press / Derek Willis scrapers (congressional press releases, 26 yrs, ~675k releases) | https://github.com/dwillis/congress-press | information | seed |
| DCInbox — official congressional e-newsletters (~90k+ mailings since 2009) | https://www.dcinbox.com/ | information | seed |
| Princeton Corpus of Political Emails (300k+ emails, 2020 cycle) | https://electionemails2020.org/ | information | seed |
| FEC individual disbursements (bulk + API) | https://www.fec.gov/data/disbursements/ | representation | seed |
| Meta Ad Library (political & issue ads, with API) | https://www.facebook.com/ads/library/ | information | seed |
| Google Ads Transparency Center | https://adstransparency.google.com/ | information | seed |
| LocalView — local government meeting videos + transcripts (~140k videos) | https://localview.net/ | representation | seed |
| Legistar — municipal legislation / agendas / votes (Granicus API) | https://webapi.legistar.com/ | governance | seed |
| IRS Form 990 filings (nonprofits) via ProPublica Nonprofit Explorer | https://projects.propublica.org/nonprofits/ | governance | seed |
| Congressional hearing witnesses | https://www.congress.gov/committees | governance | seed |
| Regulations.gov — public comments on federal rulemaking (API) | https://www.regulations.gov/ | governance | seed |
| CourtListener / RECAP — federal dockets & opinions (API) | https://www.courtlistener.com/ | governance | seed |
| Glassdoor — employer reviews | https://www.glassdoor.com/ | information | seed |
| Blind — anonymous verified-employee posts | https://www.teamblind.com/ | information | seed |
| Wayback Machine — policy-page / ToS diffs over time | https://web.archive.org/ | information | seed |
| Kalshi — regulated event/prediction markets | https://kalshi.com/ | governance | seed |
| Polymarket — prediction markets | https://polymarket.com/ | governance | seed |
| Snapshot — off-chain DAO governance votes (GraphQL) | https://snapshot.org/ | governance | seed |
| Tally — on-chain DAO governance & proposals | https://www.tally.xyz/ | governance | seed |
| OpenRouter — LLM usage rankings / model marketplace | https://openrouter.ai/rankings | information | seed |
| LMArena (Chatbot Arena) — pairwise model preference battles | https://lmarena.ai/ | information | seed |
| Indian Parliament raw proceedings — Lok Sabha + Rajya Sabha questions/debates/mentions, all MPs → 31 Dec 2025 | https://zenodo.org/records/18146342 | representation | new |
| C-QUERI — congressional hearing questions/exchanges/responses (paired Q→A) | https://arxiv.org/abs/2509.21548 | governance | new |
| American local government elections DB (de Benedictis-Kessner et al.; ~78k candidates, 1989–2021) | https://www.nature.com/articles/s41597-023-02792-x | representation | new |
| Malaysian Election Corpus (MECo), 1955–2025 | https://arxiv.org/pdf/2505.06564 | representation | new |
| EU "Have Your Say" public-consultation full-text corpus (all input to EU legislation + attachments, through May 2025) | https://zenodo.org/records/15864330 | governance | new |
| Mexican municipal-elections precinct-level database (1994–2019; 456k precinct returns, 15.6k elections) | https://www.nature.com/articles/s41597-025-04918-9 | representation | new |
| Opioid Industry Documents Archive (OIDA) — millions of discovery-disgorged internal corporate documents; bulk-open on AWS | https://registry.opendata.aws/oida/ | governance | new |
| DataJud — Brazil CNJ National Judiciary Database (case metadata + docket movements, all courts, public API) | https://datajud-wiki.cnj.jus.br/api-publica/ | governance | new |

<!-- Found delta 2026-08-08 (frontier 10): 4 added (sandboxed pass) + 2 added (open-egress re-run) -->
<!-- Found delta 2026-08-09 (frontier 1): 2 added -->

## Rejected

_Datasets considered and rejected, with reasons — so they are never re-litigated._

| Dataset | URL | Reason |
|---------|-----|--------|
| School board elections, 16 states (openICPSR 229162) | https://www.openicpsr.org/openicpsr/project/229162/ | Replication data for a specific 2025 paper (Kogan/Lavertu/Peskowitz) — claimed. |
| US federal procurement 1979–2023 (~100M actions) | https://www.nature.com/articles/s41597-025-05714-1 | Underlying FPDS/USASpending source is heavily mined; harmonized panel is nice but not unclaimed. |
| Global contract-level public procurement (13 countries, GTI) | https://www.sciencedirect.com/science/article/pii/S2352340924003810 | Already exploited by depositors' corruption-risk research. |
| EUPDCorp / ParlaMint EU parliament debates | https://zenodo.org/records/15056399 | EU/ParlaMint parliamentary corpora are heavily mined in NLP. |
| Swiss Federal Supreme Court Dataset (SCD) | https://zenodo.org/records/11092977 | Legal-NLP space is crowded; marginal on unclaimed. |
| Corpus of Decisions: ICJ (CD-ICJ) | https://zenodo.org/records/10030647 | Single court, not panel-able at scale. |
| Conditional Congressional Communication (DVN/XRZ1UJ) | https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/XRZ1UJ | Collides with DCInbox (e-newsletters) and Congress Press (releases) seeds. |
| Revolving-door replication sets (DVN/MCYUKY; Amakudata) | https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/MCYUKY | Replication data for published papers — claimed by definition. |
| Fake Reviews Dataset (OSF, 2025) | https://osf.io/tyue9/ | Constructed/labeled ML dataset, not incidentally accumulated exhaust. |
| Annotated Spanish election debate transcriptions 1993–2023 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12480686/ | Small and partly annotated for existing NLP tasks. |
| Apple App Store privacy labels (weekly since 2022) | https://arxiv.org/pdf/2206.02658 | Frontier-4 (platform exhaust), logged there; borderline on the trawl frontier. |
| ParlSpeech V2 (6.3M parliamentary speeches, 9 democracies) | https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/L4OAKN | One of the most-used comparative parliamentary corpora — not unclaimed. |
| Nomic Congressional Database (every congressional Tweet, daily-updated) | https://arxiv.org/abs/2505.00006 | Introduced by a published paper (digital-twin of Congress); congressional tweets heavily mined. |
| FCC net-neutrality comment corpus (~24M, Stanford RegLab) | https://reglab.stanford.edu/data/fcc-comment-dataset/ | The 2017 fake-comment episode is extensively studied — claimed. |
| AGORA — AI Governance & Regulatory Archive (Zenodo 20229467) | https://zenodo.org/records/20229467 | Deliberately curated "living collection," not incidentally accumulated exhaust. |
| MeetingBank — 6-city council meetings (video/transcript/minutes) | https://meetingbank.github.io/ | Small (6 cities), NLP-summarization-mined; overlaps LocalView seed genre. |
| BICAM — Bulk Ingestion of Congressional Actions & Materials | https://pubmed.ncbi.nlm.nih.gov/41006307/ | Curated congressional research dataset; congressional data saturated. |
| Telegram 2024 U.S. election corpus (~1B posts) | https://arxiv.org/pdf/2410.23638 | Constructed study corpus; platform exhaust (frontier 4), not a trawl deposit. |
| Grand Débat National citizen-consultation corpus (GDN-CC) | https://arxiv.org/pdf/2601.14944 | Single 2019 event, already studied; not panel-able. |
| Free Law Project judicial financial-disclosure DB (250k pp, 1.5M holdings, 2003–2020) | https://www.courtlistener.com/ | Collides with CourtListener seed; already mined by the WSJ recusal investigation. |
| EOIR immigration-court asylum decisions / Deportation Data Project | https://www.openimmigration.us/ | Asylum-judge disparity ("Refugee Roulette") is among the most-studied legal datasets. |
| "Lobbying by Brief" business-law amicus filings, 2005–2022 (NY/CA/DE/TX/NV) | https://scholar.smu.edu/smulr/vol78/iss1/4/ | No verifiable public deposit; data underlies a published law-review article. |
| Amici Space Project — amicus signers, SCOTUS merits 1953–2013 | https://amicispace.ucmerced.edu/data | SCOTUS amicus heavily studied; coverage ends 2013. |
| Debt Collection Lab — state civil-court default judgments | https://debtcollectionlab.org/research/ | Established research project (Pew/Wilf-Townsend); underlying dockets claimed. |
| Pile of Law — 256GB open legal corpus | https://arxiv.org/pdf/2207.00220 | Heavily used for LLM training/filtering; not unclaimed. |

<!-- Rejected delta 2026-08-08 (frontier 10): 11 added (sandboxed pass) + 8 added (open-egress re-run) -->
<!-- Rejected delta 2026-08-09 (frontier 1): 6 added -->

---

## Active research agenda — the three layers

Relevance is scored against this fixed agenda so the hunt stays anchored (rubric
criterion **e**). A find should cleanly hit one of these:

- **Information** — how political information is produced, distributed, and
  distorted: persuasion, advertising, media, disclosure, strategic communication.
  *Behaviorally revealing when the text/spend was optimized under real stakes.*
- **Representation** — how citizen preferences and voices get expressed and
  aggregated into collective choice: elections, participation, deliberation,
  constituent contact, campaign finance.
- **Governance** — how institutions make, contest, and enforce binding decisions:
  courts, agencies, legislatures, procurement, corporate and DAO governance.

The Willis rubric (used every run in Phase 2):

1. **Optimized-under-pressure / behaviorally revealed** — revealed behavior under
   stakes, not stated preference.
2. **Incidentally accumulated / longitudinal** — a byproduct that piled up, not
   assembled to be studied.
3. **Unclaimed** — Google Scholar shows little prior academic use (required check).
4. **Panel-able** — repeated observations of the same units over time.
5. **Maps to a layer** — Information, Representation, or Governance.

Score 1–5 each, 25 max. Kill anything < 18/25.
