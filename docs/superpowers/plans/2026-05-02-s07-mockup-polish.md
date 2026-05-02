# s07 Mockup Polish Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete the Phase 0 mockup by expanding the Weekly Pulse to all 6 KPIs, adding MD productivity features (Sticky Notes, Print, Last Updated), creating stub API routes for PRODUCTION=0, and writing the developer handoff document.

**Architecture:** All changes stay within Phase 0 scope — `app/mockup/dummy_data.py`, `app/templates/dashboard.html`, `app/static/script.js`, `app/static/style.css`. New `app/api/` stub is minimal (2 files). Handoff doc is plain markdown. No new dependencies.

**Tech Stack:** Python 3.13, FastAPI, Jinja2, vanilla HTML/CSS/JS, localStorage API

---

## File Map

| File | Action | Purpose |
|---|---|---|
| `tasks/TASK-007-mockup-polish.md` | Create | Session task tracker |
| `app/mockup/dummy_data.py` | Modify | Add `kpis` dict to WEEKLY_PULSE rows; add `last_updated` to companies |
| `app/templates/dashboard.html` | Modify | Pulse KPI selector pills; span-based KPI data cells; sticky notes HTML; Print button; last-updated span |
| `app/static/script.js` | Modify | `switchPulseKpi()`, sticky notes JS, `printDashboard()` |
| `app/static/style.css` | Modify | Pulse KPI pills, sticky notes widget, `@media print`, `.card-last-updated` |
| `app/api/__init__.py` | Create | Empty package init |
| `app/api/routes.py` | Create | Catch-all stub returning JSON for PRODUCTION=0 |
| `app/main.py` | Modify | Wire stub API router in PRODUCTION=0 branch |
| `docs/HANDOFF.md` | Create | Developer handoff document |

---

## Task 1: Create task file

**Files:**
- Create: `tasks/TASK-007-mockup-polish.md`

- [ ] **Step 1: Create the task file**

```markdown
# TASK-007 — s07 Mockup Polish & Developer Handoff

## Goal
Final mockup polish and handoff preparation.

## Scope
app/mockup/ · app/templates/ · app/static/ · app/api/ · docs/

## Checklist
- [ ] Carry-over: Weekly Pulse expanded to all 6 KPIs
- [ ] Sticky Notes panel (localStorage)
- [ ] Last Updated timestamp on company cards
- [ ] Print / Export view
- [ ] ENV flag: stub API for PRODUCTION=0
- [ ] docs/HANDOFF.md
- [ ] Final smoke test
```

- [ ] **Step 2: Commit**

```bash
git add tasks/TASK-007-mockup-polish.md
git commit -m "[TASK-007] chore: add task file TASK-007-mockup-polish.md"
```

---

## Task 2: Extend WEEKLY_PULSE — all 6 KPIs per company

**Files:**
- Modify: `app/mockup/dummy_data.py` — replace flat fields on each WEEKLY_PULSE row and total with a nested `kpis` dict

The current flat fields (`committed`, `actual`, `delta`, `delta_sign`, `actual_pct`) on each row are **removed** and replaced with a `kpis` dict. The template will be updated in Task 4 to match.

- [ ] **Step 1: Replace WEEKLY_PULSE in dummy_data.py**

Find the existing `WEEKLY_PULSE = { ... }` block (lines ~968–1035) and replace it entirely with:

