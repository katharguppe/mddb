# s07 Mockup Polish — Design Spec
**Date:** 2026-05-02
**Session:** s07
**Branch:** feature/TASK-007-mockup-polish
**Scope:** app/mockup/, app/templates/, app/static/, app/api/, docs/

---

## 1. Carry-over: Weekly Pulse — All 6 KPIs

### Problem
Weekly Pulse (Section W) currently shows Revenue only. The MD requires all 6 KPIs visible:
Revenue · Invoiced · Payments · Meetings · Proposals · Target.

### Design

**dummy_data.py — WEEKLY_PULSE structure change**
Each row in `WEEKLY_PULSE["rows"]` gains a `kpis` dict keyed by KPI slug:

```python
"kpis": {
    "revenue":   {"committed": "Rs.9 Cr",  "actual": "Rs.9.8 Cr", "delta": "+0.8 Cr", "delta_sign": "pos", "actual_pct": 109},
    "invoiced":  {"committed": "Rs.7 Cr",  "actual": "Rs.6.5 Cr", "delta": "−0.5 Cr", "delta_sign": "neg", "actual_pct": 93},
    "payments":  {"committed": "Rs.5 Cr",  "actual": "Rs.4.2 Cr", "delta": "−0.8 Cr", "delta_sign": "neg", "actual_pct": 84},
    "meetings":  {"committed": "45",        "actual": "48",         "delta": "+3",       "delta_sign": "pos", "actual_pct": 107},
    "proposals": {"committed": "20",        "actual": "15",         "delta": "−5",       "delta_sign": "neg", "actual_pct": 75},
    "target":    {"committed": "Rs.80 Cr", "actual": "—",          "delta": "—",        "delta_sign": "neu", "actual_pct": None},
}
```

Top-level `WEEKLY_PULSE["total"]` also gains a `kpis` dict with the same shape for the CORPORATE TOTAL row.

The old flat fields (`committed`, `actual`, `delta`, `delta_sign`, `actual_pct`) on each row are removed and replaced entirely by the nested `kpis` dict.

**dashboard.html — KPI selector row above the pulse table**
A pill-tab row above `<table class="pulse-table">`:
```html
<div class="pulse-kpi-selector" id="pulse-kpi-selector">
  <button class="pulse-kpi-pill active" onclick="switchPulseKpi('revenue')">Revenue</button>
  <button class="pulse-kpi-pill" onclick="switchPulseKpi('invoiced')">Invoiced</button>
  <button class="pulse-kpi-pill" onclick="switchPulseKpi('payments')">Payments</button>
  <button class="pulse-kpi-pill" onclick="switchPulseKpi('meetings')">Meetings</button>
  <button class="pulse-kpi-pill" onclick="switchPulseKpi('proposals')">Proposals</button>
  <button class="pulse-kpi-pill" onclick="switchPulseKpi('target')">Target</button>
</div>
```

Table `<td>` cells for Committed/Actual/Delta/Status are rendered per-KPI using Jinja2 data attributes:
```html
<td data-kpi="revenue">{{ row.kpis.revenue.committed }}</td>
<td data-kpi="invoiced" class="hidden">{{ row.kpis.invoiced.committed }}</td>
...
```

**script.js — switchPulseKpi(kpi)**
```js
function switchPulseKpi(kpi) {
    // Update active pill
    document.querySelectorAll('.pulse-kpi-pill').forEach(p =>
        p.classList.toggle('active', p.textContent.trim().toLowerCase() === kpi));
    // Show/hide data columns
    document.querySelectorAll('[data-kpi]').forEach(td =>
        td.classList.toggle('hidden', td.dataset.kpi !== kpi));
}
```

Default call: `switchPulseKpi('revenue')` in the page init block.

**style.css — pulse-kpi-selector styles**
Pills styled identically to `.tf-pill` (the time-filter pills) but amber-accented to distinguish from the WTD/MTD filter row.

---

## 2. Sticky Notes Widget

### Design
Fixed bottom-right overlay. Two states: collapsed (icon) and expanded (textarea panel).

**HTML** (appended to `base.html` `<body>` or injected via `dashboard.html` extra block):
```html
<div id="sticky-notes" class="sticky-notes-collapsed">
  <button id="sticky-notes-toggle" onclick="toggleStickyNotes()" title="MD Notes">&#128221;</button>
  <div id="sticky-notes-panel">
    <div class="sticky-notes-header">MD Notes</div>
    <textarea id="sticky-notes-ta" rows="6" placeholder="Quick reminders..."></textarea>
    <div class="sticky-notes-footer">
      <span id="sticky-notes-charcount">0 chars</span>
      <button onclick="saveStickyNotes()">Save</button>
    </div>
  </div>
</div>
```

