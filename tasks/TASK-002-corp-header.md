# TASK-002 -- Corporate Header & KPI Strip

**Status:** In Progress
**Session:** s01 (Phase 0 -- Mockup)
**Scope:** app/mockup/dummy_data.py, app/mockup/routes.py,
           app/templates/dashboard.html, app/static/style.css

## Goal
Build Section A (header bar with live clock + time-filter toggle) and
Section B (6-card corporate KPI strip) using dummy data rendered via Jinja2.

## Acceptance Criteria
- [ ] Header bar: title left, clock updates every second, WTD/MTD/QTD/YTD toggle right
- [ ] WTD active by default with amber highlight; clicking another tab highlights it
- [ ] 6 KPI cards rendered in one row from dummy_data.py (not hardcoded in HTML)
- [ ] Each card: label, current value (large bold), target (small muted), % badge, delta arrow
- [ ] % badge color follows the 4-band color rule (red / red-orange / amber / green)
- [ ] Delta: green ^ arrow for positive, red v arrow for negative, with absolute value
- [ ] Numbers formatted as "Rs. XX Cr" via Jinja2 custom filter
- [ ] No JS frameworks -- vanilla JS only
- [ ] PRODUCTION=1 serves dummy data; no MongoDB calls

## Files Changed
- CREATE  app/mockup/dummy_data.py
- MODIFY  app/mockup/routes.py
- MODIFY  app/templates/dashboard.html
- MODIFY  app/static/style.css
