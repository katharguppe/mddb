from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.mockup.dummy_data import CORP_KPIS

templates_path = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_path))


def _fmt_crore(value: float) -> str:
    """Format a float as 'Rs. X.X Cr' (1 decimal place)."""
    return f"Rs. {value:,.1f} Cr"


# Register the custom filter so templates can use {{ value | crore }}
templates.env.filters["crore"] = _fmt_crore

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Render the MD Dashboard mockup."""
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "corp_kpis": CORP_KPIS,
        },
    )
