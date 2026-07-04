# AGENTS.md

## Project scope
**Page Turner** — a Django book review app.
Planned apps (not yet scaffolded):

| App | Purpose |
|-----|---------|
| `apps/books` | Book catalog, reviews, ratings |
| `apps/accounts` | Users, roles, reading lists |
| `apps/api` | DRF endpoints |
| `apps/web` | Server-rendered UI (reader- and staff-facing) |

The project is in its **initial state** — only the virtual environment exists. No Django project, apps, or code have been created yet.

## Important project conventions
- Put business workflow logic in `services.py`, not in views or serializers.
- Put reusable read/query logic in `selectors.py`.
- Keep Celery tasks thin; they should call service functions.

## Current state
- **Python 3.10**, Django 5.2, ruff, coverage, pytest, pytest-django, pytest-cov installed
- Django project scaffolded at `config/`, `manage.py` exists
- `books` app created with `Book` and `Review` models
- Migrations for `books` created and applied
- Database schema documented in `openspec/database_design.md`
- The AGENTS.md is the **authoritative config** — update it as the project evolves

## Commands
Run server: `python manage.py runserver`
Run tests: `pytest`
Create migrations: `python manage.py makemigrations`
Apply migrations: `python manage.py migrate`
Lint: `ruff check .`
Format: `ruff format .`

## Things that are easy to break (once built)
API response shapes in `apps/api`
role/permission checks in `apps/accounts`
review/rating status transitions in `apps/books/services.py`

## Change coupling (once built)
If you change:
a model also check serializers, factories, and admin
review workflow also check tasks and notifications
permissions also check both web views and API endpoints

## Constraints
Do not edit old migrations; create a new one instead.
Do not rename API fields or URL names unless explicitly asked.
Prefer small, targeted changes over broad refactors.

## Testing expectations (once built)
Add or update tests for:
review/rating status changes
permission changes
API response changes
