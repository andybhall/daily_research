# Probe — Leading the Future (AI industry super PAC), FEC filings

**Source:** FEC OpenData API, committee **C00916114 "LEADING THE FUTURE"**
(https://api.open.fec.gov/v1/). Pulled 2026-09-09 with the public DEMO_KEY (rate-limited
to 40/hr — one call was throttled and retried). Watchdog trackers on the same committee:
Demand Progress **AI Money Watch** (https://aimoneywatch.org/), Transformer News
(https://elections.transformernews.ai/pacs/C00916114).

## Computed this run (from the FEC API)
- **Committee totals, 2026 cycle** (`fec_totals.json`, coverage end 2026-06-30):
  receipts **$75,788,224**, disbursements **$44,755,781**, cash-on-hand
  **$31,032,443**, contributions **$75,100,000**, independent expenditures $0 (as of
  the 6/30 report).
- **Donor concentration:** only **20 itemized receipts** on record. Largest single
  itemized gifts (`donors_chart.csv`): A16Z Capital Management LLC **$25,000,000**;
  Ben Horowitz, Marc Andreessen, Greg Brockman (OpenAI president), and Anna Brockman
  **$12,500,000 each**; Perplexity (Perplex AI Inc.) **$100,000**. A handful of
  a16z- and OpenAI-linked donors account for essentially the entire war chest.
  (Note: itemized rows span filings across 2025–2026 periods and should not be summed
  naively against the cycle total; the totals above are the authoritative aggregates.)

## Not from my probe (reporting, cited in memo)
- The LTF **network** (LTF + Think Big PAC + American Mission PAC) has raised
  >$125–140M and spent >$24M in federal primaries (CNBC/NOTUS, FEC filings).
- AI Money Watch: 21 races, 13 endorsed candidates (Demand Progress).

## Files
- `fec_totals.json` — committee totals.
- `fec_receipts.json` — top itemized receipts (Schedule A).
- `donors_chart.csv` — largest single gift per donor (chart source).
- `top_donors.csv` — raw top receipts incl. custodian-bank interest lines.
