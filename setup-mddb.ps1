# ==============================================================================
# setup-mddb.ps1
# MD Dashboard -- Fidelitus Corp  |  Project Bootstrap
# Owner: Srinivas / Fidelitus Corp
# Run once. Safe to re-run (idempotent).
# ==============================================================================

$PROJECT_NAME  = "MD Dashboard"
$PROJECT_ROOT  = "D:\Fidelitus\mddb"
$PHASE_CURRENT = 0

Write-Host ""
Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "  FIDELITUS CORP -- MD DASHBOARD -- PROJECT BOOTSTRAP"            -ForegroundColor Cyan
Write-Host "  Phase 0 = Mockup (Srinivas)  |  Phase 1 = Integration (Dev)"   -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host ""

# -- 1. Folder structure -------------------------------------------------------
Write-Host "[ 1/7 ] Creating folder structure..." -ForegroundColor Yellow

$folders = @(
    "tasks",
    "docs",
    "docs\plans",
    "tests",
    ".claude\skills",
    "app\mockup",
    "app\api",
    "app\auth",
    "app\data",
    "app\ui",
    "app\static",
    "app\templates"
)

foreach ($f in $folders) {
    $path = Join-Path $PROJECT_ROOT $f
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path | Out-Null
        Write-Host "  [OK] $f" -ForegroundColor Green
    } else {
        Write-Host "  [--] $f (exists)" -ForegroundColor DarkGray
    }
}

# -- 2. CLAUDE.md --------------------------------------------------------------
Write-Host ""
Write-Host "[ 2/7 ] Writing CLAUDE.md..." -ForegroundColor Yellow

$claudeMd = @'
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
'@

$claudeMd | Set-Content "$PROJECT_ROOT\CLAUDE.md" -Encoding UTF8
Write-Host "  [OK] CLAUDE.md written." -ForegroundColor Green

# -- 3. TOOLS.md ---------------------------------------------------------------
Write-Host ""
Write-Host "[ 3/7 ] Writing TOOLS.md..." -ForegroundColor Yellow

$toolsMd = @'
# TOOLS.md -- MD Dashboard . Fidelitus Corp

## Plugins (install once in Claude Code via /plugin at USER scope)
  superpowers       Sub-agent orchestration (brainstorm / write-plan / execute-plan)
  code-simplifier   Refactor helper
  context7          Live API docs -- no hallucinated method names
  context-mode      98% context savings on large outputs

## MCPs (auto-loaded from .mcp.json)
  filesystem        Read files without pasting into chat
  memory            Persist schema decisions, open questions
  sequential-thinking  Architecture and complex debugging

## Session Launcher
  cd D:\Fidelitus\mddb
  .\mddb-sessions.ps1 -Session list            # see all sessions
  .\mddb-sessions.ps1 -Session s01-scaffold    # run a session
  .\mddb-sessions.ps1 -Session audit           # read-only audit (any phase)
  .\mddb-sessions.ps1 -Session debug           # one error . one file

## Test Commands (fill after scaffold)
  python -m pytest tests/ -v
  uvicorn app.main:app --reload --port 8000

## Mongo Inspect (Phase 1)
  mongosh fidelitus --eval "db.leads.findOne()"
  mongosh fidelitus --eval "db.getCollectionNames()"
'@

$toolsMd | Set-Content "$PROJECT_ROOT\TOOLS.md" -Encoding UTF8
Write-Host "  [OK] TOOLS.md written." -ForegroundColor Green

# -- 4. SKILLS.md + skill files ------------------------------------------------
Write-Host ""
Write-Host "[ 4/7 ] Writing SKILLS.md + skill files..." -ForegroundColor Yellow

$skillsMd = @'
# SKILLS.md -- MD Dashboard . Fidelitus Corp

| Command      | File                           | What it does                    |
|--------------|--------------------------------|---------------------------------|
| task-create  | .claude/skills/task-create.md  | Create a new TASK-XXX.md (PDCA) |
| audit-module | .claude/skills/audit-module.md | Read-only audit, no code change |
'@
$skillsMd | Set-Content "$PROJECT_ROOT\SKILLS.md" -Encoding UTF8

$taskCreateSkill = @'
# Skill: task-create
1. Ask: task title + phase (0=mockup / 1=integration)
2. Find next TASK number in tasks/
3. Create tasks/TASK-XXX-<slug>.md with PDCA template
4. Create branch: feature/TASK-XXX
5. Report path + branch name
'@
$taskCreateSkill | Set-Content "$PROJECT_ROOT\.claude\skills\task-create.md" -Encoding UTF8

$auditSkill = @'
# Skill: audit-module
READ ONLY. No code changes in this session.
1. Read all files in the specified module directory
2. Read relevant MongoDB collection metadata from mongo-backup/
3. Produce a report: what exists, what is missing, what needs wiring
4. List open questions for the developer to answer
5. Output a proposed TASK for the next session
'@
$auditSkill | Set-Content "$PROJECT_ROOT\.claude\skills\audit-module.md" -Encoding UTF8

Write-Host "  [OK] SKILLS.md + skill files written." -ForegroundColor Green

