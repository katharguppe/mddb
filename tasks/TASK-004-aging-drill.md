# TASK-004 -- Aging Drill-Down Panel

**Status:** In Progress
**Session:** s04 (Phase 0 -- Mockup)
**Scope:** app/mockup/dummy_data.py, app/templates/dashboard.html,
           app/templates/partials/aging_panel.html (create),
           app/static/style.css, app/static/script.js ONLY.

## Goal
Replace the placeholder "Know More" panel on each company card with a live
aging drill-down: 5 bucket pills (7d / 14d / 21d / 90d / NPA), each expanding
a table of committed-but-not-delivered payment items. Corporate KPI strip cards
are also clickable to show an aggregated corporate aging panel.

## Acceptance Criteria
- [ ] Aging data in dummy_data.py for all 6 companies + corporate aggregate
- [ ] 5 aging bucket pills rendered per company card in the Know More panel
- [ ] Each pill shows: bucket label + item count + total value (Rs.)
- [ ] Clicking a pill shows/hides that bucket's detail table (no page reload)
- [ ] Clicking the same pill again collapses the table
- [ ] Clicking a different pill collapses current + expands new one
- [ ] Table columns: Company/Team | Team Member | Value (Rs.) | Days Overdue | Reason
- [ ] Corporate KPI cards clickable → shows corporate aging panel below the strip
- [ ] Corporate panel aggregates all 6 companies, same 5-bucket structure
- [ ] Pill color: amber accent (#e8a838) when active; muted when inactive
- [ ] Panel slide-down max-height is sufficient for table content (JS-driven)
- [ ] Vanilla JS only, no frameworks

## Files Changed
- MODIFY  app/mockup/dummy_data.py
- CREATE  app/templates/partials/aging_panel.html
- MODIFY  app/templates/dashboard.html
- MODIFY  app/static/style.css
- MODIFY  app/static/script.js