```python
WEEKLY_PULSE = {
    "week_label":      "Week of 21 Apr – 25 Apr 2026",
    "committed_label": "Last committed: Mon 21 Apr",
    "rows": [
        {
            "id":   "transactions",
            "name": "Fidelitus Transactions",
            "kpis": {
                "revenue":   {"committed": "Rs.9 Cr",    "actual": "Rs.9.8 Cr",  "delta": "+0.8 Cr",   "delta_sign": "pos", "actual_pct": 109},
                "invoiced":  {"committed": "Rs.7 Cr",    "actual": "Rs.6.5 Cr",  "delta": "−0.5 Cr",   "delta_sign": "neg", "actual_pct": 93},
                "payments":  {"committed": "Rs.5 Cr",    "actual": "Rs.4.2 Cr",  "delta": "−0.8 Cr",   "delta_sign": "neg", "actual_pct": 84},
                "meetings":  {"committed": "45",          "actual": "48",          "delta": "+3",         "delta_sign": "pos", "actual_pct": 107},
                "proposals": {"committed": "20",          "actual": "15",          "delta": "−5",         "delta_sign": "neg", "actual_pct": 75},
                "target":    {"committed": "Rs.80 Cr",   "actual": "—",           "delta": "—",          "delta_sign": "neu", "actual_pct": None},
            },
        },
        {
            "id":   "projects",
            "name": "Fidelitus Projects",
            "kpis": {
                "revenue":   {"committed": "Rs.4 Cr",    "actual": "Rs.1.8 Cr",  "delta": "−2.2 Cr",   "delta_sign": "neg", "actual_pct": 45},
                "invoiced":  {"committed": "Rs.3 Cr",    "actual": "Rs.1.5 Cr",  "delta": "−1.5 Cr",   "delta_sign": "neg", "actual_pct": 50},
                "payments":  {"committed": "Rs.2 Cr",    "actual": "Rs.0.8 Cr",  "delta": "−1.2 Cr",   "delta_sign": "neg", "actual_pct": 40},
                "meetings":  {"committed": "30",          "actual": "18",          "delta": "−12",        "delta_sign": "neg", "actual_pct": 60},
                "proposals": {"committed": "12",          "actual": "8",           "delta": "−4",         "delta_sign": "neg", "actual_pct": 67},
                "target":    {"committed": "Rs.60 Cr",   "actual": "—",           "delta": "—",          "delta_sign": "neu", "actual_pct": None},
            },
        },
        {
            "id":   "fms",
            "name": "Fidelitus FMS",
            "kpis": {
                "revenue":   {"committed": "Rs.2.5 Cr",  "actual": "Rs.2.1 Cr",  "delta": "−0.4 Cr",   "delta_sign": "neg", "actual_pct": 84},
                "invoiced":  {"committed": "Rs.2 Cr",    "actual": "Rs.1.8 Cr",  "delta": "−0.2 Cr",   "delta_sign": "neg", "actual_pct": 90},
                "payments":  {"committed": "Rs.1.5 Cr",  "actual": "Rs.1.3 Cr",  "delta": "−0.2 Cr",   "delta_sign": "neg", "actual_pct": 87},
                "meetings":  {"committed": "25",          "actual": "22",          "delta": "−3",         "delta_sign": "neg", "actual_pct": 88},
                "proposals": {"committed": "10",          "actual": "9",           "delta": "−1",         "delta_sign": "neg", "actual_pct": 90},
                "target":    {"committed": "Rs.30 Cr",   "actual": "—",           "delta": "—",          "delta_sign": "neu", "actual_pct": None},
            },
        },
        {
            "id":   "hrlabs",
            "name": "Fidelitus HR Labs",
            "kpis": {
                "revenue":   {"committed": "Rs.1.5 Cr",  "actual": "Rs.0.3 Cr",  "delta": "−1.2 Cr",   "delta_sign": "neg", "actual_pct": 20},
                "invoiced":  {"committed": "Rs.1 Cr",    "actual": "Rs.0.4 Cr",  "delta": "−0.6 Cr",   "delta_sign": "neg", "actual_pct": 40},
                "payments":  {"committed": "Rs.0.8 Cr",  "actual": "Rs.0.2 Cr",  "delta": "−0.6 Cr",   "delta_sign": "neg", "actual_pct": 25},
                "meetings":  {"committed": "20",          "actual": "9",           "delta": "−11",        "delta_sign": "neg", "actual_pct": 45},
                "proposals": {"committed": "8",           "actual": "4",           "delta": "−4",         "delta_sign": "neg", "actual_pct": 50},
                "target":    {"committed": "Rs.25 Cr",   "actual": "—",           "delta": "—",          "delta_sign": "neu", "actual_pct": None},
            },
        },
        {
            "id":   "technology",
            "name": "Fidelitus Technology",
            "kpis": {
                "revenue":   {"committed": "Rs.1.2 Cr",  "actual": "Rs.0.5 Cr",  "delta": "−0.7 Cr",   "delta_sign": "neg", "actual_pct": 42},
                "invoiced":  {"committed": "Rs.0.8 Cr",  "actual": "Rs.0.4 Cr",  "delta": "−0.4 Cr",   "delta_sign": "neg", "actual_pct": 50},
                "payments":  {"committed": "Rs.0.5 Cr",  "actual": "Rs.0.2 Cr",  "delta": "−0.3 Cr",   "delta_sign": "neg", "actual_pct": 40},
                "meetings":  {"committed": "15",          "actual": "8",           "delta": "−7",         "delta_sign": "neg", "actual_pct": 53},
                "proposals": {"committed": "6",           "actual": "4",           "delta": "−2",         "delta_sign": "neg", "actual_pct": 67},
                "target":    {"committed": "Rs.20 Cr",   "actual": "—",           "delta": "—",          "delta_sign": "neu", "actual_pct": None},
            },
        },
        {
            "id":   "gcc",
            "name": "Fidelitus GCC Nexus",
            "kpis": {
                "revenue":   {"committed": "Rs.0.5 Cr",  "actual": "Rs.0.05 Cr", "delta": "−0.45 Cr",  "delta_sign": "neg", "actual_pct": 10},
                "invoiced":  {"committed": "Rs.0",       "actual": "Rs.0",        "delta": "—",          "delta_sign": "neu", "actual_pct": 0},
                "payments":  {"committed": "Rs.0",       "actual": "Rs.0",        "delta": "—",          "delta_sign": "neu", "actual_pct": 0},
                "meetings":  {"committed": "5",           "actual": "3",           "delta": "−2",         "delta_sign": "neg", "actual_pct": 60},
                "proposals": {"committed": "4",           "actual": "3",           "delta": "−1",         "delta_sign": "neg", "actual_pct": 75},
                "target":    {"committed": "Rs.25 Cr",   "actual": "—",           "delta": "—",          "delta_sign": "neu", "actual_pct": None},
            },
        },
    ],
    "total": {
        "kpis": {
            "revenue":   {"committed": "Rs.18.7 Cr",  "actual": "Rs.14.55 Cr", "delta": "−4.15 Cr",  "delta_sign": "neg", "actual_pct": 78},
            "invoiced":  {"committed": "Rs.13.8 Cr",  "actual": "Rs.10.6 Cr",  "delta": "−3.2 Cr",   "delta_sign": "neg", "actual_pct": 77},
            "payments":  {"committed": "Rs.9.8 Cr",   "actual": "Rs.6.7 Cr",   "delta": "−3.1 Cr",   "delta_sign": "neg", "actual_pct": 68},
            "meetings":  {"committed": "140",          "actual": "108",          "delta": "−32",        "delta_sign": "neg", "actual_pct": 77},
            "proposals": {"committed": "60",           "actual": "43",           "delta": "−17",        "delta_sign": "neg", "actual_pct": 72},
            "target":    {"committed": "Rs.240 Cr",   "actual": "—",            "delta": "—",          "delta_sign": "neu", "actual_pct": None},
        },
    },
}
```

