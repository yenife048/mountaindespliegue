from django.shortcuts import render
from carro.carro import Carro

# Create your views here.

def car(request):
    return render(request, "core/ver_carrito.html")

def mostrar(request):
    carro = Carro(request)
    cantidad = carro.contar_productos()
    return render(request, 'core/base.html',{'cantidad': cantidad})