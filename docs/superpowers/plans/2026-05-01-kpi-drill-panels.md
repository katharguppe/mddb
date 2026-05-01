# KPI Drill-Down Panels (Know More) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the single aging panel in each company's Know More section with a 5-tab KPI panel (Revenue · Invoiced · Payments · Meetings · Proposals), where each tab shows an item-level detail table; the Payments tab reuses the existing aging_panel macro.

**Architecture:** A new `KPI_DETAILS` dict in `dummy_data.py` holds per-company item rows for Revenue, Invoiced, Meetings, and Proposals (Payments is already covered by `AGING_DATA`). A new Jinja2 macro `kpi_tabs_panel` in `partials/kpi_tabs_panel.html` renders the tab strip and five panels, calling the existing `aging_panel` macro for the Payments tab. `dashboard.html` swaps the direct `aging_panel` call for `kpi_tabs_panel`. Vanilla JS in `script.js` handles tab switching and initialises the Revenue tab when Know More opens.

**Tech Stack:** Python 3.13, FastAPI, Jinja2, vanilla HTML/CSS/JS

---

## File Map

| Action | Path | Responsibility |
|--------|------|----------------|
| CREATE | `tasks/TASK-005-kpi-drill-panels.md` | Task tracking file |
| MODIFY | `app/mockup/dummy_data.py` | Append `KPI_DETAILS` dict (6 companies × 4 KPIs) |
| CREATE | `app/templates/partials/kpi_tabs_panel.html` | Jinja2 macro: tab strip + 5 content panels |
| MODIFY | `app/mockup/routes.py` | Pass `KPI_DETAILS` to template context |
| MODIFY | `app/templates/dashboard.html` | Replace `aging_panel` call with `kpi_tabs_panel` |
| MODIFY | `app/static/style.css` | Tab strip + status badge styles |
| MODIFY | `app/static/script.js` | `switchKpiTab()` + update `toggleDetails()` to init Revenue tab |

---

## Task 1: Create the TASK file

**Files:**
- Create: `tasks/TASK-005-kpi-drill-panels.md`

- [ ] **Step 1: Write the task file**

```markdown
# TASK-005 -- KPI Drill-Down Panels (Know More)

**Status:** In Progress
**Session:** s05 (Phase 0 -- Mockup)
**Scope:** app/mockup/dummy_data.py, app/templates/dashboard.html,
           app/templates/partials/kpi_tabs_panel.html (create),
           app/mockup/routes.py, app/static/style.css, app/static/script.js ONLY.

## Goal
Replace the single aging panel in each company Know More section with a
5-tab panel: Revenue · Invoiced · Payments · Meetings · Proposals.
Each tab shows an item-level detail table. Payments tab reuses the
existing aging_panel macro (TASK-004). All data from dummy_data.py.

## Acceptance Criteria
- [ ] Know More panel shows 5 tabs: Revenue | Invoiced | Payments | Meetings | Proposals
- [ ] Revenue tab: table — Client | BD Person | Value | Type | Status
- [ ] Invoiced tab: table — Client | Invoice Ref | Amount | Date | Status
- [ ] Payments tab: existing aging bucket pills + tables (aging_panel macro unchanged)
- [ ] Meetings tab: table — Client | BD Person | Date | Type | Next Step
- [ ] Proposals tab: table — Client | BD Person | Value | Submitted | Status
- [ ] Status cells use color badges: green=Closed/Paid/Accepted, amber=Committed/Pending/Shortlisted, red=Overdue/Declined
- [ ] Revenue tab active by default when Know More opens
- [ ] Clicking a tab switches content without page reload
- [ ] Vanilla JS only, no frameworks
- [ ] KPI_DETAILS in dummy_data.py for all 6 companies

## Files Changed
- MODIFY  app/mockup/dummy_data.py
- CREATE  app/templates/partials/kpi_tabs_panel.html
- MODIFY  app/mockup/routes.py
- MODIFY  app/templates/dashboard.html
- MODIFY  app/static/style.css
- MODIFY  app/static/script.js
```

- [ ] **Step 2: Commit**

```bash
git add tasks/TASK-005-kpi-drill-panels.md
git commit -m "[TASK-005] chore: add task file for KPI drill-down panels"
```

