# Probe — GAO federal-AI oversight recommendations

**Sources fetched this run:** GAO AI-work overview (gao.gov/products/gao-24-107237)
and the flagship report GAO-24-105980 (gao.gov/products/gao-24-105980). GAO's
Recommendations Database (gao.gov/reports-testimonies/recommendations-database) is
the filterable, status-tracked access point.

## Verified this run
- GAO has issued **~50 AI products since 2018**, with **20 ongoing AI projects**.
- Flagship (Dec 2023) GAO-24-105980: **35 recommendations to 19 agencies** on
  implementing federal AI requirements.
- **Implementation status (as tracked by GAO):** Closed–Implemented **17**, Open
  **15**, Closed–Not Implemented **3** (`gao_ai_recs_status.csv`).
- **OPM** received the most (5); OMB 2; the rest 2–4 each (Commerce, Education,
  Energy, HHS, DHS, Interior, Labor, State, Transportation, Treasury, VA, EPA, GSA,
  NASA, USAID).
- Key gaps flagged: only **5 of 23 agencies** had comprehensive AI use-case
  inventories (15 incomplete/inaccurate); OMB had not issued AI acquisition
  guidance; OPM had not established an AI occupational series; missing
  regulatory-authority and EO 13960 high-impact-AI plans.

## Why it's a distinct object
Independent-oversight leg of federal AI governance — whether agencies actually
comply — separate from the ledger's Federal AI Use Case Inventory (the systems,
08-13), the (now de-published) CAIO roster (staffing), and the Congressional AI
hearings corpus (legislative, 09-02). Each GAO recommendation is status-tracked
over time → a recommendation × agency × status × year panel.

## Files
- `gao_ai_recs_status.csv` — flagship recommendation status (chart source).
