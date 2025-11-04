from django.urls import path

from .views import Home

app_name = 'django_sample_components'

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
