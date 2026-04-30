# TASK-001: MD Dashboard Scaffold

**Status:** In Progress
**Assigned:** Phase 0 (Srinivas)
**Scope:** app/ root + app/mockup/ + app/static/ + app/templates/

## Deliverables

- [x] tasks/TASK-001-scaffold.md (this file)
- [ ] .env (PRODUCTION=1)
- [ ] .gitignore (Python + .env)
- [ ] requirements.txt (fastapi, uvicorn, motor, python-dotenv, jinja2)
- [ ] app/config.py (settings loader)
- [ ] app/main.py (FastAPI app factory)
- [ ] app/mockup/routes.py (GET "/" route)
- [ ] app/templates/base.html (Jinja2 base, dark theme)
- [ ] app/templates/dashboard.html (dashboard page)
- [ ] app/static/style.css (CSS variables from md_dashboard_v2.html)

## Design Constraints

- No heavy JS frameworks — vanilla JS only
- Graphics: light, clear, distinct
- Dark bg #0d1117, surface #161b22, accent amber #e8a838
- Font: DM Sans (body) + Syne (headings) from Google Fonts
- Reuse CSS variables from md_dashboard_v2.html

## Git Branches

- base: main
- feature: dev (PR optional for Phase 0)
- commits: [TASK-001] verb: what changed
