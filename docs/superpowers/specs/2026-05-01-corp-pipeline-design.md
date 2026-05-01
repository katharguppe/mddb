# Design Spec — Corporate Leads Pipeline (TASK-005)
Date: 2026-05-01
Session: s05 (Phase 0 mockup)

## Goal

Add Section C — "Corporate Leads Pipeline" — below the Subsidiaries company cards on the MD Dashboard.
This shows the 6-stage BD pipeline for leads personally sourced or assigned by the MD / corporate team,
with WTD metrics, % achievement badges, WoW deltas, and an aging drill-down per stage.

## Scope

Files touched (Phase 0 mockup only):
- `app/mockup/dummy_data.py`
- `app/templates/dashboard.html`
- `app/static/style.css`

Files NOT touched:
- `app/mockup/routes.py` — already passes `data` and `aging` dicts; no change needed
- `app/static/script.js` — existing `toggleDetails(id)` reused as-is
- `app/templates/partials/aging_panel.html` — existing macro reused as-is

## Pipeline Stages (left → right)

| # | Stage       | Count | Target | Pct | Delta dir | Delta val | Value    |
|---|-------------|-------|--------|-----|-----------|-----------|----------|
| 1 | Leads       | 42    | 50     | 84% | up        | +7 WoW    | —        |
| 2 | Meetings    | 18    | 25     | 72% | up        | +3 WoW    | —        |
| 3 | Proposals   | 11    | 15     | 73% | up        | +2 WoW    | Rs.38 Cr |
| 4 | Orders      | 6     | 10     | 60% | up        | +1 WoW    | Rs.24 Cr |
| 5 | Invoices    | 4     | 8      | 50% | none      | 0 WoW     | Rs.18 Cr |
| 6 | Collections | 3     | 6      | 50% | down      | -1 WoW    | Rs.9 Cr  |

Period: WTD ending 2026-04-25.

## Color Rule (same as everywhere)

- < 25% → BRIGHT RED `#ef4444`
- 26–50% → RED-ORANGE `#f97316`
- 51–75% → AMBER `#f59e0b`
- > 75% → GREEN `#22c55e`

## Aging Drill-Down

Clicking "Details →" on a stage card slides down a full-width aging panel (reuses
the existing `aging_panel` macro and `.company-details` CSS class / JS).

Aging keys in `AGING_DATA`: `pipeline_leads`, `pipeline_meetings`, `pipeline_proposals`,
`pipeline_orders`, `pipeline_invoices`, `pipeline_collections`.

Only Collections has explicit dummy data (per spec). All other stages get empty buckets
(pills render as disabled, correct behaviour).

### Collections aging (dummy)

**7 Days — Rs.3.2 Cr — 2 items**

| Company | Member | Value | Days | Reason |
|---|---|---|---|---|
| Fidelitus Transactions | Amit Shah | Rs.2 Cr | 5d | Payment by EOM confirmed |
| Fidelitus Projects | Deepa Iyer | Rs.1.2 Cr | 7d | Client OOO till Friday |

**NPA — Rs.2.1 Cr — 1 item**

| Company | Member | Value | Days | Reason |
|---|---|---|---|---|
| Fidelitus GCC Nexus | Kiran Bhat | Rs.2.1 Cr | 95d | Negotiations ongoing |

## Data Architecture

```
DASHBOARD_DATA["pipeline"] = [
    {
        "id":        "pipeline_leads",   # used as HTML id / aging key
        "stage":     "Leads",
        "count":     42,
        "target":    50,
        "pct":       84,
        "delta_dir": "up",              # "up" | "down" | "none"
        "delta_val": "+7 WoW",
        "value":     None,              # None -> display "—"
    },
    ... (5 more)
]

AGING_DATA["pipeline_collections"] = {
    "7d":  { "count": 2, "total": "Rs.3.2 Cr", "items": [...] },
    "14d": { "count": 0, "total": "Rs.0",       "items": [] },
    "21d": { "count": 0, "total": "Rs.0",       "items": [] },
    "90d": { "count": 0, "total": "Rs.0",       "items": [] },
    "npa": { "count": 1, "total": "Rs.2.1 Cr",  "items": [...] },
}
# Other stages: all 5 buckets empty
```

## HTML Structure (Section C)

```
<section class="section">
    <div class="section-label">Corporate Leads Pipeline — WTD Apr 25, 2026</div>
    <div class="pipeline-flow">
        {% for stage in data.pipeline %}
        <div class="pipeline-stage-card">
            <div class="pipeline-stage-name">{{ stage.stage }}</div>
            <div class="pipeline-count">{{ stage.count }} <span class="pipeline-target">/ {{ stage.target }}</span></div>
            <div class="pipeline-value">{{ stage.value or "—" }}</div>
            <div class="pipeline-footer">
                <span class="pct-badge {{ pct_class(stage.pct) }}">{{ stage.pct }}%</span>
                {% if stage.delta_dir == "up" %}<span class="delta-up">▲</span>
                {% elif stage.delta_dir == "down" %}<span class="delta-down">▼</span>
                {% endif %}
                <span class="pipeline-delta-text">{{ stage.delta_val }}</span>
            </div>
            <a class="pipeline-details-link" onclick="toggleDetails('{{ stage.id }}')">Details →</a>
        </div>
        {% endfor %}
    </div>

    {# Per-stage aging panels #}
    {% for stage in data.pipeline %}
    <div class="company-details pipeline-aging-panel" id="details-{{ stage.id }}">
        {{ aging_panel(stage.id, aging[stage.id]) }}
    </div>
    {% endfor %}
</section>
```

## CSS additions (style.css)

```
.pipeline-flow              — 6-col grid; connector arrows via ::after on each card (last-child suppressed)
.pipeline-stage-card        — card with border, padding, flex-col layout
.pipeline-stage-name        — eyebrow label (uppercase, small, secondary color)
.pipeline-count             — large number (heading font)
.pipeline-target            — " / target" in secondary color
.pipeline-value             — Rs.XX Cr or "—" in accent color
.pipeline-footer            — flex row: pct-badge + delta arrow + delta text
.pipeline-delta-text        — small delta string (+N WoW)
.pipeline-details-link      — styled text link (accent color, no underline, small)
.pipeline-aging-panel.open  — max-height: 1000px !important (same pattern as corporate)
```

## Reuse Map

| Existing mechanism        | Reused for pipeline |
|---------------------------|---------------------|
| `aging_panel` macro       | Per-stage drill-down |
| `toggleDetails(id)`       | "Details →" click handler |
| `.company-details` class  | Slide-down animation |
| `pct_class()` macro       | Stage pct badge color |
| `.pct-badge` CSS          | Stage pct badge style |
| `.delta-up/down/none` CSS | WoW delta arrows |

## Out of Scope

- No script.js changes
- No routes.py changes
- No aging_panel.html changes
- No new template partials
- No "Stage" column in aging tables (stage is implicit from which panel is open)
