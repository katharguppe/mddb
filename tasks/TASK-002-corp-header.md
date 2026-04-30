# TASK-002 -- Corporate Header & KPI Strip

**Status:** Done
**Session:** s01 (Phase 0 -- Mockup)
**Scope:** app/mockup/dummy_data.py, app/mockup/routes.py,
           app/templates/dashboard.html, app/static/style.css

## Goal
Build Section A (header bar with live clock + time-filter toggle) and
Section B (6-card corporate KPI strip) using dummy data rendered via Jinja2.

## Acceptance Criteria
- [x] Header bar: title left, clock updates every second, WTD/MTD/QTD/YTD toggle right
- [x] WTD active by default with amber highlight; clicking another tab highlights it
- [x] 6 KPI cards rendered in one row from dummy_data.py (not hardcoded in HTML)
- [x] Each card: label, current value (large bold), target (small muted), % badge, delta arrow
- [x] % badge color follows the 4-band color rule (red / red-orange / amber / green)
- [x] Delta: green ^ arrow for positive, red v arrow for negative, with absolute value
- [x] Numbers formatted as "Rs. XX Cr" via Jinja2 custom filter
- [x] No JS frameworks -- vanilla JS only
- [x] PRODUCTION=1 serves dummy data; no MongoDB calls

## Files Changed
- CREATE  app/mockup/dummy_data.py
- MODIFY  app/mockup/routes.py
- MODIFY  app/templates/dashboard.html
- MODIFY  app/static/style.css
