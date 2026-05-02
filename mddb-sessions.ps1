# ==============================================================================
# mddb-sessions.ps1
# MD Dashboard -- Fidelitus Corp  |  Session Launcher
# Owner: Srinivas / Fidelitus Corp
#
# PHASE 0  (Sessions s01-s07)  ->  Srinivas runs -- full mockup, dummy data
# PHASE 1  (Sessions s08-s15)  ->  Developer runs -- live MongoDB integration
#
# Usage:
#   .\mddb-sessions.ps1 -Session list           # list all sessions
#   .\mddb-sessions.ps1 -Session s01-scaffold   # run a session
#   .\mddb-sessions.ps1 -Session audit          # read-only audit (any phase)
#   .\mddb-sessions.ps1 -Session debug          # one error . one file
# ==============================================================================

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet(
        "s01-scaffold",
        "s02-corp-header",
        "s03-company-cards",
        "s04-aging-drill",
        "s05-corp-pipeline",
        "s06-weekly-delta",
        "s07-mockup-polish",
        "s08-db-audit",
        "s09-auth-hook",
        "s10-leads-wire",
        "s11-finance-wire",
        "s12-targets-wire",
        "s13-company-split",
        "s14-aging-live",
        "s15-prod-cutover",
        "audit",
        "debug",
        "list"
    )]
    [string]$Session
)

$PROJECT_ROOT = "D:\Fidelitus\mddb"
$HAIKU        = "claude-haiku-4-5-20251001"
$SONNET       = "claude-sonnet-4-6"

