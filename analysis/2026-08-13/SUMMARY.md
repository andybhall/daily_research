# Federal AI Use Case Inventory live-probe results — 2026-08-13

**Source:** OMB 2024 consolidated inventory CSV (62 columns), pulled today from
`https://raw.githubusercontent.com/ombegov/2024-Federal-AI-Use-Case-Inventory/main/data/2024_consolidated_ai_inventory_raw.csv`.
Each row = one agency-reported AI use case (mandated under EO 13960 + OMB M-24-10).

| Metric | 2024 |
|---|---|
| Use cases | 1,757 |
| Distinct agencies | 37 |
| Columns per record | 62 |
| Rights- or Safety-Impacting (rights 59 + safety 18 + both 150) | 227 |
| Already **Retired** | 133 |

**Top agencies:** HHS (271), Veterans Affairs (229), Homeland Security (183),
Interior (180), USAID (137), Agriculture (89), Energy (79), Labor (70).

**Dev-stage lifecycle:** Operation & Maintenance 627 · Acquisition/Development 351 ·
Initiated 329 · Implementation & Assessment 275 · Retired 133 · Planned 20.

**Panel:** OMB publishes this annually (2023 → 2024 → 2025); 2025 already reports
3,611 use cases across 56 agencies (a 105% YoY jump), so agency × year × dev-stage
is a real longitudinal panel. Note: `18_date_initiated` is almost entirely empty —
a genuine missingness caveat. Breakdowns in `fed_ai_inventory_breakdowns.csv`.
