# Corporate Header & KPI Strip Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build Section A (header bar with live clock + WTD/MTD/QTD/YTD toggle) and Section B (6-card corporate KPI strip) using Jinja2-rendered dummy data.

**Architecture:** Dummy data lives in `app/mockup/dummy_data.py` as a Python dict. `routes.py` registers a Jinja2 custom filter (`crore`) and passes the dict to `dashboard.html`. The template renders the header and KPI strip; vanilla JS handles the live clock and tab toggle. No MongoDB; no JS frameworks.

**Tech Stack:** Python 3.13, FastAPI, Jinja2Templates, vanilla HTML/CSS/JS

---

## File Map

| Action | File | Responsibility |
|--------|------|---------------|
| CREATE | `app/mockup/dummy_data.py` | Single source of truth for all dummy KPI values |
| MODIFY | `app/mockup/routes.py` | Register `crore` Jinja2 filter; inject `corp_kpis` into template context |
| MODIFY | `app/templates/dashboard.html` | Section A header bar + Section B KPI card grid |
| MODIFY | `app/static/style.css` | Header bar layout, time-filter toggle, KPI card styles, badge colors, delta arrows |
| CREATE | `tasks/TASK-002-corp-header.md` | Task tracking file (already created) |

---

## Task 1: Create dummy_data.py

**Files:**
- Create: `app/mockup/dummy_data.py`

- [ ] **Step 1: Write the file**

```python
# app/mockup/dummy_data.py
"""
Dummy data for Phase 0 mockup (PRODUCTION=1).
FY 2025-26, week ending 2026-04-25.
All monetary values in Crores (Rs.).
"""

CORP_KPIS = [
    {
        "label": "Target for Year",
        "target": 240.0,          # Rs. Cr
        "current": 187.0,         # Rs. Cr
        "pct": 78,                # % achieved
        "delta": 6.2,             # WoW delta (positive = up)
        "unit": "cr",             # "cr" => format as Rs. XX Cr; "count" => plain number
    },
    {
        "label": "Revenue (Booking)",
        "target": 240.0,
        "current": 142.0,
        "pct": 59,
        "delta": 4.1,
        "unit": "cr",
    },
    {
        "label": "Invoiced",
        "target": 180.0,
        "current": 98.0,
        "pct": 54,
        "delta": 3.8,
        "unit": "cr",
    },
    {
        "label": "Payments",
        "target": 160.0,
        "current": 71.0,
        "pct": 44,
        "delta": -1.2,
        "unit": "cr",
    },
    {
        "label": "Meetings",
        "target": 1200,
        "current": 847,
        "pct": 71,
        "delta": 32,
        "unit": "count",
    },
    {
        "label": "Proposals",
        "target": 900,
        "current": 512,
        "pct": 57,
        "delta": 18,
        "unit": "count",
    },
]
```

- [ ] **Step 2: Verify Python syntax**

```bash
python -c "from app.mockup.dummy_data import CORP_KPIS; print(len(CORP_KPIS), 'KPIs loaded')"
```
Expected output: `6 KPIs loaded`

- [ ] **Step 3: Commit**

```bash
git add app/mockup/dummy_data.py tasks/TASK-002-corp-header.md
git commit -m "[TASK-002] feat: add corporate KPI dummy data"
```

---

## Task 2: Update routes.py — register Jinja2 filter + inject data

**Files:**
- Modify: `app/mockup/routes.py`

The current file has no `dummy_data` import and no custom filters. We need to:
1. Import `CORP_KPIS` from `dummy_data`.
2. Register a `crore` Jinja2 filter on `templates.env`.
3. Pass `corp_kpis` in the template context.

- [ ] **Step 1: Write the updated routes.py**

Replace the full contents of `app/mockup/routes.py` with:

```python
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.mockup.dummy_data import CORP_KPIS

templates_path = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_path))


def _fmt_crore(value: float) -> str:
    """Format a float as 'Rs. X.X Cr' (1 decimal place)."""
    return f"Rs. {value:,.1f} Cr"


# Register the custom filter so templates can use {{ value | crore }}
templates.env.filters["crore"] = _fmt_crore

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Render the MD Dashboard mockup."""
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "corp_kpis": CORP_KPIS,
        },
    )
```

- [ ] **Step 2: Verify the server starts without errors**

```bash
uvicorn app.main:app --reload --port 8000
```
Expected: `INFO:     Application startup complete.` with no import errors. Stop with Ctrl+C.

