from django import forms

class SugerenciaForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True,widget=forms.TextInput(attrs={'placeholder':'Escriba su nombre','class':'form-control'}),
                           min_length=3, max_length=100)
    email = forms.EmailField(label='Email',required=True,widget=forms.EmailInput(attrs={
        'placeholder':'Escriba su email','class':'form-control'}),min_length=3, max_length=100)
    content = forms.CharField(label="Contenido", required=True,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Escribe tu sugerencia','rows':3}))