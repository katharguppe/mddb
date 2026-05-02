# Weekly Pulse Panel Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Weekly Pulse section showing committed-vs-actual revenue delta for the MD's review meeting, visible only on the WTD time filter.

**Architecture:** All data lives in `dummy_data.py` as a `WEEKLY_PULSE` dict; `routes.py` passes it to Jinja2; `dashboard.html` renders a comparison table and a new time-filter pill strip in the header; `style.css` and `script.js` handle show/hide logic. No new files, no new routes, no new partials.

**Tech Stack:** Python 3.13, FastAPI, Jinja2, vanilla HTML/CSS/JS

**Spec:** `docs/superpowers/specs/2026-05-02-weekly-pulse-design.md`

---

## File Map

| File | Change |
|------|--------|
| `app/mockup/dummy_data.py` | Add `WEEKLY_PULSE` dict at bottom |
| `app/mockup/routes.py` | Import `WEEKLY_PULSE`; add to template context |
| `app/templates/dashboard.html` | Wrap header right-side; add time-filter pills; insert Weekly Pulse section |
| `app/static/style.css` | Add `.header-right`, `.time-filter`, `.tf-pill`, `.weekly-pulse-section`, `.pulse-table` rules |
| `app/static/script.js` | Add `setTimePeriod()` function; call it on load |

---

## Task 1: Add WEEKLY_PULSE data to dummy_data.py

**Files:**
- Modify: `app/mockup/dummy_data.py` — append `WEEKLY_PULSE` dict after `KPI_AGING`

- [ ] **Step 1: Append WEEKLY_PULSE to the bottom of dummy_data.py**

Open `app/mockup/dummy_data.py` and add at the very end:

```python
# Weekly Pulse: committed (Mon) vs actual (Fri) revenue for the current review week.
# actual_pct = round(actual / committed * 100). Status colors via pct_class macro.
WEEKLY_PULSE = {
    "week_label":      "Week of 21 Apr – 25 Apr 2026",
    "committed_label": "Last committed: Mon 21 Apr",
    "rows": [
        {
            "id":         "transactions",
            "name":       "Fidelitus Transactions",
            "committed":  "Rs.9 Cr",
            "actual":     "Rs.9.8 Cr",
            "delta":      "+0.8 Cr",
            "delta_sign": "pos",
            "actual_pct": 109,
        },
        {
            "id":         "projects",
            "name":       "Fidelitus Projects",
            "committed":  "Rs.4 Cr",
            "actual":     "Rs.1.8 Cr",
            "delta":      "−2.2 Cr",
            "delta_sign": "neg",
            "actual_pct": 45,
        },
        {
            "id":         "fms",
            "name":       "Fidelitus FMS",
            "committed":  "Rs.2.5 Cr",
            "actual":     "Rs.2.1 Cr",
            "delta":      "−0.4 Cr",
            "delta_sign": "neg",
            "actual_pct": 84,
        },
        {
            "id":         "hrlabs",
            "name":       "Fidelitus HR Labs",
            "committed":  "Rs.1.5 Cr",
            "actual":     "Rs.0.3 Cr",
            "delta":      "−1.2 Cr",
            "delta_sign": "neg",
            "actual_pct": 20,
        },
        {
            "id":         "technology",
            "name":       "Fidelitus Technology",
            "committed":  "Rs.1.2 Cr",
            "actual":     "Rs.0.5 Cr",
            "delta":      "−0.7 Cr",
            "delta_sign": "neg",
            "actual_pct": 42,
        },
        {
            "id":         "gcc",
            "name":       "Fidelitus GCC Nexus",
            "committed":  "Rs.0.5 Cr",
            "actual":     "Rs.0.05 Cr",
            "delta":      "−0.45 Cr",
            "delta_sign": "neg",
            "actual_pct": 10,
        },
    ],
    "total": {
        "committed":  "Rs.18.7 Cr",
        "actual":     "Rs.14.55 Cr",
        "delta":      "−4.15 Cr",
        "delta_sign": "neg",
        "actual_pct": 78,
    },
}
```