---

## Task 2: Add `KPI_DETAILS` to `dummy_data.py`

**Files:**
- Modify: `app/mockup/dummy_data.py`

Append the entire block below at the end of the file (after `AGING_DATA["corporate"] = _build_corporate_aging()`).

- [ ] **Step 1: Append `KPI_DETAILS` to `app/mockup/dummy_data.py`**

```python
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
```

- [ ] **Step 2: Verify the file parses without error**

```bash
cd D:/Fidelitus/mddb && python -c "from app.mockup.dummy_data import KPI_DETAILS; print('companies:', list(KPI_DETAILS.keys())); print('transactions tabs:', list(KPI_DETAILS['transactions'].keys()))"
```

Expected output:
```
companies: ['transactions', 'projects', 'fms', 'hrlabs', 'technology', 'gcc']
transactions tabs: ['revenue', 'invoiced', 'meetings', 'proposals']
```

- [ ] **Step 3: Commit**

```bash
git add app/mockup/dummy_data.py
git commit -m "[TASK-005] feat: add KPI_DETAILS dummy data for all 6 companies"
```

---

## Task 3: Create `partials/kpi_tabs_panel.html`

**Files:**
- Create: `app/templates/partials/kpi_tabs_panel.html`

- [ ] **Step 1: Write `app/templates/partials/kpi_tabs_panel.html`**

```jinja2
{# app/templates/partials/kpi_tabs_panel.html
   Macro: kpi_tabs_panel(company_id, kpi_details, aging)
   kpi_details = KPI_DETAILS[company_id]
   aging       = AGING_DATA[company_id]
#}
{% from "partials/aging_panel.html" import aging_panel %}

{% macro kpi_tabs_panel(company_id, kpi_details, aging) %}
<div class="kpi-tabs-container" id="kpi-tabs-{{ company_id }}">

    {# ── Tab strip ── #}
    <div class="kpi-tab-strip">
        <button class="kpi-tab active"
                data-tab="revenue"
                onclick="switchKpiTab('{{ company_id }}', 'revenue')">Revenue</button>
        <button class="kpi-tab"
                data-tab="invoiced"
                onclick="switchKpiTab('{{ company_id }}', 'invoiced')">Invoiced</button>
        <button class="kpi-tab"
                data-tab="payments"
                onclick="switchKpiTab('{{ company_id }}', 'payments')">Payments</button>
        <button class="kpi-tab"
                data-tab="meetings"
                onclick="switchKpiTab('{{ company_id }}', 'meetings')">Meetings</button>
        <button class="kpi-tab"
                data-tab="proposals"
                onclick="switchKpiTab('{{ company_id }}', 'proposals')">Proposals</button>
    </div>

    {# ── Revenue panel ── #}
    <div class="kpi-tab-panel active" id="kpi-panel-{{ company_id }}-revenue">
        {% if kpi_details.revenue.items %}
        <table class="kpi-detail-table">
            <thead>
                <tr>
                    <th>Client</th><th>BD Person</th><th>Value</th><th>Type</th><th>Status</th>
                </tr>
            </thead>
            <tbody>
                {% for item in kpi_details.revenue.items %}
                <tr>
                    <td>{{ item.client }}</td>
                    <td>{{ item.bd }}</td>
                    <td class="kpi-detail-value">{{ item.value }}</td>
                    <td>{{ item.type }}</td>
                    <td><span class="status-badge status-{{ item.status | lower | replace(' ', '-') }}">{{ item.status }}</span></td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <p class="kpi-empty-state">No revenue items recorded.</p>
        {% endif %}
    </div>

    {# ── Invoiced panel ── #}
    <div class="kpi-tab-panel" id="kpi-panel-{{ company_id }}-invoiced">
        {% if kpi_details.invoiced.items %}
        <table class="kpi-detail-table">
            <thead>
                <tr>
                    <th>Client</th><th>Invoice Ref</th><th>Amount</th><th>Date</th><th>Status</th>
                </tr>
            </thead>
            <tbody>
                {% for item in kpi_details.invoiced.items %}
                <tr>
                    <td>{{ item.client }}</td>
                    <td class="kpi-detail-ref">{{ item.ref }}</td>
                    <td class="kpi-detail-value">{{ item.amount }}</td>
                    <td>{{ item.date }}</td>
                    <td><span class="status-badge status-{{ item.status | lower | replace(' ', '-') }}">{{ item.status }}</span></td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <p class="kpi-empty-state">No invoices recorded.</p>
        {% endif %}
    </div>

    {# ── Payments panel: reuse aging_panel macro ── #}
    <div class="kpi-tab-panel" id="kpi-panel-{{ company_id }}-payments">
        {{ aging_panel(company_id, aging) }}
    </div>

    {# ── Meetings panel ── #}
    <div class="kpi-tab-panel" id="kpi-panel-{{ company_id }}-meetings">
        {% if kpi_details.meetings.items %}
        <table class="kpi-detail-table">
            <thead>
                <tr>
                    <th>Client</th><th>BD Person</th><th>Date</th><th>Type</th><th>Next Step</th>
                </tr>
            </thead>
            <tbody>
                {% for item in kpi_details.meetings.items %}
                <tr>
                    <td>{{ item.client }}</td>
                    <td>{{ item.bd }}</td>
                    <td class="kpi-detail-date">{{ item.date }}</td>
                    <td>{{ item.type }}</td>
                    <td class="kpi-detail-nextstep">{{ item.next_step }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <p class="kpi-empty-state">No meetings recorded.</p>
        {% endif %}
    </div>

    {# ── Proposals panel ── #}
    <div class="kpi-tab-panel" id="kpi-panel-{{ company_id }}-proposals">
        {% if kpi_details.proposals.items %}
        <table class="kpi-detail-table">
            <thead>
                <tr>
                    <th>Client</th><th>BD Person</th><th>Value</th><th>Submitted</th><th>Status</th>
                </tr>
            </thead>
            <tbody>
                {% for item in kpi_details.proposals.items %}
                <tr>
                    <td>{{ item.client }}</td>
                    <td>{{ item.bd }}</td>
                    <td class="kpi-detail-value">{{ item.value }}</td>
                    <td class="kpi-detail-date">{{ item.submitted }}</td>
                    <td><span class="status-badge status-{{ item.status | lower | replace(' ', '-') }}">{{ item.status }}</span></td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <p class="kpi-empty-state">No proposals recorded.</p>
        {% endif %}
    </div>

</div>
{% endmacro %}
```

