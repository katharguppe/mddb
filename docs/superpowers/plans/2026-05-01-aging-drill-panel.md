# Aging Drill-Down Panel Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the placeholder "Know More" panel on each company card with a live aging drill-down showing 5 bucket pills (7d / 14d / 21d / 90d / NPA), each expandable to a table of committed-but-not-delivered payment items; corporate KPI strip cards are also clickable to show an aggregated corporate aging panel.

**Architecture:** All aging data lives in `dummy_data.py` under an `AGING_DATA` dict keyed by company slug (+ `"corporate"` for the aggregate). A Jinja2 macro in `partials/aging_panel.html` renders the pills + hidden table wrappers for one company. `dashboard.html` imports the macro and embeds it inside the existing `company-details` slide-down div; a separate corporate panel sits below the KPI strip. Vanilla JS in `script.js` handles pill toggle (highlight + show/hide table) and corporate panel open/close. No page reloads.

**Tech Stack:** Python 3.13, FastAPI, Jinja2, vanilla HTML/CSS/JS

---

## File Map

| Action | Path | Responsibility |
|--------|------|----------------|
| CREATE | `tasks/TASK-004-aging-drill.md` | Task tracking file |
| MODIFY | `app/mockup/dummy_data.py` | Add `AGING_DATA` dict for 6 companies + corporate |
| CREATE | `app/templates/partials/aging_panel.html` | Jinja2 macro: pills + table wrappers |
| MODIFY | `app/templates/dashboard.html` | Import macro; embed in company cards; add corporate panel |
| MODIFY | `app/static/style.css` | Aging pill + table styles; fix `max-height` for deep panels |
| MODIFY | `app/static/script.js` | Pill-toggle logic; corporate panel toggle |

---

## Task 1: Create the TASK file

**Files:**
- Create: `tasks/TASK-004-aging-drill.md`

- [ ] **Step 1: Write the task file**

```markdown
# TASK-004 -- Aging Drill-Down Panel

**Status:** In Progress
**Session:** s04 (Phase 0 -- Mockup)
**Scope:** app/mockup/dummy_data.py, app/templates/dashboard.html,
           app/templates/partials/aging_panel.html (create),
           app/static/style.css, app/static/script.js ONLY.

## Goal
Replace the placeholder "Know More" panel on each company card with a live
aging drill-down: 5 bucket pills (7d / 14d / 21d / 90d / NPA), each expanding
a table of committed-but-not-delivered payment items. Corporate KPI strip cards
are also clickable to show an aggregated corporate aging panel.

## Acceptance Criteria
- [ ] Aging data in dummy_data.py for all 6 companies + corporate aggregate
- [ ] 5 aging bucket pills rendered per company card in the Know More panel
- [ ] Each pill shows: bucket label + item count + total value (Rs.)
- [ ] Clicking a pill shows/hides that bucket's detail table (no page reload)
- [ ] Clicking the same pill again collapses the table
- [ ] Clicking a different pill collapses current + expands new one
- [ ] Table columns: Company/Team | Team Member | Value (Rs.) | Days Overdue | Reason
- [ ] Corporate KPI cards clickable → shows corporate aging panel below the strip
- [ ] Corporate panel aggregates all 6 companies, same 5-bucket structure
- [ ] Pill color: amber accent (#e8a838) when active; muted when inactive
- [ ] Panel slide-down max-height is sufficient for table content (JS-driven)
- [ ] Vanilla JS only, no frameworks

## Files Changed
- MODIFY  app/mockup/dummy_data.py
- CREATE  app/templates/partials/aging_panel.html
- MODIFY  app/templates/dashboard.html
- MODIFY  app/static/style.css
- MODIFY  app/static/script.js
```

- [ ] **Step 2: Commit**

```bash
git add tasks/TASK-004-aging-drill.md
git commit -m "[TASK-004] chore: add task file for aging drill-down panel"
```

---

## Task 2: Add aging data to `dummy_data.py`

**Files:**
- Modify: `app/mockup/dummy_data.py`

