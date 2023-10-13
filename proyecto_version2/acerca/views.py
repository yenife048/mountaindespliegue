from django.shortcuts import render
from .models import ContenidoAcerca


# Create your views here.

def acerca(request):
    contenidos1=ContenidoAcerca.objects.get(id=1)
    contenidos2=ContenidoAcerca.objects.get(id=2)
    contenidos3=ContenidoAcerca.objects.get(id=3)

    return render(request, "acerca/acerca.html",{'contenidos1':contenidos1,
                                                'contenidos2':contenidos2, 'contenidos3':contenidos3,})