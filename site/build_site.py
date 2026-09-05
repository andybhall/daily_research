#!/usr/bin/env python3
"""Static-site generator for the Daily Dataset Hunt.

Reads memos/*.md + LEDGER.md and writes a public site into docs/ (served by
GitHub Pages from main/docs). Stdlib-only — no external dependencies.

Run from the repo root:  python3 site/build_site.py
"""
import html
import re
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEMOS = ROOT / "memos"
DOCS = ROOT / "docs"
SITE_TITLE = "The Daily Dataset Hunt"
SITE_TAGLINE = ("An autonomous daily search for unclaimed, AI-relevant datasets for "
                "Free Systems research — how AI is reshaping political information, "
                "representation, and governance.")
REPO_URL = "https://github.com/andybhall/daily_research"

# ---------------------------------------------------------------------------
# Minimal, bounded Markdown -> HTML for the memo subset we author:
# headings, bold, italic, inline code, links, bullet lists, tables, blockquotes, hr.
# ---------------------------------------------------------------------------

def _inline(text: str) -> str:
    """Inline formatting on an already-plain (unescaped) string."""
    out = html.escape(text, quote=False)
    # inline code first (protect its contents from further formatting)
    codes = []
    def _stash_code(m):
        codes.append(m.group(1))
        return f"\x00CODE{len(codes)-1}\x00"
    out = re.sub(r"`([^`]+)`", _stash_code, out)
    # links [text](url)
    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
                 lambda m: f'<a href="{html.escape(m.group(2), quote=True)}" '
                           f'rel="noopener">{m.group(1)}</a>', out)
    # bold then italic
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", out)
    # restore code
    for i, c in enumerate(codes):
        out = out.replace(f"\x00CODE{i}\x00", f"<code>{html.escape(c, quote=False)}</code>")
    return out


