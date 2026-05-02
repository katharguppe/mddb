# Audit Fixes — Phase 0 Mockup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the 4 real issues identified by the 2026-05-02 mockup audit.

**Architecture:** All changes are confined to Phase 0 data/template/style files. No routing or Python logic changes. `dummy_data.py` is the single source of truth for all mock values.

**Tech Stack:** Python 3.13, Jinja2 templates, vanilla CSS, vanilla JS. FastAPI served via `uvicorn app.main:app --reload`.

---

## Audit False-Positive Log (do NOT fix these)

The audit subagent mis-reported the following as issues. They are already correct:
- **C-1** — `_build_corporate_aging()` correctly sums Rs. values via `_parse_cr()`.
- **S-1** — Target card is already non-clickable; `{% if loop.first %}` omits `onclick`.
- **S-3** — Button text toggle works; JS attribute selector matches rendered HTML.
- **S-4** — All 6 pipeline stages have dummy aging items.
- **M-5** — `.company-details.open` has exactly one CSS rule, no `!important`.
- **M-6** — `.ckpi-target-placeholder` does not exist anywhere.
- **M-7** — Both JS toggle functions already have `if (!panel) return` null-guards.

---

## Files Modified

| File | Change |
|------|--------|
| `app/mockup/dummy_data.py` | Fix corporate KPI targets + recalc pcts; add Payments delta |
| `app/templates/dashboard.html` | Fix `pct_class` boundary at 25% |
| `app/static/style.css` | Add per-bucket severity colours to aging pills |

No new files created.

---

## Task 1 — Fix Corporate KPI Target Denominator + Payments Delta

**Files:**
- Modify: `app/mockup/dummy_data.py` lines 5–51

**Background:**
Company targets (dummy_data.py lines 59–135) sum to Rs.240 Cr:
- Transactions Rs.80 Cr + Projects Rs.60 Cr + FMS Rs.30 Cr + HR Labs Rs.25 Cr + Technology Rs.20 Cr + GCC Rs.25 Cr = **Rs.240 Cr**

The corporate `"Target for Year"` card correctly shows `"Rs.240 Cr"` (line 10–11).
But Revenue, Invoiced, and Payments KPIs all have `"target": "Rs.320 Cr"` (lines 18, 25, 32) — wrong denominator — making the percentage badges incorrect.

Correct percentages with Rs.240 Cr denominator:
- Revenue: 142 / 240 = **59%** (currently shows 44%)
- Invoiced: 108 / 240 = **45%** (currently shows 34%)
- Payments: 71 / 240 = **30%** (currently shows 22%)

Also, Payments has `"delta": None` (line 34) — only KPI with no trend direction. Set to `"up"`.

- [ ] **Step 1: Edit dummy_data.py — fix three target strings and three pct values, add Payments delta**

Replace the Revenue KPI dict (lines 15–21):
```python
            {
                "label": "Revenue (Booking)",
                "value": "Rs.142 Cr",
                "target": "Rs.240 Cr",
                "pct": 59,
                "delta": "up",
            },
```

Replace the Invoiced KPI dict (lines 22–28):
```python
            {
                "label": "Invoiced Amounts",
                "value": "Rs.108 Cr",
                "target": "Rs.240 Cr",
                "pct": 45,
                "delta": "up",
            },
```

Replace the Payments KPI dict (lines 29–35):
```python
            {
                "label": "Payments Received",
                "value": "Rs.71 Cr",
                "target": "Rs.240 Cr",
                "pct": 30,
                "delta": "up",
            },
```

- [ ] **Step 2: Verify the six corporate KPIs are now consistent**

After editing, the `DASHBOARD_DATA["corporate"]["kpis"]` block should look exactly like:
```python
    "corporate": {
        "kpis": [
            {
                "label": "Target for Year",
                "value": "Rs.240 Cr",
                "target": "Rs.240 Cr",
                "pct": None,
                "delta": None,
            },
            {
                "label": "Revenue (Booking)",
                "value": "Rs.142 Cr",
                "target": "Rs.240 Cr",
                "pct": 59,
                "delta": "up",
            },
            {
                "label": "Invoiced Amounts",
                "value": "Rs.108 Cr",
                "target": "Rs.240 Cr",
                "pct": 45,
                "delta": "up",
            },
            {
                "label": "Payments Received",
                "value": "Rs.71 Cr",
                "target": "Rs.240 Cr",
                "pct": 30,
                "delta": "up",
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
```

- [ ] **Step 3: Commit**

```bash
git add app/mockup/dummy_data.py
git commit -m "[TASK-007] fix: corporate KPI target Rs.240 Cr, recalc pcts, add Payments delta"
```

---

## Task 2 — Fix pct_class Boundary at 25%

**Files:**
- Modify: `app/templates/dashboard.html` line 11

