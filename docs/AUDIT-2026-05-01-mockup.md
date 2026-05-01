# AUDIT-2026-05-01 — Phase 0 Mockup Audit

**Date:** 2026-05-01
**Scope:** `app/mockup/`, `app/templates/`, `app/static/`
**Session:** Audit A — READ-ONLY
**Auditor:** Claude Code (Sonnet 4.6)
**PRD Reference:** `prd.md`, `CLAUDE.md`

---

## Summary

Phase 0 mockup is functionally complete for sessions s01–s05.
Sections A (Corporate KPI Strip), B (Company Cards + Aging), and C (Corporate Pipeline) all render and interact correctly. One data bug, several UX gaps, and a planned-but-not-yet-built feature (KPI drill tabs) are noted below.

**Sessions completed:** TASK-001 through TASK-005
**Sessions remaining (Phase 0):** s06 (KPI drill tabs — plan written), s07 (TBD)

---

## Severity Legend

| Severity | Meaning |
|----------|---------|
| **CRITICAL** | Data is wrong or misleading to the MD |
| **SIGNIFICANT** | UX gap or functional incomplete that the MD will notice |
| **MINOR** | Technical debt, edge case, polish item |
| **PLANNED** | Known gap — plan exists, not a bug |

---

## Section A — Corporate KPI Strip

### A1 · CRITICAL · Corporate Aging `total` shows count string, not monetary value

**File:** `app/mockup/dummy_data.py:391`

```python
result[bucket] = {"count": count, "items": items, "total": f"{count} items"}
```

The `_build_corporate_aging()` function sets `total` to `"8 items"` instead of summing
monetary values across subsidiaries. Every other bucket (transactions, projects, fms, etc.)
has a proper monetary total like `"Rs.2.1 Cr"`.

**Impact:** Corporate aging pills display e.g. `8 items` where the MD expects a rupee value.
This is visible immediately when clicking any corporate KPI card.

---

### A2 · SIGNIFICANT · `"Target for Year"` card is clickable but shouldn't be

**File:** `app/templates/dashboard.html:32–34`

All 6 KPI cards use `onclick="toggleCorporateAging()"`. The "Target for Year" card has
`pct: None` and `delta: None` — it is not a committed/actual item. Clicking it opens the
aging panel, which is misleading. The aging panel is about *delayed commitments*, not the
annual target.

**Impact:** MD may be confused by what "Target for Year" clicking reveals.

---

### A3 · SIGNIFICANT · WoW delta arrows missing for Invoiced and Payments KPIs

**File:** `app/mockup/dummy_data.py:27–35`

```python
{"label": "Invoiced Amounts",  ..., "delta": None},
{"label": "Payments Received", ..., "delta": None},
```

PRD explicitly states: *"Delta from previous meeting weekly"* for all KPIs.
Revenue, Meetings, and Proposals have deltas. Invoiced and Payments do not.

**Impact:** MD loses the WoW trend signal for two of the most important financial KPIs.

---

### A4 · MINOR · Color-coding boundary at exactly 25% is off-spec

**File:** `app/templates/dashboard.html:10`

```jinja2
{%- elif pct <= 25 -%}kpi-status-red
```

CLAUDE.md spec: `< 25%` → BRIGHT RED, `26–50%` → RED-ORANGE.
Code uses `<= 25`, so exactly `25%` renders as RED instead of RED-ORANGE.
Gap at 25% exactly — spec leaves it undefined; code errs slightly toward RED.

**Impact:** Edge case only. Low likelihood of a KPI landing precisely on 25%.

---

### A5 · MINOR · No financial year / period label on Corporate KPI Strip

The section label says "Corporate KPIs" with no year or period context.
Section C has `"WTD Apr 25, 2026"` but Section A has none.

**Impact:** MD cannot tell at a glance whether these are FY2026 YTD figures.

---

## Section B — Company Cards

### B1 · PLANNED · `"Know More"` still shows only aging panel (KPI drill tabs not built)

**Plan exists:** `docs/superpowers/plans/2026-05-01-kpi-drill-panels.md`

The plan specifies replacing the current single aging panel inside Know More with a
5-tab panel: **Revenue · Invoiced · Payments · Meetings · Proposals**.
`KPI_DETAILS` dummy data, `kpi_tabs_panel` partial, and JS tab switching are all
fully specced but not yet in the codebase.

**Current state:** Know More opens to show only the aging (Payments) bucket pills.
The MD sees payments aging but cannot drill into Revenue, Invoiced, Meetings, or Proposals.

**Action required:** Execute plan in next session (s06).

---

