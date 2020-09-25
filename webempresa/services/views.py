"""Services views."""

from django.shortcuts import render
from .models import Service


def services(request):
    """
    To show the data we created from admin services
    """
    services = Service.objects.all()    
    return render(request, 'services/services.html', {'services': services})
