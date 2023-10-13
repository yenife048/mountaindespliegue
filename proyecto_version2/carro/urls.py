from django.urls import path

from .import views

app_name="carro"#evitar la colicion 

urlpatterns = [
    
    path('agregar/<int:hamburguesas_id>/', views.agregar_producto, name="agregar"),
    path('agregar_p/<int:hamburguesas_id>/', views.aumentar_producto, name="agregar_p"),
    path('eliminar/<int:hamburguesas_id>/', views.eliminar_productos, name="eliminar"),
    path('restar/<int:hamburguesas_id>/', views.restar_productos, name="restar"),
    path('limpiar/', views.limpiar_carro, name="limpiar"),

]
