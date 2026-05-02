# app/api/routes.py
# Stub routes for PRODUCTION=0 (Phase 1 -- not yet implemented).
# Returns a clear message so the developer knows to set PRODUCTION=1 for the mockup.

from fastapi import APIRouter

router = APIRouter()


@router.get("/{path:path}")
async def not_implemented(path: str):
    return {
        "status": "not implemented",
        "note": "set PRODUCTION=1 in .env to use the Phase 0 mockup",
        "path": path,
    }
