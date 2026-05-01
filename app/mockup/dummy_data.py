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
    "pipeline": [
        {
            "id":        "pipeline_leads",
            "stage":     "Leads",
            "count":     42,
            "target":    50,
            "pct":       84,
            "delta_dir": "up",
            "delta_val": "+7 WoW",
            "value":     None,
        },
        {
            "id":        "pipeline_meetings",
            "stage":     "Meetings",
            "count":     18,
            "target":    25,
            "pct":       72,
            "delta_dir": "up",
            "delta_val": "+3 WoW",
            "value":     None,
        },
        {
            "id":        "pipeline_proposals",
            "stage":     "Proposals",
            "count":     11,
            "target":    15,
            "pct":       73,
            "delta_dir": "up",
            "delta_val": "+2 WoW",
            "value":     "Rs.38 Cr",
        },
        {
            "id":        "pipeline_orders",
            "stage":     "Orders",
            "count":     6,
            "target":    10,
            "pct":       60,
            "delta_dir": "up",
            "delta_val": "+1 WoW",
            "value":     "Rs.24 Cr",
        },
        {
            "id":        "pipeline_invoices",
            "stage":     "Invoices",
            "count":     4,
            "target":    8,
            "pct":       50,
            "delta_dir": "none",
            "delta_val": "0 WoW",
            "value":     "Rs.18 Cr",
        },
        {
            "id":        "pipeline_collections",
            "stage":     "Collections",
            "count":     3,
            "target":    6,
            "pct":       50,
            "delta_dir": "down",
            "delta_val": "-1 WoW",
            "value":     "Rs.9 Cr",
        },
    ],
}

