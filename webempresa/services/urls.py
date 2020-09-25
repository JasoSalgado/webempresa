"""Services urls."""

# Django modules
from django.urls import path

# Services modules
from . import views

urlpatterns = [
    path('', views.services, name='services'),
]
