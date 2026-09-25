# Probe — AI/ML H-1B labor market (DOL OFLC LCA disclosure data)

**Authoritative source (confirmed this run):** DOL Office of Foreign Labor
Certification LCA disclosure files — quarterly .xlsx, **FY2008–FY2025**, bulk-
downloadable, fields: employer, job title, SOC/O*NET code, wage, wage level,
worksite, case status (https://www.dol.gov/agencies/eta/foreign-labor/performance).
AI/ML aggregate verified via OFLC-derived reporting (VisaPulse, visapulseusa.com/ai-jobs).

## Verified this run
- **FY2025: 7,536 AI/ML LCA filings**, up from **2,807 in FY2020 (+168%)**.
- **Average wage $277K** for AI/ML roles vs **$121K** across all H-1B — a **+131% premium**.
- **Top sponsors** (AI/ML filings; cumulative): Amazon 4,252 ($165K avg), Apple 2,115
  ($187K), Microsoft 1,989 ($147K), LinkedIn 999, Qualcomm 656
  (`ai_h1b_top_sponsors.csv`).
- **Top titles** (cumulative): Machine Learning Engineer 13,218 ($248K), Applied
  Scientist 7,797 ($209K), AI Engineer 682 ($156K).
- **Geography:** California 15,107 filings ($290K avg), Washington 5,978 ($165K).

## Honesty note (partial probe)
I verified the AI/ML slice from OFLC-derived reporting and confirmed the DOL bulk
files as the open authoritative source; I did **not** compute the full
employer × role × wage × worksite panel from the raw xlsx this run (the quarterly
files are large). That panel is the build step. Note some VisaPulse title/sponsor
counts are cumulative/multi-year, not FY2025-only.

## Agenda note
The economic edge of the agenda: the AI-industry labor supply and the concentration
of AI talent in a handful of firms — governance-adjacent (AI-power concentration;
the AI-talent immigration fight), not squarely political information/representation.

## Files
- `ai_h1b_top_sponsors.csv` — top AI/ML H-1B sponsors (chart source).
