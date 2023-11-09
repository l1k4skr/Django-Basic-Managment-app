from django import forms
from .models import Cliente

class LoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'razon_social', 'direccion', 'email', 'telefono']
        # Puedes añadir widgets personalizados si es necesario