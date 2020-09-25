from django.urls import path
from . import views

urlpatterns = [
    # Path from contact
    path('', views.contact, name='contact'),
]