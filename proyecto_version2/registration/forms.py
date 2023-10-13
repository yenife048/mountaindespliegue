from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationEmail(UserCreationForm):
    email=forms.EmailField(required=True,help_text="es un campo requerido con formato valido para correo")

    class Meta:
        model=User
        fields=("username","email","password1","password2")
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'El email ya esta registrado, prueba otro.')
        return email