- [ ] **Step 2: Add `last_updated` field to each company in DASHBOARD_DATA["companies"]**

In the same file, find each company dict inside `DASHBOARD_DATA["companies"]` and add `"last_updated"` after `"dot_color"`:

```python
# transactions
"last_updated": "25 Apr 2026, 9:30 AM",

# projects
"last_updated": "25 Apr 2026, 10:15 AM",

# fms
"last_updated": "25 Apr 2026, 9:00 AM",

# hrlabs
"last_updated": "25 Apr 2026, 11:00 AM",

# technology
"last_updated": "25 Apr 2026, 9:45 AM",

# gcc
"last_updated": "25 Apr 2026, 2:00 PM",
```

- [ ] **Step 3: Verify Python syntax**

```bash
python -c "from app.mockup.dummy_data import DASHBOARD_DATA, WEEKLY_PULSE; print('OK', len(WEEKLY_PULSE['rows']), 'rows')"
```

Expected output: `OK 6 rows`

- [ ] **Step 4: Commit**

```bash
git add app/mockup/dummy_data.py
git commit -m "[TASK-007] feat: expand WEEKLY_PULSE to all 6 KPIs; add last_updated to companies"
```

---

## Task 3: Update dashboard.html — Weekly Pulse section

**Files:**
- Modify: `app/templates/dashboard.html` — Section W only

The pulse table currently renders flat row fields (`row.committed`, `row.actual`, etc.). Replace with the new `kpis`-nested structure using spans per KPI inside each data cell.

- [ ] **Step 1: Replace Section W entirely**

Find the `{# ── Section W: Weekly Pulse ── #}` block (starts at `<section class="section weekly-pulse-section"`) and replace it with:

