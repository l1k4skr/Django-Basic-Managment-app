from django import forms
from .models import Cliente, Maquinaria

class LoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'razon_social', "rut", 'direccion', 'email', 'telefono']
        # Puedes añadir widgets personalizados si es necesario

class MaquinariaForm(forms.ModelForm):
    class Meta:
        model = Maquinaria
        fields = ['ORDEN', 'CLIENTE', 'MAQUINARIA', 'MARCA', 'AÑO', 'FECHA', 'PROBLEMA']
        # Puedes añadir widgets personalizados si es necesario