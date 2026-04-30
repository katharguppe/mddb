# Company Cards Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 6 subsidiary company cards (3-per-row CSS grid) below the corporate KPI strip, rendered from `dummy_data.py` via Jinja2, with a vanilla-JS slide-down "Know More" panel per card.

**Architecture:** `dummy_data.py` holds all mock data; `routes.py` imports and forwards it as `data` to the Jinja2 template; `dashboard.html` renders both the corporate KPI strip (Section A) and the companies grid (Section B) via template loops; `style.css` provides all layout and visual rules.

**Tech Stack:** Python 3.13, FastAPI, Jinja2, Uvicorn, vanilla HTML/CSS/JS, pytest + httpx (tests)

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `tasks/TASK-003-company-cards.md` | CREATE | session task tracker |
| `app/mockup/dummy_data.py` | CREATE | single source of truth for all mock data |
| `app/mockup/routes.py` | MODIFY | import data dict, pass to template |
| `app/templates/dashboard.html` | MODIFY | render KPI strip + company cards |
| `app/static/style.css` | MODIFY | grid, card, panel, button rules |
| `tests/test_company_cards.py` | CREATE | integration smoke tests |

---

## Task 1: Create the task file

**Files:**
- Create: `tasks/TASK-003-company-cards.md`

- [ ] **Step 1: Write the task file**

```markdown
# TASK-003 -- Company Cards

**Status:** In Progress
**Session:** s03 (Phase 0 -- Mockup)
**Scope:** app/mockup/dummy_data.py, app/mockup/routes.py,
           app/templates/dashboard.html, app/static/style.css

## Goal
Add 6 subsidiary company cards in a 3-per-row CSS grid below the
corporate KPI strip, rendered from dummy_data.py via Jinja2.

## Acceptance Criteria
- [ ] 6 company cards rendered in a 3-per-row grid from dummy_data.py (not hardcoded)
- [ ] Each card has a 3px top border in its unique dot color
- [ ] Each card shows all 6 KPIs with value, % badge (correct color band), and delta arrow
- [ ] "Know More" button toggles slide-down panel with JS (no page reload)
- [ ] Details panel shows placeholder text "Aging analysis — Session 04"
- [ ] PRODUCTION=1 serves dummy data; no MongoDB calls
- [ ] Responsive: 1 column on mobile (768px and below)
- [ ] No JS frameworks -- vanilla JS only

## Files Changed
- CREATE  app/mockup/dummy_data.py
- MODIFY  app/mockup/routes.py   (3-line change -- necessary dependency)
- MODIFY  app/templates/dashboard.html
- MODIFY  app/static/style.css
```

- [ ] **Step 2: Commit**

```bash
git add tasks/TASK-003-company-cards.md
git commit -m "[TASK-003] chore: add task file"
```

---

## Task 2: Create `dummy_data.py`

**Files:**
- Create: `app/mockup/dummy_data.py`

- [ ] **Step 1: Write the file**

