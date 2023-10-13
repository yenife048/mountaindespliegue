from django.shortcuts import render,redirect
from.forms import PedidosForm
from django.core.mail import EmailMessage
from django.urls import reverse
from carro.carro import Carro
from carro.context_processor import importe_total_carro
from django.core.mail import send_mail
  
def enviar_confirmacion_remitente(email_remitente, contenido):
    # Ingresa aquí la dirección de correo electrónico desde la que deseas enviar el correo de confirmación
    email_administrador = "yenyadrada@misena.edu.co"

    asunto = "CONFIRMACIÓN DE TU PEDIDO"
    send_mail(asunto, contenido, email_administrador, [email_remitente], fail_silently=True)


  
def pedidos(request):
        
    pedido_form = PedidosForm()
    carro = Carro(request)
    total = importe_total_carro(request)


     # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Obtén el correo electrónico y el nombre del usuario autenticado
        email_usuario = request.user.email
        nombre_usuario = request.user.username  # Suponiendo que el nombre de usuario se almacena en el campo 'username'
        # Crea una instancia del formulario y establece el correo electrónico y el nombre del usuario como valores predeterminados
        pedido_form = PedidosForm(initial={'email': email_usuario, 'name': nombre_usuario})
    else:
        # Si el usuario no está autenticado, crea una instancia del formulario vacío
        pedido_form = PedidosForm()

    if request.method == "POST":
        pedido_form =PedidosForm(data=request.POST)
        if pedido_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')    
            telefono = request.POST.get('telefono','')    
            entregas = pedido_form.cleaned_data['entregas']
            direccion = request.POST.get('direccion','')    
            indicaciones = request.POST.get('indicaciones','')    
            pagos = pedido_form.cleaned_data['pagos']
            codigo = request.POST.get('codigo','')
             
            cart_items = carro.carro.values()
            
                
            message = f"""Email: {email}\n\nEscribió:\n\n codigo:{codigo}\n\n telefono:{telefono}\n\n tipo de entrega:{entregas}\n\n direccion:{direccion}\n\n indicaciones adiccionales:{indicaciones}\n\n tipo de pago: {pagos}"""  
            
            message += "\n\nProductos en el carrito:\n"
            
            total_pagar= f"Debe pagar: {total['importe_total_carro']:.3f} $"

            for item in cart_items:
                message += f"- {item['nombre']}: Cantidad: {item['cantidad']}, Precio: {float(item['precio']):.3f} $ \n"
            
            email_destinatario = "yenyadrada@misena.edu.co"   
            email_enviado=EmailMessage("PEDIDOS: Nuevo Mensaje","De {} <{}>\n\n TOTAL DE TODO:\n\n{}".format(name,message,total_pagar),
            "",[email_destinatario],reply_to=[email])
            
            #email=EmailMessage("PEDIDOS: Nuevo Mensaje","De {} <{}>\n\n TOTAL DE TODO:\n\n{}".format(name,message,total_pagar),"",["yenniferadrada@gmail.com"],reply_to=[email])  
            
            try:#excepcion
                email_enviado.send()
                #mensaje de envio en el caso que todo este bien
                # Enviar correo de confirmación al remitente
                contenido_confirmacion = f"Gracias por tu compra, la hemos recibido correctamente. recuerda que si tu opción fue nequi debes pagar a este numero:314 412 66 68, En mensaje ingresa el código: {codigo} y tu total es: {total_pagar}."
                enviar_confirmacion_remitente(email, contenido_confirmacion)
                carro.limpiar_carro()

                return redirect(reverse('inicio')+"?okpedido")
            
            except:
                #error que direcciona a fail
                return redirect(reverse('pedido')+"?fail")
    #return redirect(reverse('pedido')+"?Enviado Correctamente")
    return render(request, "pedido/finalizar_compra.html",{'form':pedido_form})