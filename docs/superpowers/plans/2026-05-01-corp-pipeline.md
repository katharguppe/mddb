# Corporate Leads Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Section C — Corporate Leads Pipeline — below the Subsidiaries company cards, with 6 horizontal stage cards, % badges, WoW deltas, and per-stage aging drill-down panels.

**Architecture:** All data lives in `dummy_data.py`; the route already passes `data` and `aging` to the template, so no route change is needed. The template adds a new `<section>` using the existing `aging_panel` macro and `toggleDetails()` JS function. CSS adds the 6-col pipeline grid and stage card styles.

**Tech Stack:** Python dict (dummy data), Jinja2 (template), vanilla CSS (layout/styles). No new JS — existing `toggleDetails(id)` handles the slide-down.

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `app/mockup/dummy_data.py` | Modify | Add `DASHBOARD_DATA["pipeline"]` (6 stages) + 6 `AGING_DATA["pipeline_*"]` entries |
| `app/templates/dashboard.html` | Modify | Add Section C HTML block after Section B |
| `app/static/style.css` | Modify | Add `.pipeline-*` CSS classes |

---

## Task 1: Add pipeline dummy data

**Files:**
- Modify: `app/mockup/dummy_data.py`

- [ ] **Step 1: Add `"pipeline"` key to `DASHBOARD_DATA`**

Open `app/mockup/dummy_data.py`. After the closing `]` of the `"companies"` list (line 131), and before the closing `}` of `DASHBOARD_DATA`, add a comma and the pipeline list:

```python
    "pipeline": [
        {
            "id":        "pipeline_leads",
            "stage":     "Leads",
            "count":     42,
            "target":    50,
            "pct":       84,
            "delta_dir": "up",
            "delta_val": "+7 WoW",
            "value":     None,
        },
        {
            "id":        "pipeline_meetings",
            "stage":     "Meetings",
            "count":     18,
            "target":    25,
            "pct":       72,
            "delta_dir": "up",
            "delta_val": "+3 WoW",
            "value":     None,
        },
        {
            "id":        "pipeline_proposals",
            "stage":     "Proposals",
            "count":     11,
            "target":    15,
            "pct":       73,
            "delta_dir": "up",
            "delta_val": "+2 WoW",
            "value":     "Rs.38 Cr",
        },
        {
            "id":        "pipeline_orders",
            "stage":     "Orders",
            "count":     6,
            "target":    10,
            "pct":       60,
            "delta_dir": "up",
            "delta_val": "+1 WoW",
            "value":     "Rs.24 Cr",
        },
        {
            "id":        "pipeline_invoices",
            "stage":     "Invoices",
            "count":     4,
            "target":    8,
            "pct":       50,
            "delta_dir": "none",
            "delta_val": "0 WoW",
            "value":     "Rs.18 Cr",
        },
        {
            "id":        "pipeline_collections",
            "stage":     "Collections",
            "count":     3,
            "target":    6,
            "pct":       50,
            "delta_dir": "down",
            "delta_val": "-1 WoW",
            "value":     "Rs.9 Cr",
        },
    ],
```

The `DASHBOARD_DATA` dict now has three keys: `"corporate"`, `"companies"`, `"pipeline"`.

- [ ] **Step 2: Add a helper and pipeline aging entries to `AGING_DATA`**

At the bottom of `app/mockup/dummy_data.py`, after the `AGING_DATA["corporate"] = _build_corporate_aging()` line, add:

```python
# ── Pipeline aging (per stage) ──────────────────────────────────────────────
def _empty_pipeline_bucket():
    return {
        "7d":  {"count": 0, "total": "Rs.0", "items": []},
        "14d": {"count": 0, "total": "Rs.0", "items": []},
        "21d": {"count": 0, "total": "Rs.0", "items": []},
        "90d": {"count": 0, "total": "Rs.0", "items": []},
        "npa": {"count": 0, "total": "Rs.0", "items": []},
    }

AGING_DATA["pipeline_leads"]     = _empty_pipeline_bucket()
AGING_DATA["pipeline_meetings"]  = _empty_pipeline_bucket()
AGING_DATA["pipeline_proposals"] = _empty_pipeline_bucket()
AGING_DATA["pipeline_orders"]    = _empty_pipeline_bucket()
AGING_DATA["pipeline_invoices"]  = _empty_pipeline_bucket()
AGING_DATA["pipeline_collections"] = {
    "7d": {
        "count": 2,
        "total": "Rs.3.2 Cr",
        "items": [
            {
                "company": "Fidelitus Transactions",
                "member":  "Amit Shah",
                "value":   "Rs.2 Cr",
                "days":    5,
                "reason":  "Payment by EOM confirmed",
            },
            {
                "company": "Fidelitus Projects",
                "member":  "Deepa Iyer",
                "value":   "Rs.1.2 Cr",
                "days":    7,
                "reason":  "Client OOO till Friday",
            },
        ],
    },
    "14d": {"count": 0, "total": "Rs.0", "items": []},
    "21d": {"count": 0, "total": "Rs.0", "items": []},
    "90d": {"count": 0, "total": "Rs.0", "items": []},
    "npa": {
        "count": 1,
        "total": "Rs.2.1 Cr",
        "items": [
            {
                "company": "Fidelitus GCC Nexus",
                "member":  "Kiran Bhat",
                "value":   "Rs.2.1 Cr",
                "days":    95,
                "reason":  "Negotiations ongoing",
            },
        ],
    },
}
```

- [ ] **Step 3: Verify data loads cleanly**

Run from the project root:
```bash
python -c "
from app.mockup.dummy_data import DASHBOARD_DATA, AGING_DATA
stages = DASHBOARD_DATA['pipeline']
print('Stages:', [s['stage'] for s in stages])
print('Pipeline aging keys:', [k for k in AGING_DATA if k.startswith('pipeline')])
print('Collections 7d count:', AGING_DATA['pipeline_collections']['7d']['count'])
print('Collections NPA count:', AGING_DATA['pipeline_collections']['npa']['count'])
"
```

Expected output:
```
Stages: ['Leads', 'Meetings', 'Proposals', 'Orders', 'Invoices', 'Collections']
Pipeline aging keys: ['pipeline_leads', 'pipeline_meetings', 'pipeline_proposals', 'pipeline_orders', 'pipeline_invoices', 'pipeline_collections']
Collections 7d count: 2
Collections NPA count: 1
```

- [ ] **Step 4: Commit**

```bash
git add app/mockup/dummy_data.py
git commit -m "[TASK-005] feat: add corporate pipeline dummy data and aging entries"
```

---

## Task 2: Add Section C to dashboard.html

**Files:**
- Modify: `app/templates/dashboard.html`

- [ ] **Step 1: Add Section C after the closing `</section>` of Section B**

In `app/templates/dashboard.html`, locate line 107 (`    </section>`) — the closing tag of Section B (the Subsidiaries section). Insert the following block immediately after it, before `</main>`:

```html
    {# ── Section C: Corporate Leads Pipeline ── #}
    <section class="section">
        <div class="section-label">Corporate Leads Pipeline — WTD Apr 25, 2026</div>
        <div class="pipeline-flow">
            {% for stage in data.pipeline %}
            <div class="pipeline-stage-card">
                <div class="pipeline-stage-name">{{ stage.stage }}</div>
                <div class="pipeline-count">
                    {{ stage.count }}<span class="pipeline-target"> / {{ stage.target }}</span>
                </div>
                <div class="pipeline-value">{{ stage.value if stage.value else "—" }}</div>
                <div class="pipeline-footer">
                    <span class="pct-badge {{ pct_class(stage.pct) }}">{{ stage.pct }}%</span>
                    {% if stage.delta_dir == "up" %}<span class="delta-up">▲</span>
                    {% elif stage.delta_dir == "down" %}<span class="delta-down">▼</span>
                    {% endif %}
                    <span class="pipeline-delta-text">{{ stage.delta_val }}</span>
                </div>
                <a class="pipeline-details-link"
                   onclick="toggleDetails('{{ stage.id }}')">Details →</a>
            </div>
            {% endfor %}
        </div>

        {# Per-stage aging panels — hidden until Details clicked #}
        {% for stage in data.pipeline %}
        <div class="company-details pipeline-aging-panel" id="details-{{ stage.id }}">
            {{ aging_panel(stage.id, aging[stage.id]) }}
        </div>
        {% endfor %}
    </section>
```

