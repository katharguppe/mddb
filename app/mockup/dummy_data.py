# app/mockup/dummy_data.py
# Single source of truth for Phase 0 mock data.
# PRODUCTION=1 -> this file is used. PRODUCTION=0 -> live MongoDB replaces it.

DASHBOARD_DATA = {
    "corporate": {
        "kpis": [
            {
                "label": "Target for Year",
                "value": "Rs.320 Cr",
                "target": "Rs.320 Cr",
                "pct": None,
                "delta": None,
            },
            {
                "label": "Revenue (Booking)",
                "value": "Rs.142 Cr",
                "target": "Rs.320 Cr",
                "pct": 44,
                "delta": "up",
            },
            {
                "label": "Invoiced Amounts",
                "value": "Rs.108 Cr",
                "target": "Rs.320 Cr",
                "pct": 34,
                "delta": None,
            },
            {
                "label": "Payments Received",
                "value": "Rs.71 Cr",
                "target": "Rs.320 Cr",
                "pct": 22,
                "delta": None,
            },
            {
                "label": "Meetings Done",
                "value": "971",
                "target": "1200",
                "pct": 81,
                "delta": "up",
            },
            {
                "label": "Proposals Submitted",
                "value": "530",
                "target": "800",
                "pct": 66,
                "delta": "up",
            },
        ]
    },
    "companies": [
        {
            "id": "transactions",
            "name": "Fidelitus Transactions",
            "dot_color": "#3b82f6",
            "kpis": [
                {"label": "Target",    "value": "Rs.80 Cr", "pct": None, "delta": None},
                {"label": "Revenue",   "value": "Rs.68 Cr", "pct": 85,   "delta": "up"},
                {"label": "Invoiced",  "value": "Rs.54 Cr", "pct": 68,   "delta": None},
                {"label": "Payments",  "value": "Rs.42 Cr", "pct": 53,   "delta": None},
                {"label": "Meetings",  "value": "320",       "pct": 88,   "delta": "up"},
                {"label": "Proposals", "value": "180",       "pct": 79,   "delta": "up"},
            ],
        },
        {
            "id": "projects",
            "name": "Fidelitus Projects",
            "dot_color": "#10b981",
            "kpis": [
                {"label": "Target",    "value": "Rs.60 Cr", "pct": None, "delta": None},
                {"label": "Revenue",   "value": "Rs.29 Cr", "pct": 48,   "delta": "down"},
                {"label": "Invoiced",  "value": "Rs.21 Cr", "pct": 35,   "delta": None},
                {"label": "Payments",  "value": "Rs.14 Cr", "pct": 23,   "delta": None},
                {"label": "Meetings",  "value": "210",       "pct": 61,   "delta": None},
                {"label": "Proposals", "value": "140",       "pct": 55,   "delta": None},
            ],
        },
        {
            "id": "fms",
            "name": "Fidelitus FMS",
            "dot_color": "#a855f7",
            "kpis": [
                {"label": "Target",    "value": "Rs.30 Cr", "pct": None, "delta": None},
                {"label": "Revenue",   "value": "Rs.24 Cr", "pct": 80,   "delta": "up"},
                {"label": "Invoiced",  "value": "Rs.19 Cr", "pct": 63,   "delta": None},
                {"label": "Payments",  "value": "Rs.16 Cr", "pct": 53,   "delta": None},
                {"label": "Meetings",  "value": "180",       "pct": 72,   "delta": None},
                {"label": "Proposals", "value": "95",        "pct": 67,   "delta": None},
            ],
        },
        {
            "id": "hrlabs",
            "name": "Fidelitus HR Labs",
            "dot_color": "#f43f5e",
            "kpis": [
                {"label": "Target",    "value": "Rs.25 Cr", "pct": None, "delta": None},
                {"label": "Revenue",   "value": "Rs.11 Cr", "pct": 44,   "delta": "down"},
                {"label": "Invoiced",  "value": "Rs.8 Cr",  "pct": 32,   "delta": None},
                {"label": "Payments",  "value": "Rs.5 Cr",  "pct": 20,   "delta": None},
                {"label": "Meetings",  "value": "150",       "pct": 48,   "delta": None},
                {"label": "Proposals", "value": "62",        "pct": 41,   "delta": None},
            ],
        },
        {
            "id": "technology",
            "name": "Fidelitus Technology",
            "dot_color": "#22d3ee",
            "kpis": [
                {"label": "Target",    "value": "Rs.20 Cr", "pct": None, "delta": None},
                {"label": "Revenue",   "value": "Rs.9 Cr",  "pct": 45,   "delta": None},
                {"label": "Invoiced",  "value": "Rs.6 Cr",  "pct": 30,   "delta": None},
                {"label": "Payments",  "value": "Rs.4 Cr",  "pct": 20,   "delta": None},
                {"label": "Meetings",  "value": "87",        "pct": 57,   "delta": None},
                {"label": "Proposals", "value": "35",        "pct": 47,   "delta": None},
            ],
        },
        {
            "id": "gcc",
            "name": "Fidelitus GCC Nexus",
            "dot_color": "#e8a838",
            "kpis": [
                {"label": "Target",    "value": "Rs.25 Cr", "pct": None, "delta": None},
                {"label": "Revenue",   "value": "Rs.1 Cr",  "pct": 4,    "delta": "down"},
                {"label": "Invoiced",  "value": "Rs.0",     "pct": 0,    "delta": None},
                {"label": "Payments",  "value": "Rs.0",     "pct": 0,    "delta": None},
                {"label": "Meetings",  "value": "24",        "pct": 21,   "delta": None},
                {"label": "Proposals", "value": "18",        "pct": 24,   "delta": None},
            ],
        },
    ],
}
