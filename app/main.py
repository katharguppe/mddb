from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.config import Settings

# Initialize settings
settings = Settings()

# Create FastAPI app
app = FastAPI(
    title="MD Dashboard",
    description="MD-level consolidated dashboard for Fidelitus Corp",
    version="0.1.0"
)

# Mount static files (CSS, JS, images)
static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Conditional routing based on PRODUCTION flag
if settings.PRODUCTION == "1":
    # Phase 0: Serve mockup routes
    from app.mockup import routes as mockup_routes
    app.include_router(mockup_routes.router)
else:
    # Phase 1: Serve live API routes (not implemented yet)
    # from app.api import leads, finance, targets, companies, aging
    # app.include_router(leads.router, prefix="/api/leads")
    # ... etc
    pass

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}