### B2 · SIGNIFICANT · `"Know More"` button has no open/closed state feedback

**File:** `app/templates/dashboard.html:93`, `app/static/script.js:2`

The button text stays `"Know More →"` regardless of whether the panel is open or closed.
There is no visual affordance that the panel is already expanded, or that clicking again
will close it.

**Impact:** MD may click repeatedly not realising it's a toggle, or leave panels open
unintentionally.

---

### B3 · CRITICAL · Company targets do not sum to corporate target

**File:** `app/mockup/dummy_data.py:58–130`

| Company | Target |
|---------|--------|
| Fidelitus Transactions | Rs.80 Cr |
| Fidelitus Projects | Rs.60 Cr |
| Fidelitus FMS | Rs.30 Cr |
| Fidelitus HR Labs | Rs.25 Cr |
| Fidelitus Technology | Rs.20 Cr |
| Fidelitus GCC Nexus | Rs.25 Cr |
| **Sum** | **Rs.240 Cr** |
| **Corporate** | **Rs.320 Cr** |

Gap: **Rs.80 Cr unaccounted for.** Revenue cross-check is clean (sum = Rs.142 Cr = corporate).
The target discrepancy is conspicuous and will confuse the MD during mockup review.

*Note: Revenue sums correctly (68+29+24+11+9+1 = Rs.142 Cr = corporate Rs.142 Cr ✓)*

---

### B4 · MINOR · WoW deltas very uneven across company cards

Most companies show a delta only for Revenue. Fidelitus Technology shows none at all.
Per PRD, WoW delta should be shown for all committed KPIs where movement exists.

| Company | Deltas present |
|---------|---------------|
| Transactions | Revenue ▲, Meetings ▲, Proposals ▲ |
| Projects | Revenue ▼ |
| FMS | Revenue ▲ |
| HR Labs | Revenue ▼ |
| Technology | *(none)* |
| GCC Nexus | Revenue ▼ |

---

## Section C — Corporate Leads Pipeline

### C1 · SIGNIFICANT · Five of six pipeline "Details →" panels open empty

**File:** `app/mockup/dummy_data.py:407–411`

```python
AGING_DATA["pipeline_leads"]     = _empty_pipeline_bucket()
AGING_DATA["pipeline_meetings"]  = _empty_pipeline_bucket()
AGING_DATA["pipeline_proposals"] = _empty_pipeline_bucket()
AGING_DATA["pipeline_orders"]    = _empty_pipeline_bucket()
AGING_DATA["pipeline_invoices"]  = _empty_pipeline_bucket()
```

Clicking "Details →" on Leads, Meetings, Proposals, Orders, or Invoices opens a panel
showing 5 disabled pills and nothing else. Only Collections has real data.

**Impact:** MD will click Details on pipeline stages and see a blank panel — feels broken.

---

### C2 · MINOR · Pipeline date hardcoded in template

**File:** `app/templates/dashboard.html:111`

```html
<div class="section-label">Corporate Leads Pipeline — WTD Apr 25, 2026</div>
```

Expected for Phase 0 mockup. Must be made dynamic in Phase 1 (s10+).

---

### C3 · MINOR · Section C not covered by KPI drill plan

The `2026-05-01-kpi-drill-panels.md` plan only upgrades Section B (company cards).
Section C pipeline has no planned drill-down beyond the aging panel.
No action needed now — noting for s07 scoping.

---

## Aging Panel (All Sections)

### D1 · MINOR · Aging bucket pills have no severity colour differentiation

All five pills (7d, 14d, 21d, 90d, NPA) render with the same styling regardless of
severity. An NPA pill (>90 days, highest risk) looks identical to a 7d pill.

PRD intent and CLAUDE.md color-coding rule imply that the MD should read risk at a glance.
NPA should have a red border/background; 90d should be red-orange; 7d should remain neutral.

---

### D2 · MINOR · `days` field in aging items can exceed the bucket's time range

Example: `transactions.90d` item has `"days": 67` (not yet 90 days).
This item sits in the 90d bucket but its `days` value is 67.
Naming is slightly misleading — the 90d bucket appears to mean "up to 90 days" not ">90 days".
NPA is `> 90 days`. The bucket labelling is consistent with `CLAUDE.md`'s `90 days` bucket,
but verify with MD whether the 90d bucket means "21–90 days" or ">90 days".

---

## CSS / Styling

### E1 · MINOR · `.company-details.open` defined twice with `!important` escalation

**File:** `app/static/style.css:366, 535`

```css
/* Line 366 — original */
.company-details.open { max-height: 120px; }

/* Line 535 — override */
.company-details.open { max-height: 800px !important; }
```