- [ ] **Step 2: Commit**

```bash
git add app/templates/partials/kpi_tabs_panel.html
git commit -m "[TASK-005] feat: add kpi_tabs_panel Jinja2 macro partial"
```

---

## Task 4: Update `routes.py`

**Files:**
- Modify: `app/mockup/routes.py`

- [ ] **Step 1: Update import and template context**

Replace the full contents of `app/mockup/routes.py`:

```python
# app/mockup/routes.py
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.mockup.dummy_data import DASHBOARD_DATA, AGING_DATA, KPI_DETAILS

templates_path = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_path))

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Render the MD Dashboard mockup."""
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "data": DASHBOARD_DATA,
            "aging": AGING_DATA,
            "kpi_details": KPI_DETAILS,
        },
    )
```

- [ ] **Step 2: Commit**

```bash
git add app/mockup/routes.py
git commit -m "[TASK-005] feat: pass KPI_DETAILS to dashboard template context"
```

---

## Task 5: Update `dashboard.html`

**Files:**
- Modify: `app/templates/dashboard.html`

Two changes:
1. Import `kpi_tabs_panel` macro (replace the `aging_panel` import).
2. Replace `aging_panel(company.id, aging[company.id])` call inside the company details div with `kpi_tabs_panel(company.id, kpi_details[company.id], aging[company.id])`.

The corporate aging panel below the KPI strip remains unchanged (it still calls `aging_panel` directly, so keep that import too — or import both).

- [ ] **Step 1: Write the full updated `dashboard.html`**