- [ ] **Step 2: Start the dev server and confirm no template errors**

```bash
uvicorn app.main:app --reload --port 8000
```

Navigate to `http://localhost:8000`. Expected: page loads, no 500 error, Section C label "Corporate Leads Pipeline" is visible (even if unstyled). If you see a Jinja2 `UndefinedError`, check that the key name in `dummy_data.py` matches exactly (`"pipeline"` and `"pipeline_collections"` etc.).

- [ ] **Step 3: Commit**

```bash
git add app/templates/dashboard.html
git commit -m "[TASK-005] feat: add Section C corporate leads pipeline HTML"
```

---

## Task 3: Add pipeline CSS

**Files:**
- Modify: `app/static/style.css`

- [ ] **Step 1: Append pipeline styles to the end of `style.css`**

Add the following block at the very end of `app/static/style.css`:

```css
/* ── Corporate Leads Pipeline (Section C) ── */
.pipeline-flow {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 0;
}

.pipeline-stage-card {
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
    padding: 1rem;
    background: #1c2330;
    border: 1px solid var(--color-border);
    border-left: none;
    position: relative;
}

.pipeline-stage-card:first-child {
    border-left: 1px solid var(--color-border);
    border-radius: 6px 0 0 6px;
}

.pipeline-stage-card:last-child {
    border-radius: 0 6px 6px 0;
}

/* Connector arrow between stages */
.pipeline-stage-card:not(:last-child)::after {
    content: '›';
    position: absolute;
    right: -0.55rem;
    top: 1rem;
    color: var(--color-text-secondary);
    font-size: 1rem;
    line-height: 1;
    z-index: 2;
}

.pipeline-stage-name {
    font-size: 0.62rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: var(--color-text-secondary);
}

.pipeline-count {
    font-family: var(--font-heading);
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--color-text-primary);
    line-height: 1;
}

.pipeline-target {
    font-family: var(--font-body);
    font-size: 0.72rem;
    font-weight: 400;
    color: var(--color-text-secondary);
}

.pipeline-value {
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--color-accent);
    min-height: 1.1rem;
}

.pipeline-footer {
    display: flex;
    align-items: center;
    gap: 0.3rem;
    flex-wrap: wrap;
}

.pipeline-delta-text {
    font-size: 0.68rem;
    color: var(--color-text-secondary);
}

.pipeline-details-link {
    display: inline-block;
    margin-top: auto;
    padding-top: 0.5rem;
    font-size: 0.72rem;
    color: var(--color-accent);
    cursor: pointer;
    text-decoration: none;
    border-top: 1px solid var(--color-border);
    transition: opacity 0.15s;
}

.pipeline-details-link:hover {
    opacity: 0.7;
}

/* Pipeline aging panel (full-width slide-down below the flow) */
.pipeline-aging-panel {
    margin-top: 0.5rem;
}

.pipeline-aging-panel.open {
    max-height: 1000px !important;
    border-top: 1px solid var(--color-border);
}

/* Responsive */
@media (max-width: 1200px) {
    .pipeline-flow {
        grid-template-columns: repeat(3, 1fr);
        overflow: visible;
    }

    .pipeline-stage-card {
        border-left: 1px solid var(--color-border);
        border-radius: 0;
    }

    .pipeline-stage-card:not(:last-child)::after {
        display: none;
    }
}

@media (max-width: 768px) {
    .pipeline-flow {
        grid-template-columns: repeat(2, 1fr);
    }
}
```

