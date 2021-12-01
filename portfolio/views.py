from django.shortcuts import render

from .models import Project

def portfolio(request):
    """Renderiza la vista de Portafolio"""
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})
