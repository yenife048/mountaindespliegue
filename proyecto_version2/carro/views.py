from django.shortcuts import render
from .carro import Carro
from productos.models import hamburguesas
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, hamburguesas_id):

    carro=Carro(request)
        
    hamburguesa=hamburguesas.objects.get(id=hamburguesas_id)
    
        
    carro.agregar(hamburguesas=hamburguesa)
    
    return redirect("inicio")

def aumentar_producto(request, hamburguesas_id):

    carro=Carro(request)
        
    hamburguesa=hamburguesas.objects.get(id=hamburguesas_id)
    
        
    carro.agregar(hamburguesas=hamburguesa)
    
    return redirect("car")

def eliminar_productos(request, hamburguesas_id):
    carro = Carro(request)
    
    hamburguesa=hamburguesas.objects.get(id=hamburguesas_id)
    
    carro.eliminar(hamburguesas=hamburguesa)
    
    return redirect("car")

def restar_productos(request, hamburguesas_id):
    carro = Carro(request)

    hamburguesa=hamburguesas.objects.get(id=hamburguesas_id)
    
    carro.restar_producto(hamburguesas=hamburguesa)
    
    return redirect("car")

def limpiar_carro(request):
    
    carro = Carro(request)
    
    carro.limpiar_carro()
    
    return redirect("car")