```jinja2
{% extends "base.html" %}
{% from "partials/aging_panel.html" import aging_panel %}
{% from "partials/kpi_tabs_panel.html" import kpi_tabs_panel %}

{% block title %}MD Dashboard . Fidelitus Corp{% endblock %}

{% block content %}
{# Macro: map percentage to CSS color-band class #}
{% macro pct_class(pct) -%}
  {%- if pct is none -%}
  {%- elif pct <= 25 -%}kpi-status-red
  {%- elif pct <= 50 -%}kpi-status-red-orange
  {%- elif pct <= 75 -%}kpi-status-amber
  {%- else -%}kpi-status-green
  {%- endif -%}
{%- endmacro %}

<header class="dashboard-header">
    <div>
        <p class="dashboard-eyebrow">Fidelitus Corp . MD Dashboard</p>
        <h1 class="dashboard-title">Consolidated View</h1>
    </div>
    <span class="phase-badge">Phase 0 Mockup</span>
</header>

<main class="dashboard-main">

    {# ── Section A: Corporate KPI Strip ── #}
    <section class="section">
        <div class="section-label">Corporate KPIs</div>
        <div class="kpi-strip">
            {% for kpi in data.corporate.kpis %}
            <div class="kpi-card kpi-card--clickable"
                 onclick="toggleCorporateAging()"
                 title="Click to view aging drill-down">
                <div class="kpi-label">{{ kpi.label }}</div>
                <div class="kpi-value">{{ kpi.value }}</div>
                {% if kpi.target %}
                <div class="kpi-target">of {{ kpi.target }}</div>
                {% endif %}
                {% if kpi.pct is not none %}
                <div class="kpi-footer">
                    <span class="pct-badge {{ pct_class(kpi.pct) }}">{{ kpi.pct }}%</span>
                    {% if kpi.delta == "up" %}<span class="delta-up">▲</span>
                    {% elif kpi.delta == "down" %}<span class="delta-down">▼</span>
                    {% endif %}
                </div>
                {% endif %}
            </div>
            {% endfor %}
        </div>

        {# ── Corporate aging panel (hidden until a KPI card is clicked) ── #}
        <div class="company-details corporate-aging-panel" id="details-corporate">
            {{ aging_panel("corporate", aging["corporate"]) }}
        </div>
    </section>

    {# ── Section B: Company Cards ── #}
    <section class="section">
        <div class="section-label">Subsidiaries</div>
        <div class="companies-grid">
            {% for company in data.companies %}
            <div class="company-card" style="border-top-color: {{ company.dot_color }}">

                {# Card header: dot + name #}
                <div class="company-card-header">
                    <span class="company-dot" style="background: {{ company.dot_color }}"></span>
                    <span class="company-name">{{ company.name }}</span>
                </div>

                {# KPI rows — skip Target row (shown in Know More panel) #}
                <div class="company-kpi-table">
                    {% for kpi in company.kpis %}
                    {% if kpi.label != "Target" %}
                    <div class="company-kpi-row">
                        <span class="ckpi-label">{{ kpi.label }}</span>
                        <span class="ckpi-value">{{ kpi.value }}</span>
                        {% if kpi.pct is not none %}
                        <span class="pct-badge {{ pct_class(kpi.pct) }}">{{ kpi.pct }}%</span>
                        {% if kpi.delta == "up" %}<span class="delta-up">▲</span>
                        {% elif kpi.delta == "down" %}<span class="delta-down">▼</span>
                        {% else %}<span class="delta-none"></span>
                        {% endif %}
                        {% endif %}
                    </div>
                    {% endif %}
                    {% endfor %}
                </div>

                {# Know More button #}
                <div class="company-card-footer">
                    <button class="btn-know-more"
                            onclick="toggleDetails('{{ company.id }}')">Know More →</button>
                </div>

                {# Slide-down details panel with KPI tab drill-down #}
                <div class="company-details" id="details-{{ company.id }}">
                    <div class="know-more-target-row">
                        Annual Target: {{ company.kpis[0].value }}
                    </div>
                    {{ kpi_tabs_panel(company.id, kpi_details[company.id], aging[company.id]) }}
                </div>

            </div>
            {% endfor %}
        </div>
    </section>

</main>
{% endblock %}

{% block extra_js %}
<script src="{{ url_for('static', path='script.js') }}"></script>
{% endblock %}
```

