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
| FARA foreign-agent filings (registrants × foreign principals, 1942→2026; bulk CSV/XML + API) | https://efile.fara.gov/api | information | new |
| India electoral bonds — SBI/ECI disclosure (company→party donations, 22,217 bonds, Apr 2019–Feb 2024) | https://www.kaggle.com/datasets/shaundanielll/electoral-bond-data-state-bank-of-india | representation | new |
| GAO bid-protest decisions (firms contesting federal contract awards; 1,000+/yr) | https://www.gao.gov/legal/bid-protests/search | governance | new |
| IRS 527 / Form 8872 — political-org contributions & expenditures (weekly bulk since 2000) | https://www.irs.gov/charities-non-profits/political-organizations/political-organization-filing-and-disclosure | representation | new |
| World Bank debarment list + Contract Awards (FY2017+) — sanctioned firms + procurement awards | https://www.worldbank.org/en/projects-operations/procurement/debarred-firms | governance | new |
| Snap Political & Advocacy Ads Library — political ad creative + spend + impressions + 20 targeting fields (yearly bulk since 2018) | https://www.snap.com/political-ads | information | new |
| FCC OPIF Political Files — broadcast/cable political ad-buy filings (per station, ongoing; search API) | https://www.fcc.gov/search/api | information | new |
| TikTok Commercial Content Library — DSA-mandated paid-ad creative + targeting + impressions (gated research API) | https://developers.tiktok.com/products/commercial-content-api | information | new |
| Hugging Face Hub metadata exhaust — models/datasets/Spaces: downloads, likes, licenses, authors, timestamps (public API) | https://huggingface.co/docs/hub/en/api | information | new |
| DSA Transparency Database — content-moderation statements of reasons (700+ platforms, automated-decision flags; daily bulk) | https://transparency.dsa.ec.europa.eu/explore-data/download | governance | new |
| X Community Notes public data — crowd notes + ratings, bridging-ranked, LLM "AI Note Writers" (daily bulk since 2021) | https://github.com/twitter/communitynotes | information | new |
| US Federal Agency AI Use Case Inventory — mandated annual inventory of government AI systems (1.7k→3.6k cases; consolidated CSV) | https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory | governance | new |
| Netherlands Algorithm Register — public register of government algorithms/high-risk AI (~1,533; open-source platform) | https://algoritmes.overheid.nl/en | governance | new |
| UK Algorithmic Transparency Recording Standard (ATRS) — mandatory public-sector algorithm-use records | https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub | governance | new |
| L1B3RT4S — hobbyist LLM-jailbreak hoard, one file per AI vendor, 22 months of git history (elder-plinius) | https://github.com/elder-plinius/L1B3RT4S | governance | new |
| Civitai community model archive — Stable-Diffusion checkpoints/LoRAs: downloads, licenses, base-model lineage, poi flag, tips (API) | https://civitai.com/api/v1/models | information | new |
| Pixiv AI-generated artwork archive — user-tagged AI art on a hobbyist platform (~15.2M works, 16.2% AI-tagged; auth API) | https://arxiv.org/pdf/2402.18463 | information | new |
| AI shareholder resolutions & proxy voting — corporate-governance-of-AI proposals + votes (EDGAR DEF 14A + Form N-PX) | https://efts.sec.gov/LATEST/search-index?q=%22artificial+intelligence%22&forms=DEF+14A | governance | new |
| Manifold Markets AI questions — play-money prediction market on AI/AGI (open API + bulk dumps since 2021) | https://docs.manifold.markets/api | information | new |
| Metaculus AI questions — reputation-stakes forecasts on AI progress/governance (open API) | https://www.metaculus.com/api/ | information | new |
| Political Deepfakes Incident Database (PDID) — coded political deepfakes/cheapfakes, 2018→present (~939 img + 502 vid; GRAIL Lab) | https://www.grail-lab.org/project/political-deepfakes-incident-database | information | new |
| Gen-Review — parallel human/AI peer-review corpus, ICLR-era (Harvard Dataverse, CC-BY, 1.6GB) | https://doi.org/10.7910/DVN/PYDPEZ | governance | new |
| Human–AI political conversations — political subset (~3.9%) of real human-LLM chat corpora | https://arxiv.org/abs/2607.00551 | information | new |
| AI Hallucination Cases Database (Charlotin) — court decisions worldwide citing AI-fabricated citations (1,934+; daily CSV) | https://www.damiencharlotin.com/hallucinations/ | governance | new |
| AI copyright/IP litigation dockets — 70+ infringement suits vs AI companies (case trackers + PACER/RECAP) | https://www.mishcon.com/generative-ai-intellectual-property-cases-and-policy-tracker | governance | new |
| Judicial AI standing orders — 300+ judges' AI-disclosure/certification requirements (RAILS/tracker) | https://trace.law/kb/court-ai-disclosure-orders | governance | new |
| US federal AI procurement (USASpending AI slice) — agency×vendor×year AI-contract obligations (free API) | https://api.usaspending.gov/ | governance | new |
| AI lobbying disclosures (LDA) — quarterly filings on "artificial intelligence" issues (Senate/House bulk) | https://lda.senate.gov/api/ | governance | new |
| AI-safety / AI-policy philanthropy — Open Philanthropy/Coefficient Giving AI-risk grants database | https://www.openphilanthropy.org/grants/ | governance | new |
| Talk2AI — longitudinal human–AI persuasive conversations (3,080 convos, 770 people × 4 weekly sessions; GitHub) | https://arxiv.org/abs/2604.04354 | information | new |
| The Levers of Political Persuasion (Science 2025) — 19 LLMs × 707 political issues, 76,977 responses, 466k fact-checked claims | https://www.science.org/doi/10.1126/science.aea3884 | information | new |
| AI election-information audits — how AI assistants answer voter questions (States United/Reuters Inst./CDT; model×question×time) | https://statesunited.org/resources/ai-and-elections/ | information | new |
| SpeechMap.ai — AI refusal/compliance on controversial political speech (375 models, 795k responses, 2023→2026) | https://speechmap.ai/ | governance | new |
| Leaked system-prompt archives — hobbyist hoard of frontier-AI system prompts, 20+ vendors, version panel 2022→2026 | https://leaked-system-prompts.com/ | governance | new |
| TrackingAI.org — LLM political-bias tracker over time (Political Compass per model; Maxim Lott) | https://www.trackingai.org/home | information | new |
| China CAC generative-AI / algorithm registry — mandatory filings for all public gen-AI services (5,800+ entries; reg#/company/province/B2B-B2C) | https://beian.cac.gov.cn/ | governance | new |
| European public-sector AI registers beyond NL — Germany (1,305 AI projects), France public-algorithm repos, EU JRC Public Sector Tech DB | https://wp.oecd.ai/app/uploads/2025/05/algorithmic-transparency-in-the-public-sector.pdf | governance | new |
| India AI-in-elections — genAI campaign content (~$50M, ~40 campaigns) + Shakti fact-check collective, 2024 general election | https://www.techpolicy.press/indias-experiments-with-ai-in-the-2024-elections-the-good-the-bad-the-inbetween/ | information | new |

<!-- Found delta 2026-08-08 (frontier 10): 4 added (sandboxed pass) + 2 added (open-egress re-run) -->
<!-- Found delta 2026-08-09 (frontier 1): 2 added -->
<!-- Found delta 2026-08-10 (frontier 2): 5 added -->
<!-- Found delta 2026-08-11 (frontier 3): 3 added -->
<!-- Found delta 2026-08-12 (frontier 4, AI-focus): 3 added -->
<!-- Found delta 2026-08-13 (frontier 5, AI-focus): 3 added -->
<!-- Found delta 2026-08-14 (frontier 6, AI-focus): 3 added -->
<!-- Found delta 2026-08-17 (frontier 9, AI-focus): 3 added -->
<!-- Found delta 2026-08-18 (frontier 10, AI-focus): 3 added -->
<!-- Found delta 2026-08-19 (frontier 1, AI-focus): 3 added -->
<!-- Found delta 2026-08-20 (frontier 2, AI-focus): 3 added -->
<!-- Found delta 2026-08-21 (frontier 3, AI-focus): 3 added -->
<!-- Found delta 2026-08-24 (frontier 6, AI-focus): 3 added -->
<!-- Found delta 2026-08-25 (frontier 7, AI-focus): 3 added -->

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
| ProZorro — Ukraine open procurement (tenders/bids since 2015) | https://www.kaggle.com/datasets/oleksastepaniuk/prozorro-public-procurement-dataset | Flagship OCDS open-contracting dataset; real prior use (CGD/DOZORRO) — not unclaimed. |
| Brazil TSE campaign finance (DivulgaCandContas / dados abertos) | https://dadosabertos.tse.jus.br/ | Corporate-donation effects already mined (Boas/Hidalgo/Richardson); foundational but studied. |
| Congressional stock trades (STOCK Act periodic transaction reports) | https://www.capitoltrades.com/ | Saturated — multiple papers + Quiver/CapitolTrades/Unusual Whales trackers. |
| Upworthy Research Archive (32,487 headline A/B tests, 2013–2015) | https://www.nature.com/articles/s41597-021-00934-7 | Famous, heavily-used content-experiment benchmark — not unclaimed. |
| Change.org petitions (text + signature outcomes) | https://reshare.ukdataservice.ac.uk/851617/ | Petition-success prediction is a saturated subfield (Zhao datasets, many papers). |
| GoFundMe crowdfunding copy (text + funding outcomes) | https://arxiv.org/pdf/2505.11367 | Extensively studied (moral-framing, cancer-campaign success papers). |
| SnorCall robocall honeypot corpus (232,723 robocalls) | https://www.usenix.org/system/files/usenixsecurity23-prasad.pdf | Ideal exhaust, but authors state the corpus cannot be released. |
| GPT Store custom-GPT metadata (GPTZoo 730k; Beetrove 349k) | https://arxiv.org/pdf/2405.15630 | Released research datasets already exist (GPTZoo/Beetrove) + multiple papers — claimed. |
| AI Incident Database / OECD AI Incidents Monitor | https://oecd.ai/en/catalogue/tools/ai-incident-database | Curated collections (assembled to be studied), ~800–7k incidents; heavily used already. |
| US Copyright Office generative-AI comment corpus (10,000+ comments) | https://www.copyright.gov/policy/artificial-intelligence/ | Sits inside the Regulations.gov seed genre — collision, not a distinct object. |
| DiffusionDB (14M Stable-Diffusion images + prompts) | https://github.com/poloclub/diffusiondb | Famous published prompt-gallery benchmark (ACL'23) — claimed. |
| verazuo/jailbreak_llms (15,140 prompts, 1,405 jailbreaks) | https://github.com/verazuo/jailbreak_llms | The published CCS'24 jailbreak dataset — the claimed version of that genre. |
| Lexica (5M+ AI-generated images + prompts) | https://lexica.art/ | Search-only; does not release its internal database in bulk. |
| ISS Voting Analytics (general proxy-voting database) | https://library.maastrichtuniversity.nl/database/iss-voting-analysis/ | Standard, heavily-used proxy DB; the AI-proposal subset is the find, not the whole DB. |
| USPED — 2024 US-election deepfakes corpus (231 items) | https://zenodo.org/records/15412865 | Curated corpus, not incidental exhaust; access restricted to vetted researchers. |
| Nature 2025 "Persuading voters using human–AI dialogues" deposit | https://doi.org/10.7910/DVN/DODEXZ | Raw conversation transcripts withheld (dual-use); request-only, not openly usable. |
| Pretrial risk-assessment / COMPAS-style tools in courts | https://www.mdpi.com/2078-2489/17/3/234 | Algorithmic-fairness literature (ProPublica COMPAS + many papers) is saturated. |
| Commercial federal-AI-contract trackers (Govly / Fed-Spend / Presenc) | https://fed-spend.com/blog/federal-ai-cybersecurity-contract-awards-2026 | Paywalled repackaging of open USASpending data — use the source API instead. |
| DebunkBot / Costello et al. conspiracy-debunking persuasion (Science 2024) | https://www.science.org/doi/10.1126/science.adq1814 | Famous, heavily-covered AI-persuasion flagship — claimed. |
| David Rozado LLM political-orientation datasets | https://www.maximumtruth.org/p/my-new-tool-to-track-ai-bias-trackingaiorg | Published/claimed academic version of AI political-bias tracking (TrackingAI is the live hobbyist panel). |
| EU AI Act high-risk AI systems database (Art. 71) | https://artificialintelligenceact.eu/article/71/ | Registration deferred from Aug 2026 to Dec 2027 — DB not yet populated; revisit when live. |

<!-- Rejected delta 2026-08-08 (frontier 10): 11 added (sandboxed pass) + 8 added (open-egress re-run) -->
<!-- Rejected delta 2026-08-09 (frontier 1): 6 added -->
<!-- Rejected delta 2026-08-10 (frontier 2): 3 added -->
<!-- Rejected delta 2026-08-11 (frontier 3): 4 added -->
<!-- Rejected delta 2026-08-12 (frontier 4): 2 added -->
<!-- Rejected delta 2026-08-13 (frontier 5): 1 added -->
<!-- Rejected delta 2026-08-14 (frontier 6): 3 added -->
<!-- Rejected delta 2026-08-17 (frontier 9): 1 added -->
<!-- Rejected delta 2026-08-18 (frontier 10): 2 added -->
<!-- Rejected delta 2026-08-19 (frontier 1): 1 added -->
<!-- Rejected delta 2026-08-20 (frontier 2): 1 added -->
<!-- Rejected delta 2026-08-21 (frontier 3): 1 added -->
<!-- Rejected delta 2026-08-24 (frontier 6): 1 added -->
<!-- Rejected delta 2026-08-25 (frontier 7): 1 added -->

---

## Active research agenda — AI × the three layers

**AI focus (hard gate).** The hunt now targets **AI's role in political systems**.
Every find must have a clear **AI nexus** — it reveals how AI systems behave, how AI
is built/deployed/governed, or how AI is reshaping the layers below. A dataset with
no AI connection is dead on arrival, however behaviorally rich (see HARNESS anti-slop
rule 6). Relevance is scored against this agenda (rubric criterion **e**): a find must
be AI-relevant *and* cleanly hit one layer.

- **Information** — how political information is produced, distributed, and
  distorted: persuasion, advertising, media, disclosure, strategic communication.
  *AI angle:* AI-generated/AI-optimized persuasion, synthetic media and deepfakes,
  chatbot/LLM outputs and logs, automated content and its detection.
- **Representation** — how citizen preferences and voices get expressed and
  aggregated into collective choice: elections, participation, deliberation,
  constituent contact, campaign finance. *AI angle:* AI in campaigning and
  deliberation, algorithmic constituent contact, AI-mediated civic participation.
- **Governance** — how institutions make, contest, and enforce binding decisions:
  courts, agencies, legislatures, procurement, corporate and DAO governance.
  *AI angle:* algorithmic decision-making in institutions, AI procurement, AI law
  and regulation, model governance, audits, and incident reporting.

*Historical note:* finds logged before the 2026-08-11 AI-focus pivot predate this
gate and are kept for collision-detection; they are not a template for new finds.

The Willis rubric (used every run in Phase 2):

1. **Optimized-under-pressure / behaviorally revealed** — revealed behavior under
   stakes, not stated preference.
2. **Incidentally accumulated / longitudinal** — a byproduct that piled up, not
   assembled to be studied.
3. **Unclaimed** — Google Scholar shows little prior academic use (required check).
4. **Panel-able** — repeated observations of the same units over time.
5. **Maps to a layer** — Information, Representation, or Governance.

Score 1–5 each, 25 max. Kill anything < 18/25.