This task appends `AGING_DATA` at the bottom of the file. The route in `routes.py` will be updated in Task 4 to pass it to the template.

- [ ] **Step 1: Append `AGING_DATA` to `app/mockup/dummy_data.py`**

Add this block at the end of the file (after `DASHBOARD_DATA`):

```python
# Aging data: committed but not delivered, grouped by overdue bucket.
# Indexed by company slug. "corporate" is the cross-company aggregate.
AGING_DATA = {
    "transactions": {
        "7d":  {
            "count": 3, "total": "Rs.2.1 Cr",
            "items": [
                {"company": "Fidelitus Trans", "member": "Rajesh Kumar",  "value": "Rs.80L",   "days": 6,   "reason": "Client travel delay, confirming by Mon"},
                {"company": "Fidelitus Trans", "member": "Priya Menon",   "value": "Rs.75L",   "days": 7,   "reason": "Cheque in transit"},
                {"company": "Fidelitus Trans", "member": "Anand Rao",     "value": "Rs.55L",   "days": 5,   "reason": "Bank processing delay"},
            ],
        },
        "14d": {
            "count": 2, "total": "Rs.1.4 Cr",
            "items": [
                {"company": "Fidelitus Trans", "member": "Suresh Nair",   "value": "Rs.90L",   "days": 13,  "reason": "NEFT rejected, re-initiated"},
                {"company": "Fidelitus Trans", "member": "Kavitha Reddy", "value": "Rs.50L",   "days": 11,  "reason": "Awaiting MD approval from client"},
            ],
        },
        "21d": {
            "count": 1, "total": "Rs.0.6 Cr",
            "items": [
                {"company": "Fidelitus Trans", "member": "Vikram Singh",  "value": "Rs.60L",   "days": 19,  "reason": "Legal vetting on agreement"},
            ],
        },
        "90d": {
            "count": 1, "total": "Rs.1.2 Cr",
            "items": [
                {"company": "Fidelitus Trans", "member": "Mohan Das",     "value": "Rs.1.2 Cr","days": 67,  "reason": "Client undergoing internal restructuring"},
            ],
        },
        "npa":  {
            "count": 1, "total": "Rs.0.9 Cr",
            "items": [
                {"company": "Fidelitus Trans", "member": "Renu Sharma",   "value": "Rs.90L",   "days": 112, "reason": "Dispute raised, legal notice sent"},
            ],
        },
    },
    "projects": {
        "7d":  {
            "count": 2, "total": "Rs.1.5 Cr",
            "items": [
                {"company": "Fidelitus Projects", "member": "Arjun Shetty",  "value": "Rs.85L",   "days": 5,  "reason": "Client site inspection pending"},
                {"company": "Fidelitus Projects", "member": "Deepa Thomas",  "value": "Rs.65L",   "days": 7,  "reason": "Contractor invoice mismatch"},
            ],
        },
        "14d": {
            "count": 2, "total": "Rs.1.1 Cr",
            "items": [
                {"company": "Fidelitus Projects", "member": "Kiran Joshi",   "value": "Rs.70L",   "days": 12, "reason": "Completion certificate delayed"},
                {"company": "Fidelitus Projects", "member": "Meera Pillai",  "value": "Rs.40L",   "days": 10, "reason": "Client on international travel"},
            ],
        },
        "21d": {
            "count": 1, "total": "Rs.0.8 Cr",
            "items": [
                {"company": "Fidelitus Projects", "member": "Rahul Verma",   "value": "Rs.80L",   "days": 18, "reason": "Scope change documentation pending"},
            ],
        },
        "90d": {
            "count": 1, "total": "Rs.0.5 Cr",
            "items": [
                {"company": "Fidelitus Projects", "member": "Sunita Bose",   "value": "Rs.50L",   "days": 55, "reason": "Dispute over punch-list items"},
            ],
        },
        "npa":  {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
    },
    "fms": {
        "7d":  {
            "count": 2, "total": "Rs.0.9 Cr",
            "items": [
                {"company": "Fidelitus FMS", "member": "Anil Kapoor",    "value": "Rs.55L",   "days": 6,  "reason": "Facility audit report awaited"},
                {"company": "Fidelitus FMS", "member": "Sneha Iyer",     "value": "Rs.35L",   "days": 4,  "reason": "Monthly invoice approval pending"},
            ],
        },
        "14d": {
            "count": 1, "total": "Rs.0.6 Cr",
            "items": [
                {"company": "Fidelitus FMS", "member": "Ramesh Gupta",   "value": "Rs.60L",   "days": 11, "reason": "Security deposit adjustment"},
            ],
        },
        "21d": {
            "count": 1, "total": "Rs.0.4 Cr",
            "items": [
                {"company": "Fidelitus FMS", "member": "Lata Srinivas",  "value": "Rs.40L",   "days": 20, "reason": "AMC renewal dispute"},
            ],
        },
        "90d": {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
        "npa":  {
            "count": 1, "total": "Rs.0.3 Cr",
            "items": [
                {"company": "Fidelitus FMS", "member": "Gopal Nair",     "value": "Rs.30L",   "days": 98, "reason": "Client entity dissolved, legal action initiated"},
            ],
        },
    },
    "hrlabs": {
        "7d":  {
            "count": 1, "total": "Rs.0.4 Cr",
            "items": [
                {"company": "Fidelitus HR Labs", "member": "Preethi Nair",   "value": "Rs.40L",   "days": 5,  "reason": "Hiring milestone not yet confirmed"},
            ],
        },
        "14d": {
            "count": 2, "total": "Rs.0.7 Cr",
            "items": [
                {"company": "Fidelitus HR Labs", "member": "Santosh Kumar",  "value": "Rs.45L",   "days": 14, "reason": "Background check delay by client"},
                {"company": "Fidelitus HR Labs", "member": "Divya Menon",    "value": "Rs.25L",   "days": 10, "reason": "PO amendment in process"},
            ],
        },
        "21d": {
            "count": 1, "total": "Rs.0.3 Cr",
            "items": [
                {"company": "Fidelitus HR Labs", "member": "Naresh Patel",   "value": "Rs.30L",   "days": 21, "reason": "Joining date pushed, payment tied to onboarding"},
            ],
        },
        "90d": {
            "count": 1, "total": "Rs.0.5 Cr",
            "items": [
                {"company": "Fidelitus HR Labs", "member": "Shobha Rao",     "value": "Rs.50L",   "days": 72, "reason": "Candidate resigned, replacement clause invoked"},
            ],
        },
        "npa":  {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
    },
    "technology": {
        "7d":  {
            "count": 1, "total": "Rs.0.3 Cr",
            "items": [
                {"company": "Fidelitus Technology", "member": "Vikash Mehta",   "value": "Rs.30L",   "days": 7,  "reason": "UAT sign-off pending from client"},
            ],
        },
        "14d": {
            "count": 1, "total": "Rs.0.2 Cr",
            "items": [
                {"company": "Fidelitus Technology", "member": "Rohini Das",     "value": "Rs.20L",   "days": 13, "reason": "Go-live delayed by client infra team"},
            ],
        },
        "21d": {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
        "90d": {
            "count": 1, "total": "Rs.0.4 Cr",
            "items": [
                {"company": "Fidelitus Technology", "member": "Sudhir Bhat",    "value": "Rs.40L",   "days": 60, "reason": "Change request scope dispute"},
            ],
        },
        "npa":  {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
    },
    "gcc": {
        "7d":  {
            "count": 1, "total": "Rs.0.5 Cr",
            "items": [
                {"company": "Fidelitus GCC Nexus", "member": "Aditya Sharma",  "value": "Rs.50L",   "days": 6,  "reason": "LOI issued, payment terms being finalised"},
            ],
        },
        "14d": {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
        "21d": {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
        "90d": {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
        "npa":  {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
    },
}

# Corporate aggregate: flatten all company items per bucket
def _build_corporate_aging():
    buckets = ["7d", "14d", "21d", "90d", "npa"]
    result = {}
    for bucket in buckets:
        items = []
        for slug_data in AGING_DATA.values():
            items.extend(slug_data[bucket]["items"])
        count = sum(len(slug_data[bucket]["items"]) for slug_data in AGING_DATA.values())
        result[bucket] = {"count": count, "items": items, "total": f"Rs. {count} items (see below)"}
    return result

AGING_DATA["corporate"] = _build_corporate_aging()
```