- [ ] **Step 2: Start the dev server and verify the page loads without 500 errors**

```bash
cd D:/Fidelitus/mddb && uvicorn app.main:app --reload --port 8000
```

Open `http://localhost:8000` — all 6 cards should render; Know More should show a tab strip with Revenue active.

- [ ] **Step 3: Commit**

```bash
git add app/templates/dashboard.html
git commit -m "[TASK-005] feat: replace aging_panel with kpi_tabs_panel in company Know More"
```

---

## Task 6: Add tab styles to `style.css`

**Files:**
- Modify: `app/static/style.css`

Append this block to the end of `style.css`:

- [ ] **Step 1: Append KPI tab CSS**

```css
/* ── KPI Tab Strip ── */
.kpi-tabs-container {
    padding: 0 0 0.5rem;
}

.kpi-tab-strip {
    display: flex;
    gap: 0.25rem;
    padding: 0.5rem 1rem 0;
    border-bottom: 1px solid var(--color-border);
    overflow-x: auto;
}

.kpi-tab {
    background: none;
    border: none;
    border-bottom: 2px solid transparent;
    padding: 0.4rem 0.75rem;
    font-family: var(--font-body);
    font-size: 0.72rem;
    font-weight: 500;
    color: var(--color-text-secondary);
    cursor: pointer;
    white-space: nowrap;
    margin-bottom: -1px;
    transition: color 0.15s, border-color 0.15s;
}

.kpi-tab:hover {
    color: var(--color-text-primary);
}

.kpi-tab.active {
    color: var(--color-accent);
    border-bottom-color: var(--color-accent);
}

/* ── KPI Tab Content Panels ── */
.kpi-tab-panel {
    display: none;
    padding: 0.75rem 1rem;
    overflow-x: auto;
}

.kpi-tab-panel.active {
    display: block;
}

/* ── KPI Detail Table (Revenue / Invoiced / Meetings / Proposals) ── */
.kpi-detail-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.75rem;
}

.kpi-detail-table th {
    text-align: left;
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--color-text-secondary);
    padding: 0.3rem 0.5rem;
    border-bottom: 1px solid var(--color-border);
    white-space: nowrap;
}

.kpi-detail-table td {
    padding: 0.35rem 0.5rem;
    color: var(--color-text-primary);
    border-bottom: 1px solid rgba(48, 54, 61, 0.4);
    vertical-align: top;
}

.kpi-detail-table tbody tr:last-child td {
    border-bottom: none;
}

.kpi-detail-value {
    font-family: var(--font-heading);
    font-weight: 700;
    color: var(--color-accent);
    white-space: nowrap;
}

.kpi-detail-ref {
    font-size: 0.68rem;
    color: var(--color-text-secondary);
    white-space: nowrap;
}

.kpi-detail-date {
    white-space: nowrap;
    color: var(--color-text-secondary);
}

.kpi-detail-nextstep {
    color: var(--color-text-secondary);
    font-style: italic;
    max-width: 14rem;
}

/* ── Status Badges ── */
.status-badge {
    display: inline-block;
    padding: 0.15rem 0.45rem;
    border-radius: 4px;
    font-size: 0.65rem;
    font-weight: 600;
    white-space: nowrap;
}

/* Green: closed / paid / accepted */
.status-closed,
.status-paid,
.status-accepted {
    background: rgba(34, 197, 94, 0.12);
    color: #22c55e;
}

/* Amber: committed / pending / shortlisted / under-review */
.status-committed,
.status-pending,
.status-shortlisted,
.status-under-review {
    background: rgba(232, 168, 56, 0.12);
    color: var(--color-accent);
}

/* Muted: submitted / sent / in-pipeline */
.status-submitted,
.status-sent,
.status-in-pipeline {
    background: rgba(255, 255, 255, 0.05);
    color: var(--color-text-secondary);
}

/* Red: overdue / declined */
.status-overdue,
.status-declined {
    background: rgba(239, 68, 68, 0.12);
    color: #ef4444;
}

/* Empty state */
.kpi-empty-state {
    font-size: 0.75rem;
    color: var(--color-text-secondary);
    font-style: italic;
    padding: 0.5rem 0;
}

/* Fix: company-details max-height must accommodate tab content */
.company-details.open {
    max-height: 1200px !important;
}
```

