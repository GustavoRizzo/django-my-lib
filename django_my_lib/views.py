from importlib.metadata import version, PackageNotFoundError

from django.conf import settings
from django.shortcuts import render
from django.views import View


def _get_version():
    try:
        return version('django-my-lib')
    except PackageNotFoundError:
        return 'dev'


class Home(View):
    def get(self, request):
        context = {
            'url_pypi': settings.URL_PYPI,
            'url_github': settings.URL_GITHUB,
            'version': _get_version(),
        }
        return render(request, 'django_my_lib/home.html', context)
