from django.shortcuts import render

def home(request):
    """Renderiza la vista de Portada"""
    return render(request, 'core/home.html')

def about(request):
    """Renderiza la vista de Acerca de"""
    return render(request, 'core/about.html')

def contact(request):
    """Renderiza la vista de Contacto"""
    return render(request, 'core/contact.html')