```html
{# ── Section W: Weekly Pulse ── #}
<section class="section weekly-pulse-section" id="weekly-pulse-section">
    <div class="section-label">
        Weekly Pulse
        <span class="pulse-week-meta">
            {{ weekly_pulse.week_label }} &nbsp;·&nbsp; {{ weekly_pulse.committed_label }}
        </span>
    </div>

    {# KPI selector pills #}
    <div class="pulse-kpi-selector" id="pulse-kpi-selector">
        <button class="pulse-kpi-pill active" onclick="switchPulseKpi('revenue')">Revenue</button>
        <button class="pulse-kpi-pill" onclick="switchPulseKpi('invoiced')">Invoiced</button>
        <button class="pulse-kpi-pill" onclick="switchPulseKpi('payments')">Payments</button>
        <button class="pulse-kpi-pill" onclick="switchPulseKpi('meetings')">Meetings</button>
        <button class="pulse-kpi-pill" onclick="switchPulseKpi('proposals')">Proposals</button>
        <button class="pulse-kpi-pill" onclick="switchPulseKpi('target')">Target</button>
    </div>

    <table class="pulse-table">
        <thead>
            <tr>
                <th>Company</th>
                <th>Committed (Mon)</th>
                <th>Actual (Fri)</th>
                <th>Delta</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            {% set kpi_keys = ['revenue','invoiced','payments','meetings','proposals','target'] %}
            {% for row in weekly_pulse.rows %}
            <tr class="pulse-row pulse-row--clickable"
                onclick="toggleDetails('{{ row.id }}')">
                <td>{{ row.name }}</td>
                <td>
                    {% for k in kpi_keys %}
                    <span class="pulse-kpi-val" data-kpi="{{ k }}"
                          {% if k != 'revenue' %}style="display:none"{% endif %}>
                        {{ row.kpis[k].committed }}
                    </span>
                    {% endfor %}
                </td>
                <td>
                    {% for k in kpi_keys %}
                    <span class="pulse-kpi-val" data-kpi="{{ k }}"
                          {% if k != 'revenue' %}style="display:none"{% endif %}>
                        {{ row.kpis[k].actual }}
                    </span>
                    {% endfor %}
                </td>
                <td>
                    {% for k in kpi_keys %}
                    <span class="pulse-kpi-val pulse-delta pulse-delta--{{ row.kpis[k].delta_sign }}"
                          data-kpi="{{ k }}"
                          {% if k != 'revenue' %}style="display:none"{% endif %}>
                        {% if row.kpis[k].delta_sign == 'pos' %}▲
                        {% elif row.kpis[k].delta_sign == 'neg' %}▼
                        {% endif %}
                        {{ row.kpis[k].delta }}
                    </span>
                    {% endfor %}
                </td>
                <td>
                    {% for k in kpi_keys %}
                    <span class="pulse-kpi-val" data-kpi="{{ k }}"
                          {% if k != 'revenue' %}style="display:none"{% endif %}>
                        {% if row.kpis[k].actual_pct is not none %}
                        <span class="pct-badge {{ pct_class(row.kpis[k].actual_pct) }}">
                            {{ row.kpis[k].actual_pct }}%
                        </span>
                        {% else %}
                        <span class="pulse-kpi-val-dash">—</span>
                        {% endif %}
                    </span>
                    {% endfor %}
                </td>
            </tr>
            {% endfor %}
        </tbody>
        <tfoot>
            <tr class="pulse-total-row">
                <td>CORPORATE TOTAL</td>
                <td>
                    {% for k in kpi_keys %}
                    <span class="pulse-kpi-val" data-kpi="{{ k }}"
                          {% if k != 'revenue' %}style="display:none"{% endif %}>
                        {{ weekly_pulse.total.kpis[k].committed }}
                    </span>
                    {% endfor %}
                </td>
                <td>
                    {% for k in kpi_keys %}
                    <span class="pulse-kpi-val" data-kpi="{{ k }}"
                          {% if k != 'revenue' %}style="display:none"{% endif %}>
                        {{ weekly_pulse.total.kpis[k].actual }}
                    </span>
                    {% endfor %}
                </td>
                <td>
                    {% for k in kpi_keys %}
                    <span class="pulse-kpi-val pulse-delta pulse-delta--{{ weekly_pulse.total.kpis[k].delta_sign }}"
                          data-kpi="{{ k }}"
                          {% if k != 'revenue' %}style="display:none"{% endif %}>
                        {% if weekly_pulse.total.kpis[k].delta_sign == 'pos' %}▲
                        {% elif weekly_pulse.total.kpis[k].delta_sign == 'neg' %}▼
                        {% endif %}
                        {{ weekly_pulse.total.kpis[k].delta }}
                    </span>
                    {% endfor %}
                </td>
                <td>
                    {% for k in kpi_keys %}
                    <span class="pulse-kpi-val" data-kpi="{{ k }}"
                          {% if k != 'revenue' %}style="display:none"{% endif %}>
                        {% if weekly_pulse.total.kpis[k].actual_pct is not none %}
                        <span class="pct-badge {{ pct_class(weekly_pulse.total.kpis[k].actual_pct) }}">
                            {{ weekly_pulse.total.kpis[k].actual_pct }}%
                        </span>
                        {% else %}
                        <span class="pulse-kpi-val-dash">—</span>
                        {% endif %}
                    </span>
                    {% endfor %}
                </td>
            </tr>
        </tfoot>
    </table>
</section>
```

- [ ] **Step 2: Add `last_updated` span inside company card header**

Find the company card header block:
```html
<div class="company-card-header">
    <span class="company-dot" style="background: {{ company.dot_color }}"></span>
    <span class="company-name">{{ company.name }}</span>
</div>
```

Replace with:
```html
<div class="company-card-header">
    <span class="company-dot" style="background: {{ company.dot_color }}"></span>
    <div class="company-name-block">
        <span class="company-name">{{ company.name }}</span>
        <span class="card-last-updated">Updated: {{ company.last_updated }}</span>
    </div>
</div>
```

- [ ] **Step 3: Add Print button to dashboard header**

Find the `<div class="header-right">` block:
```html
<div class="header-right">
    <span class="phase-badge">Phase 0 Mockup</span>
    <div class="time-filter" id="time-filter">
```

