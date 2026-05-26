
# django-my-lib 🚀

[![PyPI](https://img.shields.io/pypi/v/django-my-lib.svg)](https://pypi.org/project/django-my-lib/)


> This project is a test for creating a Django library. 🧩

## Table of Contents

- [Installation](#installation-)
- [Configuration](#configuration-)
- [Migrations](#migrations-)
- [Running locally as a developer](#running-locally-as-a-developer-)
  - [Tests](#tests-)
  - [Linting](#linting-)
  - [If using pyenv](#if-using-pyenv)
- [Updating and publishing the library](#updating-and-publishing-the-library-)
- [Use this project as a template](#use-this-project-as-a-template-for-your-own-django-library-)

## Installation 📦

You can install the library using pip or poetry:

```bash
pip install django-my-lib
# or
poetry add django-my-lib
```


## Configuration ⚙️

Add `django_my_lib` to the `INSTALLED_APPS` list in your `settings.py`:

```python
INSTALLED_APPS = [
    # ... other apps ...
    'django_my_lib',
]
```


## Migrations 🗄️

After installing and configuring, run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```


🎉 Done! Your Django library is installed and ready to use.


## Running locally as a developer 🖥️

To run the Django project locally during development, follow the steps below:

```bash
git clone https://github.com/GustavoRizzo/django-my-lib.git
cd django-my-lib
poetry install
poetry run task run-demo
```

For a more complete setup, you can run the comands:
```bash
poetry run task migrate
poetry run task createsuperuser
# or
poetry run task setup  # that will do the same as above
```


### Tests 🧪
To run the tests, use the command below inside the `demo_project` directory:

```bash
poetry run task test
```


### Linting 🧹
To check for linting issues, use the command below:

```bash
poetry run task lint
poetry run task lint-fix  # to fix issues automatically
```

## If using pyenv
To manage Python versions, you can use `pyenv`. To install `pyenv`, follow the instructions in the [pyenv GitHub repository](https://github.com/pyenv/pyenv).
```bash
pyenv update
pyenv install 3.12.0
# Activete the virtual environment with the correct Python version
python -m venv venv
source venv/bin/activate
pip install pip --upgrade
pip install poetry
poetry install
poetry run task run-demo
```


## Updating and publishing the library 🚢

To update the version, build, and publish your library, use the commands below:

```bash
poetry version patch  # to bump the version (e.g.: 0.1.0 → 0.1.1)
poetry build
tar -tzf dist/*.tar.gz | head -20  # to see the files inside the package
poetry publish
```

# Use this project as a template for your own Django library! 🌟

## Creating a new library from this template

This template is designed to be adapted by an AI assistant in seconds. Follow the steps below.

### 1. Fork the repository

On GitHub, click **"Use this template"** → **"Create a new repository"** and give it a name (e.g., `django-awesome-lib`).

### 2. Clone your new repository

```bash
git clone https://github.com/YOUR_USER/django-awesome-lib.git
cd django-awesome-lib
```

### 3. Open it in your editor with an AI assistant

Open the project in VS Code, Cursor, or any editor with Claude Code (or a similar AI assistant) available.

### 4. Update template.config.json

Open `template.config.json` and fill in your new project's values:

```json
{
  "project_name": "django-awesome-lib",
  "package_name": "django_awesome_lib",
  "app_class_name": "DjangoAwesomeLib",
  "description": "A description of what your library does.",
  "author_name": "Your Name",
  "author_email": "your@email.com",
  "github_url": "https://github.com/YOUR_USER/django-awesome-lib",
  "pypi_url": "https://pypi.org/project/django-awesome-lib/",
  "version": "0.1.0"
}
```

### 5. Send this prompt to the AI

Copy and paste the prompt below into the AI assistant chat:

```
Read the template.config.json file and use it to adapt this project to the new library.
Propagate all changes across every file in the project: rename folders, update all references
to the old package name, description, URLs, and author info. After that, run the tests and
linter to confirm everything is working.
```

The AI will handle all renames and references automatically. Done! 🎉