- [ ] **Step 2: Verify the file parses without error**

```bash
cd D:/Fidelitus/mddb && python -c "from app.mockup.dummy_data import AGING_DATA; print('corporate 7d count:', AGING_DATA['corporate']['7d']['count'])"
```

Expected output: `corporate 7d count: 10`

- [ ] **Step 3: Commit**

```bash
git add app/mockup/dummy_data.py
git commit -m "[TASK-004] feat: add aging dummy data for all 6 companies + corporate aggregate"
```

---

## Task 3: Create `partials/aging_panel.html` (Jinja2 macro)

**Files:**
- Create: `app/templates/partials/aging_panel.html`

The macro renders the 5-pill row + 5 hidden table wrappers for one company. It is imported and called inside `dashboard.html`. The `company_id` string is used as the DOM key for JS targeting.

- [ ] **Step 1: Create the partials directory and file**

```bash
mkdir -p D:/Fidelitus/mddb/app/templates/partials
```

- [ ] **Step 2: Write `app/templates/partials/aging_panel.html`**

```jinja2
{# app/templates/partials/aging_panel.html
   Macro: aging_panel(company_id, aging)
   aging = AGING_DATA[company_id]  -- dict with keys 7d / 14d / 21d / 90d / npa
#}

{% macro aging_panel(company_id, aging) %}
<div class="aging-panel">

    {# ── Target row (shown here in Know More) ── #}
    {% if target_value is defined %}
    <div class="aging-target-row">Annual Target: {{ target_value }}</div>
    {% endif %}

    {# ── Bucket pills row ── #}
    <div class="aging-pills" id="aging-pills-{{ company_id }}">
        {% set buckets = [
            ("7d",  "7 Days"),
            ("14d", "14 Days"),
            ("21d", "21 Days"),
            ("90d", "90 Days"),
            ("npa", "NPA"),
        ] %}
        {% for key, label in buckets %}
        {% set bucket = aging[key] %}
        <button
            class="aging-pill {% if bucket.count == 0 %}aging-pill--empty{% endif %}"
            data-company="{{ company_id }}"
            data-bucket="{{ key }}"
            onclick="toggleAgingBucket('{{ company_id }}', '{{ key }}')"
            {% if bucket.count == 0 %}disabled{% endif %}
        >
            <span class="aging-pill-label">{{ label }}</span>
            <span class="aging-pill-count">{{ bucket.count }}</span>
            <span class="aging-pill-total">{{ bucket.total }}</span>
        </button>
        {% endfor %}
    </div>

    {# ── Per-bucket detail tables (hidden until pill clicked) ── #}
    {% for key, label in [("7d","7 Days"),("14d","14 Days"),("21d","21 Days"),("90d","90 Days"),("npa","NPA")] %}
    {% set bucket = aging[key] %}
    {% if bucket.count > 0 %}
    <div class="aging-table-wrapper" id="aging-table-{{ company_id }}-{{ key }}">
        <table class="aging-table">
            <thead>
                <tr>
                    <th>Company / Team</th>
                    <th>Team Member</th>
                    <th>Value (Rs.)</th>
                    <th>Days Overdue</th>
                    <th>Reason Entered</th>
                </tr>
            </thead>
            <tbody>
                {% for item in bucket.items %}
                <tr>
                    <td>{{ item.company }}</td>
                    <td>{{ item.member }}</td>
                    <td class="aging-value">{{ item.value }}</td>
                    <td class="aging-days">{{ item.days }}d</td>
                    <td class="aging-reason">{{ item.reason }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    {% endif %}
    {% endfor %}

</div>
{% endmacro %}
```

