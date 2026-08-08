# Daily Dataset Hunt

An autonomous daily run that does genuinely deep discovery of **unclaimed datasets**
for Free Systems research — without degrading into a listicle generator.

The hard problem here is not scheduling. It is forcing **novelty** and **depth**
every single day. Both are solved with **state + structure**, not with a bigger
prompt. This repo *is* the memory: the ledger is versioned in git, every run is
reproducible, and the output is a committed memo plus an auto-opened GitHub issue
you can triage in under two minutes.

## How it works

Every weekday morning a **Claude scheduled Routine** fires a fresh Claude session
that executes [`HARNESS.md`](./HARNESS.md) with web search enabled. The run:

1. **Reads state first.** [`LEDGER.md`](./LEDGER.md) (everything ever found or
   rejected) and [`FRONTIERS.md`](./FRONTIERS.md) (ten rotating search frontiers).
   Anything already in the ledger is dead on arrival.
2. **Diverges** onto today's frontier (`day_of_year % 10`) and pulls ≥15 live
   candidate datasets via real web searches — no candidates from memory.
3. **Screens** each candidate 1–5 on the five-point Willis rubric and kills
   anything under 18/25 or colliding with the ledger.
4. **Deep-dives** the top two: access mechanics, collection cost, nearest existing
   paper, headline figure, first analysis.
5. **Writes** `memos/YYYY-MM-DD.md`, appends to the ledger, commits both to `main`,
   and pushes a short brief to your phone. A null day is allowed and beats a padded one.

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
| `META.md` | The weekly meta-review prompt: ranks the week's finds, flags harness drift, proposes frontier edits. |

## Operating it

### 1. The scheduled Routine

The hunt runs as a **Claude scheduled Routine** (a recurring trigger) rather than
GitHub Actions — no Anthropic API key or Actions secret is needed. The Routine
fires a fresh Claude session on weekday mornings (`0 13 * * 1-5` UTC ≈ 6am PT),
which runs `HARNESS.md`, commits the memo + ledger to `main`, and delivers a short
brief to your phone via the Routine's push notification.

Manage it from the **Routines** UI on claude.ai (pause, edit the schedule, or fire
it on demand). Because the schedule is a fixed UTC cron, the local fire time shifts
by an hour across US daylight-saving changes (6am PDT / 5am PST) — nudge the cron
if you want it pinned to 6am year-round.

### 2. Triage (the human loop, <2 min/day)

Each run pushes a brief to your phone with the best find and a link to the full
memo in `memos/`. If a find is worth pursuing, promote it in the ledger to `spec'd`
and write a project spec doc for it. Everything else stays in the ledger so it is
never re-litigated.

### 3. Tune

Edit `HARNESS.md` and `FRONTIERS.md` like source code. `META.md` is the weekly
meta-review prompt — run it on demand (or wire up a second weekly Routine) to rank
the week's finds, flag harness drift, and propose frontier edits.

## Definition of done

Repo live with `HARNESS.md`, a seeded `LEDGER.md`, `FRONTIERS.md`, the daily Routine
firing, and five consecutive weekday memos where at least two contain a find you
genuinely had not considered.