```python
# app/mockup/dummy_data.py
# Single source of truth for Phase 0 mock data.
# PRODUCTION=1 -> this file is used. PRODUCTION=0 -> live MongoDB replaces it.

DASHBOARD_DATA = {
    "corporate": {
        "kpis": [
            {
                "label": "Target for Year",
                "value": "Rs.320 Cr",
                "target": "Rs.320 Cr",
                "pct": None,
                "delta": None,
            },
            {
                "label": "Revenue (Booking)",
                "value": "Rs.142 Cr",
                "target": "Rs.320 Cr",
                "pct": 44,
                "delta": "up",
            },
            {
                "label": "Invoiced Amounts",
                "value": "Rs.108 Cr",
                "target": "Rs.320 Cr",
                "pct": 34,
                "delta": None,
            },
            {
                "label": "Payments Received",
                "value": "Rs.71 Cr",
                "target": "Rs.320 Cr",
                "pct": 22,
                "delta": None,
            },
            {
                "label": "Meetings Done",
                "value": "971",
                "target": "1200",
                "pct": 81,
                "delta": "up",
            },
            {
                "label": "Proposals Submitted",
                "value": "530",
                "target": "800",
                "pct": 66,
                "delta": "up",
            },
        ]
    },
    "companies": [
        {
            "id": "transactions",
            "name": "Fidelitus Transactions",
            "dot_color": "#3b82f6",
            "kpis": [
                {"label": "Target",    "value": "Rs.80 Cr", "pct": None, "delta": None},
                {"label": "Revenue",   "value": "Rs.68 Cr", "pct": 85,   "delta": "up"},
                {"label": "Invoiced",  "value": "Rs.54 Cr", "pct": 68,   "delta": None},
                {"label": "Payments",  "value": "Rs.42 Cr", "pct": 53,   "delta": None},
                {"label": "Meetings",  "value": "320",       "pct": 88,   "delta": "up"},
                {"label": "Proposals", "value": "180",       "pct": 79,   "delta": "up"},
            ],
        },
        {
            "id": "projects",
            "name": "Fidelitus Projects",
            "dot_color": "#10b981",
            "kpis": [
                {"label": "Target",    "value": "Rs.60 Cr", "pct": None, "delta": None},
                {"label": "Revenue",   "value": "Rs.29 Cr", "pct": 48,   "delta": "down"},
                {"label": "Invoiced",  "value": "Rs.21 Cr", "pct": 35,   "delta": None},
                {"label": "Payments",  "value": "Rs.14 Cr", "pct": 23,   "delta": None},
                {"label": "Meetings",  "value": "210",       "pct": 61,   "delta": None},
                {"label": "Proposals", "value": "140",       "pct": 55,   "delta": None},
            ],
        },
        {
            "id": "fms",
            "name": "Fidelitus FMS",
            "dot_color": "#a855f7",
            "kpis": [
                {"label": "Target",    "value": "Rs.30 Cr", "pct": None, "delta": None},
                {"label": "Revenue",   "value": "Rs.24 Cr", "pct": 80,   "delta": "up"},
                {"label": "Invoiced",  "value": "Rs.19 Cr", "pct": 63,   "delta": None},
                {"label": "Payments",  "value": "Rs.16 Cr", "pct": 53,   "delta": None},
                {"label": "Meetings",  "value": "180",       "pct": 72,   "delta": None},
                {"label": "Proposals", "value": "95",        "pct": 67,   "delta": None},
            ],
        },
        {
            "id": "hrlabs",
            "name": "Fidelitus HR Labs",
            "dot_color": "#f43f5e",
            "kpis": [
                {"label": "Target",    "value": "Rs.25 Cr", "pct": None, "delta": None},
                {"label": "Revenue",   "value": "Rs.11 Cr", "pct": 44,   "delta": "down"},
                {"label": "Invoiced",  "value": "Rs.8 Cr",  "pct": 32,   "delta": None},
                {"label": "Payments",  "value": "Rs.5 Cr",  "pct": 20,   "delta": None},
                {"label": "Meetings",  "value": "150",       "pct": 48,   "delta": None},
                {"label": "Proposals", "value": "62",        "pct": 41,   "delta": None},
            ],
        },
        {
            "id": "technology",
            "name": "Fidelitus Technology",
            "dot_color": "#22d3ee",
            "kpis": [
                {"label": "Target",    "value": "Rs.20 Cr", "pct": None, "delta": None},
                {"label": "Revenue",   "value": "Rs.9 Cr",  "pct": 45,   "delta": None},
                {"label": "Invoiced",  "value": "Rs.6 Cr",  "pct": 30,   "delta": None},
                {"label": "Payments",  "value": "Rs.4 Cr",  "pct": 20,   "delta": None},
                {"label": "Meetings",  "value": "87",        "pct": 57,   "delta": None},
                {"label": "Proposals", "value": "35",        "pct": 47,   "delta": None},
            ],
        },
        {
            "id": "gcc",
            "name": "Fidelitus GCC Nexus",
            "dot_color": "#e8a838",
            "kpis": [
                {"label": "Target",    "value": "Rs.25 Cr", "pct": None, "delta": None},
                {"label": "Revenue",   "value": "Rs.1 Cr",  "pct": 4,    "delta": "down"},
                {"label": "Invoiced",  "value": "Rs.0",     "pct": 0,    "delta": None},
                {"label": "Payments",  "value": "Rs.0",     "pct": 0,    "delta": None},
                {"label": "Meetings",  "value": "24",        "pct": 21,   "delta": None},
                {"label": "Proposals", "value": "18",        "pct": 24,   "delta": None},
            ],
        },
    ],
}
```

