from django.contrib import admin

from .models import Pedido, LineaPedido,Venta
# Register your models here.


class fechapedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)  # Asegúrate de incluir la coma al final si solo hay un campo


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'producto', 'cantidad_vendida', 'fecha_venta')

    def usuario(self, obj):
        return obj.usuario.username

    usuario.short_description = 'Usuario'  # Reemplaza 'usuario' con el nombre de tu campo de usuario

    def producto(self, obj):
        return obj.producto.title

    producto.short_description = 'Producto'  # Reemplaza 'producto' con el nombre de tu campo de producto

# Registra el modelo Pedido con la clase de administración
admin.site.register(Pedido, fechapedidoAdmin)
