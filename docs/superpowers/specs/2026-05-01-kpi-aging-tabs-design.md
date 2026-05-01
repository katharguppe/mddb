# Design Spec — KPI Aging Tabs in Company Know More Panels (TASK-006)
Date: 2026-05-01
Session: s05 continuation (Phase 0 mockup)

## Goal

Replace the single flat aging panel inside each company card's "Know More" slide-down
with a two-level drill: first select the KPI type, then select the time bucket.
Corporate aging panel (Section A) and pipeline aging panels (Section C) are NOT changed.

## Scope

Files to touch:
- `app/mockup/dummy_data.py`   — restructure 6 company AGING entries + add pipeline dummy data
- `app/templates/partials/aging_panel.html`  — add new `kpi_aging_panel` macro
- `app/static/script.js`       — add `toggleAgingKpi()`, update `resetAgingPills()`
- `app/static/style.css`       — add `.aging-kpi-tab` styles
- `app/templates/dashboard.html` — company card calls `kpi_aging_panel()` instead of `aging_panel()`

Files NOT touched:
- `app/mockup/routes.py` — unchanged
- Corporate aging panel in dashboard.html — unchanged (calls `aging_panel()`)
- Pipeline aging panels in dashboard.html — unchanged (calls `aging_panel()`)

## UI Interaction (company Know More only)

```
Annual Target: Rs.80 Cr

[ Revenue ] [ Invoiced ] [ Payments ] [ Meetings ] [ Proposals ]   ← KPI tab row
      ↓ click a tab
[ 7 Days ] [ 14 Days ] [ 21 Days ] [ 90 Days ] [ NPA ]             ← bucket pills
      ↓ click a pill
  Table: Company/Team | Member | Value | Days | Reason
```

- Default: Revenue tab active, no bucket pre-selected
- Clicking a different KPI tab resets bucket pills for that KPI
- Clicking the same KPI tab again collapses (deselects)
- Meetings / Proposals items: value column shows "—" (count-based, no Rs)

## Data Structure Change (company entries only)

### Current (2-level):
```python
AGING_DATA["transactions"] = {
    "7d":  {"count": 3, "total": "Rs.2.1 Cr", "items": [...]},
    "14d": {...}, "21d": {...}, "90d": {...}, "npa": {...}
}
```

### New (3-level):
```python
AGING_DATA["transactions"] = {
    "revenue": {
        "7d":  {"count": 1, "total": "Rs.1.2 Cr", "items": [...]},
        "14d": {"count": 1, "total": "Rs.0.9 Cr", "items": [...]},
        "21d": {"count": 0, "total": "Rs.0", "items": []},
        "90d": {"count": 0, "total": "Rs.0", "items": []},
        "npa": {"count": 0, "total": "Rs.0", "items": []},
    },
    "invoiced": { ... same 5 buckets ... },
    "payments": { ... same 5 buckets ... },   # existing items move here
    "meetings": { ... same 5 buckets, value="—" ... },
    "proposals": { ... same 5 buckets ... },
}
```

All 6 company slugs restructured. AGING_DATA["corporate"] stays 2-level (untouched).
AGING_DATA["pipeline_*"] stays 2-level (pipeline dummy data added separately).

`_build_corporate_aging()` updated to iterate the new 3-level structure — flatten
across all KPIs from all companies per time bucket.

## Existing Data Migration

Current payment-type items in AGING_DATA move under the "payments" KPI key.
New items added for "revenue", "invoiced", "meetings", "proposals" KPIs.

### Required dummy data per company × KPI

At minimum, the following buckets must be non-empty so the tabs are useful:

**Fidelitus Transactions:**
- revenue 7d: 1 item, 14d: 1 item
- invoiced 7d: 1 item, 14d: 1 item
- payments 7d/14d/21d/90d/npa: existing items moved here
- meetings 7d: 1 item (count delayed, value="—")
- proposals 7d: 1 item

**Other 5 companies:** At least 1 item per KPI in 7d or 14d bucket.
Meetings and proposals use value="—" and count-based descriptions.

## New Macro: `kpi_aging_panel(company_id, aging)`

Added to `app/templates/partials/aging_panel.html` alongside the existing `aging_panel` macro.