- [ ] **Step 3: Verify Jinja2 can parse the file (import test)**

No standalone test needed — will be validated when the server renders in Task 5.

- [ ] **Step 4: Commit**

```bash
git add app/templates/partials/aging_panel.html
git commit -m "[TASK-004] feat: add aging_panel Jinja2 macro partial"
```

---

## Task 4: Update `routes.py` to pass aging data

**Files:**
- Modify: `app/mockup/routes.py`

- [ ] **Step 1: Update the import and pass `aging` to the template context**

Current `routes.py` (full file after edit):

```python
# app/mockup/routes.py
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.mockup.dummy_data import DASHBOARD_DATA, AGING_DATA

templates_path = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_path))

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Render the MD Dashboard mockup."""
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "data": DASHBOARD_DATA, "aging": AGING_DATA},
    )
```

- [ ] **Step 2: Commit**

```bash
git add app/mockup/routes.py
git commit -m "[TASK-004] feat: pass AGING_DATA to dashboard template context"
```

---

## Task 5: Update `dashboard.html`

**Files:**
- Modify: `app/templates/dashboard.html`

Three changes:
1. Import the aging_panel macro at the top of the file.
2. Replace the `details-placeholder` paragraph inside `.company-details` with the macro call + target row.
3. Add a corporate aging panel (hidden) below the KPI strip, plus `onclick` on each KPI card.