- [ ] **Step 2: Commit**

```bash
git add app/mockup/dummy_data.py
git commit -m "[TASK-003] feat: add dummy data for corporate KPIs and 6 companies"
```

---

## Task 3: Update `routes.py`

**Files:**
- Modify: `app/mockup/routes.py`

- [ ] **Step 1: Replace the file content**

```python
# app/mockup/routes.py
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.mockup.dummy_data import DASHBOARD_DATA

templates_path = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_path))

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Render the MD Dashboard mockup."""
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "data": DASHBOARD_DATA},
    )
```

- [ ] **Step 2: Commit**

```bash
git add app/mockup/routes.py
git commit -m "[TASK-003] feat: pass DASHBOARD_DATA to template"
```

---

## Task 4: Write failing integration tests

**Files:**
- Create: `tests/test_company_cards.py`

- [ ] **Step 1: Write the test file**

```python
# tests/test_company_cards.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_dashboard_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_all_six_companies_rendered():
    html = client.get("/").text
    for name in [
        "Fidelitus Transactions",
        "Fidelitus Projects",
        "Fidelitus FMS",
        "Fidelitus HR Labs",
        "Fidelitus Technology",
        "Fidelitus GCC Nexus",
    ]:
        assert name in html, f"Company '{name}' not found in rendered HTML"


def test_six_know_more_buttons_rendered():
    html = client.get("/").text
    assert html.count("toggleDetails") == 6


def test_details_panels_rendered():
    html = client.get("/").text
    for company_id in ["transactions", "projects", "fms", "hrlabs", "technology", "gcc"]:
        assert f'id="details-{company_id}"' in html
    assert "Aging analysis" in html


def test_pct_color_bands_rendered():
    html = client.get("/").text
    # GCC Nexus revenue 4% and invoiced 0% -> red band must appear
    assert "kpi-status-red" in html
    # Transactions revenue 85% -> green band must appear
    assert "kpi-status-green" in html
```

- [ ] **Step 2: Run tests — expect failures**

```bash
pytest tests/test_company_cards.py -v
```

Expected output: `FAILED` on `test_all_six_companies_rendered` and others
(because `dashboard.html` still has the placeholder, not the rendered cards).
`test_dashboard_returns_200` may pass already — that's fine.

- [ ] **Step 3: Commit the failing tests**

```bash
git add tests/test_company_cards.py
git commit -m "[TASK-003] test: add failing integration tests for company cards"
```

---

## Task 5: Update `style.css`

**Files:**
- Modify: `app/static/style.css`

- [ ] **Step 1: Replace the existing `.dashboard-header` and `.dashboard-title` blocks, then append all new rules**

The current `style.css` has these rules that need to be REPLACED (not duplicated):
- `.dashboard-header` (lines 82-87) — add `display: flex; justify-content: space-between; align-items: flex-start;`
- `.dashboard-title` (lines 88-94) — change color from `var(--color-accent)` to `var(--color-text-primary)`, font-size from `2.5rem` to `2rem`, remove `margin-bottom`
- `.dashboard-subtitle` (lines 95-99) — REMOVE (replaced by `.dashboard-eyebrow` and `.phase-badge`)

Updated `.dashboard-header` block (replace existing):
```css
/* Dashboard Header */
.dashboard-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 1px solid var(--color-border);
    padding-bottom: var(--spacing-xl);
    margin-bottom: var(--spacing-2xl);
}

.dashboard-eyebrow {
    font-size: 0.65rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--color-accent);
    margin-bottom: 0.25rem;
}

.dashboard-title {
    color: var(--color-text-primary);
    font-size: 2rem;
    font-family: var(--font-heading);
    margin: 0;
}

.phase-badge {
    font-size: 0.65rem;
    padding: 0.25rem 0.6rem;
    border-radius: 4px;
    border: 1px solid var(--color-border);
    color: var(--color-text-secondary);
    letter-spacing: 1px;
}
```

