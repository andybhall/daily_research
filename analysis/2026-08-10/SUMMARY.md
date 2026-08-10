# FARA live-probe results — 2026-08-10

**Source:** DOJ FARA eFile bulk tables (`FARA_All_Registrants.xml`,
`FARA_All_ForeignPrincipals.xml`), pulled today via the OpenSanctions
`us_fara_filings` mirror (dataset refreshed 2026-08-10T06:09Z).
Bulk zips: https://data.opensanctions.org/datasets/latest/us_fara_filings/

| Metric | Value |
|---|---|
| Registrant rows (agents) | 7,075 |
| Foreign-principal relationships | 17,724 |
| Distinct registrants with ≥1 foreign principal | 7,064 |
| Registration_Date span (registrants) | 1942–2026 |
| Registrants representing >1 foreign principal | 1,945 (28%) |
| Max foreign principals for one registrant (#3301) | 278 |

**Top foreign-principal countries** (of 17,724 relationships): Japan 6.6%,
Canada 4.6%, Mexico 3.3%, Great Britain 3.1%, France 2.9%, South Korea 2.5%,
Germany 2.2%, Israel 1.8%, USSR 1.7%, China 1.6%, Taiwan 1.5%.

**Foreign-principal registrations/yr** rise through the first Trump term
(2017: 232 → 2018: 294 → 2019: 308), consistent with the post-2017 FARA
enforcement surge. Full country distribution in `fara_country_counts.csv`.