- [ ] **Step 1: Write the full updated `dashboard.html`**

```jinja2
{% extends "base.html" %}
{% from "partials/aging_panel.html" import aging_panel %}

{% block title %}MD Dashboard . Fidelitus Corp{% endblock %}

{% block content %}
{# Macro: map percentage to CSS color-band class #}
{% macro pct_class(pct) -%}
  {%- if pct is none -%}
  {%- elif pct <= 25 -%}kpi-status-red
  {%- elif pct <= 50 -%}kpi-status-red-orange
  {%- elif pct <= 75 -%}kpi-status-amber
  {%- else -%}kpi-status-green
  {%- endif -%}
{%- endmacro %}

<header class="dashboard-header">
    <div>
        <p class="dashboard-eyebrow">Fidelitus Corp . MD Dashboard</p>
        <h1 class="dashboard-title">Consolidated View</h1>
    </div>
    <span class="phase-badge">Phase 0 Mockup</span>
</header>

<main class="dashboard-main">

    {# ── Section A: Corporate KPI Strip ── #}
    <section class="section">
        <div class="section-label">Corporate KPIs</div>
        <div class="kpi-strip">
            {% for kpi in data.corporate.kpis %}
            <div class="kpi-card kpi-card--clickable"
                 onclick="toggleCorporateAging()"
                 title="Click to view aging drill-down">
                <div class="kpi-label">{{ kpi.label }}</div>
                <div class="kpi-value">{{ kpi.value }}</div>
                {% if kpi.target %}
                <div class="kpi-target">of {{ kpi.target }}</div>
                {% endif %}
                {% if kpi.pct is not none %}
                <div class="kpi-footer">
                    <span class="pct-badge {{ pct_class(kpi.pct) }}">{{ kpi.pct }}%</span>
                    {% if kpi.delta == "up" %}<span class="delta-up">▲</span>
                    {% elif kpi.delta == "down" %}<span class="delta-down">▼</span>
                    {% endif %}
                </div>
                {% endif %}
            </div>
            {% endfor %}
        </div>

        {# ── Corporate aging panel (hidden until a KPI card is clicked) ── #}
        <div class="company-details corporate-aging-panel" id="details-corporate">
            {{ aging_panel("corporate", aging["corporate"]) }}
        </div>
    </section>

    {# ── Section B: Company Cards ── #}
    <section class="section">
        <div class="section-label">Subsidiaries</div>
        <div class="companies-grid">
            {% for company in data.companies %}
            <div class="company-card" style="border-top-color: {{ company.dot_color }}">

                {# Card header: dot + name #}
                <div class="company-card-header">
                    <span class="company-dot" style="background: {{ company.dot_color }}"></span>
                    <span class="company-name">{{ company.name }}</span>
                </div>

                {# KPI rows — skip Target row (shown in Know More panel) #}
                <div class="company-kpi-table">
                    {% for kpi in company.kpis %}
                    {% if kpi.label != "Target" %}
                    <div class="company-kpi-row">
                        <span class="ckpi-label">{{ kpi.label }}</span>
                        <span class="ckpi-value">{{ kpi.value }}</span>
                        {% if kpi.pct is not none %}
                        <span class="pct-badge {{ pct_class(kpi.pct) }}">{{ kpi.pct }}%</span>
                        {% if kpi.delta == "up" %}<span class="delta-up">▲</span>
                        {% elif kpi.delta == "down" %}<span class="delta-down">▼</span>
                        {% else %}<span class="delta-none"></span>
                        {% endif %}
                        {% endif %}
                    </div>
                    {% endif %}
                    {% endfor %}
                </div>

                {# Know More button #}
                <div class="company-card-footer">
                    <button class="btn-know-more"
                            onclick="toggleDetails('{{ company.id }}')">Know More →</button>
                </div>

                {# Slide-down details panel with aging drill-down #}
                <div class="company-details" id="details-{{ company.id }}">
                    <div class="know-more-target-row">
                        Annual Target: {{ company.kpis[0].value }}
                    </div>
                    {{ aging_panel(company.id, aging[company.id]) }}
                </div>

            </div>
            {% endfor %}
        </div>
    </section>

</main>
{% endblock %}

{% block extra_js %}
<script src="{{ url_for('static', path='script.js') }}"></script>
{% endblock %}
```