# Aging data: committed but not delivered, grouped by overdue bucket.
# Indexed by company slug. "corporate" is the cross-company aggregate.
AGING_DATA = {
    "transactions": {
        "7d":  {
            "count": 3, "total": "Rs.2.1 Cr",
            "items": [
                {"company": "Fidelitus Trans", "member": "Rajesh Kumar",  "value": "Rs.80L",   "days": 6,   "reason": "Client travel delay, confirming by Mon"},
                {"company": "Fidelitus Trans", "member": "Priya Menon",   "value": "Rs.75L",   "days": 7,   "reason": "Cheque in transit"},
                {"company": "Fidelitus Trans", "member": "Anand Rao",     "value": "Rs.55L",   "days": 5,   "reason": "Bank processing delay"},
            ],
        },
        "14d": {
            "count": 2, "total": "Rs.1.4 Cr",
            "items": [
                {"company": "Fidelitus Trans", "member": "Suresh Nair",   "value": "Rs.90L",   "days": 13,  "reason": "NEFT rejected, re-initiated"},
                {"company": "Fidelitus Trans", "member": "Kavitha Reddy", "value": "Rs.50L",   "days": 11,  "reason": "Awaiting MD approval from client"},
            ],
        },
        "21d": {
            "count": 1, "total": "Rs.0.6 Cr",
            "items": [
                {"company": "Fidelitus Trans", "member": "Vikram Singh",  "value": "Rs.60L",   "days": 19,  "reason": "Legal vetting on agreement"},
            ],
        },
        "90d": {
            "count": 1, "total": "Rs.1.2 Cr",
            "items": [
                {"company": "Fidelitus Trans", "member": "Mohan Das",     "value": "Rs.1.2 Cr","days": 67,  "reason": "Client undergoing internal restructuring"},
            ],
        },
        "npa":  {
            "count": 1, "total": "Rs.0.9 Cr",
            "items": [
                {"company": "Fidelitus Trans", "member": "Renu Sharma",   "value": "Rs.90L",   "days": 112, "reason": "Dispute raised, legal notice sent"},
            ],
        },
    },
    "projects": {
        "7d":  {
            "count": 2, "total": "Rs.1.5 Cr",
            "items": [
                {"company": "Fidelitus Projects", "member": "Arjun Shetty",  "value": "Rs.85L",   "days": 5,  "reason": "Client site inspection pending"},
                {"company": "Fidelitus Projects", "member": "Deepa Thomas",  "value": "Rs.65L",   "days": 7,  "reason": "Contractor invoice mismatch"},
            ],
        },
        "14d": {
            "count": 2, "total": "Rs.1.1 Cr",
            "items": [
                {"company": "Fidelitus Projects", "member": "Kiran Joshi",   "value": "Rs.70L",   "days": 12, "reason": "Completion certificate delayed"},
                {"company": "Fidelitus Projects", "member": "Meera Pillai",  "value": "Rs.40L",   "days": 10, "reason": "Client on international travel"},
            ],
        },
        "21d": {
            "count": 1, "total": "Rs.0.8 Cr",
            "items": [
                {"company": "Fidelitus Projects", "member": "Rahul Verma",   "value": "Rs.80L",   "days": 18, "reason": "Scope change documentation pending"},
            ],
        },
        "90d": {
            "count": 1, "total": "Rs.0.5 Cr",
            "items": [
                {"company": "Fidelitus Projects", "member": "Sunita Bose",   "value": "Rs.50L",   "days": 55, "reason": "Dispute over punch-list items"},
            ],
        },
        "npa":  {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
    },
    "fms": {
        "7d":  {
            "count": 2, "total": "Rs.0.9 Cr",
            "items": [
                {"company": "Fidelitus FMS", "member": "Anil Kapoor",    "value": "Rs.55L",   "days": 6,  "reason": "Facility audit report awaited"},
                {"company": "Fidelitus FMS", "member": "Sneha Iyer",     "value": "Rs.35L",   "days": 4,  "reason": "Monthly invoice approval pending"},
            ],
        },
        "14d": {
            "count": 1, "total": "Rs.0.6 Cr",
            "items": [
                {"company": "Fidelitus FMS", "member": "Ramesh Gupta",   "value": "Rs.60L",   "days": 11, "reason": "Security deposit adjustment"},
            ],
        },
        "21d": {
            "count": 1, "total": "Rs.0.4 Cr",
            "items": [
                {"company": "Fidelitus FMS", "member": "Lata Srinivas",  "value": "Rs.40L",   "days": 20, "reason": "AMC renewal dispute"},
            ],
        },
        "90d": {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
        "npa":  {
            "count": 1, "total": "Rs.0.3 Cr",
            "items": [
                {"company": "Fidelitus FMS", "member": "Gopal Nair",     "value": "Rs.30L",   "days": 98, "reason": "Client entity dissolved, legal action initiated"},
            ],
        },
    },
    "hrlabs": {
        "7d":  {
            "count": 1, "total": "Rs.0.4 Cr",
            "items": [
                {"company": "Fidelitus HR Labs", "member": "Preethi Nair",   "value": "Rs.40L",   "days": 5,  "reason": "Hiring milestone not yet confirmed"},
            ],
        },
        "14d": {
            "count": 2, "total": "Rs.0.7 Cr",
            "items": [
                {"company": "Fidelitus HR Labs", "member": "Santosh Kumar",  "value": "Rs.45L",   "days": 14, "reason": "Background check delay by client"},
                {"company": "Fidelitus HR Labs", "member": "Divya Menon",    "value": "Rs.25L",   "days": 10, "reason": "PO amendment in process"},
            ],
        },
        "21d": {
            "count": 1, "total": "Rs.0.3 Cr",
            "items": [
                {"company": "Fidelitus HR Labs", "member": "Naresh Patel",   "value": "Rs.30L",   "days": 21, "reason": "Joining date pushed, payment tied to onboarding"},
            ],
        },
        "90d": {
            "count": 1, "total": "Rs.0.5 Cr",
            "items": [
                {"company": "Fidelitus HR Labs", "member": "Shobha Rao",     "value": "Rs.50L",   "days": 72, "reason": "Candidate resigned, replacement clause invoked"},
            ],
        },
        "npa":  {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
    },
    "technology": {
        "7d":  {
            "count": 1, "total": "Rs.0.3 Cr",
            "items": [
                {"company": "Fidelitus Technology", "member": "Vikash Mehta",   "value": "Rs.30L",   "days": 7,  "reason": "UAT sign-off pending from client"},
            ],
        },
        "14d": {
            "count": 1, "total": "Rs.0.2 Cr",
            "items": [
                {"company": "Fidelitus Technology", "member": "Rohini Das",     "value": "Rs.20L",   "days": 13, "reason": "Go-live delayed by client infra team"},
            ],
        },
        "21d": {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
        "90d": {
            "count": 1, "total": "Rs.0.4 Cr",
            "items": [
                {"company": "Fidelitus Technology", "member": "Sudhir Bhat",    "value": "Rs.40L",   "days": 60, "reason": "Change request scope dispute"},
            ],
        },
        "npa":  {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
    },
    "gcc": {
        "7d":  {
            "count": 1, "total": "Rs.0.5 Cr",
            "items": [
                {"company": "Fidelitus GCC Nexus", "member": "Aditya Sharma",  "value": "Rs.50L",   "days": 6,  "reason": "LOI issued, payment terms being finalised"},
            ],
        },
        "14d": {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
        "21d": {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
        "90d": {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
        "npa":  {
            "count": 0, "total": "Rs.0",
            "items": [],
        },
    },
}

# Corporate aggregate: flatten all company items per bucket
def _build_corporate_aging():
    buckets = ["7d", "14d", "21d", "90d", "npa"]
    result = {}
    for bucket in buckets:
        items = []
        for slug_data in AGING_DATA.values():
            items.extend(slug_data[bucket]["items"])
        count = sum(len(slug_data[bucket]["items"]) for slug_data in AGING_DATA.values())
        result[bucket] = {"count": count, "items": items, "total": f"{count} items"}
    return result

# NOTE: must be called before pipeline_* entries are added — iterates AGING_DATA.values()
AGING_DATA["corporate"] = _build_corporate_aging()

# ── Pipeline aging (per stage) ──────────────────────────────────────────────
def _empty_pipeline_bucket():
    return {
        "7d":  {"count": 0, "total": "Rs.0", "items": []},
        "14d": {"count": 0, "total": "Rs.0", "items": []},
        "21d": {"count": 0, "total": "Rs.0", "items": []},
        "90d": {"count": 0, "total": "Rs.0", "items": []},
        "npa": {"count": 0, "total": "Rs.0", "items": []},
    }

AGING_DATA["pipeline_leads"]     = _empty_pipeline_bucket()
AGING_DATA["pipeline_meetings"]  = _empty_pipeline_bucket()
AGING_DATA["pipeline_proposals"] = _empty_pipeline_bucket()
AGING_DATA["pipeline_orders"]    = _empty_pipeline_bucket()
AGING_DATA["pipeline_invoices"]  = _empty_pipeline_bucket()
AGING_DATA["pipeline_collections"] = {
    "7d": {
        "count": 2,
        "total": "Rs.3.2 Cr",
        "items": [
            {
                "company": "Fidelitus Transactions",
                "member":  "Amit Shah",
                "value":   "Rs.2 Cr",
                "days":    5,
                "reason":  "Payment by EOM confirmed",
            },
            {
                "company": "Fidelitus Projects",
                "member":  "Deepa Iyer",
                "value":   "Rs.1.2 Cr",
                "days":    7,
                "reason":  "Client OOO till Friday",
            },
        ],
    },
    "14d": {"count": 0, "total": "Rs.0", "items": []},
    "21d": {"count": 0, "total": "Rs.0", "items": []},
    "90d": {"count": 0, "total": "Rs.0", "items": []},
    "npa": {
        "count": 1,
        "total": "Rs.2.1 Cr",
        "items": [
            {
                "company": "Fidelitus GCC Nexus",
                "member":  "Kiran Bhat",
                "value":   "Rs.2.1 Cr",
                "days":    95,
                "reason":  "Negotiations ongoing",
            },
        ],
    },
}
