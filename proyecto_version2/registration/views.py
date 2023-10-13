from .forms import UserCreationEmail
#from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms


from django.http import JsonResponse
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationEmail
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Te has registrado correctamente!')
        return response

def get_form(self, form_class=None) :
        form=super(SignUpView,self).get_form()
        form.fields['username'].widget=forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget=forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Correo@valido.com'})
        form.fields['password1'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Confirmar Contraseña'})
        
        form.fields['username'].label='' # ocultar los label
        form.fields['password1'].label=''
        form.fields['password2'].label=''
        return form

def check_email(request):
    email = request.GET.get('email')
    user_exists = User.objects.filter(email=email).exists()
    return JsonResponse({'exists': user_exists})

@login_required  # Asegura que el usuario esté autenticado para acceder a esta vista
def reset_password_confirm(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Actualiza la sesión del usuario para mantenerlo autenticado
            messages.success(request, 'Contraseña actualizada exitosamente.')
            return redirect('inicio')  # Cambia 'inicio' por la URL a la que deseas redirigir después del proceso
        else:
            messages.error(request, 'Hubo un error al actualizar la contraseña. Por favor, corrige los errores a continuación.')

    else:
        form = SetPasswordForm(request.user)
    
    return render(request, 'ruta_a_tu_template.html', {'form': form})