- [ ] **Step 2: Verify file is valid Python**

```bash
cd D:/Fidelitus/mddb
python -c "from app.mockup.dummy_data import WEEKLY_PULSE; print(len(WEEKLY_PULSE['rows']), 'rows')"
```

Expected output: `6 rows`

- [ ] **Step 3: Commit**

```bash
git add app/mockup/dummy_data.py
git commit -m "[TASK-006] feat: add WEEKLY_PULSE dummy data"
```

---

## Task 2: Wire WEEKLY_PULSE into routes.py

**Files:**
- Modify: `app/mockup/routes.py` — import `WEEKLY_PULSE`; add to template context

- [ ] **Step 1: Update the import line**

In `app/mockup/routes.py`, change line 7 from:

```python
from app.mockup.dummy_data import DASHBOARD_DATA, AGING_DATA, KPI_DETAILS, KPI_AGING
```

to:

```python
from app.mockup.dummy_data import DASHBOARD_DATA, AGING_DATA, KPI_DETAILS, KPI_AGING, WEEKLY_PULSE
```

- [ ] **Step 2: Add weekly_pulse to the template context dict**

Change the `TemplateResponse` call (lines 18–21) from:

```python
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "data": DASHBOARD_DATA, "aging": AGING_DATA, "kpi_details": KPI_DETAILS, "kpi_aging": KPI_AGING},
    )
```

to:

```python
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request":      request,
            "data":         DASHBOARD_DATA,
            "aging":        AGING_DATA,
            "kpi_details":  KPI_DETAILS,
            "kpi_aging":    KPI_AGING,
            "weekly_pulse": WEEKLY_PULSE,
        },
    )
```

- [ ] **Step 3: Verify the server starts without errors**

```bash
cd D:/Fidelitus/mddb
uvicorn app.main:app --reload --port 8000
```

Expected: server starts, no import errors in the terminal.
Stop with Ctrl+C after confirming.

- [ ] **Step 4: Commit**

```bash
git add app/mockup/routes.py
git commit -m "[TASK-006] feat: pass weekly_pulse to dashboard template"
```

---

## Task 3: Add time-filter pills and Weekly Pulse section to dashboard.html

**Files:**
- Modify: `app/templates/dashboard.html`

### 3a — Wrap the header right side

- [ ] **Step 1: Replace the lone phase-badge span in the header**

In `app/templates/dashboard.html`, find the header block (lines 18–24):

```html
<header class="dashboard-header">
    <div>
        <p class="dashboard-eyebrow">Fidelitus Corp . MD Dashboard</p>
        <h1 class="dashboard-title">Consolidated View</h1>
    </div>
    <span class="phase-badge">Phase 0 Mockup</span>
</header>
```

Replace with:

```html
<header class="dashboard-header">
    <div>
        <p class="dashboard-eyebrow">Fidelitus Corp . MD Dashboard</p>
        <h1 class="dashboard-title">Consolidated View</h1>
    </div>
    <div class="header-right">
        <span class="phase-badge">Phase 0 Mockup</span>
        <div class="time-filter" id="time-filter">
            <button class="tf-pill active" onclick="setTimePeriod('WTD')">WTD</button>
            <button class="tf-pill"        onclick="setTimePeriod('MTD')">MTD</button>
            <button class="tf-pill"        onclick="setTimePeriod('QTD')">QTD</button>
            <button class="tf-pill"        onclick="setTimePeriod('YTD')">YTD</button>
        </div>
    </div>
</header>
```

### 3b — Insert the Weekly Pulse section

- [ ] **Step 2: Add the Weekly Pulse section between Section A and Section B**

In `app/templates/dashboard.html`, find the comment that starts Section B:

```html
    {# ── Section B: Company Cards ── #}
```

Insert the following block immediately **before** that line:

