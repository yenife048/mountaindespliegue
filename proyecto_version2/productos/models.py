from django.db import models

# Create your models here.
class categoriasprod(models.Model):
    title=models.CharField(max_length=50,verbose_name='Titulo')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado') #añade la hora automatica
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizado')
    
    class Meta:
        verbose_name="categoiriaProd"
        verbose_name_plural="categoriasProd"
        ordering = ["created"] 
        
    def __str__(self):
        return self.title

class hamburguesas(models.Model):
    title=models.CharField(max_length=50,verbose_name='Titulo')
    categorias=models.ForeignKey(categoriasprod, on_delete=models.CASCADE)
    image1=models.ImageField(verbose_name='Imagen1',upload_to="productos")#upload para que las imagenes guardadas se hagan en el directorio projects
    descrip=models.TextField(verbose_name="Descripcion")
    precio=models.FloatField(verbose_name='precio', null=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado') #añade la hora automatica
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizado')

    class Meta:
        verbose_name = "hamburguesa"
        verbose_name_plural = "hamburguesas"
        ordering = ["created"] 

    def __str__(self):
        return self.title  # <=====