- [ ] **Step 2: Hard-reload browser and verify layout**

With the dev server still running (`uvicorn app.main:app --reload --port 8000`), navigate to `http://localhost:8000` and hard-reload (`Ctrl+Shift+R`).

Verify:
- 6 stage cards appear horizontally in a single row on desktop
- Stage names are uppercase small text (secondary color)
- Count number is large and bold
- `/ target` appears beside count in secondary color
- Value shows amber for monetary stages, "—" for Leads and Meetings
- % badge appears with correct color: Leads=green (84%), Proposals=amber (73%), Collections=amber (50%), etc.
- ▲ arrow is green for up-trending stages, ▼ is red for Collections
- "Details →" appears at the bottom of each card in amber

- [ ] **Step 3: Commit**

```bash
git add app/static/style.css
git commit -m "[TASK-005] feat: add pipeline CSS — 6-col flow, stage cards, aging panel"
```

---

## Task 4: End-to-end interaction check + PR

**Files:** None (verification only)

- [ ] **Step 1: Test the aging drill-down interaction**

With the server running, click "Details →" on the **Collections** card. Verify:
- The aging panel slides down below the pipeline flow
- 5 bucket pills appear: 7 Days (count=2), 14 Days (0, disabled), 21 Days (0, disabled), 90 Days (0, disabled), NPA (count=1)

Click the **7 Days** pill. Verify a table appears with:
```
Fidelitus Transactions | Amit Shah  | Rs.2 Cr   | 5d  | Payment by EOM confirmed
Fidelitus Projects     | Deepa Iyer | Rs.1.2 Cr | 7d  | Client OOO till Friday
```

Click the **NPA** pill. Verify a table appears with:
```
Fidelitus GCC Nexus | Kiran Bhat | Rs.2.1 Cr | 95d | Negotiations ongoing
```

Click "Details →" on a **Leads** card. Verify the panel slides down with all 5 pills disabled (no aging data).

Click "Details →" on Collections again to collapse the panel. Verify it slides back up.

- [ ] **Step 2: Check % badge colors match the color rule**

| Stage | Pct | Expected color |
|---|---|---|
| Leads | 84% | Green |
| Meetings | 72% | Amber |
| Proposals | 73% | Amber |
| Orders | 60% | Amber |
| Invoices | 50% | Red-orange |
| Collections | 50% | Red-orange |

> Note: 50% falls in the 26–50% band → Red-orange. 60% → Amber. 72–73% → Amber. 84% → Green.

- [ ] **Step 3: Update task file**

In `tasks/TASK-005-corp-pipeline.md`, mark all checklist items as done (change `- [ ]` to `- [x]`).

- [ ] **Step 4: Push branch and open PR**

```bash
git push -u origin feature/TASK-005-kpi-drill-panels
```

Then open a PR from `feature/TASK-005-kpi-drill-panels` → `master` with title:
`[TASK-005] feat: add corporate leads pipeline section (Section C)`

Body:
```
## Summary
- Adds Section C — Corporate Leads Pipeline — below the Subsidiaries cards
- 6-stage horizontal flow: Leads → Meetings → Proposals → Orders → Invoices → Collections
- Each card shows count/target, value (Rs.Cr), % badge (color-coded), WoW delta
- "Details →" slides down per-stage aging drill-down (reuses Session 04 components)
- Collections aging: 2 items in 7d bucket, 1 NPA item (per spec)

## Files changed
- `app/mockup/dummy_data.py` — pipeline data + 6 aging entries
- `app/templates/dashboard.html` — Section C block
- `app/static/style.css` — pipeline CSS

## Test plan
- [ ] Page loads without errors
- [ ] 6 stage cards render in a single horizontal row (desktop)
- [ ] % badges show correct colors per the < 25 / 26–50 / 51–75 / > 75 rule
- [ ] Collections "Details →" opens aging panel; 7d and NPA pills work
- [ ] All other stage panels open (all pills disabled — no data)
- [ ] Panel collapses when "Details →" clicked again
```
