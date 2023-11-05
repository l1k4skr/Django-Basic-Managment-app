from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request ,"html/login.html")

# Reset_password view
def reset_password(request):
    return render(request ,"html/reset_password.html")

class Client_view:

    # Client view
    def client(self, request):
        return render(request ,"html/client.html")

    # New client view
    def new_client(self, request):
        return render(request ,"html/new_client.html")

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

