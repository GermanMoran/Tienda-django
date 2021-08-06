from django.shortcuts import render

from .carro import carro

from tienda.models import Producto

from django.shortcuts import redirect
# Create your views here.

def agregar_producto(request, producto_id):
    carro1 = carro(request)
    # obtenemos el producto
    producto = Producto.objects.get(id= producto_id)
    carro1.agregar(producto=producto)
    return redirect("tienda")

# Eliminar un producto

def eliminar_productos(request, producto_id):
    # Creamos el carro
    carro1 = carro(request)
    # obtenemos el producto
    producto = Producto.objects.get(id= producto_id)
    carro1.eliminar_producto(producto=producto)
    return redirect("tienda")


def restar_producto(request, producto_id):
    # Creamos el carro
    carro1 = carro(request)
    # obtenemos el producto
    producto = Producto.objects.get(id= producto_id)
    carro1.restar_productos(producto=producto)
    return redirect("tienda")


def limpiarcarro(request, producto_id):
    # Creamos el carro
    carro1 = carro(request)
    carro1.limpiar_carro()
    return redirect("tienda")