# app/mockup/dummy_data.py
# Single source of truth for Phase 0 mock data.
# PRODUCTION=1 -> this file is used. PRODUCTION=0 -> live MongoDB replaces it.

DASHBOARD_DATA = {
    "corporate": {
        "kpis": [
            {
                "label": "Target for Year",
                "value": "Rs.240 Cr",
                "target": "Rs.240 Cr",
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
                "delta": "up",
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
def _parse_cr(total_str):
    """Extract numeric Cr value from strings like 'Rs.2.1 Cr', 'Rs.0.9 Cr', 'Rs.0'."""
    import re
    m = re.search(r"Rs\.([\d.]+)\s*Cr", total_str)
    if m:
        return float(m.group(1))
    return 0.0

def _build_corporate_aging():
    buckets = ["7d", "14d", "21d", "90d", "npa"]
    result = {}
    for bucket in buckets:
        items = []
        total_cr = 0.0
        for slug_data in AGING_DATA.values():
            items.extend(slug_data[bucket]["items"])
            total_cr += _parse_cr(slug_data[bucket]["total"])
        count = len(items)
        if total_cr > 0:
            total_str = f"Rs.{total_cr:.1f} Cr"
        else:
            total_str = "Rs.0"
        result[bucket] = {"count": count, "items": items, "total": total_str}
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

AGING_DATA["pipeline_leads"] = {
    "7d": {
        "count": 2, "total": "Rs.0",
        "items": [
            {"company": "Fidelitus Transactions", "member": "Rajesh Kumar",  "value": "—", "days": 5, "reason": "Lead not contacted yet, assigned this week"},
            {"company": "Fidelitus Projects",     "member": "Arjun Shetty",  "value": "—", "days": 6, "reason": "Initial outreach email not responded to"},
        ],
    },
    "14d": {
        "count": 1, "total": "Rs.0",
        "items": [
            {"company": "Fidelitus HR Labs",      "member": "Preethi Nair",  "value": "—", "days": 10, "reason": "Warm lead, follow-up calls unanswered"},
        ],
    },
    "21d": {"count": 0, "total": "Rs.0", "items": []},
    "90d": {"count": 0, "total": "Rs.0", "items": []},
    "npa":  {"count": 0, "total": "Rs.0", "items": []},
}
AGING_DATA["pipeline_meetings"] = {
    "7d": {
        "count": 2, "total": "Rs.0",
        "items": [
            {"company": "Fidelitus Transactions", "member": "Priya Menon",   "value": "—", "days": 4, "reason": "Meeting committed, client rescheduled"},
            {"company": "Fidelitus FMS",          "member": "Anil Kapoor",   "value": "—", "days": 6, "reason": "Facility head unavailable this week"},
        ],
    },
    "14d": {
        "count": 1, "total": "Rs.0",
        "items": [
            {"company": "Fidelitus Technology",   "member": "Rohini Das",    "value": "—", "days": 11, "reason": "Demo environment not ready, delayed"},
        ],
    },
    "21d": {"count": 0, "total": "Rs.0", "items": []},
    "90d": {"count": 0, "total": "Rs.0", "items": []},
    "npa":  {"count": 0, "total": "Rs.0", "items": []},
}
AGING_DATA["pipeline_proposals"] = {
    "7d": {
        "count": 2,
        "total": "Rs.4.0 Cr",
        "items": [
            {"company": "Fidelitus Transactions", "member": "Priya Menon",   "value": "Rs.2.2 Cr", "days": 6,  "reason": "Client committee review delayed, decision by Mon"},
            {"company": "Fidelitus Projects",     "member": "Arjun Shetty",  "value": "Rs.1.8 Cr", "days": 5,  "reason": "Technical annexure revision requested"},
        ],
    },
    "14d": {
        "count": 1,
        "total": "Rs.1.5 Cr",
        "items": [
            {"company": "Fidelitus FMS",          "member": "Anil Kapoor",   "value": "Rs.1.5 Cr", "days": 12, "reason": "Procurement team awaiting legal clearance"},
        ],
    },
    "21d": {"count": 0, "total": "Rs.0", "items": []},
    "90d": {"count": 0, "total": "Rs.0", "items": []},
    "npa": {"count": 0, "total": "Rs.0", "items": []},
}
AGING_DATA["pipeline_orders"] = {
    "7d": {
        "count": 2,
        "total": "Rs.5.5 Cr",
        "items": [
            {"company": "Fidelitus Transactions", "member": "Rajesh Kumar",  "value": "Rs.3.0 Cr", "days": 4,  "reason": "LOI signed, agreement drafting in progress"},
            {"company": "Fidelitus GCC Nexus",    "member": "Aditya Sharma", "value": "Rs.2.5 Cr", "days": 7,  "reason": "Client board approval pending"},
        ],
    },
    "14d": {
        "count": 1,
        "total": "Rs.2.0 Cr",
        "items": [
            {"company": "Fidelitus Projects",     "member": "Deepa Thomas",  "value": "Rs.2.0 Cr", "days": 11, "reason": "Stamp duty payment held pending registration slot"},
        ],
    },
    "21d": {"count": 0, "total": "Rs.0", "items": []},
    "90d": {"count": 0, "total": "Rs.0", "items": []},
    "npa": {"count": 0, "total": "Rs.0", "items": []},
}
AGING_DATA["pipeline_invoices"] = {
    "7d": {
        "count": 2, "total": "Rs.8 Cr",
        "items": [
            {"company": "Fidelitus Transactions", "member": "Anand Rao",     "value": "Rs.5 Cr",  "days": 5, "reason": "Invoice raised, awaiting client PO number"},
            {"company": "Fidelitus FMS",          "member": "Sneha Iyer",    "value": "Rs.3 Cr",  "days": 4, "reason": "Monthly invoice pending manager approval"},
        ],
    },
    "14d": {
        "count": 1, "total": "Rs.6 Cr",
        "items": [
            {"company": "Fidelitus Projects",     "member": "Kiran Joshi",   "value": "Rs.6 Cr",  "days": 12, "reason": "Retention invoice, milestone dispute ongoing"},
        ],
    },
    "21d": {"count": 0, "total": "Rs.0", "items": []},
    "90d": {"count": 0, "total": "Rs.0", "items": []},
    "npa":  {"count": 0, "total": "Rs.0", "items": []},
}
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

# KPI drill-down detail rows per company.
# Keys: revenue, invoiced, meetings, proposals.
# (payments drill-down is handled by AGING_DATA)
KPI_DETAILS = {
    "transactions": {
        "revenue": {"items": [
            {"client": "Prestige Office Park",   "bd": "Rajesh Kumar",  "value": "Rs.15 Cr", "type": "Commercial Lease", "status": "Closed"},
            {"client": "Embassy Business Hub",   "bd": "Priya Menon",   "value": "Rs.12 Cr", "type": "Commercial Sale",  "status": "Closed"},
            {"client": "Brigade Tech Park",      "bd": "Anand Rao",     "value": "Rs.10 Cr", "type": "Commercial Lease", "status": "Closed"},
            {"client": "Sobha Silicon Oaks",     "bd": "Suresh Nair",   "value": "Rs.9 Cr",  "type": "Commercial Lease", "status": "Closed"},
            {"client": "RMZ Infinity",           "bd": "Kavitha Reddy", "value": "Rs.8 Cr",  "type": "Commercial Lease", "status": "Closed"},
            {"client": "Salarpuria Sattva",      "bd": "Vikram Singh",  "value": "Rs.7 Cr",  "type": "Office Lease",     "status": "Committed"},
            {"client": "Bagmane Tech Park",      "bd": "Mohan Das",     "value": "Rs.7 Cr",  "type": "Office Sale",      "status": "Committed"},
        ]},
        "invoiced": {"items": [
            {"client": "Prestige Office Park",   "ref": "INV-TR-0142", "amount": "Rs.15 Cr", "date": "10 Mar", "status": "Paid"},
            {"client": "Embassy Business Hub",   "ref": "INV-TR-0138", "amount": "Rs.12 Cr", "date": "15 Mar", "status": "Paid"},
            {"client": "Brigade Tech Park",      "ref": "INV-TR-0155", "amount": "Rs.10 Cr", "date": "01 Apr", "status": "Pending"},
            {"client": "Sobha Silicon Oaks",     "ref": "INV-TR-0161", "amount": "Rs.9 Cr",  "date": "05 Apr", "status": "Pending"},
            {"client": "RMZ Infinity",           "ref": "INV-TR-0168", "amount": "Rs.8 Cr",  "date": "12 Apr", "status": "Sent"},
        ]},
        "meetings": {"items": [
            {"client": "Prestige Group",         "bd": "Rajesh Kumar",  "date": "28 Apr", "type": "Site Review",           "next_step": "Shortlisted alternate floor"},
            {"client": "Embassy Group",          "bd": "Priya Menon",   "date": "25 Apr", "type": "Deal Review",           "next_step": "LOI to be issued by Fri"},
            {"client": "RMZ Corp",               "bd": "Anand Rao",     "date": "24 Apr", "type": "Proposal Presentation", "next_step": "Awaiting internal approval"},
            {"client": "Bagmane Developers",     "bd": "Suresh Nair",   "date": "22 Apr", "type": "Requirement Call",      "next_step": "20,000 sqft office search open"},
            {"client": "Brigade Group",          "bd": "Kavitha Reddy", "date": "21 Apr", "type": "Follow-up",             "next_step": "Agreement signing next week"},
        ]},
        "proposals": {"items": [
            {"client": "RMZ Corp",               "bd": "Priya Menon",   "value": "Rs.22 Cr", "submitted": "10 Apr", "status": "Under Review"},
            {"client": "L&T Realty",             "bd": "Rajesh Kumar",  "value": "Rs.18 Cr", "submitted": "05 Apr", "status": "Shortlisted"},
            {"client": "Manyata Tech Park",      "bd": "Anand Rao",     "value": "Rs.15 Cr", "submitted": "15 Apr", "status": "Pending"},
            {"client": "Bagmane Developers",     "bd": "Suresh Nair",   "value": "Rs.12 Cr", "submitted": "20 Apr", "status": "Submitted"},
            {"client": "Tata Realty",            "bd": "Vikram Singh",  "value": "Rs.9 Cr",  "submitted": "25 Apr", "status": "Submitted"},
        ]},
    },
    "projects": {
        "revenue": {"items": [
            {"client": "Godrej Properties",      "bd": "Arjun Shetty",  "value": "Rs.8 Cr",  "type": "Project Mgmt",     "status": "Closed"},
            {"client": "Puravankara",            "bd": "Deepa Thomas",  "value": "Rs.6 Cr",  "type": "Construction Mgmt","status": "Closed"},
            {"client": "Shriram Properties",     "bd": "Kiran Joshi",   "value": "Rs.5 Cr",  "type": "Project Mgmt",     "status": "Closed"},
            {"client": "Assetz Property",        "bd": "Meera Pillai",  "value": "Rs.5 Cr",  "type": "Fit-Out Mgmt",     "status": "Committed"},
            {"client": "Arvind SmartSpaces",     "bd": "Rahul Verma",   "value": "Rs.5 Cr",  "type": "Project Mgmt",     "status": "Committed"},
        ]},
        "invoiced": {"items": [
            {"client": "Godrej Properties",      "ref": "INV-PJ-0081", "amount": "Rs.8 Cr",  "date": "12 Mar", "status": "Paid"},
            {"client": "Puravankara",            "ref": "INV-PJ-0076", "amount": "Rs.6 Cr",  "date": "20 Mar", "status": "Pending"},
            {"client": "Shriram Properties",     "ref": "INV-PJ-0089", "amount": "Rs.5 Cr",  "date": "02 Apr", "status": "Pending"},
            {"client": "Assetz Property",        "ref": "INV-PJ-0094", "amount": "Rs.2 Cr",  "date": "18 Apr", "status": "Sent"},
        ]},
        "meetings": {"items": [
            {"client": "Godrej Properties",      "bd": "Arjun Shetty",  "date": "27 Apr", "type": "Milestone Review",    "next_step": "Phase 2 kickoff in May"},
            {"client": "Puravankara",            "bd": "Deepa Thomas",  "date": "24 Apr", "type": "Site Inspection",     "next_step": "Snagging list to be closed"},
            {"client": "Shriram Properties",     "bd": "Kiran Joshi",   "date": "22 Apr", "type": "Progress Review",     "next_step": "Completion cert by 15 May"},
            {"client": "Arvind SmartSpaces",     "bd": "Rahul Verma",   "date": "19 Apr", "type": "Kick-off",            "next_step": "Resource mobilisation this week"},
        ]},
        "proposals": {"items": [
            {"client": "Mahindra Lifespaces",    "bd": "Arjun Shetty",  "value": "Rs.12 Cr", "submitted": "08 Apr", "status": "Under Review"},
            {"client": "Kolte-Patil",            "bd": "Deepa Thomas",  "value": "Rs.9 Cr",  "submitted": "14 Apr", "status": "Shortlisted"},
            {"client": "Century Real Estate",    "bd": "Kiran Joshi",   "value": "Rs.7 Cr",  "submitted": "22 Apr", "status": "Submitted"},
            {"client": "Nitesh Estates",         "bd": "Meera Pillai",  "value": "Rs.5 Cr",  "submitted": "28 Apr", "status": "Submitted"},
        ]},
    },
    "fms": {
        "revenue": {"items": [
            {"client": "KPMG India",             "bd": "Anil Kapoor",   "value": "Rs.5 Cr",  "type": "FMS Annual",       "status": "Closed"},
            {"client": "Infosys BPM",            "bd": "Sneha Iyer",    "value": "Rs.4 Cr",  "type": "FMS Annual",       "status": "Closed"},
            {"client": "Wipro Technologies",     "bd": "Ramesh Gupta",  "value": "Rs.5 Cr",  "type": "FMS Annual",       "status": "Closed"},
            {"client": "Mphasis",                "bd": "Lata Srinivas", "value": "Rs.4 Cr",  "type": "FMS Quarterly",    "status": "Closed"},
            {"client": "UST Global",             "bd": "Gopal Nair",    "value": "Rs.3 Cr",  "type": "FMS Monthly",      "status": "Committed"},
            {"client": "Mindtree",               "bd": "Anil Kapoor",   "value": "Rs.3 Cr",  "type": "FMS Annual",       "status": "Committed"},
        ]},
        "invoiced": {"items": [
            {"client": "KPMG India",             "ref": "INV-FM-0201", "amount": "Rs.5 Cr",  "date": "01 Apr", "status": "Paid"},
            {"client": "Infosys BPM",            "ref": "INV-FM-0198", "amount": "Rs.4 Cr",  "date": "01 Apr", "status": "Paid"},
            {"client": "Wipro Technologies",     "ref": "INV-FM-0205", "amount": "Rs.5 Cr",  "date": "01 Apr", "status": "Pending"},
            {"client": "Mphasis",                "ref": "INV-FM-0210", "amount": "Rs.3 Cr",  "date": "01 Apr", "status": "Pending"},
            {"client": "UST Global",             "ref": "INV-FM-0214", "amount": "Rs.2 Cr",  "date": "15 Apr", "status": "Sent"},
        ]},
        "meetings": {"items": [
            {"client": "KPMG India",             "bd": "Anil Kapoor",   "date": "29 Apr", "type": "Quarterly Review",   "next_step": "Pest control scope to be added"},
            {"client": "Wipro Technologies",     "bd": "Ramesh Gupta",  "date": "26 Apr", "type": "Facility Audit",     "next_step": "HVAC maintenance schedule"},
            {"client": "Mphasis",                "bd": "Lata Srinivas", "date": "23 Apr", "type": "Contract Renewal",   "next_step": "Revised SOW by 10 May"},
            {"client": "UST Global",             "bd": "Gopal Nair",    "date": "20 Apr", "type": "Onboarding",         "next_step": "Staff deployment this month"},
        ]},
        "proposals": {"items": [
            {"client": "Accenture India",        "bd": "Anil Kapoor",   "value": "Rs.6 Cr",  "submitted": "05 Apr", "status": "Under Review"},
            {"client": "Capgemini",              "bd": "Sneha Iyer",    "value": "Rs.4 Cr",  "submitted": "12 Apr", "status": "Shortlisted"},
            {"client": "NTT Data",               "bd": "Ramesh Gupta",  "value": "Rs.3 Cr",  "submitted": "20 Apr", "status": "Submitted"},
        ]},
    },
    "hrlabs": {
        "revenue": {"items": [
            {"client": "Deutsche Bank",          "bd": "Preethi Nair",  "value": "Rs.2 Cr",  "type": "Executive Search", "status": "Closed"},
            {"client": "Goldman Sachs",          "bd": "Santosh Kumar", "value": "Rs.2 Cr",  "type": "Bulk Staffing",    "status": "Closed"},
            {"client": "JP Morgan Chase",        "bd": "Divya Menon",   "value": "Rs.2 Cr",  "type": "Staffing Contract","status": "Closed"},
            {"client": "HSBC",                   "bd": "Naresh Patel",  "value": "Rs.2 Cr",  "type": "RPO Contract",     "status": "Closed"},
            {"client": "Barclays",               "bd": "Shobha Rao",    "value": "Rs.2 Cr",  "type": "Staffing Contract","status": "Committed"},
            {"client": "Standard Chartered",     "bd": "Preethi Nair",  "value": "Rs.1 Cr",  "type": "Executive Search", "status": "Committed"},
        ]},
        "invoiced": {"items": [
            {"client": "Deutsche Bank",          "ref": "INV-HR-0312", "amount": "Rs.2 Cr",  "date": "05 Apr", "status": "Paid"},
            {"client": "Goldman Sachs",          "ref": "INV-HR-0308", "amount": "Rs.2 Cr",  "date": "08 Apr", "status": "Pending"},
            {"client": "JP Morgan Chase",        "ref": "INV-HR-0315", "amount": "Rs.2 Cr",  "date": "12 Apr", "status": "Pending"},
            {"client": "HSBC",                   "ref": "INV-HR-0319", "amount": "Rs.1 Cr",  "date": "18 Apr", "status": "Sent"},
            {"client": "Barclays",               "ref": "INV-HR-0322", "amount": "Rs.1 Cr",  "date": "25 Apr", "status": "Sent"},
        ]},
        "meetings": {"items": [
            {"client": "Deutsche Bank",          "bd": "Preethi Nair",  "date": "28 Apr", "type": "Quarterly Review",   "next_step": "20 more positions to open in Q2"},
            {"client": "Goldman Sachs",          "bd": "Santosh Kumar", "date": "25 Apr", "type": "Placement Follow-up","next_step": "2 joiners pending offer acceptance"},
            {"client": "Barclays",               "bd": "Shobha Rao",    "date": "22 Apr", "type": "RPO Discussion",     "next_step": "SLA to be signed by 05 May"},
            {"client": "Standard Chartered",     "bd": "Divya Menon",   "date": "18 Apr", "type": "Requirement Brief",  "next_step": "5 VP-level positions to source"},
        ]},
        "proposals": {"items": [
            {"client": "Citi Bank",              "bd": "Preethi Nair",  "value": "Rs.3 Cr",  "submitted": "07 Apr", "status": "Under Review"},
            {"client": "BNP Paribas",            "bd": "Santosh Kumar", "value": "Rs.2 Cr",  "submitted": "14 Apr", "status": "Shortlisted"},
            {"client": "Societe Generale",       "bd": "Naresh Patel",  "value": "Rs.2 Cr",  "submitted": "22 Apr", "status": "Submitted"},
            {"client": "Credit Suisse",          "bd": "Divya Menon",   "value": "Rs.1 Cr",  "submitted": "28 Apr", "status": "Submitted"},
        ]},
    },
    "technology": {
        "revenue": {"items": [
            {"client": "Tata Consultancy",       "bd": "Vikash Mehta",  "value": "Rs.2.5 Cr","type": "CRM Build",        "status": "Closed"},
            {"client": "Infosys",                "bd": "Rohini Das",    "value": "Rs.2 Cr",  "type": "Portal Dev",       "status": "Closed"},
            {"client": "Wipro",                  "bd": "Sudhir Bhat",   "value": "Rs.2 Cr",  "type": "Integration",      "status": "Closed"},
            {"client": "HCL Technologies",       "bd": "Vikash Mehta",  "value": "Rs.1.5 Cr","type": "Mobile App",       "status": "Committed"},
            {"client": "Tech Mahindra",          "bd": "Rohini Das",    "value": "Rs.1 Cr",  "type": "Analytics",        "status": "Committed"},
        ]},
        "invoiced": {"items": [
            {"client": "Tata Consultancy",       "ref": "INV-TK-0441", "amount": "Rs.2.5 Cr","date": "10 Mar", "status": "Paid"},
            {"client": "Infosys",                "ref": "INV-TK-0438", "amount": "Rs.2 Cr",  "date": "20 Mar", "status": "Pending"},
            {"client": "Wipro",                  "ref": "INV-TK-0445", "amount": "Rs.1.5 Cr","date": "05 Apr", "status": "Pending"},
        ]},
        "meetings": {"items": [
            {"client": "Tata Consultancy",       "bd": "Vikash Mehta",  "date": "27 Apr", "type": "UAT Review",         "next_step": "Sign-off expected by 05 May"},
            {"client": "HCL Technologies",       "bd": "Rohini Das",    "date": "23 Apr", "type": "Scope Review",       "next_step": "Module 3 delivery plan to share"},
            {"client": "Tech Mahindra",          "bd": "Sudhir Bhat",   "date": "21 Apr", "type": "Demo",               "next_step": "POC approval in committee next week"},
        ]},
        "proposals": {"items": [
            {"client": "Mindtree",               "bd": "Vikash Mehta",  "value": "Rs.3 Cr",  "submitted": "09 Apr", "status": "Under Review"},
            {"client": "Mphasis",                "bd": "Rohini Das",    "value": "Rs.2 Cr",  "submitted": "17 Apr", "status": "Shortlisted"},
            {"client": "NIIT Technologies",      "bd": "Sudhir Bhat",   "value": "Rs.1.5 Cr","submitted": "24 Apr", "status": "Submitted"},
        ]},
    },
    "gcc": {
        "revenue": {"items": [
            {"client": "Nordea Bank",            "bd": "Aditya Sharma", "value": "Rs.1 Cr",  "type": "GCC Advisory",    "status": "Closed"},
            {"client": "Alstom",                 "bd": "Aditya Sharma", "value": "Rs.0",      "type": "GCC Setup",       "status": "In Pipeline"},
        ]},
        "invoiced": {"items": [
            {"client": "Nordea Bank",            "ref": "INV-GC-0021", "amount": "Rs.0",      "date": "--",     "status": "Pending"},
        ]},
        "meetings": {"items": [
            {"client": "Nordea Bank",            "bd": "Aditya Sharma", "date": "26 Apr", "type": "Feasibility",        "next_step": "Site visit scheduled for 10 May"},
            {"client": "Alstom",                 "bd": "Aditya Sharma", "date": "22 Apr", "type": "Introduction",       "next_step": "RFP expected in 2 weeks"},
            {"client": "Hitachi Energy",         "bd": "Aditya Sharma", "date": "18 Apr", "type": "Requirement Call",   "next_step": "Proposal to be sent by 05 May"},
        ]},
        "proposals": {"items": [
            {"client": "Alstom",                 "bd": "Aditya Sharma", "value": "Rs.8 Cr",  "submitted": "15 Apr", "status": "Under Review"},
            {"client": "Hitachi Energy",         "bd": "Aditya Sharma", "value": "Rs.6 Cr",  "submitted": "28 Apr", "status": "Submitted"},
            {"client": "ABB India",              "bd": "Aditya Sharma", "value": "Rs.5 Cr",  "submitted": "30 Apr", "status": "Submitted"},
        ]},
    },
}

# KPI aging: committed-but-delayed items per company per KPI tab.
# Keys match company slug + tab name. Bucket schema identical to AGING_DATA.
KPI_AGING = {
    "transactions": {
        "revenue": {
            "7d":  {"count": 2, "total": "Rs.14 Cr", "items": [
                {"company": "Fidelitus Trans", "member": "Vikram Singh",  "value": "Rs.7 Cr",  "days": 5, "reason": "LOI delayed pending legal review"},
                {"company": "Fidelitus Trans", "member": "Mohan Das",     "value": "Rs.7 Cr",  "days": 6, "reason": "Client board approval pending"},
            ]},
            "14d": {"count": 1, "total": "Rs.9 Cr", "items": [
                {"company": "Fidelitus Trans", "member": "Kavitha Reddy", "value": "Rs.9 Cr",  "days": 12, "reason": "Agreement redrafting by client counsel"},
            ]},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "invoiced": {
            "7d":  {"count": 2, "total": "Rs.17 Cr", "items": [
                {"company": "Fidelitus Trans", "member": "Suresh Nair",   "value": "Rs.10 Cr", "days": 4,  "reason": "Client finance team on leave"},
                {"company": "Fidelitus Trans", "member": "Anand Rao",     "value": "Rs.7 Cr",  "days": 6,  "reason": "Bank transfer initiated, clearance awaited"},
            ]},
            "14d": {"count": 1, "total": "Rs.9 Cr", "items": [
                {"company": "Fidelitus Trans", "member": "Rajesh Kumar",  "value": "Rs.9 Cr",  "days": 11, "reason": "Disputed invoice line item, revised invoice sent"},
            ]},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "meetings": {
            "7d":  {"count": 2, "total": "—", "items": [
                {"company": "Fidelitus Trans", "member": "Priya Menon",   "value": "—", "days": 3, "reason": "Client rescheduled, new slot pending confirmation"},
                {"company": "Fidelitus Trans", "member": "Anand Rao",     "value": "—", "days": 5, "reason": "Key stakeholder travelling"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "proposals": {
            "7d":  {"count": 1, "total": "Rs.22 Cr", "items": [
                {"company": "Fidelitus Trans", "member": "Priya Menon",   "value": "Rs.22 Cr", "days": 4, "reason": "Awaiting pricing sign-off from MD"},
            ]},
            "14d": {"count": 1, "total": "Rs.18 Cr", "items": [
                {"company": "Fidelitus Trans", "member": "Rajesh Kumar",  "value": "Rs.18 Cr", "days": 10, "reason": "Technical scope being finalised"},
            ]},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
    },
    "projects": {
        "revenue": {
            "7d":  {"count": 1, "total": "Rs.5 Cr", "items": [
                {"company": "Fidelitus Projects", "member": "Meera Pillai",  "value": "Rs.5 Cr",  "days": 6,  "reason": "Completion certificate not issued"},
            ]},
            "14d": {"count": 1, "total": "Rs.5 Cr", "items": [
                {"company": "Fidelitus Projects", "member": "Rahul Verma",   "value": "Rs.5 Cr",  "days": 13, "reason": "Scope change order pending client sign"},
            ]},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "invoiced": {
            "7d":  {"count": 1, "total": "Rs.6 Cr", "items": [
                {"company": "Fidelitus Projects", "member": "Deepa Thomas",  "value": "Rs.6 Cr",  "days": 5,  "reason": "Client awaiting internal PO approval"},
            ]},
            "14d": {"count": 1, "total": "Rs.5 Cr", "items": [
                {"company": "Fidelitus Projects", "member": "Kiran Joshi",   "value": "Rs.5 Cr",  "days": 12, "reason": "Invoice under dispute for punch list"},
            ]},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "meetings": {
            "7d":  {"count": 1, "total": "—", "items": [
                {"company": "Fidelitus Projects", "member": "Arjun Shetty",  "value": "—", "days": 4, "reason": "Site visit deferred due to weather"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "proposals": {
            "7d":  {"count": 1, "total": "Rs.12 Cr", "items": [
                {"company": "Fidelitus Projects", "member": "Arjun Shetty",  "value": "Rs.12 Cr", "days": 5, "reason": "Bill of quantities revision ongoing"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
    },
    "fms": {
        "revenue": {
            "7d":  {"count": 1, "total": "Rs.3 Cr", "items": [
                {"company": "Fidelitus FMS", "member": "Gopal Nair",    "value": "Rs.3 Cr",  "days": 5, "reason": "AMC sign-off delayed by facility head"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "invoiced": {
            "7d":  {"count": 1, "total": "Rs.5 Cr", "items": [
                {"company": "Fidelitus FMS", "member": "Ramesh Gupta",  "value": "Rs.5 Cr",  "days": 6, "reason": "Monthly billing cycle delay by client ERP"},
            ]},
            "14d": {"count": 1, "total": "Rs.3 Cr", "items": [
                {"company": "Fidelitus FMS", "member": "Lata Srinivas", "value": "Rs.3 Cr",  "days": 11, "reason": "Security deposit adjustment dispute"},
            ]},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "meetings": {
            "7d":  {"count": 1, "total": "—", "items": [
                {"company": "Fidelitus FMS", "member": "Anil Kapoor",   "value": "—", "days": 4, "reason": "Facility manager on leave, rescheduling"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "proposals": {
            "7d":  {"count": 1, "total": "Rs.6 Cr", "items": [
                {"company": "Fidelitus FMS", "member": "Sneha Iyer",    "value": "Rs.6 Cr",  "days": 5, "reason": "Client requesting scope addition before sign-off"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
    },
    "hrlabs": {
        "revenue": {
            "7d":  {"count": 1, "total": "Rs.2 Cr", "items": [
                {"company": "Fidelitus HR Labs", "member": "Shobha Rao",    "value": "Rs.2 Cr",  "days": 6, "reason": "Candidate joining deferred by 2 weeks"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "invoiced": {
            "7d":  {"count": 1, "total": "Rs.2 Cr", "items": [
                {"company": "Fidelitus HR Labs", "member": "Santosh Kumar", "value": "Rs.2 Cr",  "days": 5, "reason": "Client HR system delay in processing invoice"},
            ]},
            "14d": {"count": 1, "total": "Rs.2 Cr", "items": [
                {"company": "Fidelitus HR Labs", "member": "Divya Menon",   "value": "Rs.2 Cr",  "days": 10, "reason": "PO amendment blocking payment release"},
            ]},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "meetings": {
            "7d":  {"count": 1, "total": "—", "items": [
                {"company": "Fidelitus HR Labs", "member": "Preethi Nair",  "value": "—", "days": 3, "reason": "CHRO travelling, meeting moved to next week"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "proposals": {
            "7d":  {"count": 1, "total": "Rs.3 Cr", "items": [
                {"company": "Fidelitus HR Labs", "member": "Preethi Nair",  "value": "Rs.3 Cr",  "days": 4, "reason": "Pricing revision requested by client"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
    },
    "technology": {
        "revenue": {
            "7d":  {"count": 1, "total": "Rs.1.5 Cr", "items": [
                {"company": "Fidelitus Technology", "member": "Vikash Mehta",  "value": "Rs.1.5 Cr", "days": 7, "reason": "UAT sign-off delayed by client infra team"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "invoiced": {
            "7d":  {"count": 1, "total": "Rs.2 Cr", "items": [
                {"company": "Fidelitus Technology", "member": "Rohini Das",    "value": "Rs.2 Cr",   "days": 6, "reason": "Client finance freeze until Q1 close"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "meetings": {
            "7d":  {"count": 1, "total": "—", "items": [
                {"company": "Fidelitus Technology", "member": "Sudhir Bhat",   "value": "—", "days": 5, "reason": "Technical lead on bench, meeting deferred"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "proposals": {
            "7d":  {"count": 1, "total": "Rs.3 Cr", "items": [
                {"company": "Fidelitus Technology", "member": "Vikash Mehta",  "value": "Rs.3 Cr",   "days": 4, "reason": "Architecture diagram review pending internally"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
    },
    "gcc": {
        "revenue": {
            "7d":  {"count": 1, "total": "Rs.1 Cr", "items": [
                {"company": "Fidelitus GCC Nexus", "member": "Aditya Sharma", "value": "Rs.1 Cr",   "days": 6, "reason": "LOI received, formal agreement in drafting"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "invoiced": {
            "7d":  {"count": 0, "total": "Rs.0", "items": []},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "meetings": {
            "7d":  {"count": 1, "total": "—", "items": [
                {"company": "Fidelitus GCC Nexus", "member": "Aditya Sharma", "value": "—", "days": 4, "reason": "International client, time-zone scheduling in progress"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
        "proposals": {
            "7d":  {"count": 1, "total": "Rs.8 Cr", "items": [
                {"company": "Fidelitus GCC Nexus", "member": "Aditya Sharma", "value": "Rs.8 Cr",   "days": 5, "reason": "Awaiting inputs from GCC consultant"},
            ]},
            "14d": {"count": 0, "total": "Rs.0", "items": []},
            "21d": {"count": 0, "total": "Rs.0", "items": []},
            "90d": {"count": 0, "total": "Rs.0", "items": []},
            "npa":  {"count": 0, "total": "Rs.0", "items": []},
        },
    },
}