```html
    {# ── Section W: Weekly Pulse ── #}
    <section class="section weekly-pulse-section" id="weekly-pulse-section">
        <div class="section-label">
            Weekly Pulse
            <span class="pulse-week-meta">
                {{ weekly_pulse.week_label }} &nbsp;·&nbsp; {{ weekly_pulse.committed_label }}
            </span>
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
                {% for row in weekly_pulse.rows %}
                <tr class="pulse-row pulse-row--clickable"
                    onclick="toggleDetails('{{ row.id }}')">
                    <td>{{ row.name }}</td>
                    <td>{{ row.committed }}</td>
                    <td>{{ row.actual }}</td>
                    <td class="pulse-delta pulse-delta--{{ row.delta_sign }}">
                        {% if row.delta_sign == 'pos' %}▲{% else %}▼{% endif %}
                        {{ row.delta }}
                    </td>
                    <td>
                        <span class="pct-badge {{ pct_class(row.actual_pct) }}">
                            {{ row.actual_pct }}%
                        </span>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
            <tfoot>
                <tr class="pulse-total-row">
                    <td>CORPORATE TOTAL</td>
                    <td>{{ weekly_pulse.total.committed }}</td>
                    <td>{{ weekly_pulse.total.actual }}</td>
                    <td class="pulse-delta pulse-delta--{{ weekly_pulse.total.delta_sign }}">
                        {% if weekly_pulse.total.delta_sign == 'pos' %}▲{% else %}▼{% endif %}
                        {{ weekly_pulse.total.delta }}
                    </td>
                    <td>
                        <span class="pct-badge {{ pct_class(weekly_pulse.total.actual_pct) }}">
                            {{ weekly_pulse.total.actual_pct }}%
                        </span>
                    </td>
                </tr>
            </tfoot>
        </table>
    </section>

```

- [ ] **Step 3: Commit**

```bash
git add app/templates/dashboard.html
git commit -m "[TASK-006] feat: add time-filter pills and Weekly Pulse section to dashboard"
```

---

## Task 4: Add CSS for time-filter and pulse table

**Files:**
- Modify: `app/static/style.css` — append new rule blocks at the end of the file

- [ ] **Step 1: Append the following CSS to the end of app/static/style.css**

```css
/* ── Header right column (phase badge + time-filter) ── */
.header-right {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 0.5rem;
}

/* ── Time-filter pill strip ── */
.time-filter {
    display: flex;
    gap: 0.25rem;
}

.tf-pill {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 0.2rem 0.6rem;
    border-radius: 4px;
    border: 1px solid var(--color-border);
    background: transparent;
    color: var(--color-text-secondary);
    cursor: pointer;
    transition: background 0.15s, color 0.15s, border-color 0.15s;
}

.tf-pill.active,
.tf-pill:hover {
    background: var(--color-accent);
    color: #0d1117;
    border-color: var(--color-accent);
}

/* ── Weekly Pulse section visibility ── */
.weekly-pulse-section.hidden {
    display: none;
}

/* ── Pulse section meta text (week / committed date) ── */
.pulse-week-meta {
    font-size: 0.7rem;
    color: var(--color-text-secondary);
    letter-spacing: 0;
    text-transform: none;
    font-weight: 400;
}

/* ── Pulse comparison table ── */
.pulse-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.875rem;
}

.pulse-table th {
    text-align: left;
    font-size: 0.65rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: var(--color-text-secondary);
    padding: 0.5rem 0.75rem;
    border-bottom: 1px solid var(--color-border);
}

.pulse-table td {
    padding: 0.6rem 0.75rem;
    border-bottom: 1px solid rgba(48, 54, 61, 0.5);
    color: var(--color-text-primary);
}

.pulse-row--clickable {
    cursor: pointer;
    transition: background 0.15s;
}

.pulse-row--clickable:hover {
    background: rgba(255, 255, 255, 0.03);
}

.pulse-delta--pos { color: var(--color-green); font-weight: 600; }
.pulse-delta--neg { color: var(--color-red);   font-weight: 600; }

.pulse-total-row td {
    font-weight: 700;
    border-top: 1px solid var(--color-border);
    border-bottom: none;
    color: var(--color-text-primary);
}
```

