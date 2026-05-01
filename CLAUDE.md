# CLAUDE.md -- MD Dashboard . Fidelitus Corp
# Extends ~/.claude/CLAUDE.md. These rules take precedence locally.

## Project Purpose
MD-level consolidated dashboard for Fidelitus Corp and its 6 subsidiaries.
Phase 0: Full interactive mockup with dummy data (no login required).
Phase 1: Integration with existing CRM -- real MongoDB data + CRM auth.

## Stack
Python 3.13, FastAPI, Motor (async MongoDB), Jinja2, Uvicorn, HTML/CSS/JS (no framework)

## Current Phase: 0
- Phase 0  ->  all sessions s01-s07  ->  Srinivas runs
- Phase 1  ->  all sessions s08-s15  ->  Developer runs

## Companies (6 subsidiaries)
1. Fidelitus Transactions
2. Fidelitus Projects
3. Fidelitus FMS
4. Fidelitus HR Labs
5. Fidelitus Technology
6. Fidelitus GCC Nexus

## KPI Definitions (apply at both corporate and company level)
- Target for Year       -> annual revenue/booking target
- Revenue (Booking)     -> deals/bookings achieved
- Invoiced Amounts      -> invoices raised
- Payments Received     -> collections received
- Meetings Done         -> client meetings held
- Proposals Submitted   -> proposals sent

## Color Coding Rule (committed vs actual -- applies everywhere)
< 25% of committed target   -> BRIGHT RED  (#ef4444)
26-50%                      -> RED-ORANGE  (#f97316)
51-75%                      -> AMBER       (#f59e0b)
> 75%                       -> GREEN       (#22c55e)

## Aging Buckets (for delayed committed items)
7 days . 14 days . 21 days . 90 days . NPA (>90 days)

## ENV Flag
PRODUCTION=1  ->  dummy mockup data  (Phase 0 -- Srinivas)
PRODUCTION=0  ->  live MongoDB data  (Phase 1 -- Developer)
Set in .env at project root.

## Key MongoDB Collections (CRM -- do NOT modify schema)
leads                              -> lead pipeline records
meetings                           -> client meeting records
deals                              -> bookings / revenue deals
invoicereports                     -> invoice headers
invoicepayments                    -> payment receipts
invoicepaymentshares               -> split payment shares
bdtargets                          -> BD targets (team/vertical)
usertargets                        -> per-user targets
employeetargets                    -> employee-level targets
departments                        -> company/department master
ftsleads                           -> FTS-specific leads
fidelitusleads                     -> corporate / MD-sourced leads
mdfollowups                        -> MD follow-up records
mdfollowupproposals                -> proposals tracked by MD
mdassigntasks                      -> tasks assigned by MD
ftsverticalreports                 -> vertical performance reports
ftsverticalmonthlymeetingreviews   -> monthly meeting reviews
individualverticalrevenueforecasts -> revenue forecasts per vertical
stages                             -> lead pipeline stages master
sources                            -> lead sources master
users                              -> CRM users / team members
roles / user_roles                 -> roles and permissions
user_access_tokens                 -> JWT / session tokens

## Module Scope per Session
s01-s07  ->  app\mockup\ + app\static\ + app\templates\   (Phase 0)
s08      ->  READ-ONLY audit across all modules            (Phase 1 start)
s09      ->  app\auth\  only
s10      ->  app\data\leads.py  +  app\api\leads.py
s11      ->  app\data\finance.py  +  app\api\finance.py
s12      ->  app\data\targets.py  +  app\api\targets.py
s13      ->  app\data\companies.py  +  app\api\companies.py
s14      ->  app\data\aging.py  +  app\api\aging.py
s15      ->  .env  +  app\main.py  (production cutover)
debug    ->  ONE error . ONE file . ONE session
audit    ->  READ-ONLY -- no code changes

## Design Constraints (MD explicit preference)
- Graphics: light, clear, distinct -- nothing fancy
- No heavy JS frameworks -- vanilla JS only
- Existing design reference: md_dashboard_v2.html (in project root)
- Font: DM Sans (body) + Syne (headings)
- Color scheme: dark bg #0d1117, surface #161b22, accent amber #e8a838

## Git
- Branches: main / dev / feature/TASK-XXX
- Commit format: [TASK-XXX] verb: what changed
- NEVER commit .env