**JS** (~30 lines in `script.js`):
- `toggleStickyNotes()` — toggles `.sticky-notes-collapsed`
- `saveStickyNotes()` — writes `localStorage.setItem('md_notes', value)`
- On page load: reads `localStorage.getItem('md_notes')` and populates textarea
- Textarea `oninput` updates char count

**CSS**: fixed position `bottom: 1.5rem; right: 1.5rem; z-index: 1000`. Collapsed = icon button only (40×40px, amber). Expanded = 260×220px surface, `background: #1c2330`, `border: 1px solid var(--color-accent)`, border-radius 8px.

---

## 3. Last Updated Timestamp on Company Cards

### Design
Each company in `DASHBOARD_DATA["companies"]` gets a new field:
```python
"last_updated": "25 Apr 2026, 9:30 AM"
```

Template adds one line below the company name in `.company-card-header`:
```html
<span class="card-last-updated">Updated: {{ company.last_updated }}</span>
```

CSS: `font-size: 0.65rem; color: var(--color-text-secondary); letter-spacing: 0.5px;`

---

## 4. Print / Export View

### Design

**Header button** (added to dashboard header, next to `.phase-badge`):
```html
<button class="btn-print" onclick="printDashboard()">Print</button>
```

**script.js — printDashboard()**
```js
function printDashboard() {
    // Expand all panels
    document.querySelectorAll('.company-details').forEach(p => p.classList.add('open'));
    // Open Revenue tab for each company (no hardcoded slugs)
    document.querySelectorAll('.kpi-tabs-container').forEach(function(container) {
        var id = container.id.replace('kpi-tabs-', '');
        switchKpiTab(id, 'revenue');
    });
    window.print();
}
window.onafterprint = function() {
    // Collapse all panels back
    document.querySelectorAll('.company-details').forEach(p => p.classList.remove('open'));
};
```

**style.css — @media print block**
```css
@media print {
    body { background: #fff; color: #000; }
    .time-filter, .phase-badge, .btn-print, .sticky-notes-collapsed,
    .btn-know-more, .pipeline-details-link { display: none !important; }
    .section { border: 1px solid #ccc; page-break-inside: avoid; }
    .company-details { display: block !important; max-height: none !important; overflow: visible !important; }
    .kpi-tab-panel { display: block !important; }
}
```

---

## 5. ENV Flag Validation — Stub API

### Files to create

**app/api/__init__.py** — empty

**app/api/routes.py**:
```python
from fastapi import APIRouter
router = APIRouter()

@router.get("/{path:path}")
async def not_implemented(path: str):
    return {"status": "not implemented", "note": "set PRODUCTION=1 for mockup"}
```

**app/main.py** — wire in PRODUCTION=0 branch:
```python
else:
    from app.api import routes as api_routes
    app.include_router(api_routes.router)
```

This ensures PRODUCTION=0 serves a JSON stub instead of a blank page.

---

## 6. Developer Handoff Document

**File:** `docs/HANDOFF.md`

Sections:
a. How to run the mockup (PRODUCTION=1, uvicorn command, browser URL)
b. Dummy data location (app/mockup/dummy_data.py) — data structures explained
c. Where to wire real data (app/api/ + app/data/ — s09–s14 sessions)
d. Session map: s08 audit → s09 auth → s10 leads → s11 finance → s12 targets → s13 companies → s14 aging → s15 cutover
e. MongoDB collections → KPI mapping table (all 20 collections from CLAUDE.md)
f. CRM auth integration points (app/auth/ to be built in s09; JWT via user_access_tokens)
g. .env.example template (PRODUCTION, MONGO_URI, SECRET_KEY, DB_NAME)
h. Design constraints (no framework, dark theme, DM Sans + Syne, color rules, amber accent)

---

## 7. Final Smoke Test

Run: `uvicorn app.main:app --reload --port 8000`
Verify:
- Dashboard loads at http://localhost:8000
- Weekly Pulse KPI selector switches all 6 KPIs
- Sticky Notes widget opens, saves, persists on reload
- Last Updated shown on all 6 company cards
- Print button triggers print with all panels open
- Color coding correct on all KPI badges
- Corporate aging, company KPI tabs, pipeline aging — all interactive

---

## Implementation Order

1. Create `tasks/TASK-007-mockup-polish.md`
2. Extend `WEEKLY_PULSE` dummy data (all 6 KPIs per company)
3. Update `dashboard.html` — pulse KPI selector + data-kpi attributes
4. Update `script.js` — `switchPulseKpi`, sticky notes JS, `printDashboard`
5. Update `style.css` — pulse-kpi-selector, sticky notes, @media print, last-updated
6. Update `dummy_data.py` companies — add `last_updated` field
7. Update `dashboard.html` — last-updated span, sticky notes HTML, Print button
8. Create `app/api/__init__.py` + `app/api/routes.py`
9. Update `app/main.py` — wire stub API
10. Create `docs/HANDOFF.md`
11. Smoke test
