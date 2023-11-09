from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Cliente, Maquinaria, Trazabilidad
from .forms import LoginForm, ClienteForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
"""
VIEWS
- [X]  Home
- [X]  Iniciar Sesion
    - [X]  Recuperar clave
- [X]  Index
    - [X]  Cliente
        - [X]  Nuevo
    - [X]  Trazabilidad
    - [X]  Maquinaria
        - [X]  Nuevo
    - [X]  Configuración
        - [X]  Nuevo
    - [X]  Manuales
        - [X]  Nuevo
"""

# Create your views here.
# Index view
def index(request):

    return render(request ,"html/index.html")

# Home view
def home(request):
    return render(request ,"html/home.html")

# Login view
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Aquí asumimos que el campo de correo electrónico es único
            user = User.objects.get(email=email)
            print(check_password(password, user.password))
            # Verificar la contraseña; asumimos que está hashada
            print(user.password)
            print(password)
            print(password==user.password)
            if password== user.password:
                # La contraseña es correcta; ahora debes iniciar sesión al usuario manualmente
                # Necesitas manejar la sesión tú mismo si no estás usando `authenticate()`
                # Esto puede implicar establecer la ID del usuario en la sesión y manejar `logout` etc.
                # auth_login(request, user)
                return redirect('index')
            else:
                # Contraseña incorrecta
                messages.error(request, 'La contraseña es incorrecta.')
        except User.DoesNotExist:
            # No existe un usuario con ese correo electrónico
            messages.error(request, 'No existe un usuario con ese correo electrónico.')

    # Renderiza de nuevo la página de inicio de sesión con los mensajes de error si los hay
    return render(request, "html/login.html", {"form": LoginForm()})

# Reset_password view
def reset_password(request):
    return render(request ,"html/reset_password.html")

class Client_view:

    # Client view
    def client(request):
        clientes = Cliente.objects.all()
        return render(request ,"html/client.html", {'clientes': clientes})

    # New client view
    def new_client(request):
        if request.method == 'POST':
            form = ClienteForm(request.POST)
            if form.is_valid():
                # Aquí podrías hacer alguna lógica de negocio adicional si es necesario
                form.save()
                return redirect('cliente')  # Redirecciona a la URL de la página principal
        else:
            form = ClienteForm()

        # Si no es una petición POST, muestra la página con el formulario vacío
        return render(request, 'html/new_client.html', {'form': form})


# Trazability view
def trazability(request):
    return render(request ,"html/trazability.html")

class Machine_view:
    # Machine view
    def machine(request):
        return render(request ,"html/machine.html")
    # New machine view
    def new_machine(request):
        return render(request ,"html/new_machine.html")

class Manual_view:
    # Manual view
    def manual(request):
        return render(request ,"html/manual.html")
    def new_manual(request):
        return render(request ,"html/new_manual.html")



# Create an about view
def about(request):
    return render(request ,"html/about.html")

