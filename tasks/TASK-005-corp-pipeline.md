# TASK-005 — Corporate Leads Pipeline

Branch: `feature/TASK-005-corp-pipeline`
Session: s05 (Phase 0 mockup)
Spec: `docs/superpowers/specs/2026-05-01-corp-pipeline-design.md`

## Goal

Add Section C — "Corporate Leads Pipeline" — below the Subsidiaries company cards.
6-stage horizontal pipeline (Leads → Meetings → Proposals → Orders → Invoices → Collections)
with count, target, % badge, WoW delta, and per-stage aging drill-down panel.

## Scope (3 files only)

- `app/mockup/dummy_data.py`
- `app/templates/dashboard.html`
- `app/static/style.css`

## Checklist

- [x] Add `PIPELINE_DATA` to `DASHBOARD_DATA` in `dummy_data.py`
- [x] Add `AGING_DATA["pipeline_*"]` entries for all 6 stages in `dummy_data.py`
- [x] Add Section C to `dashboard.html` (pipeline flow + aging panels)
- [x] Add pipeline CSS to `style.css`
- [x] Visual check in browser
- [x] Commit + PR

## Status

- [x] Complete