- [ ] **Step 2: Start the dev server and verify the page loads without 500 errors**

```bash
cd D:/Fidelitus/mddb && uvicorn app.main:app --reload --port 8000
```

Open browser to `http://localhost:8000` — page should render with company cards intact.

- [ ] **Step 3: Commit**

```bash
git add app/templates/dashboard.html
git commit -m "[TASK-004] feat: embed aging_panel macro in company cards and corporate strip"
```

---

## Task 6: Add aging styles to `style.css`

**Files:**
- Modify: `app/static/style.css`

Append the following block to the end of `style.css`:

- [ ] **Step 1: Append aging CSS**

```css
/* ── Aging Panel ── */
.aging-panel {
    padding: 0.75rem 1rem 1rem;
}

/* Target row at top of Know More panel */
.know-more-target-row {
    font-size: 0.75rem;
    color: var(--color-text-secondary);
    padding: 0.5rem 1rem 0;
    border-top: 1px solid var(--color-border);
}

/* Bucket pills row */
.aging-pills {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-bottom: 0.75rem;
    padding-top: 0.5rem;
}

.aging-pill {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.1rem;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--color-border);
    border-radius: 6px;
    padding: 0.4rem 0.6rem;
    cursor: pointer;
    min-width: 4.5rem;
    transition: border-color 0.15s, background 0.15s;
    font-family: var(--font-body);
}

.aging-pill:hover:not(:disabled) {
    border-color: var(--color-accent);
    background: rgba(232, 168, 56, 0.08);
}

.aging-pill.active {
    border-color: var(--color-accent);
    background: rgba(232, 168, 56, 0.12);
}

.aging-pill--empty,
.aging-pill:disabled {
    opacity: 0.35;
    cursor: default;
}

.aging-pill-label {
    font-size: 0.6rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--color-text-secondary);
}

.aging-pill.active .aging-pill-label {
    color: var(--color-accent);
}

.aging-pill-count {
    font-family: var(--font-heading);
    font-size: 1rem;
    font-weight: 700;
    color: var(--color-text-primary);
    line-height: 1;
}

.aging-pill-total {
    font-size: 0.65rem;
    color: var(--color-text-secondary);
    white-space: nowrap;
}

/* Bucket detail table wrapper -- hidden by default */
.aging-table-wrapper {
    display: none;
    overflow-x: auto;
    margin-top: 0.5rem;
    border-top: 1px solid var(--color-border);
    padding-top: 0.5rem;
}

.aging-table-wrapper.open {
    display: block;
}

.aging-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.75rem;
}

.aging-table th {
    text-align: left;
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--color-text-secondary);
    padding: 0.3rem 0.5rem;
    border-bottom: 1px solid var(--color-border);
    white-space: nowrap;
}

.aging-table td {
    padding: 0.35rem 0.5rem;
    color: var(--color-text-primary);
    border-bottom: 1px solid rgba(48, 54, 61, 0.4);
    vertical-align: top;
}

.aging-table tbody tr:last-child td {
    border-bottom: none;
}

.aging-value {
    font-family: var(--font-heading);
    font-weight: 700;
    color: var(--color-accent);
    white-space: nowrap;
}

.aging-days {
    white-space: nowrap;
    color: var(--color-red-orange);
    font-weight: 600;
}

.aging-reason {
    color: var(--color-text-secondary);
    font-style: italic;
    max-width: 16rem;
}

/* Fix: deep panels need more max-height */
.company-details.open {
    max-height: 800px !important;
}

/* Corporate aging panel (sits below KPI strip) */
.corporate-aging-panel {
    margin-top: 1rem;
}

.corporate-aging-panel.open {
    max-height: 1000px !important;
    border-top: 1px solid var(--color-border);
}

/* Clickable KPI card signal */
.kpi-card--clickable {
    cursor: pointer;
}

.kpi-card--clickable:hover {
    border-color: rgba(232, 168, 56, 0.4);
    background: rgba(232, 168, 56, 0.04);
    transition: border-color 0.15s, background 0.15s;
}
```

