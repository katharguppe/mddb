# MD Dashboard Scaffold Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a working FastAPI + Jinja2 scaffold that serves a mockup dashboard with dark theme, ready for Phase 1 integration.

**Architecture:** Configuration-driven FastAPI app that reads PRODUCTION flag from .env. Phase 0 (PRODUCTION=1) serves mockup routes from app/mockup/; Phase 1 (PRODUCTION=0) will serve live data from app/api/. All templates inherit from a base Jinja2 template with DM Sans + Syne fonts and a consistent dark theme.

**Tech Stack:** Python 3.13, FastAPI, Uvicorn, Jinja2, Motor (async MongoDB driver, installed but unused in Phase 0).

---

### Task 1: Create Task Tracking Document

**Files:**
- Create: `tasks/TASK-001-scaffold.md`

- [ ] **Step 1: Write task file**

Create `tasks/TASK-001-scaffold.md`:

```markdown
# TASK-001: MD Dashboard Scaffold

**Status:** In Progress
**Assigned:** Phase 0 (Srinivas)
**Scope:** app/ root + app/mockup/ + app/static/ + app/templates/

## Deliverables

- [x] tasks/TASK-001-scaffold.md (this file)
- [ ] .env (PRODUCTION=1)
- [ ] .gitignore (Python + .env)
- [ ] requirements.txt (fastapi, uvicorn, motor, python-dotenv, jinja2)
- [ ] app/config.py (settings loader)
- [ ] app/main.py (FastAPI app factory)
- [ ] app/mockup/routes.py (GET "/" route)
- [ ] app/templates/base.html (Jinja2 base, dark theme)
- [ ] app/templates/dashboard.html (dashboard page)
- [ ] app/static/style.css (CSS variables from md_dashboard_v2.html)

## Design Constraints

- No heavy JS frameworks — vanilla JS only
- Graphics: light, clear, distinct
- Dark bg #0d1117, surface #161b22, accent amber #e8a838
- Font: DM Sans (body) + Syne (headings) from Google Fonts
- Reuse CSS variables from md_dashboard_v2.html

## Git Branches

- base: main
- feature: dev (PR optional for Phase 0)
- commits: [TASK-001] verb: what changed
```

- [ ] **Step 2: Commit**

```bash
git add tasks/TASK-001-scaffold.md
git commit -m "[TASK-001] docs: create scaffold task tracking"
```

---

### Task 2: Create .env File

**Files:**
- Create: `.env`

- [ ] **Step 1: Write .env**

Create `.env`:

```
PRODUCTION=1
```

- [ ] **Step 2: Verify .gitignore will exclude it**

(Confirmed in Task 3 below)

---

### Task 3: Create .gitignore

**Files:**
- Create: `.gitignore`

- [ ] **Step 1: Write .gitignore**

Create `.gitignore`:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.pytest_cache/
.coverage
htmlcov/
.venv/
venv/
ENV/
env/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Environment
.env
.env.local

# OS
.DS_Store
Thumbs.db
```

- [ ] **Step 2: Commit**

```bash
git add .gitignore
git commit -m "[TASK-001] build: add Python and environment gitignore"
```

---

### Task 4: Create requirements.txt

**Files:**
- Create: `requirements.txt`

- [ ] **Step 1: Write requirements.txt**

Create `requirements.txt`:

```
fastapi==0.104.1
uvicorn[standard]==0.24.0
motor==3.3.2
python-dotenv==1.0.0
jinja2==3.1.2
pydantic-settings==2.1.0
```

- [ ] **Step 2: Commit**

```bash
git add requirements.txt
git commit -m "[TASK-001] build: add Python dependencies"
```

---

### Task 5: Create app/config.py

**Files:**
- Create: `app/config.py`
- Test: `tests/test_config.py`

- [ ] **Step 1: Write failing test**

Create `tests/test_config.py`:

```python
import os
import tempfile
from pathlib import Path

