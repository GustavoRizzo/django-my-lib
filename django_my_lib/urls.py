from django.urls import path

from .views import Home

app_name = 'django_my_lib'

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