- [ ] **Step 2: Commit**

```bash
git add app/static/style.css
git commit -m "[TASK-005] feat: add KPI tab strip, detail table, and status badge CSS"
```

---

## Task 7: Update `script.js`

**Files:**
- Modify: `app/static/script.js`

Replace the full contents of `app/static/script.js`:

- [ ] **Step 1: Write the updated `script.js`**

```javascript
/* ── Company card Know More toggle ── */
function toggleDetails(id) {
    const panel = document.getElementById('details-' + id);
    panel.classList.toggle('open');

    if (panel.classList.contains('open')) {
        // Default to Revenue tab when opening
        switchKpiTab(id, 'revenue');
    } else {
        // Reset aging pills in Payments tab when closing
        resetAgingPills(id);
    }
}

/* ── KPI tab switching ── */
function switchKpiTab(companyId, tabKey) {
    const container = document.getElementById('kpi-tabs-' + companyId);
    if (!container) return;

    // Deactivate all tabs
    container.querySelectorAll('.kpi-tab').forEach(function(tab) {
        tab.classList.remove('active');
    });

    // Hide all panels
    container.querySelectorAll('.kpi-tab-panel').forEach(function(p) {
        p.classList.remove('active');
    });

    // Activate clicked tab button
    const activeTab = container.querySelector('[data-tab="' + tabKey + '"]');
    if (activeTab) activeTab.classList.add('active');

    // Show clicked panel
    const activePanel = document.getElementById('kpi-panel-' + companyId + '-' + tabKey);
    if (activePanel) activePanel.classList.add('active');
}

/* ── Corporate aging panel toggle (called by any KPI strip card click) ── */
function toggleCorporateAging() {
    const panel = document.getElementById('details-corporate');
    panel.classList.toggle('open');

    if (!panel.classList.contains('open')) {
        resetAgingPills('corporate');
    }
}

/* ── Aging bucket pill toggle (used inside Payments tab) ── */
function toggleAgingBucket(companyId, bucket) {
    const pillsContainer = document.getElementById('aging-pills-' + companyId);
    if (!pillsContainer) return;

    const clickedPill = pillsContainer.querySelector(
        '[data-company="' + companyId + '"][data-bucket="' + bucket + '"]'
    );
    const targetTable = document.getElementById(
        'aging-table-' + companyId + '-' + bucket
    );
    if (!clickedPill || !targetTable) return;

    const isAlreadyOpen = clickedPill.classList.contains('active');

    resetAgingPills(companyId);

    if (!isAlreadyOpen) {
        clickedPill.classList.add('active');
        targetTable.classList.add('open');
    }
}

/* ── Helper: close all aging pills + tables for a given company ── */
function resetAgingPills(companyId) {
    const pillsContainer = document.getElementById('aging-pills-' + companyId);
    if (!pillsContainer) return;

    pillsContainer.querySelectorAll('.aging-pill').forEach(function(pill) {
        pill.classList.remove('active');
    });

    document.querySelectorAll('[id^="aging-table-' + companyId + '-"]').forEach(function(table) {
        table.classList.remove('open');
    });
}
```

- [ ] **Step 2: Reload browser and run manual tests**

1. Open `http://localhost:8000`
2. Click **Know More →** on Fidelitus Transactions — panel opens, **Revenue** tab active, table shows 7 deals
3. Click **Invoiced** tab — Revenue panel hides, Invoiced table shows 5 rows
4. Click **Payments** tab — aging bucket pills appear
5. Click **7 Days** pill — 3-row table expands
6. Click **Meetings** tab — aging table collapses, Meetings table shows 5 rows
7. Click **Proposals** tab — Proposals table shows 5 rows with colored status badges
8. Click **Know More →** again to close — panel collapses, no JS errors in console
9. Repeat for Fidelitus GCC Nexus — Invoiced shows 1 row, Revenue shows 2 rows, Proposals shows 3 rows

- [ ] **Step 3: Commit**

```bash
git add app/static/script.js
git commit -m "[TASK-005] feat: add KPI tab switching JS, init Revenue tab on Know More open"
```