- [ ] **Step 2: Commit**

```bash
git add app/static/style.css
git commit -m "[TASK-004] feat: add aging panel CSS (pills, table, corporate panel)"
```

---

## Task 7: Update `script.js` with pill-toggle and corporate panel logic

**Files:**
- Modify: `app/static/script.js`

Replace the full contents of `script.js`:

- [ ] **Step 1: Write the updated `script.js`**

```javascript
/* ── Company card Know More toggle ── */
function toggleDetails(id) {
    const panel = document.getElementById('details-' + id);
    panel.classList.toggle('open');

    // Reset any open aging tables when collapsing the card
    if (!panel.classList.contains('open')) {
        resetAgingPills(id);
    }
}

/* ── Corporate aging panel toggle (called by any KPI strip card click) ── */
function toggleCorporateAging() {
    const panel = document.getElementById('details-corporate');
    panel.classList.toggle('open');

    if (!panel.classList.contains('open')) {
        resetAgingPills('corporate');
    }
}

/* ── Aging bucket pill toggle ── */
function toggleAgingBucket(companyId, bucket) {
    const pillsContainer = document.getElementById('aging-pills-' + companyId);
    if (!pillsContainer) return;

    const clickedPill = pillsContainer.querySelector(
        '[data-company="' + companyId + '"][data-bucket="' + bucket + '"]'
    );
    const targetTable = document.getElementById(
        'aging-table-' + companyId + '-' + bucket
    );
    if (!clickedPill || !targetTable) return;

    const isAlreadyOpen = clickedPill.classList.contains('active');

    // Close all pills + tables for this company
    resetAgingPills(companyId);

    if (!isAlreadyOpen) {
        // Open the clicked one
        clickedPill.classList.add('active');
        targetTable.classList.add('open');
    }
}

/* ── Helper: close all pills + tables for a given company ── */
function resetAgingPills(companyId) {
    const pillsContainer = document.getElementById('aging-pills-' + companyId);
    if (!pillsContainer) return;

    pillsContainer.querySelectorAll('.aging-pill').forEach(function(pill) {
        pill.classList.remove('active');
    });

    // Close all table wrappers for this company
    document.querySelectorAll('[id^="aging-table-' + companyId + '-"]').forEach(function(table) {
        table.classList.remove('open');
    });
}
```

- [ ] **Step 2: Reload browser, open a company card, click a pill — table should expand**

