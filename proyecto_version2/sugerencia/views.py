from django.shortcuts import render, redirect
from .forms import SugerenciaForm
from django.core.mail import EmailMessage
from django.urls import reverse
from django.core.mail import send_mail


# Definir la función para enviar el correo de confirmación al remitente
def enviar_confirmacion_remitente(email_remitente, contenido):
    # Ingresa aquí la dirección de correo electrónico desde la que deseas enviar el correo de confirmación
    email_administrador = "yenyadrada@misena.edu.co"

    asunto = "Confirmación de sugerencia MOUNTAIN BURGER"
    send_mail(asunto, contenido, email_administrador, [email_remitente], fail_silently=True)

# Resto de tu código
def sugerencia(request):
    sugerencia_form = SugerenciaForm()

    # Verifica si el usuario está autenticado y tiene un correo electrónico registrado
    if request.user.is_authenticated and request.user.email:
        # Obtén el correo electrónico del usuario autenticado
        email_usuario = request.user.email
        nombre_usuario = request.user.username 
        # Crea una instancia del formulario y establece el correo electrónico del usuario como valor predeterminado
        sugerencia_form = SugerenciaForm(initial={'email': email_usuario,'name': nombre_usuario})
    else:
        # Si el usuario no está autenticado o no tiene un correo electrónico registrado, crea una instancia del formulario vacío
        sugerencia_form = SugerenciaForm()
    
    if request.method == 'POST':
        sugerencia_form = SugerenciaForm(data=request.POST)
        if sugerencia_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            
            # Enviar el correo a la dirección de destino
            email_destinatario = "yenyadrada@misena.edu.co"
            email_enviado = EmailMessage(
                "SUGERENCIAS: Nuevo Mensaje",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "",
                [email_destinatario],
                reply_to=[email]
            )
            
            try:
                email_enviado.send()
                
                # Enviar correo de confirmación al remitente
                contenido_confirmacion = "Gracias por tu sugerencia. Hemos recibido tu mensaje correctamente y te responderemos lo antes posible."
                enviar_confirmacion_remitente(email, contenido_confirmacion)
                
                # Redireccionar a una página de éxito
                return redirect(reverse('sugerencia') + "?ok")
            except:
                # Redireccionar a una página de fallo
                return redirect(reverse('sugerencia') + "?error")
    
    return render(request, "sugerencia/sugerencias.html",{'form': sugerencia_form})
