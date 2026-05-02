# TASK-006 -- Weekly Pulse Panel

**Status:** In Progress
**Session:** s06 (Phase 0 -- Mockup)
**Scope:** app/mockup/dummy_data.py, app/mockup/routes.py,
           app/templates/dashboard.html, app/static/style.css,
           app/static/script.js

## Goal
Add a "Weekly Pulse" section showing this week's committed vs actual revenue
delta for the MD's review meeting. Section visible only on WTD filter; hidden
for MTD/QTD/YTD. Also adds the WTD/MTD/QTD/YTD time-filter pill strip to the
dashboard header (planned in s02, implemented here).

## Acceptance Criteria
- [ ] WEEKLY_PULSE dict added to dummy_data.py with 6 company rows + total
- [ ] weekly_pulse passed to Jinja2 template context in routes.py
- [ ] Header right side: phase badge top + time-filter pills (WTD/MTD/QTD/YTD) below
- [ ] WTD pill active (amber) by default; clicking another pill highlights it
- [ ] Weekly Pulse section placed between Corporate KPIs and Subsidiaries
- [ ] Panel header shows week range and committed date
- [ ] Comparison table: Company / Committed / Actual / Delta / Status columns
- [ ] Delta column: colored arrow + value (green for positive, red for negative)
- [ ] Status badge: 4-band color rule applied to actual_pct
- [ ] Clicking a company row expands that company's aging panel (Section B)
- [ ] Corporate Total row visible but NOT clickable
- [ ] MTD / QTD / YTD filters hide the Weekly Pulse section
- [ ] WTD filter shows the Weekly Pulse section

## Files Changed
- MODIFY  app/mockup/dummy_data.py
- MODIFY  app/mockup/routes.py
- MODIFY  app/templates/dashboard.html
- MODIFY  app/static/style.css
- MODIFY  app/static/script.js

## Design Spec
docs/superpowers/specs/2026-05-02-weekly-pulse-design.md

## Implementation Plan
docs/superpowers/plans/2026-05-02-weekly-pulse.md
