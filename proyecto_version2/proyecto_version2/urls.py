"""proyecto_version2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from core import views as core_views
from productos import views as productos_views
from acerca import views as acerca_views
from django.conf import settings 
from registration import views as registration_views
from registration import views as registration_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #-------------------------urls de cambio de contraseña----------------------------
    path('cambiar-contrasena/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('cambiar-contrasena/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('restablecer-contrasena/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('restablecer-contrasena/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('restablecer-contrasena/confirmar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('restablecer-contrasena/completar/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
    path ('check_email/', registration_views.check_email, name='check_email'),
    
    
     #---------------------url de sugerencias---------------------------
    
    path('sugerencia/', include('sugerencia.urls')),
    
     #-------------------urls de productos y carrito de compras----------------------------------------------------
    path('',productos_views.home,{'categoriasprod_id': 1}, name='inicio'),
    
    path('car/',core_views.car, name='car'),
    
    path('carro/', include('carro.urls')),
    
    
     #--------------------------urls de registro e inicio----------------------
    path('accounts/', include('django.contrib.auth.urls')),#IMPORTAR LA LIBRERIA PARA PODER UTILIZARLA EN EL LOGIN
    path('accounts/', include('registration.urls')),
    #-----------------------url de acerca de nosotros-----------------------
    path('acerca/',acerca_views.acerca, name='acerca'),
    
    
    #--------------------------url pedidos------------------------------
    path('pedido/', include('pedido.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)
