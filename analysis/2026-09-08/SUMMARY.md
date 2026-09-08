# Probe — Algorithmic Contestability Cases Database (Stewart, FAccT 2026)

**Source:** Zenodo record 18340254 (concept DOI 10.5281/zenodo.18069759),
supplementary data for "Beyond Explanation: Evidentiary Rights for Algorithmic
Accountability" ([arXiv 2603.22716](https://arxiv.org/pdf/2603.22716);
[ACM FAccT '26](https://dl.acm.org/doi/10.1145/3805689.3806532), Best Paper).
Downloaded + analyzed 2026-09-08. CC-BY-4.0, no auth. Repo stats: 20 downloads / 88 views.

## What I pulled
- The full 56 kB deposit (`cases.csv`, `cases.json`, `codebook.md`, README,
  `summary_statistics.py`). Kept the CSV + codebook + README here.

## Computed this run (from cases.csv)
- **168 cases**, **18 fields**: case_id, case_name, year, domain, jurisdiction,
  access_level, outcome, plaintiff_type, representation, outcome_type,
  algorithm_type, notes, legal_citation, docket_number, primary_source_url,
  secondary_source_url, verification_status, last_verified.
- **Provenance is real:** 165/168 carry a docket number, 165 a primary-source URL,
  157 marked Verified. Example row: `EEOC v. iTutorGroup` (Employment, US-Federal,
  2023, ML hiring age-discrimination, $365K settlement, docket 1:22-cv-02565 EDNY).
- **Domain** (chart source `cases_by_domain.csv`): Employment 39, Criminal Justice 32,
  Credit 28, Government Benefits 27, Housing 20, Healthcare 13, Platform Liability 6,
  Government/Services 3.
- **Time:** year 2012–2025, rising to a 2024 peak (39), 2023 (29), 2022/2025 (21),
  2021 (20).
- **AI nexus (algorithm_type):** machine_learning **106 (63%)**, statistical_model
  34 (20%), rule_based 23 (14%), unknown 5 — majority ML/statistical systems.
- **Outcome:** Achieved 102, Ongoing 48, Denied 18. **outcome_type:** policy_change 37,
  monetary 32, system_discontinued 14, system_modified 9, injunctive 9, pending 50.
- **Who sues:** private_class 38, individual 35, nonprofit 33, federal_agency 31,
  union 13, state_AG 11. **Jurisdiction:** US-Federal 72, US-IL 17 (BIPA), NL 7,
  UK 7, US-CA 6, US-NY 6, Italy 4, EU 3…
- **access_level** (the paper's key variable — evidentiary access): Partial 88,
  Full 52, None 28.

## Not from the data (from the paper, this run)
- The paper's headline: litigated cases **without** evidence access succeed ~**9%**;
  **with** access, ~**97%** in domains without liability shields.

## Files
- `cases_by_domain.csv` — chart source.
- `zenodo_meta.json` — record metadata.
- `algo_cases/cases.csv`, `codebook.md`, `README.md`, `summary_statistics.py`.
