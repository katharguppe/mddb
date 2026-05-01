# app/mockup/routes.py
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.mockup.dummy_data import DASHBOARD_DATA, AGING_DATA, KPI_DETAILS, KPI_AGING

templates_path = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_path))

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Render the MD Dashboard mockup."""
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "data": DASHBOARD_DATA, "aging": AGING_DATA, "kpi_details": KPI_DETAILS, "kpi_aging": KPI_AGING},
    )