def test_load_production_flag_from_env():
    """Test that PRODUCTION flag is loaded correctly."""
    # Create a temp .env file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.env', delete=False) as f:
        f.write("PRODUCTION=1\n")
        temp_env_file = f.name

    try:
        # Test loading with custom .env path
        from app.config import Settings
        settings = Settings(_env_file=temp_env_file)
        assert settings.PRODUCTION == "1"
    finally:
        os.unlink(temp_env_file)

def test_load_production_zero_from_env():
    """Test PRODUCTION=0 for Phase 1."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.env', delete=False) as f:
        f.write("PRODUCTION=0\n")
        temp_env_file = f.name

    try:
        from app.config import Settings
        settings = Settings(_env_file=temp_env_file)
        assert settings.PRODUCTION == "0"
    finally:
        os.unlink(temp_env_file)
```

- [ ] **Step 2: Run test to verify it fails**

```bash
pytest tests/test_config.py -v
```

Expected: FAIL — `ModuleNotFoundError: No module named 'app'` or `ImportError: cannot import name 'Settings'`

- [ ] **Step 3: Write app/config.py**

Create `app/config.py`:

```python
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    """Application configuration loaded from .env file."""

    PRODUCTION: str = "1"  # "1" for mockup (Phase 0), "0" for live (Phase 1)

    class Config:
        env_file = str(Path(__file__).parent.parent / ".env")
        case_sensitive = True
```

- [ ] **Step 4: Run test to verify it passes**

```bash
pytest tests/test_config.py -v
```

Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add app/config.py tests/test_config.py
git commit -m "[TASK-001] feat: add configuration loader with PRODUCTION flag"
```

---

### Task 6: Create app/mockup/routes.py

**Files:**
- Create: `app/mockup/__init__.py`
- Create: `app/mockup/routes.py`

- [ ] **Step 1: Create app/mockup/__init__.py**

Create empty `app/mockup/__init__.py`:

```python
# Mockup package
```

- [ ] **Step 2: Write app/mockup/routes.py**

Create `app/mockup/routes.py`:

```python
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pathlib import Path

# Point to templates directory
templates_path = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_path))

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Render the MD Dashboard mockup."""
    return templates.TemplateResponse("dashboard.html", {"request": request})
```

- [ ] **Step 3: Commit**

```bash
git add app/mockup/__init__.py app/mockup/routes.py
git commit -m "[TASK-001] feat: add mockup routes with dashboard endpoint"
```

---

### Task 7: Create app/main.py

**Files:**
- Create: `app/__init__.py`
- Create: `app/main.py`

- [ ] **Step 1: Create app/__init__.py**

Create empty `app/__init__.py`:

```python
# MD Dashboard application
```

- [ ] **Step 2: Write app/main.py**

Create `app/main.py`:

```python
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
```

- [ ] **Step 3: Commit**

```bash
git add app/__init__.py app/main.py
git commit -m "[TASK-001] feat: add FastAPI app factory with conditional routing"
```

---

### Task 8: Create app/templates/base.html

**Files:**
- Create: `app/templates/base.html`

- [ ] **Step 1: Write base.html**

Create `app/templates/base.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}MD Dashboard{% endblock %}</title>

    <!-- Google Fonts: DM Sans + Syne -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Syne:wght@400;500;700&display=swap" rel="stylesheet">

    <!-- Custom Stylesheet -->
    <link rel="stylesheet" href="{{ url_for('static', path='style.css') }}">

    {% block extra_css %}{% endblock %}
</head>
<body>
    <div class="container">
        {% block content %}{% endblock %}
    </div>

    {% block extra_js %}{% endblock %}
</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add app/templates/base.html
git commit -m "[TASK-001] feat: add Jinja2 base template with fonts and structure"
```

---

### Task 9: Create app/templates/dashboard.html

**Files:**
- Create: `app/templates/dashboard.html`

- [ ] **Step 1: Write dashboard.html**

Create `app/templates/dashboard.html`:

```html
{% extends "base.html" %}

{% block title %}MD Dashboard . Fidelitus Corp{% endblock %}

{% block content %}
<header class="dashboard-header">
    <h1 class="dashboard-title">MD Dashboard . Fidelitus Corp</h1>
    <p class="dashboard-subtitle">Phase 0 Mockup</p>
</header>

