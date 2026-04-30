# app/mockup/dummy_data.py
"""
Dummy data for Phase 0 mockup (PRODUCTION=1).
FY 2025-26, week ending 2026-04-25.
All monetary values in Crores (Rs.).
"""

CORP_KPIS = [
    {
        "label": "Target for Year",
        "target": 240.0,          # Rs. Cr
        "current": 187.0,         # Rs. Cr
        "pct": 78,                # % achieved
        "delta": 6.2,             # WoW delta (positive = up)
        "unit": "cr",             # "cr" => format as Rs. XX Cr; "count" => plain number
    },
    {
        "label": "Revenue (Booking)",
        "target": 240.0,
        "current": 142.0,
        "pct": 59,
        "delta": 4.1,
        "unit": "cr",
    },
    {
        "label": "Invoiced",
        "target": 180.0,
        "current": 98.0,
        "pct": 54,
        "delta": 3.8,
        "unit": "cr",
    },
    {
        "label": "Payments",
        "target": 160.0,
        "current": 71.0,
        "pct": 44,
        "delta": -1.2,
        "unit": "cr",
    },
    {
        "label": "Meetings",
        "target": 1200,
        "current": 847,
        "pct": 71,
        "delta": 32,
        "unit": "count",
    },
    {
        "label": "Proposals",
        "target": 900,
        "current": 512,
        "pct": 57,
        "delta": 18,
        "unit": "count",
    },
]