- [ ] **Step 3: Commit**

```bash
git add app/mockup/routes.py
git commit -m "[TASK-002] feat: register crore filter and inject corp_kpis into template"
```

---

## Task 3: Build HTML — Section A header bar

**Files:**
- Modify: `app/templates/dashboard.html`

Replace the entire file contents with the version below (Section A only; Section B added in Task 4).

- [ ] **Step 1: Write Section A into dashboard.html**

```html
{% extends "base.html" %}

{% block title %}MD Dashboard . Fidelitus Corp{% endblock %}

{% block content %}

<!-- ═══════════════════════════════════════════
     SECTION A — Header Bar
     ═══════════════════════════════════════════ -->
<header class="header-bar">
    <!-- Left: branding + live clock -->
    <div class="header-left">
        <span class="header-brand">FIDELITUS CORP . MD DASHBOARD</span>
        <span class="header-clock" id="liveClock"></span>
    </div>

    <!-- Right: time-filter toggle -->
    <nav class="time-filter" role="group" aria-label="Time period filter">
        <button class="tf-btn tf-active" data-period="WTD">WTD</button>
        <button class="tf-btn" data-period="MTD">MTD</button>
        <button class="tf-btn" data-period="QTD">QTD</button>
        <button class="tf-btn" data-period="YTD">YTD</button>
    </nav>
</header>

<!-- ═══════════════════════════════════════════
     SECTION B — Corporate KPI Strip
     (added in Task 4)
     ═══════════════════════════════════════════ -->
<section class="kpi-strip" aria-label="Corporate KPI Summary">
    <!-- placeholder until Task 4 -->
</section>

{% endblock %}

{% block extra_js %}
<script>
/* ── Live Clock ── */
function updateClock() {
    const now = new Date();
    const hh  = String(now.getHours()).padStart(2, '0');
    const mm  = String(now.getMinutes()).padStart(2, '0');
    const day = now.toLocaleDateString('en-IN', {
        day: '2-digit', month: 'short', year: 'numeric'
    });
    document.getElementById('liveClock').textContent = `${hh}:${mm} . ${day}`;
}
updateClock();
setInterval(updateClock, 1000);

/* ── Time-Filter Toggle ── */
document.querySelectorAll('.tf-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.tf-btn').forEach(b => b.classList.remove('tf-active'));
        btn.classList.add('tf-active');
    });
});
</script>
{% endblock %}
```

- [ ] **Step 2: Verify in browser**

Start server: `uvicorn app.main:app --reload --port 8000`
Open `http://localhost:8000/`.
Check:
- Header bar visible: brand text on left, clock ticking on right.
- WTD/MTD/QTD/YTD buttons visible; WTD amber-highlighted.
- Clicking MTD switches highlight.

- [ ] **Step 3: Commit**

```bash
git add app/templates/dashboard.html
git commit -m "[TASK-002] feat: add Section A header bar with live clock and time-filter toggle"
```

---

## Task 4: Build HTML — Section B KPI strip

**Files:**
- Modify: `app/templates/dashboard.html`

Replace the placeholder `<section class="kpi-strip">` block (added in Task 3) with the full Jinja2 loop that renders all 6 KPI cards.

- [ ] **Step 1: Replace the KPI strip section**

The `corp_kpis` list has items with keys: `label`, `target`, `current`, `pct`, `delta`, `unit`.

Color-band logic (`pct` thresholds): `< 25` → red; `26–50` → red-orange; `51–75` → amber; `> 75` → green.

Replace the `<section class="kpi-strip" …>` block with:

```html
<!-- ═══════════════════════════════════════════
     SECTION B — Corporate KPI Strip
     ═══════════════════════════════════════════ -->
<section class="kpi-strip" aria-label="Corporate KPI Summary">
  {% for kpi in corp_kpis %}
    {% if kpi.pct <= 25 %}
      {% set badge_class = "badge-red" %}
    {% elif kpi.pct <= 50 %}
      {% set badge_class = "badge-red-orange" %}
    {% elif kpi.pct <= 75 %}
      {% set badge_class = "badge-amber" %}
    {% else %}
      {% set badge_class = "badge-green" %}
    {% endif %}

    {% if kpi.delta >= 0 %}
      {% set delta_class = "delta-up" %}
      {% set delta_arrow = "▲" %}
    {% else %}
      {% set delta_class = "delta-down" %}
      {% set delta_arrow = "▼" %}
    {% endif %}

    <article class="kpi-card">
      <p class="kpi-label">{{ kpi.label }}</p>

      <p class="kpi-value">
        {% if kpi.unit == "cr" %}
          {{ kpi.current | crore }}
        {% else %}
          {{ kpi.current | int }}
        {% endif %}
      </p>

      <p class="kpi-target">
        of&nbsp;
        {% if kpi.unit == "cr" %}
          {{ kpi.target | crore }}
        {% else %}
          {{ kpi.target | int }}
        {% endif %}
      </p>

      <span class="kpi-badge {{ badge_class }}">{{ kpi.pct }}%</span>

      <p class="kpi-delta {{ delta_class }}">
        {{ delta_arrow }}&nbsp;
        {% if kpi.unit == "cr" %}
          Rs. {{ kpi.delta | abs | round(1) }} Cr WoW
        {% else %}
          {{ kpi.delta | abs | int }} WoW
        {% endif %}
      </p>
    </article>
  {% endfor %}
</section>
```

Note: Jinja2 ships `abs` and `round` as built-in filters — no custom filter needed for the delta.

- [ ] **Step 2: Verify in browser**

Open `http://localhost:8000/`.
Check all 6 cards appear in a row with correct values:
- Target for Year: Rs. 187.0 Cr / Rs. 240.0 Cr / 78% / ▲ Rs. 6.2 Cr WoW (green badge)
- Revenue: Rs. 142.0 Cr / 59% / ▲ Rs. 4.1 Cr WoW (amber badge)
- Invoiced: Rs. 98.0 Cr / 54% / ▲ Rs. 3.8 Cr WoW (amber badge)
- Payments: Rs. 71.0 Cr / 44% / ▼ Rs. 1.2 Cr WoW (red-orange badge, red delta)
- Meetings: 847 / 1200 / 71% / ▲ 32 WoW (amber badge)
- Proposals: 512 / 900 / 57% / ▲ 18 WoW (amber badge)

- [ ] **Step 3: Commit**

```bash
git add app/templates/dashboard.html
git commit -m "[TASK-002] feat: add Section B corporate KPI strip with Jinja2 loop"
```

---

## Task 5: Style — header bar CSS

**Files:**
- Modify: `app/static/style.css`

Append the following blocks to the end of `style.css` (do not replace existing styles).

- [ ] **Step 1: Append header-bar styles**

```css
/* ═══════════════════════════════════════════
   SECTION A — Header Bar
   ═══════════════════════════════════════════ */

.header-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: var(--spacing-md) var(--spacing-xl);
    background-color: var(--color-bg-surface);
    border-bottom: 1px solid var(--color-border);
    margin-bottom: var(--spacing-xl);
    gap: var(--spacing-md);
}

.header-left {
    display: flex;
    align-items: center;
    gap: var(--spacing-lg);
}

.header-brand {
    font-family: var(--font-heading);
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--color-accent);
    letter-spacing: 0.04em;
    white-space: nowrap;
}

.header-clock {
    font-family: var(--font-body);
    font-size: 0.9rem;
    color: var(--color-text-secondary);
    white-space: nowrap;
}

/* ── Time-filter toggle ── */
.time-filter {
    display: flex;
    gap: 0;
    border: 1px solid var(--color-border);
    border-radius: 6px;
    overflow: hidden;
}

.tf-btn {
    background: none;
    border: none;
    border-left: 1px solid var(--color-border);
    color: var(--color-text-secondary);
    font-family: var(--font-body);
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    padding: var(--spacing-xs) var(--spacing-md);
    cursor: pointer;
    transition: background-color 0.15s, color 0.15s;
    white-space: nowrap;
}

.tf-btn:first-child {
    border-left: none;
}

.tf-btn:hover:not(.tf-active) {
    background-color: rgba(232, 168, 56, 0.08);
    color: var(--color-text-primary);
}

.tf-btn.tf-active {
    background-color: var(--color-accent);
    color: #0d1117;
}
```

- [ ] **Step 2: Verify in browser**

Reload `http://localhost:8000/`.
Check:
- Header bar is a single dark surface stripe across the full width.
- Brand text is amber, clock is muted grey next to it.
- WTD has solid amber fill; other buttons have dark background.
- Clicking a button moves the amber fill to it.

- [ ] **Step 3: Commit**

```bash
git add app/static/style.css
git commit -m "[TASK-002] style: add header bar and time-filter toggle CSS"
```

---

## Task 6: Style — KPI card strip CSS