Replace with:
```html
<div class="header-right">
    <span class="phase-badge">Phase 0 Mockup</span>
    <button class="btn-print" onclick="printDashboard()">Print</button>
    <div class="time-filter" id="time-filter">
```

- [ ] **Step 4: Add Sticky Notes widget HTML**

Add this block just before `{% endblock %}` at the end of the template (before `{% block extra_js %}`):

```html
{# ── Sticky Notes widget ── #}
<div id="sticky-notes" class="sticky-notes sticky-notes--collapsed">
    <button class="sticky-notes-toggle" id="sticky-notes-toggle"
            onclick="toggleStickyNotes()" title="MD Notes">&#128221;</button>
    <div class="sticky-notes-panel" id="sticky-notes-panel">
        <div class="sticky-notes-header">MD Notes</div>
        <textarea id="sticky-notes-ta" rows="6"
                  placeholder="Quick reminders..."
                  oninput="updateStickyCharCount()"></textarea>
        <div class="sticky-notes-footer">
            <span id="sticky-notes-charcount">0 chars</span>
            <button onclick="saveStickyNotes()">Save</button>
        </div>
    </div>
</div>
```

- [ ] **Step 5: Commit**

```bash
git add app/templates/dashboard.html
git commit -m "[TASK-007] feat: update dashboard template — pulse KPI selector, last-updated, print button, sticky notes HTML"
```

---

## Task 4: Update script.js — three new functions

**Files:**
- Modify: `app/static/script.js`

- [ ] **Step 1: Append switchPulseKpi to script.js**

Add to the end of `app/static/script.js`:

```js
/* ── Weekly Pulse KPI selector ── */
function switchPulseKpi(kpi) {
    // Update active pill
    document.querySelectorAll('.pulse-kpi-pill').forEach(function(pill) {
        pill.classList.toggle('active', pill.textContent.trim().toLowerCase() === kpi);
    });
    // Show spans for selected KPI, hide others
    document.querySelectorAll('.pulse-kpi-val').forEach(function(span) {
        span.style.display = span.dataset.kpi === kpi ? '' : 'none';
    });
}

/* ── Sticky Notes widget ── */
(function initStickyNotes() {
    var saved = localStorage.getItem('md_notes');
    if (saved) {
        var ta = document.getElementById('sticky-notes-ta');
        if (ta) {
            ta.value = saved;
            updateStickyCharCount();
        }
    }
})();

function toggleStickyNotes() {
    var widget = document.getElementById('sticky-notes');
    if (widget) widget.classList.toggle('sticky-notes--collapsed');
}

function saveStickyNotes() {
    var ta = document.getElementById('sticky-notes-ta');
    if (ta) localStorage.setItem('md_notes', ta.value);
}

function updateStickyCharCount() {
    var ta = document.getElementById('sticky-notes-ta');
    var counter = document.getElementById('sticky-notes-charcount');
    if (ta && counter) counter.textContent = ta.value.length + ' chars';
}

/* ── Print / Export ── */
function printDashboard() {
    // Expand all detail panels
    document.querySelectorAll('.company-details').forEach(function(p) {
        p.classList.add('open');
    });
    // Switch all company KPI tabs to Revenue
    document.querySelectorAll('.kpi-tabs-container').forEach(function(container) {
        var id = container.id.replace('kpi-tabs-', '');
        switchKpiTab(id, 'revenue');
    });
    window.print();
}

window.onafterprint = function() {
    document.querySelectorAll('.company-details').forEach(function(p) {
        p.classList.remove('open');
    });
};
```

- [ ] **Step 2: Commit**

```bash
git add app/static/script.js
git commit -m "[TASK-007] feat: add switchPulseKpi, sticky notes JS, printDashboard"
```

---

## Task 5: Update style.css — four new blocks

**Files:**
- Modify: `app/static/style.css`

- [ ] **Step 1: Append all new CSS to the end of style.css**

