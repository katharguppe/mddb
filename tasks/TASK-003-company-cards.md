# TASK-003 -- Company Cards

**Status:** Done
**Session:** s03 (Phase 0 -- Mockup)
**Scope:** app/mockup/dummy_data.py, app/mockup/routes.py,
           app/templates/dashboard.html, app/static/style.css

## Goal
Add 6 subsidiary company cards in a 3-per-row CSS grid below the
corporate KPI strip, rendered from dummy_data.py via Jinja2.

## Acceptance Criteria
- [x] 6 company cards rendered in a 3-per-row grid from dummy_data.py (not hardcoded)
- [x] Each card has a 3px top border in its unique dot color
- [x] Each card shows all 6 KPIs with value, % badge (correct color band), and delta arrow
- [x] "Know More" button toggles slide-down panel with JS (no page reload)
- [x] Details panel shows placeholder text "Aging analysis — Session 04"
- [x] PRODUCTION=1 serves dummy data; no MongoDB calls
- [x] Responsive: 1 column on mobile (768px and below)
- [x] No JS frameworks -- vanilla JS only

## Files Changed
- CREATE  app/mockup/dummy_data.py
- MODIFY  app/mockup/routes.py   (3-line change -- necessary dependency)
- MODIFY  app/templates/dashboard.html
- MODIFY  app/static/style.css
