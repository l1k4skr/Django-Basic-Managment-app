from django import forms
from .models import Cliente, Maquinaria, User

class LoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

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
        fields = ['orden', 'cliente', 'maquinaria', 'marca', 'año', 'fecha', 'problema']
        # Puedes añadir widgets personalizados si es necesario