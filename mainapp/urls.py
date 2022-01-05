from django.urls import path

from .views import home, contacts, new

app_name = 'mainapp'

urlpatterns = [
    path('', home, name='home'),
    path('new/', new, name='new'),
    path('contacts/', contacts, name='contacts'),
]
