from django.db import models

from tabnanny import verbose

from django.contrib.auth import get_user_model

from productos.models import hamburguesas

from django.db.models import F, Sum, FloatField

# Create your models here.
User=get_user_model()

class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado') #añade la hora automatica
    
    
    @property
    def total(self):
        return self.lineapedido_set.aggregate(

            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())

        )["total"] or FloatField(0)

    def __str__(self):
        return self.id


    class Meta:
        db_table='pedidos'
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        ordering=['id']

class LineaPedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(hamburguesas, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado') #añade la hora automatica

    def __str__(self):
        return f'{self.cantidad} de {self.producto.title} total a pagar',Sum(F("precio")*F("cantidad"))

    class Meta:
        db_table='lineapedidos'
        verbose_name='Línea Pedido'
        verbose_name_plural='Líneas Pedidos'
        ordering=['id']