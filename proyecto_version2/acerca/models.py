from django.db import models

# Create your models here.

class ContenidoAcerca(models.Model):
    title=models.CharField(max_length=50,verbose_name='Titulo')
    contenido = models.TextField(verbose_name="Contenidos")
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado') #añade la hora automatica
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizado')

    class Meta:
        verbose_name = "Contenido"
        verbose_name_plural = "Contenidos"
        
    def __str__(self): #cambiar el nombre del proyecto
        return self.title #<=====