- [ ] **Step 2: Commit**

```bash
git add app/static/style.css
git commit -m "[TASK-006] feat: add time-filter and weekly pulse table CSS"
```

---

## Task 5: Add setTimePeriod() to script.js

**Files:**
- Modify: `app/static/script.js` — append `setTimePeriod` function; call it on load via dashboard.html

- [ ] **Step 1: Append setTimePeriod to app/static/script.js**

Add the following block at the end of `app/static/script.js`:

```js
/* ── Time-period filter ── */
function setTimePeriod(period) {
    // Update active pill
    document.querySelectorAll('.tf-pill').forEach(function(pill) {
        pill.classList.toggle('active', pill.textContent.trim() === period);
    });

    // Show Weekly Pulse only on WTD
    var pulse = document.getElementById('weekly-pulse-section');
    if (pulse) {
        pulse.classList.toggle('hidden', period !== 'WTD');
    }
}
```

- [ ] **Step 2: Call setTimePeriod on page load**

In `app/templates/dashboard.html`, find the `extra_js` block at the bottom:

```html
{% block extra_js %}
<script src="{{ url_for('static', path='script.js') }}"></script>
{% endblock %}
```

Replace with:

```html
{% block extra_js %}
<script src="{{ url_for('static', path='script.js') }}"></script>
<script>setTimePeriod('WTD');</script>
{% endblock %}
```

- [ ] **Step 3: Commit**

```bash
git add app/static/script.js app/templates/dashboard.html
git commit -m "[TASK-006] feat: add setTimePeriod JS and WTD init call"
```

---

## Task 6: Manual verification

- [ ] **Step 1: Start the server**

```bash
cd D:/Fidelitus/mddb
uvicorn app.main:app --reload --port 8000
```

Open `http://localhost:8000` in a browser.

- [ ] **Step 2: Verify the header**

- Phase badge visible top-right
- WTD / MTD / QTD / YTD pills visible below it
- WTD pill is amber/highlighted on load

- [ ] **Step 3: Verify the Weekly Pulse table**

- Table visible between Corporate KPIs and Subsidiaries sections
- Header reads "Week of 21 Apr – 25 Apr 2026  ·  Last committed: Mon 21 Apr"
- 6 company rows present with correct committed/actual/delta values
- Corporate Total row at the bottom, bold
- Delta column: green ▲ for Transactions; red ▼ for all others
- Status badges: Transactions green (109%); Projects red-orange (45%); FMS green (84%); HR Labs bright-red (20%); Technology red-orange (42%); GCC red (10%); Total green (78%)

- [ ] **Step 4: Verify filter toggling**

- Click MTD → Weekly Pulse section disappears
- Click QTD → Weekly Pulse section stays hidden
- Click YTD → Weekly Pulse section stays hidden
- Click WTD → Weekly Pulse section reappears

- [ ] **Step 5: Verify row click drill-down**

- Click any company row in the pulse table
- The matching company card in Section B expands its aging panel
- Clicking the same row again closes it

- [ ] **Step 6: Final commit**

```bash
git add -A
git commit -m "[TASK-006] chore: TASK-006 complete — Weekly Pulse panel"
```

---

## Self-Review Notes

- All 5 spec requirements covered: data, route wiring, header pills, pulse table, JS toggle.
- `pct_class` macro is defined in `dashboard.html` lines 9–16 — used in the pulse table without redefinition. ✓
- `toggleDetails(id)` is defined in `script.js` line 3 — reused in pulse row `onclick`. ✓
- `delta_sign` values `"pos"` / `"neg"` used consistently in `dummy_data.py`, Jinja2 template, and CSS classes. ✓
- No new files, no new partials, no new routes. ✓
- Corporate Total row has no `onclick` — intentional, consistent with spec. ✓
