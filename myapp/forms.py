from django import forms
from .models import Cliente, Maquinaria, User, Manual

class LoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Contraseña', max_length=100, widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'siglas', 'rut', 'direccion', 'email', 'telefono', 'cargo', 'password']
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'razon_social', "rut", 'direccion', 'email', 'telefono']
        # Puedes añadir widgets personalizados si es necesario

class MaquinariaForm(forms.ModelForm):
    class Meta:
        model = Maquinaria
        fields = ['orden', 'numero_serie', 'cliente', 'maquinaria', 'marca', 'año', 'fecha', 'problema']
        # Puedes añadir widgets personalizados si es necesario

class ManualesForm(forms.ModelForm):
    class Meta:
        model = Manual
        fields = ["nombre_manual", "tipo_manual", "año_manual", "pdf_manual"]
