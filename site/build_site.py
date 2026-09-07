#!/usr/bin/env python3
"""Static-site generator for the Daily Dataset Hunt.

Reads memos/*.md + LEDGER.md and writes a public site into docs/ (served by
GitHub Pages from main/docs). Stdlib-only — no external dependencies.

Design goals: clean, unadorned, technical-report look; scannable card feed;
a real graph on every memo (the Willis-rubric breakdown), a scores-over-time
chart on the landing page, and inline content charts wherever a memo embeds a
```chart block (a small, honest data series pulled during that day's probe).

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

RUBRIC_LABELS = [
    ("a", "Behaviorally revealed"),
    ("b", "Longitudinal / incidental"),
    ("c", "Unclaimed"),
    ("d", "Panel-able"),
    ("e", "AI × agenda"),
]

# ---------------------------------------------------------------------------
# Number / formatting helpers
# ---------------------------------------------------------------------------

def _fmt_num(v: float) -> str:
    if abs(v - round(v)) < 1e-9:
        return f"{int(round(v)):,}"
    return f"{v:,.1f}"


def _nice_ceiling(v: float) -> float:
    """Smallest 'nice' number (1/2/5 x 10^k) >= v, for a clean top gridline."""
    if v <= 0:
        return 1.0
    import math
    exp = math.floor(math.log10(v))
    base = 10 ** exp
    for mult in (1, 2, 2.5, 5, 10):
        if mult * base >= v - 1e-9:
            return mult * base
    return 10 * base


def _median(xs):
    xs = sorted(xs)
    n = len(xs)
    if not n:
        return 0
    mid = n // 2
    return xs[mid] if n % 2 else (xs[mid - 1] + xs[mid]) / 2


# ---------------------------------------------------------------------------
# SVG charts (single-series, one accent hue -> CVD-safe by construction).
# All colors reference CSS custom properties so charts follow the page theme.
# ---------------------------------------------------------------------------

def svg_rubric(subs: dict, total) -> str:
    """Horizontal bar chart of the five Willis criteria (each 0-5)."""
    W, top, rh = 460, 30, 30
    lx, bx0, bx1 = 178, 178, 410
    rows = len(RUBRIC_LABELS)
    h = top + rows * rh + 6
    p = [f'<svg class="chart chart-rubric" viewBox="0 0 {W} {h}" role="img" '
         f'aria-label="Willis rubric breakdown, {total} out of 25">']
    p.append(f'<text x="0" y="18" class="c-title">Willis rubric &mdash; {total}/25</text>')
    for i, (k, label) in enumerate(RUBRIC_LABELS):
        v = subs.get(k, 0)
        cy = top + i * rh + rh / 2
        p.append(f'<text x="{lx-12}" y="{cy+4:.0f}" class="c-lab" text-anchor="end">{html.escape(label)}</text>')
        p.append(f'<rect x="{bx0}" y="{cy-7:.0f}" width="{bx1-bx0}" height="14" rx="7" class="c-track"/>')
        w = (bx1 - bx0) * v / 5
        p.append(f'<rect x="{bx0}" y="{cy-7:.0f}" width="{w:.1f}" height="14" rx="7" class="c-bar">'
                 f'<title>{html.escape(label)}: {v}/5</title></rect>')
        p.append(f'<text x="{bx1+10}" y="{cy+4:.0f}" class="c-val">{v}</text>')
    p.append('</svg>')
    return "".join(p)


def svg_sparkbars(subs: dict) -> str:
    """Tiny 5-bar glyph of the rubric shape, for feed cards."""
    W, H, bw, gap = 68, 24, 9, 4
    p = [f'<svg class="spark" viewBox="0 0 {W} {H}" role="img" aria-label="rubric shape" focusable="false">']
    for i, (k, _) in enumerate(RUBRIC_LABELS):
        v = subs.get(k, 0)
        x = i * (bw + gap)
        bh = max(2.0, (H - 2) * v / 5)
        p.append(f'<rect x="{x}" y="{H-bh:.1f}" width="{bw}" height="{bh:.1f}" rx="2" class="c-bar"/>')
    p.append('</svg>')
    return "".join(p)


def svg_timeline(chron: list) -> str:
    """Top-find score (0-25) over time. chron is oldest->newest."""
    W, H = 660, 220
    padL, padR, padT, padB = 40, 16, 20, 30
    x0, x1, y0, y1 = padL, W - padR, padT, H - padB
    n = len(chron)

    def X(i):
        return x0 + (x1 - x0) * (i / (n - 1) if n > 1 else 0.5)

    def Y(v):
        return y1 - (y1 - y0) * (v / 25)

    p = [f'<svg class="chart chart-timeline" viewBox="0 0 {W} {H}" role="img" '
         f'aria-label="Top-find Willis score over time, out of 25">']
    p.append(f'<text x="0" y="12" class="c-title">Top-find score over time &mdash; out of 25</text>')
    # gridlines + y ticks
    for val, dashed in ((25, False), (18, True), (0, False)):
        y = Y(val)
        cls = "c-grid-kill" if dashed else "c-grid"
        p.append(f'<line x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}" class="{cls}"/>')
        p.append(f'<text x="{x0-8}" y="{y+4:.1f}" class="c-tick" text-anchor="end">{val}</text>')
    p.append(f'<text x="{x1}" y="{Y(18)-5:.1f}" class="c-note" text-anchor="end">kill line 18</text>')
    # trend line through scored days
    pts = [(X(i), Y(m["total"])) for i, m in enumerate(chron) if m["total"]]
    if len(pts) >= 2:
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        p.append(f'<path d="{d}" class="c-line"/>')
    # marks
    for i, m in enumerate(chron):
        x = X(i)
        if m["total"]:
            title = f'{m["pretty"]} — {m["topfind"]}: {m["total"]}/25'
            p.append(f'<circle cx="{x:.1f}" cy="{Y(m["total"]):.1f}" r="4" class="c-dot">'
                     f'<title>{html.escape(title)}</title></circle>')
        else:
            p.append(f'<circle cx="{x:.1f}" cy="{Y(0):.1f}" r="4" class="c-dot-null">'
                     f'<title>{html.escape(m["pretty"])} — null day</title></circle>')
    # x labels: first, last, and a few between (avoid crowding the last tick)
    step = max(1, round(n / 5))
    idxs = list(range(0, n, step))
    if (n - 1) not in idxs:
        if idxs and (n - 1 - idxs[-1]) < step * 0.5:
            idxs[-1] = n - 1
        else:
            idxs.append(n - 1)
    for i in idxs:
        if 0 <= i < n:
            p.append(f'<text x="{X(i):.1f}" y="{y1+18:.0f}" class="c-tick" '
                     f'text-anchor="middle">{html.escape(chron[i]["short"])}</text>')
    p.append('</svg>')
    return "".join(p)


def svg_line(x_labels, y_vals, unit="") -> str:
    W, H = 660, 254
    padL, padR, padT, padB = 52, 16, 24, 34
    x0, x1, y0, y1 = padL, W - padR, padT, H - padB
    n = len(x_labels)
    top = _nice_ceiling(max(y_vals)) if y_vals else 1

    def X(i):
        return x0 + (x1 - x0) * (i / (n - 1) if n > 1 else 0.5)

    def Y(v):
        return y1 - (y1 - y0) * (v / top)

    p = [f'<svg class="chart chart-line" viewBox="0 0 {W} {H}" role="img" '
         f'aria-label="line chart">']
    for frac in (0, 0.5, 1.0):
        val = top * frac
        y = Y(val)
        p.append(f'<line x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}" class="c-grid"/>')
        p.append(f'<text x="{x0-8}" y="{y+4:.1f}" class="c-tick" text-anchor="end">{_fmt_num(val)}</text>')
    if unit:
        p.append(f'<text x="{x0-8}" y="{y0-10:.1f}" class="c-note" text-anchor="end">{html.escape(unit)}</text>')
    pts = [(X(i), Y(v)) for i, v in enumerate(y_vals)]
    if len(pts) >= 2:
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        p.append(f'<path d="{d}" class="c-line"/>')
    for i, v in enumerate(y_vals):
        lbl = x_labels[i] if i < len(x_labels) else ""
        p.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="3.5" class="c-dot">'
                 f'<title>{html.escape(str(lbl))}: {_fmt_num(v)}{" " + unit if unit else ""}</title></circle>')
    step = max(1, round(n / 8))
    for i in range(n):
        if i % step == 0 or i == n - 1:
            p.append(f'<text x="{X(i):.1f}" y="{y1+18:.0f}" class="c-tick" '
                     f'text-anchor="middle">{html.escape(str(x_labels[i]))}</text>')
    p.append('</svg>')
    return "".join(p)


def svg_barh(labels, vals, unit="", cap=8) -> str:
    pairs = list(zip(labels, vals))[:cap]
    rows = len(pairs)
    W, padT, padB, rh = 660, 12, 12, 30
    lx, bx0, bx1 = 210, 210, 560
    H = padT + rows * rh + padB
    top = _nice_ceiling(max(v for _, v in pairs)) if pairs else 1
    p = [f'<svg class="chart chart-barh" viewBox="0 0 {W} {H}" role="img" aria-label="bar chart">']
    for i, (lab, v) in enumerate(pairs):
        cy = padT + i * rh + rh / 2
        short = lab if len(str(lab)) <= 30 else str(lab)[:29] + "…"
        p.append(f'<text x="{lx-12}" y="{cy+4:.0f}" class="c-lab" text-anchor="end">{html.escape(short)}</text>')
        p.append(f'<rect x="{bx0}" y="{cy-8:.0f}" width="{bx1-bx0}" height="16" rx="4" class="c-track"/>')
        w = (bx1 - bx0) * v / top
        p.append(f'<rect x="{bx0}" y="{cy-8:.0f}" width="{w:.1f}" height="16" rx="4" class="c-bar">'
                 f'<title>{html.escape(str(lab))}: {_fmt_num(v)}{" " + unit if unit else ""}</title></rect>')
        p.append(f'<text x="{bx0+w+8:.1f}" y="{cy+4:.0f}" class="c-val">{_fmt_num(v)}</text>')
    p.append('</svg>')
    return "".join(p)


def render_chart_block(meta: dict) -> str:
    """Turn a parsed ```chart block into a <figure> with an SVG."""
    ctype = meta.get("type", "line").lower()
    title = meta.get("title", "")
    unit = meta.get("unit", "")
    note = meta.get("note", "")
    source = meta.get("source", "")
    xs = [s.strip() for s in re.split(r"[,|]", meta.get("x", "")) if s.strip()]
    raw_y = [s.strip() for s in re.split(r"[,|]", meta.get("y", "")) if s.strip()]
    ys = []
    for s in raw_y:
        try:
            ys.append(float(s.replace(",", "")))
        except ValueError:
            ys.append(0.0)
    if not xs or not ys:
        return ""
    if ctype == "bar":
        svg = svg_barh(xs, ys, unit=unit)
    else:
        svg = svg_line(xs, ys, unit=unit)
    cap_bits = []
    if note:
        cap_bits.append(html.escape(note))
    if source:
        href = source if source.startswith("http") else f"../{source}"
        cap_bits.append(f'<a href="{html.escape(href, quote=True)}" rel="noopener">source</a>')
    cap = f'<figcaption>{" &middot; ".join(cap_bits)}</figcaption>' if cap_bits else ""
    t = f'<div class="fig-title">{html.escape(title)}</div>' if title else ""
    return f'<figure class="chart-fig">{t}{svg}{cap}</figure>'


# ---------------------------------------------------------------------------
# Minimal, bounded Markdown -> HTML for the memo subset we author:
# headings, bold, italic, inline code, links, lists, tables, blockquotes, hr,
# fenced code, and our ```chart data blocks.
# ---------------------------------------------------------------------------

