from django.urls import path

from .views import home, contacts

app_name = 'mainapp'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
