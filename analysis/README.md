# analysis/

Per-run live-probe artifacts from the Daily Dataset Hunt (HARNESS Phase 3.5).

Each run that reaches a live probe writes to `analysis/<RUN_DATE>/`:

- the **bounded data sample** actually pulled that run (a small API page, bulk
  subset, or scrape — a few hundred records / few MB, ToS- and rate-limit-respecting),
- any **script** used to pull and analyze it, and
- the **output** (a small table or chart) whose headline numbers appear in that
  day's memo under *Evidence from a live sample*.

Every figure in a memo's evidence line must trace to a file here — the probe exists
so a find is proven against real data, not just a landing page. Nothing here is
fabricated; if a run could not probe, its memo says so and this folder simply has no
entry for that date.
