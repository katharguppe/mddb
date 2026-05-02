# Developer Handoff — MD Dashboard . Fidelitus Corp

> Phase 0 mockup is complete. This document tells you everything you need to start Phase 1.

---

## a. How to Run the Mockup (PRODUCTION=1)

**Prerequisites:** Python 3.13, pip

```bash
# 1. Clone the repo and enter the project
cd D:/Fidelitus/mddb

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install fastapi uvicorn[standard] jinja2 python-dotenv pydantic-settings motor

# 4. Create .env (copy from .env.example)
cp .env.example .env
# Ensure PRODUCTION=1 is set

# 5. Run the server
uvicorn app.main:app --reload --port 8000

# 6. Open in browser
# http://localhost:8000
```

The dashboard loads with dummy data. No database connection required.

---

## b. Where Dummy Data Lives

All Phase 0 data is in **`app/mockup/dummy_data.py`**.

| Variable | Contents |
|---|---|
| `DASHBOARD_DATA` | Corporate KPIs + 6 company KPI cards + pipeline stages |
| `AGING_DATA` | Committed-but-delayed items per company per aging bucket |
| `KPI_DETAILS` | Drill-down rows per company per KPI tab (Revenue/Invoiced/Meetings/Proposals) |
| `KPI_AGING` | Committed-delayed items per company per KPI tab |
| `WEEKLY_PULSE` | Week-on-week committed vs actual per company per KPI |

The route that serves all this data: `app/mockup/routes.py` → GET `/`

---

## c. Where to Wire Real Data (Phase 1)

When `PRODUCTION=0`, real MongoDB data flows through:

```
app/data/<module>.py    ← query functions (Motor async)
app/api/<module>.py     ← FastAPI routers that call data functions
app/main.py             ← mounts api routers when PRODUCTION=0
app/templates/          ← same templates, same variable names
```

The templates expect the **same variable names** as the mockup routes pass.
Match these exactly when writing Phase 1 routes:

| Template variable | Mockup source | Phase 1 source |
|---|---|---|
| `data` | `DASHBOARD_DATA` | aggregated from MongoDB |
| `aging` | `AGING_DATA` | `app/data/aging.py` |
| `kpi_details` | `KPI_DETAILS` | `app/data/leads.py` + `app/data/finance.py` |
| `kpi_aging` | `KPI_AGING` | `app/data/aging.py` |
| `weekly_pulse` | `WEEKLY_PULSE` | `app/data/targets.py` |

---

## d. Session Map

| Session | Scope | Owner |
|---|---|---|
| s01–s07 | Phase 0 mockup (complete) | Srinivas |
| s08 | Read-only audit of all modules | Developer |
| s09 | `app/auth/` — CRM JWT authentication | Developer |
| s10 | `app/data/leads.py` + `app/api/leads.py` | Developer |
| s11 | `app/data/finance.py` + `app/api/finance.py` | Developer |
| s12 | `app/data/targets.py` + `app/api/targets.py` | Developer |
| s13 | `app/data/companies.py` + `app/api/companies.py` | Developer |
| s14 | `app/data/aging.py` + `app/api/aging.py` | Developer |
| s15 | `.env` + `app/main.py` — production cutover | Developer |

Start from **s08** (`tasks/TASK-008-db-audit.md` — to be created).

---

## e. MongoDB Collections → KPI Mapping

| Dashboard KPI | MongoDB Collection(s) | Key Fields |
|---|---|---|
| Revenue (Booking) | `deals` | `deal_value`, `status`, `closed_date` |
| Invoiced Amounts | `invoicereports` | `invoice_amount`, `invoice_date` |
| Payments Received | `invoicepayments`, `invoicepaymentshares` | `payment_amount`, `payment_date` |
| Meetings Done | `meetings` | `meeting_date`, `status` |
| Proposals Submitted | `mdfollowupproposals` | `proposal_date`, `amount` |
| Target for Year | `bdtargets`, `usertargets`, `employeetargets` | `target_amount`, `year` |
| Lead Pipeline | `leads`, `ftsleads`, `fidelitusleads` | `stage`, `source`, `created_at` |
| Aging (payments) | `invoicepayments` | `due_date`, `status` |
| Aging (pipeline) | `leads` | `stage`, `updated_at` |
| Department / Company master | `departments` | `company`, `department` |
| Users / Team | `users` | `name`, `department`, `role` |
| MD Follow-ups | `mdfollowups`, `mdassigntasks` | `follow_up_date`, `status` |
| Pipeline Stages master | `stages` | `stage_name`, `order` |

---

## f. CRM Auth Integration Points

The CRM uses **JWT tokens** stored in `user_access_tokens`.

Phase 1 auth flow (to be built in s09):
1. `POST /auth/login` → verify against `users` collection → issue JWT
2. All dashboard routes require `Authorization: Bearer <token>` header
3. `app/auth/middleware.py` decodes JWT on each request
4. MD role check: `user.role == 'md'` or equivalent from `roles` / `user_roles`

Files to create in s09:
- `app/auth/__init__.py`
- `app/auth/middleware.py` — JWT decode + role check
- `app/auth/routes.py` — login endpoint

---

## g. ENV Variables (.env.example)

Create `.env.example` in the project root with:

```bash
# .env.example — copy to .env and fill in values

# Phase flag
# "1" = Phase 0 mockup (dummy data, no DB)
# "0" = Phase 1 live (MongoDB + CRM auth)
PRODUCTION=1

# MongoDB (Phase 1 only — leave blank for Phase 0)
MONGO_URI=mongodb://localhost:27017
DB_NAME=fidelitus

# JWT Secret (Phase 1 only)
SECRET_KEY=replace-with-a-random-secret-key
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=480
```

---

## h. Design Constraints

These are fixed. Do not change them without MD approval.

| Constraint | Value |
|---|---|
| JS framework | None — vanilla JS only |
| CSS framework | None — custom CSS only |
| Background | `#0d1117` |
| Surface | `#161b22` |
| Accent | `#e8a838` (amber) |
| Body font | DM Sans |
| Heading font | Syne |
| KPI color: < 25% | `#ef4444` (bright red) |
| KPI color: 26–50% | `#f97316` (red-orange) |
| KPI color: 51–75% | `#f59e0b` (amber) |
| KPI color: > 75% | `#22c55e` (green) |
| Aging buckets | 7d · 14d · 21d · 90d · NPA (>90d) |

Design reference: `md_dashboard_v2.html` in project root.