Then APPEND the following new rules at the end of `style.css`:

```css
/* ── Section eyebrow label ── */
.section-label {
    font-size: 0.65rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--color-text-secondary);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--color-border);
}

/* ── % badge ── */
.pct-badge {
    font-size: 0.7rem;
    font-weight: 700;
    padding: 0.15rem 0.4rem;
    border-radius: 3px;
    background: rgba(255, 255, 255, 0.05);
}

.pct-badge.kpi-status-red        { color: var(--color-red); }
.pct-badge.kpi-status-red-orange { color: var(--color-red-orange); }
.pct-badge.kpi-status-amber      { color: var(--color-amber); }
.pct-badge.kpi-status-green      { color: var(--color-green); }

/* ── Delta arrows ── */
.delta-up   { color: var(--color-green); font-size: 0.75rem; }
.delta-down { color: var(--color-red);   font-size: 0.75rem; }
.delta-none { display: inline-block; width: 0.75rem; }

/* ── Corporate KPI Strip (Section A) ── */
.kpi-strip {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 1rem;
}

.kpi-card {
    background: #1c2330;
    border: 1px solid var(--color-border);
    border-radius: 8px;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
}

.kpi-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--color-text-secondary);
}

.kpi-value {
    font-family: var(--font-heading);
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--color-text-primary);
}

.kpi-target {
    font-size: 0.75rem;
    color: var(--color-text-secondary);
}

.kpi-footer {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    margin-top: 0.25rem;
}

/* ── Company Cards Grid (Section B) ── */
.companies-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
}

.company-card {
    background: var(--color-bg-surface);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    overflow: hidden;
    border-top-width: 3px;
    border-top-style: solid;
    display: flex;
    flex-direction: column;
}

.company-card-header {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.875rem 1rem;
    border-bottom: 1px solid var(--color-border);
}

.company-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
}

.company-name {
    font-family: var(--font-heading);
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--color-text-primary);
}

.company-kpi-table {
    padding: 0.5rem 1rem;
    flex: 1;
}

.company-kpi-row {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.3rem 0;
    border-bottom: 1px solid rgba(48, 54, 61, 0.5);
}

.company-kpi-row:last-child {
    border-bottom: none;
}

.ckpi-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--color-text-secondary);
    width: 5rem;
    flex-shrink: 0;
}

.ckpi-value {
    font-family: var(--font-heading);
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--color-text-primary);
    flex: 1;
}

.ckpi-target-placeholder {
    display: inline-block;
    width: 3rem;
}

/* ── Know More button ── */
.company-card-footer {
    padding: 0.75rem 1rem;
    border-top: 1px solid var(--color-border);
    display: flex;
    justify-content: flex-end;
}

.btn-know-more {
    background: transparent;
    border: 1px solid var(--color-accent);
    color: var(--color-accent);
    border-radius: 4px;
    padding: 0.3rem 0.8rem;
    cursor: pointer;
    font-family: var(--font-body);
    font-size: 0.78rem;
    font-weight: 500;
    transition: background 0.15s;
}

.btn-know-more:hover {
    background: rgba(232, 168, 56, 0.1);
}

/* ── Slide-down details panel ── */
.company-details {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
    background: #1c2330;
}

.company-details.open {
    max-height: 120px;
    border-top: 1px solid var(--color-border);
}

.details-placeholder {
    padding: 0.75rem 1rem;
    font-size: 0.8rem;
    color: var(--color-text-secondary);
    font-style: italic;
    margin: 0;
}

/* ── Responsive ── */
@media (max-width: 1024px) {
    .kpi-strip {
        grid-template-columns: repeat(3, 1fr);
    }
}

@media (max-width: 768px) {
    .companies-grid {
        grid-template-columns: 1fr;
    }

    .kpi-strip {
        grid-template-columns: repeat(2, 1fr);
    }
}
```

- [ ] **Step 2: Commit**