def md_to_html(md: str) -> str:
    lines = md.split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        # blank
        if not stripped:
            i += 1
            continue

        # horizontal rule
        if re.fullmatch(r"-{3,}", stripped):
            out.append("<hr>")
            i += 1
            continue

        # heading
        m = re.match(r"(#{1,6})\s+(.*)", stripped)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{_inline(m.group(2))}</h{lvl}>")
            i += 1
            continue

        # table: current line has pipes and next line is a separator row
        if "|" in line and i + 1 < n and re.match(r"\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$", lines[i+1]) and "|" in lines[i+1]:
            def cells(row):
                row = row.strip()
                if row.startswith("|"): row = row[1:]
                if row.endswith("|"): row = row[:-1]
                return [c.strip() for c in row.split("|")]
            header = cells(line)
            i += 2  # skip header + separator
            body = []
            while i < n and "|" in lines[i] and lines[i].strip():
                body.append(cells(lines[i]))
                i += 1
            thead = "".join(f"<th>{_inline(c)}</th>" for c in header)
            rows = ""
            for r in body:
                r = (r + [""] * len(header))[:len(header)]
                rows += "<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>"
            out.append(f'<div class="table-wrap"><table><thead><tr>{thead}</tr></thead>'
                       f"<tbody>{rows}</tbody></table></div>")
            continue

        # blockquote (may span multiple lines)
        if stripped.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append(f"<blockquote>{_inline(' '.join(b.strip() for b in buf))}</blockquote>")
            continue

        # bullet list
        if re.match(r"[-*]\s+", stripped):
            items = []
            while i < n and re.match(r"\s*[-*]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[i]).strip())
                i += 1
            out.append("<ul>" + "".join(f"<li>{_inline(it)}</li>" for it in items) + "</ul>")
            continue

        # ordered list
        if re.match(r"\d+\.\s+", stripped):
            items = []
            while i < n and re.match(r"\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]).strip())
                i += 1
            out.append("<ol>" + "".join(f"<li>{_inline(it)}</li>" for it in items) + "</ol>")
            continue

        # paragraph (gather until blank / block start)
        buf = [stripped]
        i += 1
        while i < n and lines[i].strip() and not re.match(r"(#{1,6}\s|[-*]\s|>|\d+\.\s)", lines[i].strip()) \
                and not re.fullmatch(r"-{3,}", lines[i].strip()) and "|" not in lines[i]:
            buf.append(lines[i].strip())
            i += 1
        out.append(f"<p>{_inline(' '.join(buf))}</p>")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Memo parsing + page rendering
# ---------------------------------------------------------------------------

def parse_memo(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    d = path.stem  # YYYY-MM-DD
    def find(pat, default=""):
        m = re.search(pat, text, re.M)
        return m.group(1).strip() if m else default
    frontier = find(r"^\*\*Frontier:\*\*\s*(.+)$")
    verdict = find(r"^\*\*Verdict:\*\*\s*(.+)$")
    topfind = find(r"^##\s*Top find:\s*(.+)$") or find(r"^##\s*Top finds?:?\s*(.+)$")
    score = find(r"\*\*Score:\s*([0-9]+/25)\*\*")
    try:
        pretty = datetime.strptime(d, "%Y-%m-%d").strftime("%B %-d, %Y")
    except ValueError:
        pretty = d
    return {"date": d, "pretty": pretty, "frontier": frontier, "verdict": verdict,
            "topfind": topfind, "score": score, "body_html": md_to_html(text)}


CSS = """
:root{--bg:#faf9f7;--fg:#1a1a1a;--muted:#5c5c5c;--line:#e3e0da;--card:#fff;--accent:#8a5a2b;--accent2:#b5843f;--code:#f0ede8}
@media (prefers-color-scheme:dark){:root{--bg:#14140f;--fg:#ececec;--muted:#a5a5a5;--line:#2c2c26;--card:#1c1c17;--accent:#d9a45b;--accent2:#c98f42;--code:#22221c}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-text-size-adjust:100%}
.wrap{max-width:820px;margin:0 auto;padding:0 20px}
header.site{border-bottom:1px solid var(--line);padding:34px 0 22px;margin-bottom:8px}
header.site h1{margin:0;font-size:26px;letter-spacing:-.02em}
header.site h1 a{color:var(--fg);text-decoration:none}
header.site p{color:var(--muted);margin:.5em 0 0;font-size:15px}
nav.top{margin-top:14px;font-size:14px}
nav.top a{color:var(--accent);text-decoration:none;margin-right:16px}
nav.top a:hover{text-decoration:underline}
a{color:var(--accent)}
h2{font-size:21px;letter-spacing:-.01em;margin:1.6em 0 .5em}
h3{font-size:17px;margin:1.4em 0 .4em}
hr{border:0;border-top:1px solid var(--line);margin:2em 0}
blockquote{margin:1em 0;padding:.4em 1em;border-left:3px solid var(--accent2);background:var(--card);color:var(--muted);border-radius:0 6px 6px 0}
code{background:var(--code);padding:.12em .38em;border-radius:4px;font-size:.88em;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.table-wrap{overflow-x:auto;margin:1.1em 0}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}
th{background:var(--card);font-weight:600}
ul,ol{padding-left:1.3em}
li{margin:.28em 0}
.feed{list-style:none;padding:0;margin:18px 0}
.feed li{border:1px solid var(--line);background:var(--card);border-radius:10px;padding:16px 18px;margin:0 0 14px}
.feed .date{font-size:13px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
.feed .frontier{font-size:13px;color:var(--accent2);margin:.15em 0 .5em}
.feed h2{margin:.1em 0 .35em;font-size:18px}
.feed h2 a{color:var(--fg);text-decoration:none}
.feed h2 a:hover{color:var(--accent)}
.feed .verdict{margin:.2em 0;color:var(--fg)}
.feed .meta{font-size:13.5px;color:var(--muted);margin-top:.5em}
.badge{display:inline-block;background:var(--accent);color:#fff;border-radius:20px;padding:1px 9px;font-size:12px;font-weight:600;margin-left:6px}
footer.site{border-top:1px solid var(--line);margin:40px 0 60px;padding-top:18px;color:var(--muted);font-size:13px}
.backlink{display:inline-block;margin:18px 0 4px;font-size:14px}
.memo :first-child{margin-top:.2em}
"""

def page(title, body, rel="", description=None):
    desc = html.escape(description or SITE_TAGLINE, quote=True)
    nav = (f'<nav class="top"><a href="{rel}index.html">Home</a>'
           f'<a href="{rel}ledger.html">Ledger</a>'
           f'<a href="{REPO_URL}" rel="noopener">GitHub</a></nav>')
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{desc}">
<link rel="stylesheet" href="{rel}style.css">
</head><body><div class="wrap">
<header class="site"><h1><a href="{rel}index.html">{html.escape(SITE_TITLE)}</a></h1>
<p>{html.escape(SITE_TAGLINE)}</p>{nav}</header>
{body}
<footer class="site">Autonomous daily research · memos and ledger are versioned in
<a href="{REPO_URL}" rel="noopener">git</a>. Built {date.today().isoformat()}.</footer>
</div></body></html>"""


def build():
    memo_files = sorted((p for p in MEMOS.glob("*.md") if p.stem[0].isdigit()),
                        key=lambda p: p.stem, reverse=True)
    memos = [parse_memo(p) for p in memo_files]

    (DOCS / "memo").mkdir(parents=True, exist_ok=True)
    (DOCS / ".nojekyll").write_text("")
    (DOCS / "style.css").write_text(CSS)

    # per-memo pages
    for m in memos:
        body = f'<article class="memo">{m["body_html"]}</article>' \
               f'<a class="backlink" href="../index.html">&larr; All briefs</a>'
        (DOCS / "memo" / f'{m["date"]}.html').write_text(
            page(f'Dataset Hunt — {m["pretty"]}', body, rel="../",
                 description=m["verdict"] or SITE_TAGLINE))

    # index feed
    items = []
    for m in memos:
        score = f'<span class="badge">{html.escape(m["score"])}</span>' if m["score"] else ""
        tf = f'<div class="meta">Top find: {_inline(m["topfind"])}{score}</div>' if m["topfind"] else ""
        items.append(
            f'<li><div class="date">{html.escape(m["pretty"])}</div>'
            f'<div class="frontier">{_inline(m["frontier"])}</div>'
            f'<h2><a href="memo/{m["date"]}.html">{_inline(m["verdict"] or m["date"])}</a></h2>'
            f'{tf}</li>')
    index_body = (f'<p style="color:var(--muted)">{len(memos)} daily briefs · '
                  f'newest first.</p><ul class="feed">{"".join(items)}</ul>')
    (DOCS / "index.html").write_text(page(SITE_TITLE, index_body))

    # ledger page
    ledger_md = (ROOT / "LEDGER.md").read_text(encoding="utf-8")
    (DOCS / "ledger.html").write_text(
        page("Ledger — The Daily Dataset Hunt",
             f'<article class="memo">{md_to_html(ledger_md)}</article>',
             description="Every dataset the hunt has found or rejected."))

    print(f"Built docs/: {len(memos)} memos + index + ledger")


if __name__ == "__main__":
    build()