# -- 5. TASK-000 ---------------------------------------------------------------
Write-Host ""
Write-Host "[ 5/7 ] Creating TASK-000 (Repo Init)..." -ForegroundColor Yellow

$task000 = "$PROJECT_ROOT\tasks\TASK-000-repo-init.md"
if (-not (Test-Path $task000)) {
    $task000Content = @'
# TASK-000: Repo Init -- MD Dashboard

## Status: DONE
## Phase: 0
## Objective
Bootstrap project structure, CLAUDE.md, TOOLS.md, sessions script, .env.example.

## PDCA Log
### Cycle 1
**Plan:** Run setup-mddb.ps1
**Approved:** Yes
**Do:** Script executed
**Check:** All folders and config files present
**Act:** Proceed to s01-scaffold

## Checkpoints
| Step          | Status | Notes                    |
|---------------|--------|--------------------------|
| Folders       | done   | All 12 folders created   |
| CLAUDE.md     | done   |                          |
| TOOLS.md      | done   |                          |
| SKILLS.md     | done   |                          |
| sessions.ps1  | done   |                          |
| .env.example  | done   |                          |
'@
    $task000Content | Set-Content $task000 -Encoding UTF8
    Write-Host "  [OK] tasks/TASK-000-repo-init.md" -ForegroundColor Green
} else {
    Write-Host "  [--] TASK-000 already exists" -ForegroundColor DarkGray
}

# -- 6. .env.example -----------------------------------------------------------
Write-Host ""
Write-Host "[ 6/7 ] Writing .env.example..." -ForegroundColor Yellow

$envExample = @'
# .env.example -- copy to .env and fill values
# NEVER commit .env to git

# -- Mode flag -----------------------------------------------------------------
# PRODUCTION=1  ->  dummy mockup data  (Phase 0 -- Srinivas)
# PRODUCTION=0  ->  live MongoDB data  (Phase 1 -- Developer)
PRODUCTION=1

# -- MongoDB -------------------------------------------------------------------
# Phase 1: developer fills these from CRM environment
MONGO_URI=mongodb://localhost:27017
MONGO_DB=fidelitus

# -- CRM Auth ------------------------------------------------------------------
# Phase 1: developer fills from CRM backend config
CRM_BASE_URL=http://localhost:3000
CRM_JWT_SECRET=FILL_IN
CRM_SESSION_COOKIE=FILL_IN

# -- Dashboard -----------------------------------------------------------------
DASHBOARD_PORT=8000
DASHBOARD_HOST=0.0.0.0

# -- MD User -------------------------------------------------------------------
# Phase 1: the MongoDB _id or username of the MD in the CRM users collection
MD_USER_ID=FILL_IN
'@

$envExample | Set-Content "$PROJECT_ROOT\.env.example" -Encoding UTF8
Write-Host "  [OK] .env.example written (copy to .env and fill values)" -ForegroundColor Green

# -- 7. .mcp.json --------------------------------------------------------------
Write-Host ""
Write-Host "[ 7/7 ] Writing .mcp.json..." -ForegroundColor Yellow

$npmGlobalRoot = (npm root -g 2>$null).Trim()

$mcpJson = "{
  `"mcpServers`": {
    `"filesystem`": {
      `"command`": `"node`",
      `"args`": [`"$npmGlobalRoot\\@modelcontextprotocol\\server-filesystem\\dist\\index.js`", `"$PROJECT_ROOT`"]
    },
    `"memory`": {
      `"command`": `"node`",
      `"args`": [`"$npmGlobalRoot\\@modelcontextprotocol\\server-memory\\dist\\index.js`"]
    },
    `"sequential-thinking`": {
      `"command`": `"node`",
      `"args`": [`"$npmGlobalRoot\\@modelcontextprotocol\\server-sequential-thinking\\dist\\index.js`"]
    }
  }
}"

$mcpJson | Set-Content "$PROJECT_ROOT\.mcp.json" -Encoding UTF8
Write-Host "  [OK] .mcp.json written." -ForegroundColor Green

# -- Summary -------------------------------------------------------------------
Write-Host ""
Write-Host "=================================================================" -ForegroundColor Green
Write-Host "  [OK] MD Dashboard bootstrap complete." -ForegroundColor Green
Write-Host ""
Write-Host "  NEXT STEPS:" -ForegroundColor Cyan
Write-Host "    1. Review CLAUDE.md -- confirm company names, KPIs" -ForegroundColor White
Write-Host "    2. Copy .env.example -> .env (leave PRODUCTION=1 for mockup)" -ForegroundColor White
Write-Host "    3. Run first session:" -ForegroundColor White
Write-Host "         .\mddb-sessions.ps1 -Session s01-scaffold" -ForegroundColor Yellow
Write-Host ""
Write-Host "  HANDOFF NOTE FOR DEVELOPER:" -ForegroundColor Cyan
Write-Host "    Start from session s08-db-audit (Phase 1)." -ForegroundColor White
Write-Host "    Fill .env with real MONGO_URI, CRM_JWT_SECRET, MD_USER_ID." -ForegroundColor White
Write-Host "    Set PRODUCTION=0 only after s15-prod-cutover passes all checks." -ForegroundColor White
Write-Host "=================================================================" -ForegroundColor Green
Write-Host ""