```bash
git add app/static/style.css
git commit -m "[TASK-003] style: add KPI strip, company card grid, details panel, and button styles"
```

---

## Task 6: Update `dashboard.html`

**Files:**
- Modify: `app/templates/dashboard.html`

- [ ] **Step 1: Replace the entire file content**

```html
{% extends "base.html" %}

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
            <div class="kpi-card">
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

                {# KPI rows #}
                <div class="company-kpi-table">
                    {% for kpi in company.kpis %}
                    <div class="company-kpi-row">
                        <span class="ckpi-label">{{ kpi.label }}</span>
                        <span class="ckpi-value">{{ kpi.value }}</span>
                        {% if kpi.pct is not none %}
                        <span class="pct-badge {{ pct_class(kpi.pct) }}">{{ kpi.pct }}%</span>
                        {% if kpi.delta == "up" %}<span class="delta-up">▲</span>
                        {% elif kpi.delta == "down" %}<span class="delta-down">▼</span>
                        {% else %}<span class="delta-none"></span>
                        {% endif %}
                        {% else %}
                        <span class="ckpi-target-placeholder"></span>
                        <span class="delta-none"></span>
                        {% endif %}
                    </div>
                    {% endfor %}
                </div>

                {# Know More button #}
                <div class="company-card-footer">
                    <button class="btn-know-more"
                            onclick="toggleDetails('{{ company.id }}')">Know More →</button>
                </div>

                {# Slide-down details panel (hidden until toggled) #}
                <div class="company-details" id="details-{{ company.id }}">
                    <p class="details-placeholder">Aging analysis — Session 04</p>
                </div>

            </div>
            {% endfor %}
        </div>
    </section>

</main>
{% endblock %}

{% block extra_js %}
<script>
function toggleDetails(id) {
    document.getElementById('details-' + id).classList.toggle('open');
}
</script>
{% endblock %}
```

- [ ] **Step 2: Commit**

```bash
git add app/templates/dashboard.html
git commit -m "[TASK-003] feat: render corporate KPI strip and 6 company cards from dummy data"
```

---

## Task 7: Run tests — expect all green

- [ ] **Step 1: Run the full test suite**

```bash
pytest tests/test_company_cards.py -v
```

Expected output:
```
tests/test_company_cards.py::test_dashboard_returns_200            PASSED
tests/test_company_cards.py::test_all_six_companies_rendered       PASSED
tests/test_company_cards.py::test_six_know_more_buttons_rendered   PASSED
tests/test_company_cards.py::test_details_panels_rendered          PASSED
tests/test_company_cards.py::test_pct_color_bands_rendered         PASSED

5 passed in X.XXs
```

If any test fails, check the failure message — it will name the exact company or attribute missing from the rendered HTML. Fix in `dashboard.html` or `dummy_data.py` before proceeding.

- [ ] **Step 2: Also run the existing test suite to confirm nothing broke**

```bash
pytest tests/ -v
```

Expected: all existing tests still pass (test_config.py should be unaffected).

---

## Task 8: Visual check and final commit

- [ ] **Step 1: Start the server**

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000` in a browser.

- [ ] **Step 2: Verify visually**

| Check | Expected |
|---|---|
| Corporate KPI strip | 6 cards in a single row |
| Subsidiaries section | 3 cards × 2 rows |
| Dot colors | Each company has a distinct dot and border-top |
| % badges | GCC Nexus shows red, Transactions shows green |
| Delta arrows | ▲ for "up", ▼ for "down", blank otherwise |
| Know More button | Amber border, amber text |
| Click Know More | Panel slides down, shows "Aging analysis — Session 04" |
| Click again | Panel slides back up |
| Resize to <768px | Cards collapse to 1 column |

- [ ] **Step 3: Update task file status to Done**

Edit `tasks/TASK-003-company-cards.md` — change `**Status:** In Progress` to `**Status:** Done` and tick all acceptance criteria checkboxes.

- [ ] **Step 4: Final commit**

```bash
git add tasks/TASK-003-company-cards.md
git commit -m "[TASK-003] chore: mark task complete"
```