Manual test steps:
1. Open `http://localhost:8000`
2. Click "Know More →" on **Fidelitus Transactions** — panel slides down, 5 pills visible
3. Click the **7 Days** pill — table appears with 3 rows (Rajesh Kumar, Priya Menon, Anand Rao)
4. Click **7 Days** again — table hides
5. Click **14 Days** — shows 2 rows; **7 Days** table stays closed
6. Click any **Corporate KPI** card — corporate aging panel appears below the strip
7. Click the same card again — panel collapses
8. Click a pill in the corporate panel — table shows items from all companies

- [ ] **Step 3: Commit**

```bash
git add app/static/script.js
git commit -m "[TASK-004] feat: add aging pill toggle and corporate panel JS"
```

---

## Task 8: Finish the branch

- [ ] **Step 1: Run the server one final time and verify all 6 companies + corporate**

```bash
cd D:/Fidelitus/mddb && uvicorn app.main:app --reload --port 8000
```

For each company card:
- Know More opens
- Pills render with correct counts/totals per spec
- Empty buckets (count=0) show disabled pills
- Tables expand/collapse correctly

For corporate panel:
- Clicking any KPI card opens/closes the panel
- 7d pill shows 10 items (sum across all companies)

- [ ] **Step 2: Mark TASK-004 status as Done**

Edit `tasks/TASK-004-aging-drill.md` — change `Status: In Progress` → `Status: Done`

- [ ] **Step 3: Final commit**

```bash
git add tasks/TASK-004-aging-drill.md
git commit -m "[TASK-004] chore: mark task complete"
```

- [ ] **Step 4: Push and open PR**

```bash
git push origin feature/TASK-004-aging-drill
gh pr create --title "[TASK-004] feat: aging drill-down panel for company cards + corporate KPIs" \
  --body "$(cat <<'EOF'
## Summary
- Adds aging dummy data for all 6 companies + corporate aggregate in `dummy_data.py`
- Jinja2 macro in `partials/aging_panel.html` renders 5 bucket pills + expandable tables
- Know More panel now shows Target + aging pills instead of placeholder text
- Corporate KPI strip cards are clickable to reveal aggregated aging panel
- Pill toggle: click to expand table, click again to collapse, switch pills collapses previous

## Test plan
- [ ] All 6 company Know More panels open and show 5 aging pills
- [ ] Fidelitus Transactions 7d pill: 3 items, Rs.2.1 Cr — matches spec exactly
- [ ] Empty buckets (gcc has 4 empty buckets) show disabled pills
- [ ] Corporate panel opens when any KPI card is clicked
- [ ] Corporate 7d pill shows items from all companies
- [ ] No JS frameworks used

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

---

## Self-Review

**Spec coverage check:**

| Requirement | Task |
|---|---|
| Aging bucket pills (7d/14d/21d/90d/NPA) per company card | Task 3, 5, 6 |
| Pill shows count + total | Task 3 |
| Click pill → expand table | Task 7 |
| Table columns: Company/Team / Member / Value / Days / Reason | Task 3 |
| Dummy data for all 6 companies | Task 2 |
| Store under `aging` key indexed by company slug | Task 2 |
| Corporate aggregate across all companies | Task 2 |
| Corporate KPI cards clickable | Task 5 |
| Corporate panel shows company column | Task 3 (item.company in each row) |
| Vanilla JS only, no page reload | Task 7 |
| Toggle pill → show/hide table | Task 7 |
| `max-height` fix for deep panels | Task 6 |

**Placeholder scan:** No TBD / TODO / "similar to" patterns found.

**Type consistency:** `AGING_DATA` used consistently across tasks 2, 4, 5. Macro called as `aging_panel(company_id, aging[company_id])` in Task 5 matching macro signature `aging_panel(company_id, aging)` in Task 3. JS function `toggleAgingBucket(companyId, bucket)` called in Task 3 template, defined in Task 7. DOM IDs `aging-pills-{id}`, `aging-table-{id}-{bucket}` consistent across Task 3 and Task 7.
