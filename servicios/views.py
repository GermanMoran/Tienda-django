from django.shortcuts import render
from servicios.models import servicios
# Create your views here.

def Servicios(request):

    ser = servicios.objects.all()
    return render(request,'servicios/servicios.html', {'servicios':ser})