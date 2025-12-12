<!-- Auto-generated guidance for AI coding agents working on this repo -->
# Copilot instructions for the `ex5` Django project

This repository is a small Django project named `dk` with a single app `mathapp` (located at `dk/mathapp`). The goal of these notes is to give an AI agent the concrete, discoverable knowledge needed to be productive here.

- Project entrypoint: `dk/manage.py` (run commands from repo root or `cd dk`).
- Django version declared in `dk/dk/settings.py` header: 5.2.8 — use this when installing dependencies.
- Database: SQLite at `BASE_DIR / 'db.sqlite3'` (no external DB configuration).

Key locations and patterns
- App code: `dk/mathapp/` — views live in `dk/mathapp/views.py`, models in `dk/mathapp/models.py`, tests in `dk/mathapp/tests.py`.
- Templates: `dk/mathapp/templates/mathapp/math.html` — template expects context variables `l`, `b`, and `area` (see form inputs `name="length"`, `name="breadth"` and template usage `{{l}}`, `{{b}}`, `{{area}}`).
- Settings: `dk/dk/settings.py` — note `INSTALLED_APPS` includes `'mathapp'`, `DEBUG = True`, `ALLOWED_HOSTS = ["*"]`, and `STATICFILES_DIRS` references `myapp/static` (this does not match `mathapp` and is a likely inconsistency to watch for).
- URLs: `dk/dk/urls.py` currently only exposes the admin route. `mathapp` is not included in project `urlpatterns` — add routes here or create `dk/mathapp/urls.py` and `include()` it.

Developer workflows (commands & examples)
- Create and activate a virtual environment (PowerShell):
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  pip install Django==5.2.8
  ```
- Run the dev server (from repo root):
  ```powershell
  python dk/manage.py migrate
  python dk/manage.py runserver
  # or: cd dk; python manage.py runserver
  ```
- Run tests:
  ```powershell
  python dk/manage.py test
  ```

Project-specific gotchas and actionable checks
- `dk/mathapp/views.py` contains syntax errors and inconsistent variable names (example: it sets keys like `context['1']` and uses `'myapp/math.html'`). Before editing views, ensure template names and context keys match — the template uses `{{l}}`, `{{b}}`, `{{area}}` and is located at `mathapp/math.html`.
- `STATICFILES_DIRS` points to `myapp/static` while the app is `mathapp`. If adding static assets, either change settings or place files under `myapp/static` per current config. Confirm intended layout with the maintainer.
- Routes: to expose the math form add either a URL pattern in `dk/dk/urls.py` or create `dk/mathapp/urls.py`. Example minimal addition to `dk/dk/urls.py`:
  ```python
  from django.urls import include, path
  urlpatterns += [ path('', include('mathapp.urls')) ]
  ```

What to edit and tests an AI agent can run quickly
- Fix or implement `rectarea` in `dk/mathapp/views.py` to read `request.POST['length']` and `request.POST['breadth']`, compute area, and render `mathapp/math.html` with keys `l`, `b`, `area`.
- Add a `mathapp/urls.py` with a path for the form and ensure `dk/dk/urls.py` includes it.
- After changes, run `python dk/manage.py runserver` and exercise the form in the browser, or run `python dk/manage.py test` if adding unit tests.

Integration and external dependencies
- No external services are configured. All data is stored in the local SQLite file at `db.sqlite3`.
- If you add packages, update a `requirements.txt` and include pinned versions (pin Django to 5.2.8 to match generated settings comment).

When editing: be conservative and explicit
- Prefer small, testable edits (fix a view, run migrations, run server) rather than sweeping refactors.
- Document any deviation from the current layout (for example changing `STATICFILES_DIRS`) in `README.md`.

If something is unclear, ask the maintainer about intended app name and static layout before renaming paths.

---
If you want, I can now:
- open a PR-style patch to create a working `rectarea` view and a `mathapp/urls.py`, or
- only add this instruction file and wait for feedback.

Please tell me which follow-up you prefer.