**Files:**
- Modify: `app/static/style.css`

Append the KPI card styles to the end of `style.css`.

- [ ] **Step 1: Append KPI card styles**

```css
/* ═══════════════════════════════════════════
   SECTION B — Corporate KPI Strip
   ═══════════════════════════════════════════ */

.kpi-strip {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: var(--spacing-md);
    padding: 0 var(--spacing-xl) var(--spacing-xl);
}

.kpi-card {
    background-color: var(--color-bg-surface);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    padding: var(--spacing-md) var(--spacing-lg);
    display: flex;
    flex-direction: column;
    gap: var(--spacing-xs);
}

.kpi-label {
    font-family: var(--font-body);
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--color-text-secondary);
    margin: 0;
}

.kpi-value {
    font-family: var(--font-heading);
    font-size: 1.45rem;
    font-weight: 700;
    color: var(--color-text-primary);
    margin: 0;
    line-height: 1.1;
}

.kpi-target {
    font-family: var(--font-body);
    font-size: 0.78rem;
    color: var(--color-text-secondary);
    margin: 0;
}

/* ── Percentage badge ── */
.kpi-badge {
    display: inline-block;
    font-family: var(--font-body);
    font-size: 0.78rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
    align-self: flex-start;
    margin-top: var(--spacing-xs);
}

.badge-red        { background-color: rgba(239, 68,  68,  0.18); color: #ef4444; }
.badge-red-orange { background-color: rgba(249, 115, 22,  0.18); color: #f97316; }
.badge-amber      { background-color: rgba(245, 158, 11,  0.18); color: #f59e0b; }
.badge-green      { background-color: rgba(34,  197, 94,  0.18); color: #22c55e; }

/* ── Delta row ── */
.kpi-delta {
    font-family: var(--font-body);
    font-size: 0.78rem;
    font-weight: 500;
    margin: 0;
    margin-top: auto;
    padding-top: var(--spacing-xs);
}

.delta-up   { color: #22c55e; }
.delta-down { color: #ef4444; }

/* ── Responsive: collapse to 2-col on small screens ── */
@media (max-width: 900px) {
    .kpi-strip {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 480px) {
    .kpi-strip {
        grid-template-columns: 1fr;
    }
    .header-bar {
        flex-direction: column;
        align-items: flex-start;
    }
}
```

- [ ] **Step 2: Verify in browser**

Reload `http://localhost:8000/`.
Check:
- All 6 KPI cards display in a single row on a wide screen.
- Each card: small uppercase label, large bold value, muted target, coloured badge, delta row.
- Badge colours match: Target (green), Revenue (amber), Invoiced (amber), Payments (red-orange), Meetings (amber), Proposals (amber).
- Payments delta is red with ▼ arrow.
- All other deltas are green with ▲ arrow.

- [ ] **Step 3: Commit**

```bash
git add app/static/style.css
git commit -m "[TASK-002] style: add KPI card strip layout and badge/delta styles"
```

---

## Self-Review Checklist

### Spec coverage

| Requirement | Task |
|---|---|
| Header bar: brand left, clock ticking | Task 3, 5 |
| Clock updates every second | Task 3 (JS `setInterval`) |
| WTD/MTD/QTD/YTD toggle, WTD default amber | Task 3, 5 |
| 6 KPI cards in one row | Task 4, 6 |
| Label, current (large bold), target (muted) | Task 4, 6 |
| % badge, 4-band color rule | Task 4, 6 |
| Delta arrow (^ green / v red) + absolute delta | Task 4, 6 |
| Dummy data in dummy_data.py, not hardcoded in HTML | Task 1 |
| Jinja2 renders data into template | Task 2, 4 |
| `crore` filter for monetary formatting | Task 2 |
| No JS frameworks | Tasks 3, 5, 6 |
| PRODUCTION=1 -- no MongoDB calls | Existing main.py; dummy_data.py has no DB import |

### Placeholder scan
No TBDs, TODOs, or "similar to" references present.

### Type consistency
- `kpi.unit == "cr"` branch used identically in Task 4 (value, target, delta).
- `badge_class` variable set in Task 4 and used in `kpi-badge {{ badge_class }}` in same task.
- CSS class names defined in Task 6 (`badge-red`, `badge-red-orange`, `badge-amber`, `badge-green`, `delta-up`, `delta-down`) match exactly what Task 4 emits.
- `crore` filter registered in Task 2 and called in Task 4.

All consistent. No gaps found.
