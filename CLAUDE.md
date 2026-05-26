# CLAUDE.md — django-my-lib

## Project Overview

**django-my-lib** is a reusable Django library template designed to be used as a base for creating and publishing Django packages to PyPI. It includes a `demo_project` for local development and testing.

- **Package:** `django_my_lib`
- **Current version:** 0.1.7
- **Python:** >=3.14
- **Django:** >=5.2
- **License:** MIT
- **PyPI:** https://pypi.org/project/django-my-lib/
- **GitHub:** https://github.com/GustavoRizzo/django-my-lib

## Project Structure

```
django-my-lib/
├── django_my_lib/          # The library package (published to PyPI)
│   ├── templates/          # HTML templates
│   ├── templatetags/       # Custom template tags
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── apps.py
├── demo_project/           # Local Django project for development/testing
│   ├── kernel/             # Django settings, urls, wsgi/asgi
│   └── manage.py
├── .github/workflows/      # CI pipelines
│   └── ci.yml              # Runs lint + test on push/PR to main
├── template.config.json    # All project-specific values (for fork adaptation)
├── pyproject.toml          # Project config (Poetry + Ruff + Taskipy)
└── poetry.lock
```

## Development Commands (via taskipy)

All commands are run with `poetry run task <name>`:

| Command | Description |
|---|---|
| `task run-demo` | Run the demo project server |
| `task migrate` | Apply database migrations |
| `task setup` | Migrate + create superuser |
| `task test` | Run the test suite |
| `task lint` | Run ruff linter |
| `task lint-fix` | Run ruff linter and auto-fix |

## Toolchain

- **Dependency manager:** Poetry
- **Linter/Formatter:** Ruff (`line-length = 120`, rules: F, E, W, I, N, UP, B)
- **Type checker:** mypy
- **Task runner:** taskipy

## Publishing Workflow

**Manual:**
```bash
poetry version patch   # bump version (e.g. 0.1.7 → 0.1.8)
poetry build
poetry publish
```

## Forking This Template

All project-specific values are centralized in [template.config.json](template.config.json). When forking to create a new library, update that file first, then ask the AI:

> "Adapte este template para um novo app chamado `django-cache-tools`. Leia o `template.config.json`, atualize os valores para o novo projeto e propague as mudanças em todos os arquivos."

Files that reference template values and will need updating:
- `template.config.json`
- `pyproject.toml` (name, description, version, author)
- `django_my_lib/` → rename folder to new package name
- `django_my_lib/apps.py` (class name, app name)
- `demo_project/kernel/settings.py` (INSTALLED_APPS, URL_PYPI, URL_GITHUB)
- `demo_project/kernel/tests/` (app_name references)
- `django_my_lib/templates/django_my_lib/` → rename folder
- `django_my_lib/urls.py` (app_name)
- `README.md`
- `.github/workflows/` (se quiser CI no novo repositório)

## Language Convention

- **Communication & internal Claude files:** Portuguese is allowed
- **Code, variable names, comments:** English only