```css
/* ── Weekly Pulse KPI selector pills ── */
.pulse-kpi-selector {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-bottom: 1rem;
}

.pulse-kpi-pill {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    padding: 0.3rem 0.75rem;
    border-radius: 20px;
    border: 1px solid var(--color-accent);
    background: transparent;
    color: var(--color-text-secondary);
    cursor: pointer;
    transition: background 0.15s, color 0.15s;
}

.pulse-kpi-pill.active,
.pulse-kpi-pill:hover {
    background: var(--color-accent);
    color: #000;
}

.pulse-kpi-val-dash {
    color: var(--color-text-secondary);
}

/* ── Company card last-updated ── */
.company-name-block {
    display: flex;
    flex-direction: column;
    gap: 0.1rem;
}

.card-last-updated {
    font-size: 0.6rem;
    color: var(--color-text-secondary);
    letter-spacing: 0.3px;
}

/* ── Print button ── */
.btn-print {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 0.3rem 0.75rem;
    border-radius: 4px;
    border: 1px solid var(--color-border);
    background: transparent;
    color: var(--color-text-secondary);
    cursor: pointer;
    transition: border-color 0.15s, color 0.15s;
}

.btn-print:hover {
    border-color: var(--color-accent);
    color: var(--color-accent);
}

/* ── Sticky Notes widget ── */
#sticky-notes {
    position: fixed;
    bottom: 1.5rem;
    right: 1.5rem;
    z-index: 1000;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 0.5rem;
}

.sticky-notes-toggle {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 1px solid var(--color-accent);
    background: var(--color-bg-surface);
    color: var(--color-accent);
    font-size: 1.1rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.15s;
}

.sticky-notes-toggle:hover {
    background: var(--color-accent);
    color: #000;
}

.sticky-notes-panel {
    width: 260px;
    background: #1c2330;
    border: 1px solid var(--color-accent);
    border-radius: 8px;
    padding: 0.75rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.sticky-notes--collapsed .sticky-notes-panel {
    display: none;
}

.sticky-notes-header {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--color-accent);
}

.sticky-notes-panel textarea {
    width: 100%;
    background: var(--color-bg-primary);
    border: 1px solid var(--color-border);
    border-radius: 4px;
    color: var(--color-text-primary);
    font-family: var(--font-body);
    font-size: 0.8rem;
    padding: 0.4rem;
    resize: vertical;
}

.sticky-notes-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.sticky-notes-footer span {
    font-size: 0.65rem;
    color: var(--color-text-secondary);
}

.sticky-notes-footer button {
    font-size: 0.7rem;
    font-weight: 600;
    padding: 0.2rem 0.6rem;
    border-radius: 4px;
    border: 1px solid var(--color-accent);
    background: transparent;
    color: var(--color-accent);
    cursor: pointer;
}

.sticky-notes-footer button:hover {
    background: var(--color-accent);
    color: #000;
}

/* ── @media print ── */
@media print {
    body {
        background: #fff !important;
        color: #000 !important;
    }

    .time-filter,
    .phase-badge,
    .btn-print,
    #sticky-notes,
    .btn-know-more,
    .pipeline-details-link {
        display: none !important;
    }

    .section {
        border: 1px solid #ccc !important;
        background: #fff !important;
        page-break-inside: avoid;
        margin-bottom: 1rem;
    }

    .company-details {
        display: block !important;
        max-height: none !important;
        overflow: visible !important;
    }

    .kpi-tab-panel {
        display: block !important;
    }

    .kpi-tab-strip {
        display: none !important;
    }

    .pct-badge {
        border: 1px solid #999;
    }

    a {
        text-decoration: none;
    }
}
```

- [ ] **Step 2: Commit**

```bash
git add app/static/style.css
git commit -m "[TASK-007] feat: add pulse KPI pills, sticky notes, print button, last-updated CSS"
```

---

## Task 6: Create stub API for PRODUCTION=0

**Files:**
- Create: `app/api/__init__.py`
- Create: `app/api/routes.py`
- Modify: `app/main.py`

- [ ] **Step 1: Create app/api/__init__.py**

```python
# app/api/__init__.py
```

(Empty file — makes `app/api` a Python package.)

- [ ] **Step 2: Create app/api/routes.py**

```python
# app/api/routes.py
# Stub routes for PRODUCTION=0 (Phase 1 -- not yet implemented).
# Returns a clear message so the developer knows to set PRODUCTION=1 for the mockup.

from fastapi import APIRouter

router = APIRouter()


@router.get("/{path:path}")
async def not_implemented(path: str):
    return {
        "status": "not implemented",
        "note": "set PRODUCTION=1 in .env to use the Phase 0 mockup",
        "path": path,
    }
```

- [ ] **Step 3: Wire stub router into main.py**

Find the PRODUCTION=0 branch in `app/main.py`:
```python
else:
    # Phase 1: Serve live API routes (not implemented yet)
    # from app.api import leads, finance, targets, companies, aging
    # app.include_router(leads.router, prefix="/api/leads")
    # ... etc
    pass
```

Replace with:
```python
else:
    # Phase 1: stub — returns JSON until real routes are built in s09-s14
    from app.api import routes as api_routes
    app.include_router(api_routes.router)
```

- [ ] **Step 4: Verify PRODUCTION=1 still works**

```bash
python -c "
import os; os.environ['PRODUCTION']='1'
from app.main import app
print('PRODUCTION=1 routes:', [r.path for r in app.routes])
"
```

Expected: list includes `/` (the mockup dashboard route).

- [ ] **Step 5: Commit**

```bash
git add app/api/__init__.py app/api/routes.py app/main.py
git commit -m "[TASK-007] feat: add stub API routes for PRODUCTION=0"
```

---

## Task 7: Create docs/HANDOFF.md

**Files:**
- Create: `docs/HANDOFF.md`

