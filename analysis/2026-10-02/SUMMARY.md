# 2026-10-02 — Public comments on federal AI rulemaking (regulations.gov)

**Object:** The public-comment corpora on federal AI rulemakings/inquiries, pulled via the open
regulations.gov API — a record of *who shows up to shape US AI governance*, and the channel the
GAO (July 2026) says is now being distorted by AI-generated mass comments.

## Verified this run
- Copyright Office AI Notice of Inquiry (docket **COLC-2023-0006**): **10,371 comments**
  — verified live via `GET https://api.regulations.gov/v4/comments?filter[docketId]=COLC-2023-0006`
  (DEMO_KEY; `meta.totalElements = 10371`). Rate-limited after one call.
- NIST AI EO 14110 RFI (NIST-2023-0009): **214 comments** (nist.gov).
- OMB draft AI memo M-24-10: **196 comments** (whitehouse.gov).

## Why it matters
The copyright/training-data question (artists, creators, publishers, AI firms) mobilized ~50x the
participation of the technical AI-governance RFIs, which drew mostly organized interests. The
comment corpora are open, incidental, longitudinal (2023→2026 across dockets), and panel-able by
docket × commenter × organization × position × date.

## Honest caveats
- Only the Copyright docket count was verified live via the API this run (DEMO_KEY rate limit);
  OMB/NIST counts are from authoritative agency pages, not re-pulled from the API.
- "Comments as data" is a well-established genre (Balla on mass-comment campaigns; influence-tracing
  work). The unbuilt part is the **AI-specific cross-docket participation panel** + the
  AI-generated-comment distortion layer. A full build needs a keyed regulations.gov API pull.
