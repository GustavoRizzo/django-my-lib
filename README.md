
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

## Updating and publishing the library 🚢

To update the version, build, and publish your library, use the commands below:

```bash
poetry version patch  # to bump the version (e.g.: 0.1.0 → 0.1.1)
poetry build
tar -tzf dist/*.tar.gz | head -20  # to see the files inside the package
poetry publish
```
