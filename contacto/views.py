from django.shortcuts import render

from .form import FormularioContacto

# Create your views here.
def contacto(request):
    #Creamos una instancia de la clase formulario contacto
    formulario_contacto = FormularioContacto()
    return render(request,'contacto/contacto.html',{'miFormulario':formulario_contacto})