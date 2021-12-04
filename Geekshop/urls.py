from django.contrib import admin
from django.urls import path, include

from .views import home, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', include('mainapp.urls')),
]
