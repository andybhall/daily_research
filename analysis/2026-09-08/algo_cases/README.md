# Algorithmic Contestability Cases Database

Supplementary data repository for "Beyond Explanation: Evidentiary Rights for Algorithmic Accountability" (ACM FAccT '26).

## Overview

This repository contains a comprehensive database of 168 legal cases, regulatory actions, and administrative proceedings involving algorithmic decision-making systems across seven domains. The dataset documents evidence access levels and contestation outcomes to support empirical analysis of procedural rights in algorithmic accountability.

## Citation

If you use this dataset, please cite:

```bibtex
@inproceedings{anonymous2026beyond,
  title={Beyond Explanation: Evidentiary Rights for Algorithmic Accountability},
  author={Anonymous},
  booktitle={Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency},
  year={2026},
  publisher={ACM}
}
```

## Dataset Description

### Domains Covered

| Domain | Cases | Description |
|--------|-------|-------------|
| Employment | 39 | Hiring algorithms, gig worker management, workplace surveillance |
| Housing | 20 | Tenant screening, rental pricing, fair housing |
| Healthcare | 13 | Insurance denials, clinical decision support, prior authorization |
| Criminal Justice | 32 | Risk assessment, facial recognition, predictive policing |
| Government Benefits | 30 | Welfare automation, fraud detection, eligibility determination |
| Credit & Consumer | 28 | Lending algorithms, insurance pricing, consumer protection |
| Platform Liability | 6 | Content moderation, recommendation algorithms, Section 230 |

### Key Variables

**Core Variables:**
- `case_id`: Unique identifier (e.g., EMP-01, HOU-01, CJ-01)
- `case_name`: Primary case or system name
- `year`: Year of primary legal action or resolution
- `domain`: Subject matter domain
- `jurisdiction`: Geographic jurisdiction (US state, country, or international body)
- `access_level`: Evidence access achieved (Full, Partial, None)
- `outcome`: Contestation result (Achieved, Denied, Ongoing)
- `notes`: Brief description of key facts and outcomes

**Confound Control Variables:**
- `plaintiff_type`: Entity bringing the challenge (federal_agency, state_AG, nonprofit, private_class, individual, union, academic, internal, corporate, state_agency)
- `representation`: Type of legal representation (government, public_interest, private_counsel, union_counsel, public_defender, academic, pro_se, internal)
- `outcome_type`: Type of relief obtained (monetary, injunctive, policy_change, system_modified, system_discontinued, pending, none)
- `algorithm_type`: Technical classification (rule_based, statistical_model, machine_learning, unknown)

**Verification Fields:**
- `legal_citation`: Primary legal citation or docket number
- `docket_number`: Court docket or regulatory filing ID
- `primary_source_url`: Link to authoritative source
- `secondary_source_url`: Backup source
- `verification_status`: Verified / Needs Review / Unable to Verify
- `last_verified`: Date of last verification

See `codebook.md` for complete variable definitions and coding rules.

## Files

```
algorithmic-contestability-cases-anonymous/
├── cases.csv              # All 168 cases in CSV format
├── cases.json             # Same data in JSON format
├── codebook.md            # Variable definitions and coding methodology
├── citations.bib          # Bibliography of primary sources
├── summary_statistics.py  # Reproducible summary statistics
└── README.md              # This file
```

## Methodology

### Case Selection

Cases were identified through systematic review of:
1. Legal databases (Westlaw, LexisNexis, PACER, CourtListener)
2. Regulatory enforcement actions (FTC, CFPB, EEOC, DOJ, HUD)
3. International court decisions and data protection authority rulings
4. Academic literature on algorithmic accountability
5. Investigative journalism and civil society reports

### Inclusion Criteria

- Involves algorithmic or automated decision-making system
- Includes documented legal challenge, regulatory action, or administrative proceeding
- Evidence access level can be determined from available documentation
- Occurred between 2012-2025

### Coding Independence

**Important**: The `access_level` variable was coded independently of the `outcome` variable. Access levels were determined based on documented disclosure events (court orders, FOIA responses, regulatory audits) without reference to case outcomes. This sequential coding process prevents tautological correlation.

### Verification Status

As of January 2025:
- **Verified**: 160 cases (92%) - Primary source confirmed accessible
- **Unable to Verify**: 2 cases (1%) - Cannot locate authoritative primary source
- **Unverified**: 12 cases (7%) - Added after initial verification sweep

## Known Limitations

1. **Survivorship Bias**: Only cases reaching public attention are observable
2. **Selection Effects**: Case strength may correlate with both access and outcome
3. **Ongoing Cases**: 30% of cases have unknown final outcomes
4. **Geographic Concentration**: 79% of cases are from the United States
5. **Temporal Clustering**: 52% of cases are from 2023-2025
6. **Algorithm Heterogeneity**: Systems range from simple rules to complex ML models

## Data Quality

### Summary Statistics

| Metric | Value |
|--------|-------|
| Total Cases | 168 |
| Verified Sources | 160 (92%) |
| With Primary URLs | 168 (98%) |
| With Any URL | 168 (100%) |

### Outcome Distribution

| Outcome | Count | Percentage |
|---------|-------|------------|
| Achieved | 102 | 60.7% |
| Ongoing | 51 | 30.2% |
| Denied | 18 | 10.7% |

## License

This dataset is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt the material with appropriate attribution.

## Contact

For questions about the dataset or to report corrections, please contact the authors.

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01 | Initial anonymous release with 168 cases |
| 1.1 | 2026-03 | Updated README statistics, synced JSON with CSV, corrected domain labels |