<main class="dashboard-main">
    <!-- Placeholder for dashboard content -->
    <section class="section">
        <p class="placeholder-text">Dashboard content coming soon...</p>
    </section>
</main>
{% endblock %}
```

- [ ] **Step 2: Commit**

```bash
git add app/templates/dashboard.html
git commit -m "[TASK-001] feat: add dashboard template extending base"
```

---

### Task 10: Create app/static/style.css

**Files:**
- Create: `app/static/style.css`

**Prerequisites:** Extract CSS variables from `md_dashboard_v2.html` in project root to find exact color palette.

- [ ] **Step 1: Read md_dashboard_v2.html to extract CSS variables**

From project root, examine `md_dashboard_v2.html` to find:
- Exact color values for dark bg, surface, accent
- Font settings
- Base CSS variable definitions

Expected findings:
- Dark background: `#0d1117`
- Surface/card background: `#161b22`
- Accent amber: `#e8a838`
- Border/subtle: `#30363d`
- Text primary: `#c9d1d9`

- [ ] **Step 2: Write style.css with CSS variables**

Create `app/static/style.css`:

```css
/* CSS Variables - Dark Theme */
:root {
    --color-bg-primary: #0d1117;
    --color-bg-surface: #161b22;
    --color-accent: #e8a838;
    --color-border: #30363d;
    --color-text-primary: #c9d1d9;
    --color-text-secondary: #8b949e;
    --color-red: #ef4444;
    --color-red-orange: #f97316;
    --color-amber: #f59e0b;
    --color-green: #22c55e;

    --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --font-heading: 'Syne', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;
    --spacing-2xl: 3rem;
}

/* Reset & Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html, body {
    height: 100%;
    width: 100%;
}

body {
    background-color: var(--color-bg-primary);
    color: var(--color-text-primary);
    font-family: var(--font-body);
    font-size: 1rem;
    line-height: 1.5;
}

/* Container */
.container {
    width: 100%;
    max-width: 1400px;
    margin: 0 auto;
    padding: var(--spacing-xl);
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading);
    font-weight: 700;
    line-height: 1.2;
    color: var(--color-text-primary);
}

h1 {
    font-size: 2.5rem;
    margin-bottom: var(--spacing-lg);
}

h2 {
    font-size: 2rem;
    margin-bottom: var(--spacing-md);
}

h3 {
    font-size: 1.5rem;
    margin-bottom: var(--spacing-md);
}

p {
    margin-bottom: var(--spacing-md);
    color: var(--color-text-secondary);
}

/* Dashboard Header */
.dashboard-header {
    border-bottom: 1px solid var(--color-border);
    padding-bottom: var(--spacing-xl);
    margin-bottom: var(--spacing-2xl);
}

.dashboard-title {
    color: var(--color-accent);
    font-size: 2.5rem;
    font-family: var(--font-heading);
    margin-bottom: var(--spacing-sm);
}

.dashboard-subtitle {
    color: var(--color-text-secondary);
    font-size: 1rem;
    font-weight: 400;
}

/* Dashboard Main */
.dashboard-main {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-2xl);
}

/* Sections */
.section {
    background-color: var(--color-bg-surface);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    padding: var(--spacing-xl);
}

.section h2 {
    margin-top: 0;
}

.placeholder-text {
    text-align: center;
    color: var(--color-text-secondary);
    padding: var(--spacing-2xl) var(--spacing-xl);
    font-style: italic;
}

/* KPI Color Coding */
.kpi-status-red {
    color: var(--color-red);
}

.kpi-status-red-orange {
    color: var(--color-red-orange);
}

.kpi-status-amber {
    color: var(--color-amber);
}

.kpi-status-green {
    color: var(--color-green);
}

/* Responsive */
@media (max-width: 768px) {
    .container {
        padding: var(--spacing-lg);
    }

    .dashboard-title {
        font-size: 2rem;
    }

    h1 {
        font-size: 2rem;
    }

    h2 {
        font-size: 1.5rem;
    }
}
```

- [ ] **Step 3: Commit**

```bash
git add app/static/style.css
git commit -m "[TASK-001] style: add CSS variables and base styles with dark theme"
```

---
