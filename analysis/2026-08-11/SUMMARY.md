# Snap Political Ads live-probe results — 2026-08-11

**Source:** Snap Political & Advocacy Ads Library, yearly bulk ZIPs pulled today
(`https://storage.googleapis.com/ad-manager-political-ads-dump/political/<YEAR>/PoliticalAds.zip`).
Each row is one political ad: **CreativeUrl** (the copy) + **Spend** + **Impressions**
+ **StartDate/EndDate** + **PayingAdvertiserName/Committee** + ~20 targeting columns.

| Metric | 2024 | 2026 (YTD) |
|---|---|---|
| Ads | 23,027 | 5,121 |
| Distinct paying advertisers | 626 | 217 |
| Total USD spend | $29,403,590 | $2,520,367 |
| Total impressions | 3,765,057,742 | 941,836,621 |
| Start-date span | 2022-11-01 → 2024-12-31 | 2025-02-20 → 2026-08-11 |
| Ads using geo/interest/segment microtargeting | 86% | 59% |

**Panel structure:** 68 paying advertisers appear in BOTH the 2024 and 2026 files
(e.g. AFSCME) — a real cross-cycle advertiser panel, not a single snapshot.
Top 2024 advertisers by ad count: Harris for President (6,470), Voter Formation
Project (1,262), Biden for President (993). Full top-40 in
`snap_top_advertisers_2024.csv`; field list in `snap_field_readme.txt`.