- [ ] **Step 1: Create docs/HANDOFF.md**

```markdown
# Developer Handoff — MD Dashboard . Fidelitus Corp

> Phase 0 mockup is complete. This document tells you everything you need to start Phase 1.

---

## a. How to Run the Mockup (PRODUCTION=1)

**Prerequisites:** Python 3.13, pip

```bash
# 1. Clone the repo and enter the project
cd D:/Fidelitus/mddb

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install fastapi uvicorn[standard] jinja2 python-dotenv pydantic-settings motor

# 4. Create .env (copy from .env.example)
cp .env.example .env
# Ensure PRODUCTION=1 is set

# 5. Run the server
uvicorn app.main:app --reload --port 8000

# 6. Open in browser
# http://localhost:8000
```

The dashboard loads with dummy data. No database connection required.

---

## b. Where Dummy Data Lives

All Phase 0 data is in **`app/mockup/dummy_data.py`**.

| Variable | Contents |
|---|---|
| `DASHBOARD_DATA` | Corporate KPIs + 6 company KPI cards + pipeline stages |
| `AGING_DATA` | Committed-but-delayed items per company per aging bucket |
| `KPI_DETAILS` | Drill-down rows per company per KPI tab (Revenue/Invoiced/Meetings/Proposals) |
| `KPI_AGING` | Committed-delayed items per company per KPI tab |
| `WEEKLY_PULSE` | Week-on-week committed vs actual per company per KPI |

The route that serves all this data: `app/mockup/routes.py` → GET `/`

---

## c. Where to Wire Real Data (Phase 1)

When `PRODUCTION=0`, real MongoDB data flows through:

```
app/data/<module>.py    ← query functions (Motor async)
app/api/<module>.py     ← FastAPI routers that call data functions
app/main.py             ← mounts api routers when PRODUCTION=0
app/templates/          ← same templates, same variable names
```

The templates expect the **same variable names** as the mockup routes pass.
Match these exactly when writing Phase 1 routes:

| Template variable | Mockup source | Phase 1 source |
|---|---|---|
| `data` | `DASHBOARD_DATA` | aggregated from MongoDB |
| `aging` | `AGING_DATA` | `app/data/aging.py` |
| `kpi_details` | `KPI_DETAILS` | `app/data/leads.py` + `app/data/finance.py` |
| `kpi_aging` | `KPI_AGING` | `app/data/aging.py` |
| `weekly_pulse` | `WEEKLY_PULSE` | `app/data/targets.py` |

---

## d. Session Map

| Session | Scope | Owner |
|---|---|---|
| s01–s07 | Phase 0 mockup (complete) | Srinivas |
| s08 | Read-only audit of all modules | Developer |
| s09 | `app/auth/` — CRM JWT authentication | Developer |
| s10 | `app/data/leads.py` + `app/api/leads.py` | Developer |
| s11 | `app/data/finance.py` + `app/api/finance.py` | Developer |
| s12 | `app/data/targets.py` + `app/api/targets.py` | Developer |
| s13 | `app/data/companies.py` + `app/api/companies.py` | Developer |
| s14 | `app/data/aging.py` + `app/api/aging.py` | Developer |
| s15 | `.env` + `app/main.py` — production cutover | Developer |

Start from **s08** (`tasks/TASK-008-db-audit.md` — to be created).

---

## e. MongoDB Collections → KPI Mapping

| Dashboard KPI | MongoDB Collection(s) | Key Fields |
|---|---|---|
| Revenue (Booking) | `deals` | `deal_value`, `status`, `closed_date` |
| Invoiced Amounts | `invoicereports` | `invoice_amount`, `invoice_date` |
| Payments Received | `invoicepayments`, `invoicepaymentshares` | `payment_amount`, `payment_date` |
| Meetings Done | `meetings` | `meeting_date`, `status` |
| Proposals Submitted | `mdfollowupproposals` | `proposal_date`, `amount` |
| Target for Year | `bdtargets`, `usertargets`, `employeetargets` | `target_amount`, `year` |
| Lead Pipeline | `leads`, `ftsleads`, `fidelitusleads` | `stage`, `source`, `created_at` |
| Aging (payments) | `invoicepayments` | `due_date`, `status` |
| Aging (pipeline) | `leads` | `stage`, `updated_at` |
| Department / Company master | `departments` | `company`, `department` |
| Users / Team | `users` | `name`, `department`, `role` |
| MD Follow-ups | `mdfollowups`, `mdassigntasks` | `follow_up_date`, `status` |
| Pipeline Stages master | `stages` | `stage_name`, `order` |

---

## f. CRM Auth Integration Points

The CRM uses **JWT tokens** stored in `user_access_tokens`.

Phase 1 auth flow (to be built in s09):
1. `POST /auth/login` → verify against `users` collection → issue JWT
2. All dashboard routes require `Authorization: Bearer <token>` header
3. `app/auth/middleware.py` decodes JWT on each request
4. MD role check: `user.role == 'md'` or equivalent from `roles` / `user_roles`

Files to create in s09:
- `app/auth/__init__.py`
- `app/auth/middleware.py` — JWT decode + role check
- `app/auth/routes.py` — login endpoint

---

## g. ENV Variables (.env.example)

```bash
# .env.example — copy to .env and fill in values

