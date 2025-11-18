# Ao criar uma páginas precisamos configurar  a URL, o VIEW e o TEMPLATE.

from django.urls import path, include
from .views import homepage

urlpatterns = [
    path('', homepage),
]