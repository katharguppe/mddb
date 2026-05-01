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