def _inline(text: str) -> str:
    out = html.escape(text, quote=False)
    codes = []

    def _stash_code(m):
        codes.append(m.group(1))
        return f"\x00CODE{len(codes)-1}\x00"

    out = re.sub(r"`([^`]+)`", _stash_code, out)
    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
                 lambda m: f'<a href="{html.escape(m.group(2), quote=True)}" '
                           f'rel="noopener">{m.group(1)}</a>', out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", out)
    for i, c in enumerate(codes):
        out = out.replace(f"\x00CODE{i}\x00", f"<code>{html.escape(c, quote=False)}</code>")
    return out


def md_to_html(md: str) -> str:
    lines = md.split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # fenced block ``` ... ```  (info string may be "chart")
        m = re.match(r"```+\s*(\w*)\s*$", stripped)
        if m:
            info = m.group(1).lower()
            i += 1
            buf = []
            while i < n and not re.match(r"```+\s*$", lines[i].strip()):
                buf.append(lines[i])
                i += 1
            i += 1  # closing fence
            if info == "chart":
                meta = {}
                for b in buf:
                    if ":" in b:
                        k, v = b.split(":", 1)
                        meta[k.strip().lower()] = v.strip()
                out.append(render_chart_block(meta))
            else:
                code = html.escape("\n".join(buf), quote=False)
                out.append(f"<pre><code>{code}</code></pre>")
            continue

        if re.fullmatch(r"-{3,}", stripped):
            out.append("<hr>")
            i += 1
            continue

        m = re.match(r"(#{1,6})\s+(.*)", stripped)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{_inline(m.group(2))}</h{lvl}>")
            i += 1
            continue

        if "|" in line and i + 1 < n and re.match(r"\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$", lines[i+1]) and "|" in lines[i+1]:
            def cells(row):
                row = row.strip()
                if row.startswith("|"):
                    row = row[1:]
                if row.endswith("|"):
                    row = row[:-1]
                return [c.strip() for c in row.split("|")]
            header = cells(line)
            i += 2
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

        if stripped.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append(f"<blockquote>{_inline(' '.join(b.strip() for b in buf))}</blockquote>")
            continue

        if re.match(r"[-*]\s+", stripped):
            items = []
            while i < n and re.match(r"\s*[-*]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[i]).strip())
                i += 1
            out.append("<ul>" + "".join(f"<li>{_inline(it)}</li>" for it in items) + "</ul>")
            continue

        if re.match(r"\d+\.\s+", stripped):
            items = []
            while i < n and re.match(r"\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]).strip())
                i += 1
            out.append("<ol>" + "".join(f"<li>{_inline(it)}</li>" for it in items) + "</ol>")
            continue

        buf = [stripped]
        i += 1
        while i < n and lines[i].strip() and not re.match(r"(#{1,6}\s|[-*]\s|>|\d+\.\s|```)", lines[i].strip()) \
                and not re.fullmatch(r"-{3,}", lines[i].strip()) and "|" not in lines[i]:
            buf.append(lines[i].strip())
            i += 1
        out.append(f"<p>{_inline(' '.join(buf))}</p>")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Memo parsing
# ---------------------------------------------------------------------------

def parse_memo(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    d = path.stem

    # optional YAML-ish front-matter: --- \n title: .. \n summary: .. \n ---
    fm, text = {}, raw
    if raw.startswith("---\n"):
        end = raw.find("\n---", 4)
        if end != -1:
            for line in raw[4:end].split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip().lower()] = v.strip()
            text = raw[end + 4:].lstrip("\n")

    def find(pat, default=""):
        m = re.search(pat, text, re.M)
        return m.group(1).strip() if m else default

    frontier = find(r"^\*\*Frontier:\*\*\s*(.+)$")
    verdict = find(r"^\*\*Verdict:\*\*\s*(.+)$")
    topfind = find(r"^##\s*Top find:\s*(.+)$") or find(r"^##\s*Top finds?:?\s*(.+)$")
    score = find(r"\*\*Score:\s*([0-9]+/25)\*\*")

    subs, total = {}, None
    ms = re.search(r"\*\*Score:\s*(\d+)/25\*\*\s*\(a(\d)\s*b(\d)\s*c(\d)\s*d(\d)\s*e(\d)\)", text)
    if ms:
        total = int(ms.group(1))
        subs = {k: int(ms.group(j)) for j, k in enumerate(("a", "b", "c", "d", "e"), start=2)}

    fnum = None
    mf = re.match(r"\s*(\d+)\.", frontier)
    if mf:
        fnum = int(mf.group(1))

    null_day = bool(re.search(r"null day", verdict, re.I)) or total is None

    try:
        dt = datetime.strptime(d, "%Y-%m-%d")
        pretty = dt.strftime("%B %-d, %Y")
        short = dt.strftime("%b %-d")
    except ValueError:
        pretty = short = d

    # body for the memo page: drop the H1 + Frontier + Verdict (shown in header)
    body_lines = []
    for ln in text.split("\n"):
        s = ln.strip()
        if s.startswith("# Dataset Hunt") or s.startswith("**Frontier:**") or s.startswith("**Verdict:**"):
            continue
        body_lines.append(ln)
    body_md = "\n".join(body_lines).lstrip("\n")

    title = fm.get("title") or topfind or d
    summary = fm.get("summary") or verdict

    return {"date": d, "pretty": pretty, "short": short, "frontier": frontier,
            "fnum": fnum, "verdict": verdict, "topfind": topfind, "score": score,
            "title": title, "summary": summary,
            "subs": subs, "total": total, "null_day": null_day,
            "body_html": md_to_html(body_md)}


# ---------------------------------------------------------------------------
# CSS + page shell
# ---------------------------------------------------------------------------

CSS = """
:root{color-scheme:light;
 --bg:#f5f6f8;--surface:#ffffff;--fg:#15171c;--muted:#5c626d;--line:#e3e6eb;
 --accent:#2a6fd6;--accent-weak:#e7eefb;--accent-ink:#fff;--code:#eef1f5}
@media (prefers-color-scheme:dark){:root{color-scheme:dark;
 --bg:#0c0d10;--surface:#15171b;--fg:#eceef2;--muted:#969ba6;--line:#252932;
 --accent:#5192f0;--accent-weak:#16223a;--accent-ink:#0c0d10;--code:#1b1e24}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
 font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
 -webkit-text-size-adjust:100%}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:1000px;margin:0 auto;padding:0 22px}
.wrap.narrow{max-width:760px}

header.site{padding:30px 0 20px;border-bottom:1px solid var(--line);margin-bottom:26px}
header.site h1{margin:0;font-size:23px;letter-spacing:-.02em;font-weight:680}
header.site h1 a{color:var(--fg)}
header.site .tag{color:var(--muted);margin:.45em 0 0;font-size:14.5px;max-width:70ch}
nav.top{margin-top:16px;font-size:14px;display:flex;gap:20px}
nav.top a{color:var(--muted);font-weight:550}
nav.top a:hover{color:var(--accent);text-decoration:none}

h2{font-size:20px;letter-spacing:-.01em;margin:1.7em 0 .5em;font-weight:640}
h3{font-size:16.5px;margin:1.5em 0 .4em;font-weight:620}
hr{border:0;border-top:1px solid var(--line);margin:2em 0}
p{margin:.7em 0}
blockquote{margin:1.1em 0;padding:.7em 1.1em;border-left:3px solid var(--accent);
 background:var(--accent-weak);border-radius:0 8px 8px 0}
blockquote p{margin:.2em 0}
code{background:var(--code);padding:.12em .38em;border-radius:4px;font-size:.87em;
 font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
pre{background:var(--code);padding:14px 16px;border-radius:8px;overflow-x:auto;font-size:13px}
pre code{background:none;padding:0}
.table-wrap{overflow-x:auto;margin:1.2em 0}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{border-bottom:1px solid var(--line);padding:8px 11px;text-align:left;vertical-align:top}
th{font-weight:620;color:var(--muted);font-size:12.5px;text-transform:uppercase;letter-spacing:.03em}
ul,ol{padding-left:1.25em}
li{margin:.3em 0}

/* stat tiles */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px;margin:0 0 24px}
.stat{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:15px 17px}
.stat .n{font-size:27px;font-weight:680;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.stat .k{color:var(--muted);font-size:12.5px;margin-top:2px;text-transform:uppercase;letter-spacing:.03em}

/* overview chart panel */
.panel{background:var(--surface);border:1px solid var(--line);border-radius:12px;
 padding:16px 18px;margin:0 0 26px}
.section-label{font-size:12.5px;text-transform:uppercase;letter-spacing:.05em;
 color:var(--muted);margin:0 0 12px;font-weight:600}

/* feed cards */
.feed{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;
 list-style:none;padding:0;margin:0}
.card{background:var(--surface);border:1px solid var(--line);border-radius:12px;
 padding:16px 17px;display:flex;flex-direction:column;transition:border-color .15s}
.card:hover{border-color:var(--accent)}
.card a.block{color:inherit}
.card .row{display:flex;align-items:center;gap:10px;margin-bottom:9px}
.chip{font-size:11.5px;font-weight:600;color:var(--accent);background:var(--accent-weak);
 border-radius:20px;padding:2px 9px;white-space:nowrap}
.card .date{font-size:12px;color:var(--muted);margin-left:auto;font-variant-numeric:tabular-nums}
.card h2{font-size:16px;margin:0 0 6px;line-height:1.35;font-weight:620}
.card h2 a{color:var(--fg)}
.card h2 a:hover{color:var(--accent);text-decoration:none}
.card .say{color:var(--muted);font-size:13.5px;line-height:1.5;margin:0 0 12px;flex:1}
.card .foot{display:flex;align-items:center;gap:10px;margin-top:auto;
 padding-top:11px;border-top:1px solid var(--line)}
.card .foot .badge{margin-left:auto}
.badge{display:inline-block;background:var(--accent);color:var(--accent-ink);
 border-radius:20px;padding:2px 10px;font-size:12px;font-weight:640;font-variant-numeric:tabular-nums}
.badge.null{background:var(--muted)}

/* memo page */
.memo-head .title{font-size:28px;line-height:1.18;letter-spacing:-.02em;font-weight:700;margin:0 0 12px}
.memo-head .desc{font-size:17.5px;line-height:1.5;color:var(--fg);margin:0 0 10px;max-width:64ch}
.memo-head .meta{font-size:12.5px;color:var(--muted);margin:0 0 20px;font-variant-numeric:tabular-nums}
.lead-band{display:grid;grid-template-columns:1.4fr .9fr;gap:18px;
 background:var(--surface);border:1px solid var(--line);border-radius:12px;
 padding:18px 20px;margin:0 0 8px;align-items:center}
.lead-band .score{text-align:center;border-left:1px solid var(--line);padding-left:18px}
.lead-band .score .n{font-size:40px;font-weight:700;letter-spacing:-.02em;line-height:1;font-variant-numeric:tabular-nums}
.lead-band .score .n small{font-size:19px;color:var(--muted);font-weight:600}
.lead-band .score .k{color:var(--muted);font-size:12px;margin-top:5px;text-transform:uppercase;letter-spacing:.04em}
.null-band{background:var(--surface);border:1px solid var(--line);border-radius:12px;
 padding:16px 20px;margin:0 0 8px;color:var(--muted)}
.memo article{margin-top:22px}
.memo article :first-child{margin-top:0}

/* charts */
.chart{display:block;width:100%;height:auto;margin:2px auto}
svg text{font-family:inherit}
svg .c-title{fill:var(--fg);font-size:13px;font-weight:640}
svg .c-lab{fill:var(--muted);font-size:12px}
svg .c-val{fill:var(--fg);font-size:12px;font-weight:640;font-variant-numeric:tabular-nums}
svg .c-tick{fill:var(--muted);font-size:11px;font-variant-numeric:tabular-nums}
svg .c-note{fill:var(--muted);font-size:10.5px}
svg .c-track{fill:var(--accent-weak)}
svg .c-bar{fill:var(--accent)}
svg .c-grid{stroke:var(--line);stroke-width:1}
svg .c-grid-kill{stroke:var(--muted);stroke-width:1;stroke-dasharray:3 3;opacity:.6}
svg .c-line{fill:none;stroke:var(--accent);stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
svg .c-dot{fill:var(--accent);stroke:var(--surface);stroke-width:1.5}
svg .c-dot-null{fill:var(--surface);stroke:var(--muted);stroke-width:1.5}
.spark{width:68px;height:24px}
.chart-fig{margin:1.6em 0;background:var(--surface);border:1px solid var(--line);
 border-radius:12px;padding:16px 18px 10px}
.chart-fig .fig-title{font-size:14px;font-weight:620;margin-bottom:6px;color:var(--fg)}
.chart-fig figcaption{color:var(--muted);font-size:12px;margin-top:4px}

.backlink{display:inline-block;margin:26px 0 4px;font-size:14px;font-weight:550}
footer.site{border-top:1px solid var(--line);margin:44px 0 60px;padding-top:18px;
 color:var(--muted);font-size:13px}

@media (max-width:560px){
 .lead-band{grid-template-columns:1fr}
 .lead-band .score{border-left:0;border-top:1px solid var(--line);padding-left:0;padding-top:14px}
}
"""


def page(title, body, rel="", description=None, wide=True):
    desc = html.escape(description or SITE_TAGLINE, quote=True)
    nav = (f'<nav class="top"><a href="{rel}index.html">Home</a>'
           f'<a href="{rel}ledger.html">Ledger</a>'
           f'<a href="{REPO_URL}" rel="noopener">GitHub</a></nav>')
    wrapcls = "wrap" if wide else "wrap narrow"
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{desc}">
<link rel="stylesheet" href="{rel}style.css">
</head><body><div class="{wrapcls}">
<header class="site"><h1><a href="{rel}index.html">{html.escape(SITE_TITLE)}</a></h1>
<p class="tag">{html.escape(SITE_TAGLINE)}</p>{nav}</header>
{body}
<footer class="site">Autonomous daily research &middot; memos and ledger are versioned in
<a href="{REPO_URL}" rel="noopener">git</a>. Built {date.today().isoformat()}.</footer>
</div></body></html>"""


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build():
    memo_files = sorted((p for p in MEMOS.glob("*.md") if p.stem[0].isdigit()),
                        key=lambda p: p.stem, reverse=True)
    memos = [parse_memo(p) for p in memo_files]

    (DOCS / "memo").mkdir(parents=True, exist_ok=True)
    (DOCS / ".nojekyll").write_text("")
    (DOCS / "style.css").write_text(CSS)

    # ---- per-memo pages ----
    for m in memos:
        head = (f'<div class="memo-head"><h1 class="title">{_inline(m["title"])}</h1>'
                f'<p class="desc">{_inline(m["summary"])}</p>'
                f'<div class="meta">{html.escape(m["pretty"])}</div></div>')

        if m["subs"]:
            band = (f'<div class="lead-band"><div class="rubric">{svg_rubric(m["subs"], m["total"])}</div>'
                    f'<div class="score"><div class="n">{m["total"]}<small>/25</small></div>'
                    f'<div class="k">Willis score</div></div></div>')
        else:
            band = '<div class="null-band">Null day &mdash; nothing cleared the bar. The screened candidates are recorded below and in the ledger.</div>'

        body = (f'{head}{band}'
                f'<div class="memo"><article>{m["body_html"]}</article></div>'
                f'<a class="backlink" href="../index.html">&larr; All datasets</a>')
        (DOCS / "memo" / f'{m["date"]}.html').write_text(
            page(f'{m["title"]}', body, rel="../",
                 description=m["summary"] or SITE_TAGLINE, wide=False))

    # ---- landing page ----
    cards = []
    for m in memos:
        spark = svg_sparkbars(m["subs"]) if m["subs"] else ""
        if m["null_day"] and not m["total"]:
            badge = '<span class="badge null">null</span>'
        else:
            badge = f'<span class="badge">{html.escape(m["score"])}</span>' if m["score"] else ""
        cards.append(
            f'<li class="card">'
            f'<div class="row"><span class="date">{html.escape(m["short"])}</span></div>'
            f'<h2><a href="memo/{m["date"]}.html">{_inline(m["title"])}</a></h2>'
            f'<p class="say">{_inline(m["summary"])}</p>'
            f'<div class="foot">{spark}{badge}</div></li>')

    index_body = f'<ul class="feed">{"".join(cards)}</ul>'
    (DOCS / "index.html").write_text(page(SITE_TITLE, index_body, wide=True))

    # ---- ledger page ----
    ledger_md = (ROOT / "LEDGER.md").read_text(encoding="utf-8")
    (DOCS / "ledger.html").write_text(
        page("Ledger — The Daily Dataset Hunt",
             f'<div class="memo"><article>{md_to_html(ledger_md)}</article></div>',
             description="Every dataset the hunt has found or rejected.", wide=False))

    print(f"Built docs/: {len(memos)} memos + index + ledger")


if __name__ == "__main__":
    build()
