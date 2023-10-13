from django.shortcuts import render,redirect
from .models import categoriasprod
#from carro.carro import Carro
from productos.models import hamburguesas
from carro.carro import Carro


# Create your views here.

def home(request, categoriasprod_id): #esperar una respuesta (request)
    categorias = categoriasprod.objects.all()
    cate1 = categoriasprod.objects.get(id=1)
    cate2 = categoriasprod.objects.get(id=2)
    cate3 = categoriasprod.objects.get(id=3)
    cate5 = categoriasprod.objects.get(id=5)
    cate4 = categoriasprod.objects.get(id=4)
    cate6 = categoriasprod.objects.get(id=6)
    carro = Carro(request)
    cantidad = carro.contar_productos()
    return render(request,'productos/home.html',{'categorias':categorias,'cate1':cate1,
                'cate2':cate2,'cate3':cate3,'cate5':cate5,'cate4':cate4,'cate6':cate6,'cantidad': cantidad})