```
KPI_TABS = [
    ("revenue",   "Revenue"),
    ("invoiced",  "Invoiced"),
    ("payments",  "Payments"),
    ("meetings",  "Meetings"),
    ("proposals", "Proposals"),
]
```

Renders:
1. KPI tab row — buttons with class `aging-kpi-tab`, data-company + data-kpi attrs
2. Per-KPI: a div containing the 5 bucket pills + tables (hidden until tab active)
   - Pills: `id="aging-pills-{company_id}-{kpi}"`
   - Tables: `id="aging-table-{company_id}-{kpi}-{bucket}"`

## ID Scheme

| Element | ID pattern |
|---|---|
| KPI tabs container | `aging-kpis-{company_id}` |
| KPI tab button | `data-company="{id}" data-kpi="{kpi}"` |
| Bucket pills container | `aging-pills-{company_id}-{kpi}` |
| Detail table | `aging-table-{company_id}-{kpi}-{bucket}` |
| Per-KPI content div | `aging-kpi-content-{company_id}-{kpi}` |

## JS Changes (script.js)

New function:
```javascript
function toggleAgingKpi(companyId, kpi) {
    // 1. If already active: deselect all → collapse
    // 2. Else: deselect all, activate selected tab, show its bucket pills div
    // 3. Reset bucket pills for newly activated KPI
}
```

Updated `resetAgingPills(companyId)` → `resetAgingPills(companyId, kpi)`:
- Resets pills + tables for a specific KPI only
- Used by both `toggleAgingKpi` and `toggleAgingBucket`

`toggleAgingBucket(companyId, bucket)` → `toggleAgingBucket(companyId, kpi, bucket)`:
- Now requires kpi param to build correct element IDs

## CSS Additions (style.css)

```
.aging-kpi-tabs       — flex row, gap, margin-bottom, border-bottom separator
.aging-kpi-tab        — similar to .aging-pill but wider, horizontal text
.aging-kpi-tab.active — amber border + amber text (same as .aging-pill.active)
.aging-kpi-content    — hidden by default; display:block when parent tab is active
```

## dashboard.html Change

Company card aging panel call changes from:
```
{{ aging_panel(company.id, aging[company.id]) }}
```
to:
```
{{ kpi_aging_panel(company.id, aging[company.id]) }}
```

Import line at top of dashboard.html updates to:
```
{% from "partials/aging_panel.html" import aging_panel, kpi_aging_panel %}
```

## Pipeline Aging Dummy Data (Part 2)

Add non-empty items to the 5 currently-empty pipeline stages in AGING_DATA.
Uses the existing 2-level structure (no structural change).

Minimum: 1-2 items in 7d or 14d bucket per stage so pills are not all disabled.

### Dummy items (pipeline stages):

**pipeline_leads (7d: 2 items)**
- Fidelitus Transactions / Rajesh Kumar / 12 leads / 5d / Awaiting client meeting confirmation
- Fidelitus Projects / Arjun Shetty / 8 leads / 7d / Proposal stage pending, leads on hold

**pipeline_meetings (7d: 2 items)**
- Fidelitus FMS / Anil Kapoor / 3 meetings / 4d / Client rescheduled twice, confirming this week
- Fidelitus HR Labs / Preethi Nair / 2 meetings / 6d / Decision maker unavailable

**pipeline_proposals (7d: 1 item, 14d: 1 item)**
- 7d: Fidelitus Technology / Vikash Mehta / Rs.4.5 Cr / 6d / Technical evaluation in progress
- 14d: Fidelitus GCC Nexus / Aditya Sharma / Rs.8 Cr / 11d / Client legal review ongoing

**pipeline_orders (7d: 1 item)**
- Fidelitus Transactions / Suresh Nair / Rs.6 Cr / 7d / Agreement signing delayed by client travel

**pipeline_invoices (7d: 1 item, 14d: 1 item)**
- 7d: Fidelitus Projects / Kiran Joshi / Rs.5 Cr / 5d / Completion certificate awaited
- 14d: Fidelitus FMS / Ramesh Gupta / Rs.3.2 Cr / 12d / Client queries on invoice line items

Note: for leads/meetings, value="—" (count-based stages).

## Out of Scope

- Corporate aging panel: NO change
- Pipeline aging structure: NO change (only data populated)
- Routes, config, auth: NO change
- Time-filter wiring: handled in s06
