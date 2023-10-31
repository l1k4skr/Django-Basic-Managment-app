from django.http import HttpResponse

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
# Home view
def home(request):
    return HttpResponse("<h1>This is the home view.</h1>")

# Login view
def login(request):
    return HttpResponse("<h1>This is the login view.</h1>")

# Reset_password view
def reset_password(request):
    return HttpResponse("<h1>This is the reset_password view.</h1>")

class Client_view:

    # Client view
    def client(request):
        return HttpResponse("<h1>This is the client view.</h1>")

    # New client view
    def new_client(request):
        return HttpResponse("<h1>This is the new_client view.</h1>")

# Trazability view
def trazability(request):
    return HttpResponse("<h1>This is the trazability view.</h1>")

class Machine_view:
    # Machine view
    def machine(request):
        return HttpResponse("<h1>This is the machine view.</h1>")
    def new_machine(request):
        return HttpResponse("<h1>This is the new_machine view.</h1>")

class Manual_view:
    # Manual view
    def manual(request):
        return HttpResponse("<h1>This is the manual view.</h1>")
    def new_manual(request):
        return HttpResponse("<h1>This is the new_manual view.</h1>")


# index view
def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

# Create an about view
def about(request):
    return HttpResponse("<h1>This is the about view.</h1>")

