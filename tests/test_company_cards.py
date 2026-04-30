# tests/test_company_cards.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_dashboard_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_all_six_companies_rendered():
    html = client.get("/").text
    for name in [
        "Fidelitus Transactions",
        "Fidelitus Projects",
        "Fidelitus FMS",
        "Fidelitus HR Labs",
        "Fidelitus Technology",
        "Fidelitus GCC Nexus",
    ]:
        assert name in html, f"Company '{name}' not found in rendered HTML"


def test_six_know_more_buttons_rendered():
    html = client.get("/").text
    assert html.count("toggleDetails") == 6, f"Expected 6 toggleDetails calls, found {html.count('toggleDetails')}"


def test_details_panels_rendered():
    html = client.get("/").text
    for company_id in ["transactions", "projects", "fms", "hrlabs", "technology", "gcc"]:
        assert f'id="details-{company_id}"' in html, f"Details panel for '{company_id}' not found"
    assert "Aging analysis" in html, "Aging analysis placeholder text not found"


def test_pct_color_bands_rendered():
    html = client.get("/").text
    # GCC Nexus revenue 4% and invoiced 0% -> red band must appear
    assert "kpi-status-red" in html, "No red KPI badge found (GCC Nexus 4% revenue should render red)"
    # Transactions revenue 85% -> green band must appear
    assert "kpi-status-green" in html, "No green KPI badge found (Transactions 85% revenue should render green)"