The `!important` override was added as a fix comment. The KPI drill plan adds a third:
`max-height: 1200px !important`. This is cascading technical debt.

A single appropriate value or a CSS custom property would be cleaner.

---

### E2 · MINOR · Unused CSS class `.ckpi-target-placeholder`

**File:** `app/static/style.css:328`

```css
.ckpi-target-placeholder { display: inline-block; width: 3rem; }
```

Not referenced in any template. Dead code.

---

## JavaScript

### F1 · MINOR · No null-guard on `panel` in `toggleDetails` / `toggleCorporateAging`

**File:** `app/static/script.js:3, 14`

```javascript
const panel = document.getElementById('details-' + id);
panel.classList.toggle('open');  // throws if panel is null
```

For Phase 0 with static templates this is low risk. Worth fixing before Phase 1 to
prevent silent JS errors if a template is ever rendered without the expected element.

---

### F2 · MINOR · Multiple pipeline panels can be open simultaneously

`toggleDetails(id)` only toggles the targeted panel; it does not close any other open
panels. Multiple company cards or pipeline panels can be open at the same time.
This may be intentional (MD may want to compare), but should be confirmed.

---

## PRD Compliance Summary

| PRD Requirement | Status |
|----------------|--------|
| Corporate KPI strip: 6 KPIs with values | ✓ Complete |
| Color coding: <25% RED, 26-50% RED-ORANGE, 51-75% AMBER, >75% GREEN | ✓ Complete (minor boundary issue at 25%) |
| WoW delta arrows per KPI | Partial — missing on Invoiced, Payments |
| 6 company cards with same KPIs | ✓ Complete |
| Know More → aging drill by bucket (7d/14d/21d/90d/NPA) | ✓ Complete |
| Know More → KPI detail tables (Revenue/Invoiced/Meetings/Proposals) | Planned (s06) |
| Corporate Leads Pipeline: 6-stage with count/target/delta | ✓ Complete |
| Pipeline Details → aging drill | Partial — only Collections has real data |
| PRODUCTION flag (PRODUCTION=1 → dummy data) | ✓ Complete |
| Fonts: DM Sans + Syne | ✓ Complete |
| Color scheme: dark bg, surface, amber accent | ✓ Complete |
| No heavy JS frameworks | ✓ Vanilla JS only |

---

## Recommended Fix Order

### Before showing to MD (s06 session pre-work)

| # | Issue | File | Severity |
|---|-------|------|----------|
| 1 | Corporate aging `total` shows "X items" not Rs. value | `dummy_data.py:391` | CRITICAL |
| 2 | Company targets don't sum to Rs.320 Cr (Rs.80 Cr gap) | `dummy_data.py:58–130` | CRITICAL |
| 3 | Empty pipeline Details panels for 5 of 6 stages | `dummy_data.py:407–411` | SIGNIFICANT |
| 4 | WoW delta missing for Invoiced Amounts + Payments Received | `dummy_data.py:27–35` | SIGNIFICANT |

### During s06 session

| # | Issue | File | Severity |
|---|-------|------|----------|
| 5 | Build KPI drill tabs (Revenue/Invoiced/Meetings/Proposals) | Plan exists | PLANNED |
| 6 | "Know More" button text doesn't change when panel is open | `dashboard.html:93` | SIGNIFICANT |
| 7 | "Target for Year" card should not be clickable | `dashboard.html:32` | SIGNIFICANT |

### Polish (s07)

| # | Issue | File | Severity |
|---|-------|------|----------|
| 8 | Add financial year / period label to Section A | `dashboard.html` | MINOR |
| 9 | Aging pill severity colours (NPA = red, 90d = red-orange) | `style.css` | MINOR |
| 10 | Remove duplicate `max-height` `!important` overrides | `style.css` | MINOR |
| 11 | Remove unused `.ckpi-target-placeholder` CSS class | `style.css` | MINOR |
| 12 | Add null-guard to `toggleDetails` JS | `script.js` | MINOR |

---

## Files Audited

| File | Lines | Status |
|------|-------|--------|
| `app/mockup/dummy_data.py` | 449 | Issues: A3, B3, C1, D2 |
| `app/mockup/routes.py` | 21 | Clean |
| `app/templates/base.html` | 25 | Clean |
| `app/templates/dashboard.html` | 147 | Issues: A1-link, A2, B2 |
| `app/templates/partials/aging_panel.html` | 66 | Clean |
| `app/static/style.css` | 694 | Issues: E1, E2 |
| `app/static/script.js` | 60 | Issues: F1, F2 |

---

*End of Audit*