---

## Task 8: Finish the branch

- [ ] **Step 1: Run the server one final time and verify all 6 companies**

```bash
cd D:/Fidelitus/mddb && uvicorn app.main:app --reload --port 8000
```

For each company card:
- Know More opens with Revenue tab active
- All 5 tabs switch correctly
- Payments tab shows aging pills (existing behavior unchanged)
- Status badges show correct colors (green/amber/muted/red)
- GCC Nexus shows minimal data without errors (no empty-state crashes)

- [ ] **Step 2: Mark TASK-005 status as Done**

Edit `tasks/TASK-005-kpi-drill-panels.md` — change `Status: In Progress` → `Status: Done`

- [ ] **Step 3: Final commit**

```bash
git add tasks/TASK-005-kpi-drill-panels.md
git commit -m "[TASK-005] chore: mark task complete"
```

- [ ] **Step 4: Push and open PR**

```bash
git push origin feature/TASK-005-kpi-drill-panels
gh pr create --title "[TASK-005] feat: KPI drill-down tab panels in company Know More" \
  --body "$(cat <<'EOF'
## Summary
- Adds `KPI_DETAILS` dummy data for all 6 companies (Revenue, Invoiced, Meetings, Proposals)
- New Jinja2 macro `kpi_tabs_panel` renders a 5-tab panel inside each company Know More
- Revenue tab active by default on open; Payments tab reuses existing aging_panel macro
- Status badges color-coded: green=Closed/Paid, amber=Committed/Pending, red=Overdue/Declined
- `toggleDetails` initialises Revenue tab on open; `switchKpiTab` handles tab switching

## Test plan
- [ ] All 6 company Know More panels open with Revenue tab active
- [ ] All 5 tabs switch correctly without page reload
- [ ] Fidelitus Transactions Revenue: 7 items visible
- [ ] Payments tab: aging pills work as before (TASK-004 regression check)
- [ ] Status badges render correct colors for Closed, Pending, Submitted, Declined
- [ ] GCC Nexus (minimal data): no JS errors, no template crashes
- [ ] Corporate aging panel (KPI strip click) unaffected

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

---

## Self-Review

**Spec coverage check:**

| Requirement | Task |
|---|---|
| Revenue tab: Client / BD Person / Value / Type / Status | Task 3, 5 |
| Invoiced tab: Client / Invoice Ref / Amount / Date / Status | Task 3, 5 |
| Payments tab: existing aging pills (unchanged) | Task 3 |
| Meetings tab: Client / BD Person / Date / Type / Next Step | Task 3, 5 |
| Proposals tab: Client / BD Person / Value / Submitted / Status | Task 3, 5 |
| Status color badges (green/amber/muted/red) | Task 6 |
| Revenue tab default on open | Task 7 |
| Vanilla JS tab switching, no page reload | Task 7 |
| KPI_DETAILS dummy data for all 6 companies | Task 2 |
| Payments aging panel unaffected (regression) | Task 3, 7 |
| Corporate aging panel unaffected (regression) | Task 5 |

**Placeholder scan:** No TBD / TODO / "similar to" patterns. All table columns, all dummy data, all CSS classes, all JS function bodies fully written.

**Type consistency:**
- `kpi_tabs_panel(company_id, kpi_details, aging)` defined in Task 3 and called in Task 5 as `kpi_tabs_panel(company.id, kpi_details[company.id], aging[company.id])` ✓
- `switchKpiTab(companyId, tabKey)` defined in Task 7, called in Task 3 template as `switchKpiTab('{{ company_id }}', 'revenue')` etc. ✓
- DOM IDs `kpi-tabs-{id}`, `kpi-panel-{id}-{tab}` consistent across Task 3 and Task 7 ✓
- CSS classes `kpi-tab`, `kpi-tab.active`, `kpi-tab-panel`, `kpi-tab-panel.active` consistent across Task 6 and Task 3 ✓
- Status CSS classes follow pattern `status-{status|lower|replace(' ','-')}` — all values (closed, paid, committed, pending, shortlisted, under-review, submitted, sent, in-pipeline, overdue, declined) have matching CSS rules in Task 6 ✓