# Phase flag
# "1" = Phase 0 mockup (dummy data, no DB)
# "0" = Phase 1 live (MongoDB + CRM auth)
PRODUCTION=1

# MongoDB (Phase 1 only — leave blank for Phase 0)
MONGO_URI=mongodb://localhost:27017
DB_NAME=fidelitus

# JWT Secret (Phase 1 only)
SECRET_KEY=replace-with-a-random-secret-key
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=480
```

---

## h. Design Constraints

These are fixed. Do not change them without MD approval.

| Constraint | Value |
|---|---|
| JS framework | None — vanilla JS only |
| CSS framework | None — custom CSS only |
| Background | `#0d1117` |
| Surface | `#161b22` |
| Accent | `#e8a838` (amber) |
| Body font | DM Sans |
| Heading font | Syne |
| KPI color: < 25% | `#ef4444` (bright red) |
| KPI color: 26–50% | `#f97316` (red-orange) |
| KPI color: 51–75% | `#f59e0b` (amber) |
| KPI color: > 75% | `#22c55e` (green) |
| Aging buckets | 7d · 14d · 21d · 90d · NPA (>90d) |

Design reference: `md_dashboard_v2.html` in project root.
```

- [ ] **Step 2: Commit**

```bash
git add docs/HANDOFF.md
git commit -m "[TASK-007] docs: add developer handoff document"
```

---

## Task 8: Final smoke test

- [ ] **Step 1: Start the server**

```bash
uvicorn app.main:app --reload --port 8000
```

Expected: `INFO: Application startup complete.`

- [ ] **Step 2: Open http://localhost:8000 and verify each item**

Check these manually in the browser:

| Item | Expected |
|---|---|
| Dashboard loads | No 500 errors, all sections visible |
| Weekly Pulse KPI pills | Clicking Invoiced/Payments/etc. swaps all data columns |
| Weekly Pulse color badges | Red for HR Labs (20%), green for Transactions revenue (109%) |
| Sticky Notes icon (bottom-right) | Amber notepad icon visible |
| Sticky Notes — open | Click icon → panel expands with textarea |
| Sticky Notes — save + reload | Type a note, Save, reload page → note persists |
| Last Updated on cards | Shown below each company name (e.g. "Updated: 25 Apr 2026, 9:30 AM") |
| Print button in header | Visible, click → all panels expand → print dialog opens |
| After print dialog closes | Panels collapse back |
| Corporate aging | Click any KPI card → aging panel opens |
| Company Know More | Opens KPI tabs panel |
| Pipeline Details | Opens per-stage aging panel |

- [ ] **Step 3: Verify PRODUCTION=0 stub**

Temporarily set `PRODUCTION=0` in `.env`, restart server, visit `http://localhost:8000/anything`.

Expected response:
```json
{"status": "not implemented", "note": "set PRODUCTION=1 in .env to use the Phase 0 mockup", "path": "anything"}
```

Restore `PRODUCTION=1` in `.env` before committing.

- [ ] **Step 4: Final commit**

```bash
git add -A
git commit -m "[TASK-007] chore: s07 complete — mockup polish and developer handoff"
```

- [ ] **Step 5: Create PR**

```bash
git push -u origin feature/TASK-007-mockup-polish
gh pr create \
  --title "[TASK-007] s07 Mockup Polish & Developer Handoff" \
  --body "## Summary
- Expand Weekly Pulse to all 6 KPIs with pill selector
- Add Sticky Notes widget (localStorage, bottom-right)
- Add Last Updated timestamp on company cards
- Add Print/Export view with @media print stylesheet
- Add stub API routes for PRODUCTION=0
- Add docs/HANDOFF.md for developer onboarding

## Test plan
- [ ] WTD Weekly Pulse: click each KPI pill, verify data + color coding changes
- [ ] Sticky Notes: open, type, save, reload — note persists
- [ ] Last Updated visible on all 6 company cards
- [ ] Print button: panels open, print dialog triggers, panels close after
- [ ] PRODUCTION=0: stub returns JSON (not blank page)
- [ ] All existing panels still work (corporate aging, company KPI tabs, pipeline)"
```
```

- [ ] **Step 6: Update memory — project status**

After PR is merged, update `C:\Users\K S S\.claude\projects\D--Fidelitus-mddb\memory\project_status.md`:
- s07 done (PR merged)
- Phase 0 mockup complete
- Next: s08 db-audit (Phase 1 start, developer takes over)
