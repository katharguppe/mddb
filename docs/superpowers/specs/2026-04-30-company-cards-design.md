# Design Spec — TASK-003: Company Cards
**Date:** 2026-04-30
**Session:** s03 (Phase 0 — Mockup)
**Status:** Approved

---

## Overview

Add 6 subsidiary company cards below the corporate KPI strip on the MD Dashboard.
Each card shows the same 6 KPIs as the corporate strip, a color-coded % badge,
a delta indicator, and a "Know More" button that toggles a slide-down details panel.

---

## Files Changed

| File | Action | Notes |
|---|---|---|
| `tasks/TASK-003-company-cards.md` | CREATE | task tracking file |
| `app/mockup/dummy_data.py` | CREATE | corporate + companies data dict |
| `app/mockup/routes.py` | MODIFY | import dummy_data, pass to template |
| `app/templates/dashboard.html` | MODIFY | KPI strip + company cards sections |
| `app/static/style.css` | MODIFY | grid, card, panel, button styles |

> `routes.py` is a necessary 3-line dependency even though it is outside the stated
> module scope. It must pass `DASHBOARD_DATA` to the template for Jinja2 rendering.

---

## Data Structure — `dummy_data.py`

Single dict `DASHBOARD_DATA` with two top-level keys:

```python
DASHBOARD_DATA = {
    "corporate": { ... },   # 6 KPIs — corporate consolidated (s02 data)
    "companies": [
        {
            "id": str,           # slug used for HTML id attr ("transactions")
            "name": str,         # "Fidelitus Transactions"
            "dot_color": str,    # hex color unique per company
            "kpis": {
                "target":    {"value": str},
                "revenue":   {"value": str, "pct": int, "delta": "up"|"down"|None},
                "invoiced":  {"value": str, "pct": int, "delta": None},
                "payments":  {"value": str, "pct": int, "delta": None},
                "meetings":  {"value": str, "pct": int, "delta": "up"|"down"|None},
                "proposals": {"value": str, "pct": int, "delta": "up"|"down"|None},
            }
        },
        ...  # 6 companies
    ]
}
```

### Company Dot Colors

| Company | Dot Color |
|---|---|
| Fidelitus Transactions | `#3b82f6` (blue) |
| Fidelitus Projects | `#10b981` (emerald) |
| Fidelitus FMS | `#a855f7` (purple) |
| Fidelitus HR Labs | `#f43f5e` (rose) |
| Fidelitus Technology | `#22d3ee` (cyan) |
| Fidelitus GCC Nexus | `#e8a838` (amber) |

### Dummy Values (from spec)

| Company | Target | Rev (%) | Inv (%) | Pay (%) | Meet (%) | Prop (%) |
|---|---|---|---|---|---|---|
| Transactions | Rs.80 Cr | Rs.68 Cr 85%^ | Rs.54 Cr 68% | Rs.42 Cr 53% | 320 88%^ | 180 79%^ |
| Projects     | Rs.60 Cr | Rs.29 Cr 48%v | Rs.21 Cr 35% | Rs.14 Cr 23% | 210 61%  | 140 55%  |
| FMS          | Rs.30 Cr | Rs.24 Cr 80%^ | Rs.19 Cr 63% | Rs.16 Cr 53% | 180 72%  | 95 67%   |
| HR Labs      | Rs.25 Cr | Rs.11 Cr 44%v | Rs.8 Cr 32%  | Rs.5 Cr 20%  | 150 48%  | 62 41%   |
| Technology   | Rs.20 Cr | Rs.9 Cr 45%   | Rs.6 Cr 30%  | Rs.4 Cr 20%  | 87 57%   | 35 47%   |
| GCC Nexus    | Rs.25 Cr | Rs.1 Cr 4%v   | Rs.0 0%      | Rs.0 0%      | 24 21%   | 18 24%   |

---

## Template — `dashboard.html`

Two sections inside `<main class="dashboard-main">`:

### Section A — Corporate KPI Strip
- Six `.kpi-card` elements in a single-row flex/grid.
- Data from `data.corporate` passed by routes.py.

### Section B — Company Cards
- Section header: "Subsidiaries" (uppercase label + divider line, matching reference design).
- `.companies-grid` wraps all 6 cards — CSS grid, 3 columns.
- Jinja2 `{% for company in data.companies %}` loop renders each card.

**Per-card structure:**
```
┌──────────────────────────────────────────┐  ← border-top: 3px solid dot_color
│ ●  Company Name               [slug tag] │
├──────────────────────────────────────────┤
│ Target     Rs.80 Cr                      │
│ Revenue    Rs.68 Cr   /Rs.80Cr  [85%] ▲ │
│ Invoiced   Rs.54 Cr   /Rs.80Cr  [68%]   │
│ Payments   Rs.42 Cr   /Rs.80Cr  [53%]   │
│ Meetings   320        /365      [88%] ▲  │
│ Proposals  180        /228      [79%] ▲  │
├──────────────────────────────────────────┤
│                      [Know More →]       │
└──────────────────────────────────────────┘
▼ slide-down panel (hidden, toggled by JS)
  "Aging analysis — Session 04"
```

---

## CSS — `style.css`

New rules added:

```css
/* Companies section */
.companies-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
}

/* Company card */
.company-card {
    background: var(--color-bg-surface);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    overflow: hidden;
    /* border-top color set via inline style="border-top-color: <dot_color>" */
    border-top-width: 3px;
    border-top-style: solid;
}

.company-card-header { ... }   /* name row with dot */
.company-kpi-table { ... }     /* KPI list */
.company-kpi-row { ... }       /* single KPI row — flex */
.pct-badge { ... }             /* colored % pill — reuses kpi-status-* vars */
.delta-up { color: var(--color-green); }
.delta-down { color: var(--color-red); }

/* Know More button */
.btn-know-more {
    background: transparent;
    border: 1px solid var(--color-accent);
    color: var(--color-accent);
    border-radius: 4px;
    padding: 0.25rem 0.75rem;
    cursor: pointer;
    font-family: var(--font-body);
    font-size: 0.8rem;
}
.btn-know-more:hover { background: rgba(232,168,56,0.1); }

/* Slide-down details panel */
.company-details {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
    border-top: 1px solid var(--color-border);
}
.company-details.open { max-height: 120px; }
```

Responsive: at `max-width: 768px`, grid drops to 1 column.

---

## JavaScript (inline in dashboard.html)

```js
function toggleDetails(id) {
    const panel = document.getElementById('details-' + id);
    panel.classList.toggle('open');
}
```

One function, no dependencies. Button calls `onclick="toggleDetails('{{ company.id }}')"`.

---

## % Badge Color Rule

| Range | Class | Color |
|---|---|---|
| ≤ 25% | `kpi-status-red` | `#ef4444` |
| 26–50% | `kpi-status-red-orange` | `#f97316` |
| 51–75% | `kpi-status-amber` | `#f59e0b` |
| > 75% | `kpi-status-green` | `#22c55e` |

Applied via Jinja2 macro or inline conditional in template.

---

## Acceptance Criteria

- [ ] 6 company cards rendered in a 3-per-row grid from `dummy_data.py` (not hardcoded)
- [ ] Each card has a 3px top border in its unique dot color
- [ ] Each card shows all 6 KPIs with value, % badge (correct color band), and delta arrow
- [ ] "Know More" button toggles slide-down panel with JS (no page reload)
- [ ] Details panel shows placeholder text "Aging analysis — Session 04"
- [ ] PRODUCTION=1 serves dummy data; no MongoDB calls
- [ ] Responsive: 1 column on mobile (≤768px)
- [ ] No JS frameworks — vanilla JS only
