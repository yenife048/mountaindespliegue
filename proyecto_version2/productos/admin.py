from django.contrib import admin
from .models import hamburguesas,categoriasprod

#Register your models here.

class categoriasprodAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class hamburguesasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    



#admin.site.register(producto, ProductosAdmin)
admin.site.register(categoriasprod, categoriasprodAdmin)
admin.site.register(hamburguesas, hamburguesasAdmin)
