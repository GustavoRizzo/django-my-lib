
# django-my-lib 🚀

[![PyPI](https://img.shields.io/pypi/v/django-my-lib.svg)](https://pypi.org/project/django-my-lib/)


> This project is a test for creating a Django library. 🧩


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

## Rename the project and package
To rename the project and package, follow these steps:
1. On github click on the "Use this template" button to create a new repository based on this template. Give it a new name (e.g., `django-awesome-lib`).

2. Inside the project folder, rename the package folder from `django_my_lib` to your desired name (e.g., `django_awesome_lib`).
```bash
mv django_my_lib django_awesome_lib
```

3. Make CTRL+F and replace all occurrences of `django_my_lib` with `django_awesome_lib` in the codebase.

4. Rename template folder: On django_awesome_lib/templates, rename the folder from `demo_project` to your desired name (e.g., `demo_awesome_project`).
```bash
mv django_awesome_lib/templates/django_my_lib django_awesome_lib/templates/django_awesome_lib
```

5. Make CTRL+F and replace all occurrences of `django-my-lib` with `django-awesome-lib` in the codebase.

6. Ajdust the project name in the `pyproject.toml` file.
```toml
[tool.poetry]
name = "django-awesome-lib"
version = "0.1.0"
description = "This project is a test for creating a Django library."
authors = [
    "Your Name <your.email@example.com>"
]
```

7. Adjust README.md to reflect the new project name and package name.
```markdown
# django-awesome-lib 🚀
[![PyPI](https://img.shields.io/pypi/v/django-awesome-lib.svg)](https://pypi.org/project/django-awesome-lib/)
> This my brand new project is a test for creating a Django library. 🧩
```

8. Now you are free to start developing your new Django library! 🎉