# ==============================================================================
#  SESSION DEFINITIONS
# ==============================================================================
$sessions = @{

    # --------------------------------------------------------------------------
    #  PHASE 0 -- MOCKUP  (Srinivas runs s01 -> s07)
    # --------------------------------------------------------------------------

    "s01-scaffold" = @{
        model = $HAIKU
        phase = "0 - Mockup"
        task  = "TASK-001"
        label = "Session 01 - Project Scaffold"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: Python 3.13, FastAPI, Motor (async MongoDB), Jinja2, Uvicorn, vanilla HTML/CSS/JS
Task file: tasks/TASK-001-scaffold.md  (create it first)
Module scope: app/ root, app/mockup/, app/static/, app/templates/  ONLY.
PRODUCTION flag: currently 1 (mockup mode -- use dummy data throughout Phase 0).

GOAL -- Create the working project skeleton:
1. app/main.py
   FastAPI app factory. Read PRODUCTION from .env.
   PRODUCTION=1 -> serve mockup routes from app/mockup/
   PRODUCTION=0 -> serve live routes from app/api/

2. app/config.py
   Load .env via python-dotenv. Expose settings object.

3. app/mockup/routes.py
   Single GET "/" route -> renders templates/dashboard.html

4. app/templates/base.html
   Base Jinja2 template. Include DM Sans + Syne from Google Fonts.
   Dark theme: bg #0d1117, surface #161b22, accent amber #e8a838.

5. app/templates/dashboard.html
   Extends base. Empty body for now -- just heading "MD Dashboard . Fidelitus Corp".

6. app/static/style.css
   CSS variables matching md_dashboard_v2.html already in project root.
   Reference that file for exact palette -- do NOT re-invent.

7. requirements.txt
   fastapi, uvicorn[standard], motor, python-dotenv, jinja2

8. .gitignore
   Standard Python + .env

Design constraints:
- No JS frameworks. Vanilla JS only.
- Graphics: light, clear, distinct -- nothing fancy.
- Reuse the exact CSS variables already in md_dashboard_v2.html.

Context7: use for FastAPI + Jinja2 StaticFiles mount API.
PDCA: present plan before touching any file. One file change per step.
'@
    }

    "s02-corp-header" = @{
        model = $SONNET
        phase = "0 - Mockup"
        task  = "TASK-002"
        label = "Session 02 - Corporate Header + KPI Strip"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: FastAPI + Jinja2 + vanilla HTML/CSS/JS
Task file: tasks/TASK-002-corp-header.md  (create it first)
Module scope: app/mockup/routes.py, app/mockup/dummy_data.py,
              app/templates/dashboard.html, app/static/style.css  ONLY.
PRODUCTION=1 (dummy data throughout).

GOAL -- Build the top section of the dashboard with dummy data.

SECTION A -- Header bar
  Left:  "FIDELITUS CORP . MD DASHBOARD"  |  Live clock (HH:MM . date)
  Right: Time-filter toggle: WTD . MTD . QTD . YTD
         (WTD = active by default, amber highlight, vanilla JS toggle)

SECTION B -- Corporate KPI Strip (6 cards in one row)
  Cards: Target for Year . Revenue (Booking) . Invoiced . Payments . Meetings . Proposals
  Each card shows:
    - Label
    - Current value  (large, bold)
    - Target value   (small, muted)
    - % achieved     (colored badge per rule below)
    - Delta arrow vs last week  (^ green / v red with absolute delta value)

Color coding rule (% of committed target achieved this period):
  < 25%   -> bright red   #ef4444
  26-50%  -> red-orange   #f97316
  51-75%  -> amber        #f59e0b
  >75%    -> green        #22c55e

DUMMY DATA (FY 2025-26, week ending 2026-04-25):
  Target for Year:   Rs.240 Cr  achieved Rs.187 Cr  (78%)   delta +Rs.6.2 Cr WoW
  Revenue/Booking:   Rs.240 Cr  achieved Rs.142 Cr  (59%)   delta +Rs.4.1 Cr WoW
  Invoiced:          Rs.180 Cr  achieved Rs.98 Cr   (54%)   delta +Rs.3.8 Cr WoW
  Payments:          Rs.160 Cr  achieved Rs.71 Cr   (44%)   delta -Rs.1.2 Cr WoW
  Meetings:          1200        achieved 847         (71%)   delta +32 WoW
  Proposals:         900         achieved 512         (57%)   delta +18 WoW

Dummy data must live in app/mockup/dummy_data.py as a Python dict -- not hardcoded in HTML.
Jinja2 renders it into the template.

Context7: use for Jinja2 template filters (format large numbers as Rs. XX Cr).
PDCA: present plan before touching any file.
'@
    }

    "s03-company-cards" = @{
        model = $SONNET
        phase = "0 - Mockup"
        task  = "TASK-003"
        label = "Session 03 - 6 Company Cards"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: FastAPI + Jinja2 + vanilla HTML/CSS/JS
Task file: tasks/TASK-003-company-cards.md  (create it first)
Module scope: app/mockup/dummy_data.py, app/templates/dashboard.html,
              app/static/style.css  ONLY.
PRODUCTION=1 (dummy data).

GOAL -- Add the 6 subsidiary company cards below the corporate KPI strip.

Layout: 3 cards per row (CSS grid), each company in a bordered box.

Companies:
  1. Fidelitus Transactions
  2. Fidelitus Projects
  3. Fidelitus FMS
  4. Fidelitus HR Labs
  5. Fidelitus Technology
  6. Fidelitus GCC Nexus

Each company card shows (same 6 KPIs as corporate strip):
  - Company name + a color accent dot (unique per company)
  - Target . Revenue . Invoiced . Payments . Meetings . Proposals
  - % achieved badge (same color rule as Session 02)
  - Delta vs last week (^ up / v down)
  - "Know More ->" button (amber, opens a details panel -- wire in Session 04)

DUMMY DATA (realistic, varied percentages so colors differ):
  Fidelitus Transactions: Target Rs.80Cr  Rev Rs.68Cr(85%^)  Inv Rs.54Cr(68%)  Pay Rs.42Cr(53%)  Meet 320(88%^)  Prop 180(79%^)
  Fidelitus Projects:     Target Rs.60Cr  Rev Rs.29Cr(48%v)  Inv Rs.21Cr(35%)  Pay Rs.14Cr(23%)  Meet 210(61%)   Prop 140(55%)
  Fidelitus FMS:          Target Rs.30Cr  Rev Rs.24Cr(80%^)  Inv Rs.19Cr(63%)  Pay Rs.16Cr(53%)  Meet 180(72%)   Prop 95(67%)
  Fidelitus HR Labs:      Target Rs.25Cr  Rev Rs.11Cr(44%v)  Inv Rs.8Cr(32%)   Pay Rs.5Cr(20%)   Meet 150(48%)   Prop 62(41%)
  Fidelitus Technology:   Target Rs.20Cr  Rev Rs.9Cr(45%)    Inv Rs.6Cr(30%)   Pay Rs.4Cr(20%)   Meet 87(57%)    Prop 35(47%)
  Fidelitus GCC Nexus:    Target Rs.25Cr  Rev Rs.1Cr(4%v)    Inv Rs.0(0%)      Pay Rs.0(0%)      Meet 24(21%)    Prop 18(24%)

Add dummy data to app/mockup/dummy_data.py under key "companies".

"Know More" button: clicking it shows/hides a slide-down details panel
on the same card (vanilla JS toggle, no page reload).
For now: placeholder text "Aging analysis -- Session 04".

PDCA: present plan before touching any file.
'@
    }

    "s04-aging-drill" = @{
        model = $SONNET
        phase = "0 - Mockup"
        task  = "TASK-004"
        label = "Session 04 - Aging Drill-Down Panel"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: FastAPI + Jinja2 + vanilla HTML/CSS/JS
Task file: tasks/TASK-004-aging-drill.md  (create it first)
Module scope: app/mockup/dummy_data.py, app/templates/dashboard.html,
              app/templates/partials/aging_panel.html (create),
              app/static/style.css  ONLY.
PRODUCTION=1 (dummy data).

GOAL -- Build the aging drill-down shown when MD clicks "Know More ->" on any
company card OR on any corporate KPI value.

Aging rule (MD specified):
  Committed but not delivered, grouped by days overdue:
  7 days . 14 days . 21 days . 90 days . NPA (> 90 days)

AGING PANEL STRUCTURE (slide-down within the card):
  Row of 5 aging bucket summary pills (7d . 14d . 21d . 90d . NPA)
  Each pill: bucket label + count + total value (Rs.)
  Clicking a pill expands a table:
    | Company/Team | Team Member | Value (Rs.) | Days Overdue | Reason Entered |

DUMMY DATA -- Fidelitus Transactions -- Payments aging:
  7 days:  3 items  Rs.2.1 Cr
    - Fidelitus Trans / Rajesh Kumar  / Rs.80L  / 6d   / Client travel delay, confirming by Mon
    - Fidelitus Trans / Priya Menon   / Rs.75L  / 7d   / Cheque in transit
    - Fidelitus Trans / Anand Rao     / Rs.55L  / 5d   / Bank processing delay
  14 days: 2 items  Rs.1.4 Cr
    - Fidelitus Trans / Suresh Nair   / Rs.90L  / 13d  / NEFT rejected, re-initiated
    - Fidelitus Trans / Kavitha Reddy / Rs.50L  / 11d  / Awaiting MD approval from client
  21 days: 1 item   Rs.0.6 Cr
    - Fidelitus Trans / Vikram Singh  / Rs.60L  / 19d  / Legal vetting on agreement
  90 days: 1 item   Rs.1.2 Cr
    - Fidelitus Trans / Mohan Das     / Rs.1.2Cr/ 67d  / Client undergoing internal restructuring
  NPA:     1 item   Rs.0.9 Cr
    - Fidelitus Trans / Renu Sharma   / Rs.90L  / 112d / Dispute raised, legal notice sent

Apply same aging dummy data structure (different names/amounts) for all 6 companies.
Store in app/mockup/dummy_data.py under "aging" key, indexed by company slug.

Corporate KPIs (from Session 02) should also be clickable to show a corporate-level
aging panel aggregating across all companies (same buckets, shows company column).

Vanilla JS only. No page reload. Toggle bucket pill -> show/hide table rows.
PDCA: present plan before touching any file.
'@
    }

    "s05-corp-pipeline" = @{
        model = $SONNET
        phase = "0 - Mockup"
        task  = "TASK-006"
        label = "Session 05 cont. - KPI Aging Tabs + Pipeline Data"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: FastAPI + Jinja2 + vanilla HTML/CSS/JS
PRODUCTION=1 (dummy data).

== COMPLETED IN PREVIOUS SESSION (do NOT redo) ==
TASK-005 is DONE and PR#4 is open (feature/TASK-005-kpi-drill-panels -> master).
  - Section C: Corporate Leads Pipeline added (6 stage cards, Details-> aging)
  - dummy_data.py: DASHBOARD_DATA["pipeline"] + AGING_DATA["pipeline_*"] entries
  - dashboard.html: Section C block using existing aging_panel macro
  - style.css: pipeline CSS (6-col grid, stage cards, responsive)
  - PR#4: merge it first before starting new work if not already merged.

== THIS SESSION: TASK-006 ==
Task file: tasks/TASK-006-kpi-aging-tabs.md  (create it)
Spec: docs/superpowers/specs/2026-05-01-kpi-aging-tabs-design.md  (READ THIS FIRST)
Branch: create feature/TASK-006-kpi-aging-tabs from master after merging PR#4.

Module scope:
  app/mockup/dummy_data.py
  app/templates/partials/aging_panel.html
  app/static/script.js
  app/static/style.css
  app/templates/dashboard.html

GOAL A -- KPI aging tabs in individual company Know More panels.
When MD clicks "Know More" on any company card, show a two-level drill:
  Level 1: [ Revenue ] [ Invoiced ] [ Payments ] [ Meetings ] [ Proposals ]
  Level 2: [ 7 Days ] [ 14 Days ] [ 21 Days ] [ 90 Days ] [ NPA ]
  Level 3: detail table (Company/Team | Member | Value | Days | Reason)

Corporate aging panel (Section A) and pipeline aging (Section C): NO CHANGE.

DATA STRUCTURE CHANGE (company entries only):
  Current: AGING_DATA["transactions"] = { "7d": {...}, "14d": {...}, ... }
  New:     AGING_DATA["transactions"] = {
             "revenue":   { "7d": {...}, "14d": {...}, "21d": {}, "90d": {}, "npa": {} },
             "invoiced":  { same 5 buckets },
             "payments":  { same 5 buckets },   <- existing items move here
             "meetings":  { same 5 buckets, value="--" },
             "proposals": { same 5 buckets },
           }
All 6 company slugs change. _build_corporate_aging() must be updated to flatten
across all KPIs (still produces 2-level output for corporate panel).
Pipeline entries stay 2-level.

NEW MACRO: kpi_aging_panel(company_id, aging) in aging_panel.html
NEW JS:    toggleAgingKpi(companyId, kpi) in script.js
           toggleAgingBucket signature -> toggleAgingBucket(companyId, kpi, bucket)
NEW CSS:   .aging-kpi-tab styles in style.css
TEMPLATE:  company card calls kpi_aging_panel() instead of aging_panel()

GOAL B -- Add dummy data to all pipeline aging stages.
Currently Leads/Meetings/Proposals/Orders/Invoices pipeline stages show all-disabled pills.
Populate each with 1-2 real items in 7d/14d bucket.
Exact dummy items are in the spec file.
For Leads and Meetings: value="--" (count-based, no Rs).

PDCA: read the spec first, then present implementation plan before touching any file.
'@
    }

    "s06-weekly-delta" = @{
        model = $SONNET
        phase = "0 - Mockup"
        task  = "TASK-006"
        label = "Session 06 - Weekly Delta / Committed vs Actual"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: FastAPI + Jinja2 + vanilla HTML/CSS/JS
Task file: tasks/TASK-006-weekly-delta.md  (create it first)
Module scope: app/mockup/dummy_data.py, app/templates/dashboard.html,
              app/static/style.css  ONLY.
PRODUCTION=1 (dummy data).

GOAL -- Add a "Weekly Pulse" section showing this week's commitments vs actuals
for the MD's review meeting. This surfaces the DELTA prominently.

WEEKLY PULSE PANEL -- placed just above the company cards (below corporate KPI strip).
  Header: "Week of 21 Apr - 25 Apr 2026  .  Last committed: Mon 21 Apr"

  Two-column comparison table per company:
  | Company                  | Committed (Mon) | Actual (Fri) | Delta    | Status |
  |--------------------------|-----------------|--------------|----------|--------|
  | Fidelitus Transactions   | Rs.9Cr          | Rs.9.8Cr     | +0.8Cr   | GREEN  |
  | Fidelitus Projects       | Rs.4Cr          | Rs.1.8Cr     | -2.2Cr   | RED    |
  | Fidelitus FMS            | Rs.2.5Cr        | Rs.2.1Cr     | -0.4Cr   | ORANGE |
  | Fidelitus HR Labs        | Rs.1.5Cr        | Rs.0.3Cr     | -1.2Cr   | RED    |
  | Fidelitus Technology     | Rs.1.2Cr        | Rs.0.5Cr     | -0.7Cr   | RED    |
  | Fidelitus GCC Nexus      | Rs.0.5Cr        | Rs.0.05Cr    | -0.45Cr  | BRTRED |
  |--------------------------|-----------------|--------------|----------|--------|
  | CORPORATE TOTAL          | Rs.18.7Cr       | Rs.14.55Cr   | -4.15Cr  | ORANGE |

  Color coding: same rule (<25% -> BRTRED, 26-50% -> RED, 51-75% -> ORANGE, >75% -> GREEN).
  Delta column: colored text + arrow icon (^ or v).
  Clicking any company row expands the same aging panel from Session 04.

Time-filter wiring (WTD/MTD/QTD/YTD from Session 02 header):
  - WTD  -> show weekly pulse table
  - MTD / QTD / YTD -> hide weekly pulse (not relevant)
  Wire via vanilla JS toggling a CSS class on the weekly-pulse section.

PDCA: present plan before touching any file.
'@
    }

    "s07-mockup-polish" = @{
        model = $SONNET
        phase = "0 - Mockup"
        task  = "TASK-007"
        label = "Session 07 - Mockup Polish + Handoff Prep"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: FastAPI + Jinja2 + vanilla HTML/CSS/JS
Task file: tasks/TASK-007-mockup-polish.md  (create it first)
Module scope: ALL mockup files (app/mockup/, app/templates/, app/static/)
PRODUCTION=1 (dummy data).

GOAL -- Final mockup review, polish, and developer handoff preparation.

== CARRY-OVER FROM s06 (do this FIRST, before any polish work) ==
Weekly Pulse panel (Section W) currently shows Revenue only.
Expand it to ALL 6 KPIs: Revenue . Invoiced . Payments . Meetings . Proposals . Target.
Same committed-vs-actual-vs-delta structure per KPI per company.
Add a KPI selector row above the pulse table (pill tabs, vanilla JS).
Dummy data for all KPIs already exists in WEEKLY_PULSE -- extend it.
Prerequisite: merge PR#6 (feature/TASK-006-weekly-pulse) before starting s07.

TASKS IN THIS SESSION:

1. FULL REVIEW
   Read every template and dummy data file. Report:
   - Any missing KPIs from PRD
   - Any color coding bugs
   - Any broken interactions (aging panels, pipeline drill-downs)
   - Any responsive layout issues

2. ADDITIONS for a holding-company MD (beyond PRD):
   a. Sticky Notes panel (top-right corner): MD can jot quick reminders
      (vanilla JS localStorage -- no backend needed in Phase 0)
   b. "Last updated" timestamp on each company card
   c. Print / Export view: "Print" button hides nav, expands all panels,
      triggers window.print() with a clean CSS @print stylesheet

3. ENV FLAG VALIDATION
   Confirm:
   - When PRODUCTION=1 -> dummy_data.py feeds all sections
   - When PRODUCTION=0 -> app/api/ routes are called instead
   Create app/api/__init__.py and app/api/routes.py with stub endpoints:
     {"status": "not implemented -- set PRODUCTION=1 for mockup"}

4. DEVELOPER HANDOFF DOCUMENT
   Create docs/HANDOFF.md with sections:
   a. How to run the mockup (PRODUCTION=1)
   b. Where dummy data lives (app/mockup/dummy_data.py)
   c. Where to wire real data (app/api/ + app/data/)
   d. Session map: start from s08-db-audit
   e. MongoDB collections mapped to each dashboard KPI
   f. CRM auth integration points
   g. ENV variables to fill (.env.example)
   h. Design constraints (no framework, dark theme, fonts, color rules)

5. FINAL CHECK
   Run: uvicorn app.main:app --reload --port 8000
   Confirm dashboard loads at http://localhost:8000
   All panels interactive, all color coding correct.

PDCA: present plan, get approval for additions, then implement.
After this session the mockup is COMPLETE and ready to share with developer.
'@
    }

    # --------------------------------------------------------------------------
    #  PHASE 1 -- INTEGRATION  (Developer runs s08 -> s15)
    #  IMPORTANT: Read docs/HANDOFF.md FIRST before starting any session.
    # --------------------------------------------------------------------------

    "s08-db-audit" = @{
        model = $SONNET
        phase = "1 - Integration - START HERE"
        task  = "TASK-008"
        label = "Session 08 - MongoDB Schema Audit (READ-ONLY)"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: Python 3.13, FastAPI, Motor (async MongoDB), Fidelitus CRM MongoDB
Task file: tasks/TASK-008-db-audit.md  (create it first)
Module scope: READ-ONLY -- do NOT modify any file in this session.
IMPORTANT: Read docs/HANDOFF.md first before doing anything else.

GOAL -- Audit the real MongoDB database and produce a field-level mapping document.

STEP 1 -- Connect to MongoDB and list all collections:
  mongosh $MONGO_DB --eval "db.getCollectionNames().sort()"

STEP 2 -- For each collection below, run findOne() and note actual field names:
  Priority collections:
  - leads            -> find: vertical/company, stage, source, created_date, assigned_to
  - meetings         -> find: vertical, date, client, outcome, created_by
  - deals            -> find: vertical, value, booking_date, lead_id, stage
  - invoicereports   -> find: vertical, amount, invoice_date, client, status
  - invoicepayments  -> find: vertical, amount, payment_date, invoice_id, status
  - bdtargets        -> find: vertical, period, target_type, target_value
  - usertargets      -> find: user_id, vertical, period, target_value, achieved
  - employeetargets  -> find: same pattern as usertargets
  - departments      -> find: department_name, vertical, parent
  - ftsleads         -> find: similar to leads
  - fidelitusleads   -> find: source_md flag?, vertical, stage
  - mdfollowups      -> find: lead_id, date, outcome
  - mdfollowupproposals -> find: proposal_value, status, date
  - stages           -> find ALL (master list of pipeline stages)
  - users            -> find: name, role, department, vertical (NO passwords)

STEP 3 -- Produce docs/DB-SCHEMA-MAP.md:
  For each KPI on the dashboard, the exact MongoDB query needed:
  | Dashboard KPI     | Collection(s)  | Filter fields      | Aggregation   |
  |-------------------|----------------|--------------------|---------------|
  | Revenue (Booking) | deals          | vertical, date     | sum(value)    |
  | ...               | ...            | ...                | ...           |

STEP 4 -- Flag UNKNOWNS:
  - Collections missing (e.g. company-level targets)
  - Fields that are ambiguous or inconsistently named
  - Whether MD user has a special flag in users collection
  - Whether verticals map cleanly to the 6 companies

OUTPUT: docs/DB-SCHEMA-MAP.md + console report of unknowns.
No code changes. No new routes. READ-ONLY session.
Share DB-SCHEMA-MAP.md with Srinivas for review before proceeding to s09.
'@
    }

    "s09-auth-hook" = @{
        model = $SONNET
        phase = "1 - Integration"
        task  = "TASK-009"
        label = "Session 09 - CRM Auth Integration"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: FastAPI, Motor, Fidelitus CRM JWT auth
Task file: tasks/TASK-009-auth-hook.md  (create it first)
Module scope: app/auth/  ONLY.
Prerequisite: docs/DB-SCHEMA-MAP.md must exist from Session 08.

GOAL -- Integrate the CRM existing JWT authentication so the MD Dashboard
requires the same login as the CRM.

TASKS:
1. Read app/auth/ (currently empty). Read docs/HANDOFF.md auth section.

2. Implement app/auth/middleware.py:
   - FastAPI middleware that checks for the CRM JWT in the request cookie
     (cookie name from CRM_SESSION_COOKIE in .env)
   - If valid JWT (verify with CRM_JWT_SECRET): extract user _id + role
   - If invalid / missing: redirect to CRM login (CRM_BASE_URL + /login)
   - Only allow users whose role includes MD-level access
     (check users collection for user matching MD_USER_ID in .env)

3. Implement app/auth/deps.py:
   - FastAPI dependency: get_current_md_user()
   - Returns the authenticated MD user dict from MongoDB users collection

4. Wire dependency into app/api/routes.py (stub from Session 07):
   - All routes require get_current_md_user()

5. Test: confirm redirect to CRM login when no cookie is present.

Context7: use for FastAPI middleware + dependency injection docs.
PDCA: present plan, get approval, then implement.
'@
    }

    "s10-leads-wire" = @{
        model = $SONNET
        phase = "1 - Integration"
        task  = "TASK-010"
        label = "Session 10 - Wire Leads + Meetings from MongoDB"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: FastAPI, Motor (async MongoDB)
Task file: tasks/TASK-010-leads-wire.md  (create it first)
Module scope: app/data/leads.py  +  app/api/leads.py  ONLY.
Prerequisite: docs/DB-SCHEMA-MAP.md (s08) + auth working (s09).

GOAL -- Replace dummy data for Leads and Meetings KPIs with real MongoDB queries.
Use docs/DB-SCHEMA-MAP.md for exact collection names and field paths.

1. app/data/leads.py -- async Motor functions:
   - get_corporate_leads_summary(period: str, db) -> dict
     Query: fidelitusleads or leads filtered by MD-sourced flag
     Return: count, target, % achieved, delta_wow
   - get_company_leads_summary(company_slug: str, period: str, db) -> dict
     Query: leads filtered by vertical matching company
   - get_leads_aging(company_slug: str, db) -> dict
     Return: buckets {7d, 14d, 21d, 90d, npa} each with count + value + detail list
   - get_meetings_summary(company_slug: str, period: str, db) -> dict

2. app/api/leads.py -- FastAPI router:
   GET /api/leads/corporate?period=wtd
   GET /api/leads/{company}/summary?period=wtd
   GET /api/leads/{company}/aging
   GET /api/meetings/{company}/summary?period=wtd
   All protected by get_current_md_user() dependency.

3. Update app/templates/dashboard.html:
   When PRODUCTION=0: fetch from /api/leads/* via JS fetch() on page load.
   When PRODUCTION=1: continue using Jinja2 dummy data (no change to Phase 0).

Context7: use for Motor async aggregation pipeline docs.
PDCA: present plan before touching any file.
'@
    }

    "s11-finance-wire" = @{
        model = $SONNET
        phase = "1 - Integration"
        task  = "TASK-011"
        label = "Session 11 - Wire Invoices + Payments + Revenue"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: FastAPI, Motor (async MongoDB)
Task file: tasks/TASK-011-finance-wire.md  (create it first)
Module scope: app/data/finance.py  +  app/api/finance.py  ONLY.
Prerequisite: DB-SCHEMA-MAP.md (s08) + auth (s09).

GOAL -- Wire Revenue (Booking), Invoiced, and Payments KPIs from real MongoDB.

1. app/data/finance.py -- async Motor functions:
   - get_revenue_summary(company_slug: str, period: str, db) -> dict
     Source: deals collection, aggregate sum(value) by vertical + date range
   - get_invoiced_summary(company_slug: str, period: str, db) -> dict
     Source: invoicereports collection
   - get_payments_summary(company_slug: str, period: str, db) -> dict
     Source: invoicepayments collection
   - get_proposals_summary(company_slug: str, period: str, db) -> dict
     Source: mdfollowupproposals or equivalent
   - get_finance_aging(company_slug: str, kpi: str, db) -> dict
     kpi: one of revenue|invoiced|payments|proposals
     Return: 5 aging buckets with detail rows (team member, value, days, reason)

2. app/api/finance.py -- FastAPI router:
   GET /api/finance/{company}/revenue?period=wtd
   GET /api/finance/{company}/invoiced?period=wtd
   GET /api/finance/{company}/payments?period=wtd
   GET /api/finance/{company}/proposals?period=wtd
   GET /api/finance/{company}/aging?kpi=payments

3. Period logic helper in app/data/utils.py:
   period_to_date_range(period: str) -> (start: datetime, end: datetime)
   Supports: wtd, mtd, qtd, ytd

Context7: use for Motor aggregation + Motor date filtering docs.
PDCA: present plan before touching any file.
'@
    }

    "s12-targets-wire" = @{
        model = $SONNET
        phase = "1 - Integration"
        task  = "TASK-012"
        label = "Session 12 - Wire Targets from MongoDB"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: FastAPI, Motor (async MongoDB)
Task file: tasks/TASK-012-targets-wire.md  (create it first)
Module scope: app/data/targets.py  +  app/api/targets.py  ONLY.
Prerequisite: DB-SCHEMA-MAP.md (s08).

GOAL -- Wire annual and period targets for all KPIs from real MongoDB.

NOTE: The PRD states targets may NOT exist in the DB. Use DB-SCHEMA-MAP.md unknowns
section to determine what exists. If targets are missing:
  Create app/data/targets_config.py (Python dict, NOT in MongoDB) so the developer
  can fill them manually. Document this clearly in docs/HANDOFF.md.

1. app/data/targets.py:
   - get_annual_target(company_slug: str, kpi: str, db) -> float or None
     Source: bdtargets or usertargets (check DB-SCHEMA-MAP.md)
     Return None if not found (UI shows "--" instead of a target)
   - get_period_target(company_slug: str, kpi: str, period: str, db) -> float or None
     Pro-rate annual target by period if no period-specific target exists
   - get_committed_this_week(company_slug: str, kpi: str, db) -> float or None
     Source: check for a weekly commitment collection in DB-SCHEMA-MAP.md

2. app/api/targets.py:
   GET /api/targets/{company}/{kpi}?period=wtd
   GET /api/targets/corporate/{kpi}?period=ytd

3. Color coding computed server-side as a string (red/orange/amber/green)
   based on actual vs target, returned in the API response.

PDCA: present plan. Flag clearly if targets DB is empty -- that is a valid finding.
'@
    }

    "s13-company-split" = @{
        model = $SONNET
        phase = "1 - Integration"
        task  = "TASK-013"
        label = "Session 13 - Per-Company Data Routing"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: FastAPI, Motor (async MongoDB)
Task file: tasks/TASK-013-company-split.md  (create it first)
Module scope: app/data/companies.py  +  app/api/companies.py  ONLY.
Prerequisite: s10, s11, s12 complete.

GOAL -- Wire the 6 company cards to pull real data for all KPIs in one API call.

1. app/data/companies.py:
   COMPANY_SLUGS mapping (use DB-SCHEMA-MAP.md to confirm exact vertical names):
     "transactions" -> "Fidelitus Transactions"  -> vertical filter value
     "projects"     -> "Fidelitus Projects"       -> vertical filter value
     "fms"          -> "Fidelitus FMS"            -> vertical filter value
     "hrlabs"       -> "Fidelitus HR Labs"        -> vertical filter value
     "technology"   -> "Fidelitus Technology"     -> vertical filter value
     "gcc"          -> "Fidelitus GCC Nexus"      -> vertical filter value

   - get_company_dashboard(company_slug: str, period: str, db) -> dict
     Calls finance, leads, meetings, targets in parallel (asyncio.gather)
     Returns one consolidated dict with all 6 KPIs + color codes + deltas

   - get_corporate_dashboard(period: str, db) -> dict
     Aggregates all companies + fidelitusleads for corporate strip

2. app/api/companies.py:
   GET /api/dashboard/corporate?period=wtd
   GET /api/dashboard/{company}?period=wtd
   GET /api/dashboard/all?period=wtd  (corporate + all 6 companies in one call)

3. Update dashboard.html JS:
   On page load (PRODUCTION=0): single fetch to /api/dashboard/all?period=wtd
   Populate all cards and corporate strip from response.
   Time-filter button click: re-fetch with new period param.

Context7: use for asyncio.gather with Motor + FastAPI docs.
PDCA: present plan before touching any file.
'@
    }

    "s14-aging-live" = @{
        model = $SONNET
        phase = "1 - Integration"
        task  = "TASK-014"
        label = "Session 14 - Live Aging Analysis"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: FastAPI, Motor (async MongoDB)
Task file: tasks/TASK-014-aging-live.md  (create it first)
Module scope: app/data/aging.py  +  app/api/aging.py  ONLY.
Prerequisite: s10-s13 complete.

GOAL -- Replace dummy aging data with real overdue calculations from MongoDB.

Aging definition: item is overdue if it has a due_date or committed_date and
actual delivery date is past that date.
Buckets: 0-7d . 8-14d . 15-21d . 22-90d . >90d (NPA).

1. app/data/aging.py:
   - get_aging_for_kpi(company_slug: str, kpi: str, db) -> dict
     kpi: payments | invoiced | proposals | collections
     For each bucket: count, total_value, list of detail rows
     Detail row: {company, team_member_name, value, days_overdue, reason}
     - team_member_name: join with users collection on assigned_to field
     - reason: from last note/comment on the record (check notes collection)
     - days_overdue: (today - due_date).days

   - get_aging_corporate(kpi: str, db) -> dict
     Aggregate across all companies, add company column to detail rows

2. app/api/aging.py:
   GET /api/aging/{company}/{kpi}    -> company-level aging
   GET /api/aging/corporate/{kpi}    -> corporate aging
   Both return: {buckets: [...], last_updated: ISO timestamp}

3. Dashboard JS: when MD clicks aging bucket pill (PRODUCTION=0),
   fetch live data from /api/aging/{company}/{kpi}?bucket=7d
   Replace dummy panel rows with real data.

FLAG: if due_date / committed_date fields do not exist in the DB, report to developer
to check calendarfollowups, mdfollowups, meettaskfollowups in DB-SCHEMA-MAP.md.

PDCA: present plan. Flag all schema assumptions explicitly.
'@
    }

    "s15-prod-cutover" = @{
        model = $SONNET
        phase = "1 - Integration"
        task  = "TASK-015"
        label = "Session 15 - Production Cutover + Final Testing"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: FastAPI, Motor (async MongoDB)
Task file: tasks/TASK-015-prod-cutover.md  (create it first)
Module scope: .env, app/main.py, app/templates/dashboard.html, docs/  ONLY.
Prerequisite: ALL sessions s08-s14 complete and reviewed.

GOAL -- Flip PRODUCTION=0, verify end-to-end, finalize for live use.

PRE-CUTOVER CHECKLIST (do NOT flip flag until all pass):
  [ ] All 6 company API endpoints return real data (test with httpx)
  [ ] Corporate strip aggregation matches sum of company values
  [ ] Auth: unauthenticated request redirects to CRM login
  [ ] Auth: MD user session loads dashboard correctly
  [ ] Aging panels show real data (not dummy)
  [ ] Time-filter (WTD/MTD/QTD/YTD) changes data correctly
  [ ] Weekly Pulse table reflects real committed vs actual
  [ ] Color coding matches rule (<25% bright red ... >75% green)
  [ ] No secrets in any committed file (.env excluded from git)
  [ ] uvicorn runs cleanly with no import errors

FLIP FLAG: set PRODUCTION=0 in .env

SMOKE TEST post-cutover:
  - Load http://localhost:8000 as MD user
  - Verify each section renders with real data
  - Click all aging drill-downs
  - Switch all time-filter periods

KNOWN GAPS LOG -- create docs/KNOWN-GAPS.md:
  Any KPI where real data was not available (e.g. targets not in DB)
  State the dummy fallback used and what developer needs to configure.

UPDATE docs/HANDOFF.md: mark Phase 1 as COMPLETE.

DEPLOYMENT NOTE -- create docs/DEPLOY.md:
  - pip install -r requirements.txt
  - Copy .env.example -> .env, fill all values
  - uvicorn app.main:app --host 0.0.0.0 --port 8000
  - (Optional) systemd / PM2 / Docker instructions placeholder

PDCA: present full checklist, get approval before flipping flag.
'@
    }

    # --------------------------------------------------------------------------
    #  AUDIT SESSION  (use any time, either phase -- READ-ONLY)
    # --------------------------------------------------------------------------

    "audit" = @{
        model = $SONNET
        phase = "0 or 1"
        task  = "TASK-???"
        label = "Audit Session (Read-Only)"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: Python 3.13, FastAPI, Motor, Jinja2, vanilla JS

AUDIT SESSION RULES:
  READ-ONLY. Absolutely NO code changes in this session.
  One session = one module or one area of concern.
  Output: a written report only. Fixes go into a new dedicated session.

Please tell me WHAT to audit. Options:

  A. MOCKUP AUDIT (Phase 0)
     Read all files in app/mockup/, app/templates/, app/static/
     Report: missing KPIs, broken interactions, color coding gaps,
             dummy data inconsistencies, PRD compliance gaps.

  B. API AUDIT (Phase 1 -- after s09+)
     Read all files in app/api/, app/data/, app/auth/
     Report: missing endpoints, unhandled edge cases, missing auth guards,
             Motor queries that may fail on empty collections,
             field names that differ from DB-SCHEMA-MAP.md.

  C. MONGODB SCHEMA AUDIT (Phase 1)
     Connect to MongoDB (MONGO_URI from .env).
     Run findOne() on the collections you name.
     Report: actual field names vs what the data layer expects,
             missing indexes, empty collections, date field formats.

  D. SECURITY AUDIT
     Read app/auth/, .env.example, any route that accepts user input.
     Report: exposed secrets, missing auth guards, injection risks,
             any hardcoded credentials, CORS settings.

  E. FULL PROJECT AUDIT
     Read every file across all modules.
     Report: overall health, what is complete, what is missing,
             recommended next session order.

State which audit (A/B/C/D/E) and any specific focus area.
Output format: structured markdown report saved to docs/AUDIT-<date>-<area>.md
'@
    }

    # --------------------------------------------------------------------------
    #  DEBUG SESSION  (use any time, either phase)
    # --------------------------------------------------------------------------

    "debug" = @{
        model = $SONNET
        phase = "0 or 1"
        task  = "TASK-???"
        label = "Debug Session"
        prompt = @'
Jai Jagannath.

Project: MD Dashboard -- Fidelitus Corp
Stack: Python 3.13, FastAPI, Motor, Jinja2, vanilla JS

Debug rule: ONE error . ONE file . ONE session.
Do NOT fix anything beyond the reported error.

Please paste:
  (1) Full traceback or browser console error
  (2) Only the function / template block that threw it
  (3) The PRODUCTION flag value (0 or 1)

Known gotchas:
  - Motor is async -- never call await inside a sync function or Jinja2 filter
  - Jinja2 template variables: use | default("--") for missing values
  - MongoDB ObjectId: always convert to str() before returning in JSON
  - BSON dates: convert to .isoformat() before JSON serialization
  - Color coding: % is always (actual / target * 100) -- guard against target = 0
  - Aging days: use (datetime.utcnow() - due_date).days -- ensure both are naive UTC
'@
    }
}

# ==============================================================================
#  LIST MODE
# ==============================================================================
if ($Session -eq "list") {
    Write-Host ""
    Write-Host "  MD Dashboard -- Fidelitus Corp" -ForegroundColor Cyan
    Write-Host "  =================================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  -- PHASE 0 . MOCKUP  (Srinivas runs these) ---------------------" -ForegroundColor Yellow
    Write-Host ""

    $phase0 = @("s01-scaffold","s02-corp-header","s03-company-cards","s04-aging-drill","s05-corp-pipeline","s06-weekly-delta","s07-mockup-polish")
    foreach ($key in $phase0) {
        $s = $sessions[$key]
        $tag = if ($s.model -like "*haiku*") { "[Haiku ]" } else { "[Sonnet]" }
        Write-Host ("  {0,-22} {1,-40} {2}" -f $key, $s.label, $tag)
    }

    Write-Host ""
    Write-Host "  -- PHASE 1 . INTEGRATION  (Developer runs these) ---------------" -ForegroundColor Magenta
    Write-Host "     [!] Read docs/HANDOFF.md before starting s08." -ForegroundColor DarkGray
    Write-Host ""

    $phase1 = @("s08-db-audit","s09-auth-hook","s10-leads-wire","s11-finance-wire","s12-targets-wire","s13-company-split","s14-aging-live","s15-prod-cutover")
    foreach ($key in $phase1) {
        $s = $sessions[$key]
        $tag = if ($s.model -like "*haiku*") { "[Haiku ]" } else { "[Sonnet]" }
        Write-Host ("  {0,-22} {1,-40} {2}" -f $key, $s.label, $tag)
    }

    Write-Host ""
    Write-Host "  -- UTILITY -------------------------------------------------------" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host ("  {0,-22} {1,-40} {2}" -f "audit", "Read-Only Audit (any phase, A-E)", "[Sonnet]")
    Write-Host ("  {0,-22} {1,-40} {2}" -f "debug", "One error . one file . one session", "[Sonnet]")
    Write-Host ""
    Write-Host "  Usage:  .\mddb-sessions.ps1 -Session s01-scaffold" -ForegroundColor Green
    Write-Host ""
    exit 0
}

# ==============================================================================
#  RUN SESSION
# ==============================================================================
$s = $sessions[$Session]

Write-Host ""
Write-Host "  +------------------------------------------------------------+" -ForegroundColor Cyan
Write-Host ("  |  {0,-58}|" -f $s.label) -ForegroundColor Cyan
Write-Host ("  |  Phase : {0,-52}|" -f $s.phase) -ForegroundColor Cyan
Write-Host ("  |  Task  : {0,-52}|" -f $s.task) -ForegroundColor Cyan
Write-Host ("  |  Model : {0,-52}|" -f $s.model) -ForegroundColor Cyan
Write-Host "  +------------------------------------------------------------+" -ForegroundColor Cyan
Write-Host ""

if ($Session -eq "s08-db-audit") {
    Write-Host "  [!] PHASE 1 START -- DEVELOPER HANDOFF POINT" -ForegroundColor Magenta
    Write-Host "  Read docs/HANDOFF.md before pasting the prompt." -ForegroundColor Yellow
    Write-Host "  Fill .env with real MONGO_URI, CRM_JWT_SECRET, MD_USER_ID." -ForegroundColor Yellow
    Write-Host ""
}

Write-Host $s.prompt -ForegroundColor White
Write-Host ""
$s.prompt | Set-Clipboard
Write-Host "  [OK] Prompt copied to clipboard." -ForegroundColor Green
Write-Host "  Paste into Claude Code, then type:  superpowers brainstorm" -ForegroundColor Cyan
Write-Host ""

Set-Location $PROJECT_ROOT
$env:ANTHROPIC_MODEL = $s.model
claude --model $s.model
