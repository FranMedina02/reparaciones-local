from django.shortcuts import render
from reparacionesApp.models import Reparaciones
# Create your views here.

def fichas(request):
    info = Reparaciones.objects.all()
    return render(request, 'oficinaApp/fichas.html', {'fichas':info})

def ficha(request, ficha):
    print(ficha)
    info = Reparaciones.objects.get(pk=ficha)
    return render(request, 'oficinaApp/ficha.html', {'ficha':info})
