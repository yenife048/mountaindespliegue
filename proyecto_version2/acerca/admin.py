from django.contrib import admin
from .models import ContenidoAcerca

# Register your models here.
class mision_visionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(ContenidoAcerca, mision_visionAdmin)