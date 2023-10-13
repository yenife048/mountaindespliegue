import random
import string
from django import forms


def generate_random_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=4))

class PedidosForm(forms.Form):
    OPCIONES_ENTREGAS = (
        ('domicilio', 'Domicilio'),
        ('ir al lugar', 'Ir al lugar'),
    )
    OPCIONES_PAGOS = (
        ('nequi', 'Nequi'),
        ('efectivo', 'Efectivo'),
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obtén el usuario de los argumentos
        super(PedidosForm, self).__init__(*args, **kwargs)

        # Establece el correo electrónico del usuario como valor predeterminado si está autenticado
        if user and user.is_authenticated:
            self.fields['email'].initial = user.email

    name = forms.CharField(label="Nombre", min_length=3, max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Escribe tu nombre'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'placeholder':'Escriba su email'}),min_length=3, max_length=100)
    telefono = forms.CharField(label='Teléfono', required=True , widget=forms.TextInput(attrs={'placeholder': 'Escribe tu telefono'}))
    entregas = forms.ChoiceField(label="Forma de entrega", choices=OPCIONES_ENTREGAS, required=True)
    direccion = forms.CharField(label="Direccion", required=False, widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: Mz a casa 10 barrio/montecarlo'}))
    indicaciones = forms.CharField(label="Indicaciones", required=False, widget=forms.TextInput(attrs={'placeholder': 'Torre 4, Apartamento 604'}))
    pagos = forms.ChoiceField(label="Forma de pago", choices=OPCIONES_PAGOS, required=True)
    codigo = forms.CharField(label="Código de compra", required=True, initial=generate_random_code, widget=forms.TextInput(attrs={'readonly': 'readonly'}))