**Background:**
CLAUDE.md specifies: `< 25%` → BRIGHT RED. The current macro uses `<= 25` which incorrectly
colours pct=25 as red. The boundary should be exclusive (25 is amber, not red).

- [ ] **Step 1: Edit dashboard.html — change one operator**

Find (line 11):
```jinja
  {%- elif pct <= 25 -%}kpi-status-red
```

Replace with:
```jinja
  {%- elif pct < 25 -%}kpi-status-red
```

- [ ] **Step 2: Verify the full macro**

After editing, the `pct_class` macro should look exactly like:
```jinja
{% macro pct_class(pct) -%}
  {%- if pct is none -%}
  {%- elif pct < 25 -%}kpi-status-red
  {%- elif pct <= 50 -%}kpi-status-red-orange
  {%- elif pct <= 75 -%}kpi-status-amber
  {%- else -%}kpi-status-green
  {%- endif -%}
{%- endmacro %}
```

This matches CLAUDE.md exactly:
- `< 25` → red
- `26–50` (i.e. `<= 50` after the first branch) → red-orange
- `51–75` (i.e. `<= 75`) → amber
- `> 75` → green

- [ ] **Step 3: Commit**

```bash
git add app/templates/dashboard.html
git commit -m "[TASK-007] fix: pct_class boundary — < 25 (exclusive) per spec"
```

---

## Task 3 — Add Severity Colours to Aging Bucket Pills

**Files:**
- Modify: `app/static/style.css` — add rules after `.aging-pill.active` block (~line 437)

**Background:**
All aging pills look identical. The NPA (>90 days) bucket should signal the highest urgency.
Apply the project's existing status colour palette, keyed to the `data-bucket` attribute:

| Bucket | Severity | Colour |
|--------|----------|--------|
| 7d | low | default (no change) |
| 14d | moderate | amber `#f59e0b` |
| 21d | elevated | red-orange `#f97316` |
| 90d | high | red `#ef4444` |
| npa | critical | red `#ef4444` (brighter, full opacity) |

Only style the **active** state and **pill count** text — leave inactive pills identical to current
(low contrast, discoverable only on hover/click).

- [ ] **Step 1: Edit style.css — add severity rules after the `.aging-pill.active` block**

Find the existing active block (around line 434):
```css
.aging-pill.active {
    border-color: var(--color-accent);
    background: rgba(232, 168, 56, 0.12);
}
```

After that closing brace, add:
```css

/* Severity tinting for aging bucket pills (active state only) */
.aging-pill[data-bucket="14d"].active {
    border-color: #f59e0b;
    background: rgba(245, 158, 11, 0.12);
}
.aging-pill[data-bucket="14d"].active .aging-pill-label,
.aging-pill[data-bucket="14d"].active .aging-pill-count {
    color: #f59e0b;
}

.aging-pill[data-bucket="21d"].active {
    border-color: #f97316;
    background: rgba(249, 115, 22, 0.12);
}
.aging-pill[data-bucket="21d"].active .aging-pill-label,
.aging-pill[data-bucket="21d"].active .aging-pill-count {
    color: #f97316;
}

.aging-pill[data-bucket="90d"].active {
    border-color: #ef4444;
    background: rgba(239, 68, 68, 0.12);
}
.aging-pill[data-bucket="90d"].active .aging-pill-label,
.aging-pill[data-bucket="90d"].active .aging-pill-count {
    color: #ef4444;
}

.aging-pill[data-bucket="npa"].active {
    border-color: #ef4444;
    background: rgba(239, 68, 68, 0.18);
}
.aging-pill[data-bucket="npa"].active .aging-pill-label,
.aging-pill[data-bucket="npa"].active .aging-pill-count {
    color: #ef4444;
}
```

- [ ] **Step 2: Verify the data-bucket attribute is present on aging pills**

Check `app/templates/partials/aging_panel.html` — confirm the pill buttons render with
`data-bucket="{{ bucket }}"` (this is already in the template from s07). The CSS selectors
above will only work if that attribute is present.

- [ ] **Step 3: Commit**

```bash
git add app/static/style.css
git commit -m "[TASK-007] fix: aging pill severity colours — amber/orange/red by bucket"
```

---

## Manual Verification Checklist

After all tasks complete, open the dashboard in a browser (`uvicorn app.main:app --reload`
with `PRODUCTION=1` in `.env`) and verify:

- [ ] Corporate KPI strip: Revenue shows **59%** (green), Invoiced **45%** (amber), Payments **30%** (red-orange) with amber target `Rs.240 Cr` on all three
- [ ] Payments Received KPI card shows an **▲ up arrow** delta indicator
- [ ] A KPI value of exactly **25** renders in **red-orange** (not red); **24** renders in red
- [ ] Clicking an NPA aging pill highlights it in **red**; a 90d pill in red; a 21d pill in orange; a 14d pill in amber; a 7d pill in default amber accent
