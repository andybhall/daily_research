# Daily Dataset Hunt

An autonomous daily run that does genuinely deep discovery of **unclaimed datasets**
for Free Systems research — without degrading into a listicle generator.

The hard problem here is not scheduling. It is forcing **novelty** and **depth**
every single day. Both are solved with **state + structure**, not with a bigger
prompt. This repo *is* the memory: the ledger is versioned in git, every run is
reproducible, and the output is a committed memo plus an auto-opened GitHub issue
you can triage in under two minutes.

## How it works

Every weekday morning a scheduled run executes [`HARNESS.md`](./HARNESS.md) in
Claude Code headless mode with web search enabled. The run:

1. **Reads state first.** [`LEDGER.md`](./LEDGER.md) (everything ever found or
   rejected) and [`FRONTIERS.md`](./FRONTIERS.md) (ten rotating search frontiers).
   Anything already in the ledger is dead on arrival.
2. **Diverges** onto today's frontier (`day_of_year % 10`) and pulls ≥15 live
   candidate datasets via real web searches — no candidates from memory.
3. **Screens** each candidate 1–5 on the five-point Willis rubric and kills
   anything under 18/25 or colliding with the ledger.
4. **Deep-dives** the top two: access mechanics, collection cost, nearest existing
   paper, headline figure, first analysis.
5. **Writes** `memos/YYYY-MM-DD.md`, appends to the ledger, and opens a GitHub
   issue titled with the best find. A null day is allowed and beats a padded one.

The anti-slop mechanics live in [`HARNESS.md`](./HARNESS.md#anti-slop-rules) and
are explained in the spec below.

## The three-layer research agenda

Relevance is scored against a fixed agenda so the hunt stays anchored:

- **Information** — how political information is produced, distributed, and
  distorted (persuasion, advertising, media, disclosure, communications).
- **Representation** — how citizen preferences and voices get expressed and
  aggregated into collective choice (elections, participation, deliberation,
  constituent contact).
- **Governance** — how institutions make, contest, and enforce binding decisions
  (courts, agencies, legislatures, procurement, corporate/DAO governance).

## Repo layout

| Path | Role |
|------|------|
| `HARNESS.md` | The daily run prompt. The four mandatory phases + hard quality rules. Tune this like code. |
| `LEDGER.md` | Versioned state. Found / Rejected / Agenda. Read first every run. |
| `FRONTIERS.md` | Ten search frontiers + the rotation rule. |
| `memos/` | One dated memo per run (≤800 words, verified URLs mandatory). |
| `.github/workflows/daily-hunt.yml` | Cron: 6am PT weekdays. Runs the harness, commits, opens an issue. |
| `.github/workflows/weekly-meta.yml` | Sundays: ranks the week's finds, flags harness drift, proposes frontier edits. |

## Operating it

### 1. Enable the scheduled run (GitHub Actions)

The daily workflow needs one secret:

- `ANTHROPIC_API_KEY` — an Anthropic API key with web search access.
  Add it under **Settings → Secrets and variables → Actions**.

`GITHUB_TOKEN` is provided automatically; the workflow requests `contents: write`
and `issues: write` so it can commit the memo and open the issue.

Once the secret is set the cron fires on its own. You can also run it on demand
from the **Actions** tab (**Run workflow**), or lock in a run by triggering
`workflow_dispatch`.

### 2. Triage (the human loop, <2 min/day)

Each run opens an issue titled with the best find. Skim it. If a find is worth
pursuing, label it and it graduates to `spec'd` — write a project spec doc for it.
Everything else stays in the ledger so it is never re-litigated.

### 3. Tune

Edit `HARNESS.md` and `FRONTIERS.md` like source code. The weekly meta-run
proposes edits; you accept or reject them via normal PRs.

## Definition of done

Repo live with `HARNESS.md`, a seeded `LEDGER.md`, `FRONTIERS.md`, cron firing,
and five consecutive weekday memos where at least two contain a find you genuinely
had not considered.
