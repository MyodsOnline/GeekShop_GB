from django.urls import path

from .views import home, contacts

app_name = 'mainapp'

urlpatterns = [
    path('', home, name='home'),
    path('page/<int:page>/', home, name='page'),
    path('new/', home, name='new'),
    path('contacts/', contacts, name='contacts'),
]
