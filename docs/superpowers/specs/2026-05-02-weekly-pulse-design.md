# Design Spec — TASK-006: Weekly Pulse Panel
**Date:** 2026-05-02
**Session:** s06 (Phase 0 — Mockup)
**Scope:** `app/mockup/dummy_data.py`, `app/templates/dashboard.html`, `app/static/style.css`, `app/static/script.js`, `app/mockup/routes.py`

---

## Purpose

Surface the week's committed-vs-actual revenue delta prominently for the MD's Monday review meeting. The panel is visible only on the WTD time filter; hidden for MTD/QTD/YTD.

---

## Data (`dummy_data.py`)

Add a top-level `WEEKLY_PULSE` dict with:

```
WEEKLY_PULSE = {
    "week_label":      "Week of 21 Apr – 25 Apr 2026",
    "committed_label": "Last committed: Mon 21 Apr",
    "rows": [
        { "id": "transactions", "name": "Fidelitus Transactions",
          "committed": "Rs.9 Cr",  "actual": "Rs.9.8 Cr",
          "delta": "+0.8 Cr", "delta_sign": "pos",
          "actual_pct": 109 },   # actual / committed * 100
        { "id": "projects",     "name": "Fidelitus Projects",
          "committed": "Rs.4 Cr",  "actual": "Rs.1.8 Cr",
          "delta": "−2.2 Cr", "delta_sign": "neg",
          "actual_pct": 45 },
        ...one entry per company...
    ],
    "total": {
        "committed": "Rs.18.7 Cr", "actual": "Rs.14.55 Cr",
        "delta": "−4.15 Cr", "delta_sign": "neg",
        "actual_pct": 78
    }
}
```

`actual_pct` = `round(actual_cr / committed_cr * 100)`. Status color uses the existing 4-band rule:
- ≤25 → `kpi-status-red` (bright red)
- 26–50 → `kpi-status-red-orange`
- 51–75 → `kpi-status-amber`
- >75 → `kpi-status-green`

All values are hardcoded in `dummy_data.py` (Phase 0 — no calculation logic needed).

Full row values:

| Company               | committed_cr | actual_cr | actual_pct |
|-----------------------|--------------|-----------|------------|
| Fidelitus Transactions| 9.0          | 9.8       | 109        |
| Fidelitus Projects    | 4.0          | 1.8       | 45         |
| Fidelitus FMS         | 2.5          | 2.1       | 84         |
| Fidelitus HR Labs     | 1.5          | 0.3       | 20         |
| Fidelitus Technology  | 1.2          | 0.5       | 42         |
| Fidelitus GCC Nexus   | 0.5          | 0.05      | 10         |
| CORPORATE TOTAL       | 18.7         | 14.55     | 78         |

---

## Routes (`app/mockup/routes.py`)

Pass `weekly_pulse=WEEKLY_PULSE` into the existing template context dict alongside `data`, `aging`, `kpi_details`, `kpi_aging`.

---

## Template (`dashboard.html`)

### 1. Header — time-filter pills

The right side of `<header class="dashboard-header">` currently holds a single `<span class="phase-badge">`. Wrap the right side in a small flex column:

```html
<div class="header-right">
    <span class="phase-badge">Phase 0 Mockup</span>
    <div class="time-filter" id="time-filter">
        <button class="tf-pill active" onclick="setTimePeriod('WTD')">WTD</button>
        <button class="tf-pill"        onclick="setTimePeriod('MTD')">MTD</button>
        <button class="tf-pill"        onclick="setTimePeriod('QTD')">QTD</button>
        <button class="tf-pill"        onclick="setTimePeriod('YTD')">YTD</button>
    </div>
</div>
```

### 2. Weekly Pulse section

Inserted between Section A (Corporate KPIs) and Section B (Subsidiaries):

```html
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

Clicking a company row calls `toggleDetails('{{ row.id }}')` — this reuses the existing aging panel that lives inside each company card. No new JS needed for the expand behaviour.

---

## CSS (`style.css`)

### Time-filter pills (header)

```css
.header-right {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 0.5rem;
}

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
    transition: background 0.15s, color 0.15s;
}

.tf-pill.active,
.tf-pill:hover {
    background: var(--color-accent);
    color: #0d1117;
    border-color: var(--color-accent);
}
```

### Weekly Pulse section

```css
.weekly-pulse-section.hidden {
    display: none;
}

.pulse-week-meta {
    font-size: 0.65rem;
    color: var(--color-text-secondary);
    letter-spacing: 0;
    text-transform: none;
    font-weight: 400;
}

.pulse-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85rem;
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
    border-bottom: 1px solid rgba(48,54,61,0.5);
    color: var(--color-text-primary);
}

.pulse-row--clickable {
    cursor: pointer;
    transition: background 0.15s;
}

.pulse-row--clickable:hover {
    background: rgba(255,255,255,0.03);
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

---

## JS (`script.js`)

```js
/* ── Time-period filter ── */
function setTimePeriod(period) {
    // Update pill active state
    document.querySelectorAll('.tf-pill').forEach(function(pill) {
        pill.classList.toggle('active', pill.textContent.trim() === period);
    });

    // Show Weekly Pulse only for WTD
    const pulse = document.getElementById('weekly-pulse-section');
    if (pulse) {
        pulse.classList.toggle('hidden', period !== 'WTD');
    }
}
```

Initialised on page load via inline call in `dashboard.html` (bottom of `extra_js` block):
```js
setTimePeriod('WTD');
```

---

## Interaction notes

- Clicking a company row in the pulse table calls `toggleDetails(id)`, which opens the aging drill-down panel **inside the company card in Section B** (scrolls user there naturally).
- No separate aging panel is rendered inside the pulse section — the existing company-card panels are reused.
- The Corporate Total row is not clickable (no `id` to expand).

---

## What this session does NOT do

- No MTD/QTD/YTD data variants — the filter only shows/hides the pulse section.
- No per-company weekly breakdown beyond revenue — the pulse table is revenue-only as specified.
- No server-side period switching — purely client-side JS toggle.
