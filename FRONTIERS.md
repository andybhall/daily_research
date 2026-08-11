# FRONTIERS

Ten search frontiers. Each run takes `day_of_year % 10` and **must spend its
divergence phase there**. The index is 1-indexed in the list below; index `0` maps
to frontier **10**. This rotation exists to prevent mode collapse onto the same
five ideas every day — the frontier is a constraint, not a suggestion.

| idx | Frontier |
|-----|----------|
| 1 | **Legal / judicial exhaust** — dockets, sanctions orders, amicus briefs, discovery exhibits, consent decrees, PACER/RECAP corners |
| 2 | **Money trails** — procurement, financial disclosures, Form 990s, lobbying registrations, grants, subawards, sole-source contracts |
| 3 | **Optimized persuasion text** — ads, SMS/robotext, push notifications, email subject lines, A/B-tested fundraising copy |
| 4 | **Platform / API exhaust** — app-store metadata, browser extensions, model marketplaces, ToS diffs, changelogs, review corpora |
| 5 | **Institutional records** — hearing transcripts, public comments, agendas, visitor logs, staffing/payroll, calendars |
| 6 | **Collector / hobbyist archives** — the Derek Willis genre: individuals quietly hoarding structured data nobody has exploited |
| 7 | **Non-US / non-English sources** — EU transparency registers, Japan, India election tech, national open-data portals |
| 8 | **Labor & organizational** — job postings, Glassdoor/Blind reviews, union filings, WARN notices, H-1B/LCA disclosures |
| 9 | **Markets & governance** — prediction markets, DAO votes, proxy voting, shareholder resolutions, resolution disputes |
| 10 | **Wildcard: academic dataverse trawl** — ICPSR, Harvard Dataverse, Zenodo, OSF — recent deposits nobody has exploited yet |

## How to use a frontier

- **Hunt the AI angle within the frontier.** The hunt is now AI-focused (HARNESS
  anti-slop rule 6): each frontier is a search territory, but every candidate must
  have a clear AI nexus. Read each frontier as "where does AI show up *here*?" —
  e.g., AI-generated ads in persuasion text, algorithmic decisions in legal exhaust,
  AI-vendor money in the money trails, model marketplaces in platform exhaust. A
  frontier with no AI-relevant corner today is a null day, not license to drift.
- Do not treat the one-line description as the whole territory. Each frontier is a
  door into a genre. Push past the obvious first three sources.
- Think in three passes within the frontier: **collector** (who is quietly hoarding
  this?), **adversary** (who is optimizing against a metric here, leaving exhaust?),
  **bureaucrat** (what does some process incidentally log?).
- A thin day on the assigned frontier is not license to switch frontiers. Dig
  laterally: adjacent registries, cited-by trails, "who else uses this feed."

## Editing this file

The weekly meta-run (Sundays) may propose edits — retiring a mined-out frontier,
splitting a fertile one, adding a new genre. Changes land via normal PRs so the
rotation stays legible and reviewable.
