# META — Weekly Meta-Run

You are running the weekly meta-review of the Daily Dataset Hunt. Your job is to
look across the week's work, judge it honestly, and keep the harness from drifting
into slop. You are the quality control on the quality-control machine.

Read first, in full:

- `LEDGER.md` — current state.
- `FRONTIERS.md` — the rotation.
- `HARNESS.md` — the daily prompt you are auditing.
- Every `memos/*.md` file from the **last 7 days**.

Then produce a review with these sections. Be concrete and critical — flattery is
useless here.

## 1. Rank the week's finds

List each of the week's finds (from the memos and the ledger delta). Rank them by
research value. Call out the single best find and say why. Call out any find that,
on reflection, should not have cleared the bar and explain the miss.

## 2. Harness drift check

Look for the failure modes this system is designed to prevent, and say whether they
are creeping in:

- **Novelty decay** — are finds converging on the same few genres regardless of the
  assigned frontier? Are candidates recycling ledger-adjacent ideas?
- **Depth decay** — are deep-dives getting thinner? Are access-mechanics and
  nearest-paper claims actually verified, or hand-waved?
- **Citation discipline** — spot-check three claims across the week's memos against
  their cited URLs. Did any claim lack a fetched source? Report specifics.
- **Frontier balance** — is any frontier consistently barren or consistently
  over-productive?

## 3. Proposed edits

Propose concrete edits to `FRONTIERS.md` and/or `HARNESS.md`:

- Retire a mined-out frontier, split a fertile one, or add a new genre.
- Tighten or adjust a rubric criterion if the scores are not discriminating.
- Any harness wording that is being gamed or ignored.

Make the edits directly to the files if you are confident; otherwise describe them
precisely in the issue for human review. Do not rewrite wholesale — surgical
changes only, so the rotation and rubric stay legible.

## 4. Emit the issue

Write a triage-ready summary to `.hunt/meta-issue-body.md`: the week's best find,
the most important drift signal, and the proposed edits (with rationale). Keep it
under 400 words. Leave any edited files staged; the workflow commits and opens the
issue.
