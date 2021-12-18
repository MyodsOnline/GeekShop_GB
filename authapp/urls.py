from django.urls import path

from .views import test

app_name = 'auth'

urlpatterns = [
    path('', test, name='test'),
]
