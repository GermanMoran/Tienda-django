from django.shortcuts import render
from .models import Producto
# Create your views here.
def tienda(request):

    # Debemos crar una variable donde almacenar esa lista de productos
    productos = Producto.objects.all()
    return render(request,'tienda/tienda.html',{'productos':productos})