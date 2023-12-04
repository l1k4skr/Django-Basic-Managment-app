from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Cliente, Maquinaria, Trazabilidad, Manual
from .forms import LoginForm, ClienteForm, MaquinariaForm, UserForm, ManualesForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from django.http import FileResponse
import os
from django.conf import settings
from django.http import HttpResponseNotFound
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
    - []  Manuales
        - []  Nuevo
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
            # print(check_password(password, user.password))
            # # Verificar la contraseña; asumimos que está hashada
            # print(user.password)
            # print(password)
            # print(password==user.password)
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
    print(request.method)
    if request.method == 'POST':
        
        email = request.POST.get('email')
        actual_password = request.POST.get('password')
        new_password = request.POST.get('new-password')
        re_new_password = request.POST.get('re-new-password')

        # print(f"request: {request.POST}")
        # print(f"email: {email}")
        # print(f"actual_password: {actual_password}")
        # print(f"new_password: {new_password}")
        # print(f"re_new_password: {re_new_password}")

        # print(email)
        try:
            user = User.objects.get(email=email)
            # print(f"user: {user}")
            # print(f"user password: {user.password}")
            # print(f"user actual: {actual_password}")
            # print(check_password(actual_password, user.password))
            if actual_password ==  user.password:
                if new_password == re_new_password:
                    user.password = new_password
                    user.save()
                    messages.success(request, 'Se ha cambiado la contraseña correctamente.')
                else:
                    messages.error(request, 'Las contraseñas no coinciden.')
            else:
                messages.error(request, 'La contraseña actual es incorrecta.')
            # Enviar correo electrónico al usuario con la contraseña
            # Aquí debes implementar tu propia lógica para enviar el correo electrónico
        except User.DoesNotExist:
            # No existe un usuario con ese correo electrónico
            messages.error(request, 'No existe un usuario con ese correo electrónico.')
        except Exception as e:
            # Algo salió mal
            messages.error(request, 'Algo salió mal.')
            print(e)
    return render(request ,"html/reset_password.html")

class Client_view:

    # Client view
    def client(request):
        clientes = Cliente.objects.all()
        print(clientes)
        return render(request ,"html/client.html", {'clientes': clientes})

    # New client view
    def new_client(request):
        if request.method == 'POST':

            # Crea un formulario de cliente y rellénalo con los datos de la petición
            form = ClienteForm(request.POST)
        
            # Verifica si el formulario es válido
            print(f"Formulario: {(form.is_valid())}")

            if form.is_valid():
                # Aquí podrías hacer alguna lógica de negocio adicional si es necesario
                form.save()
                messages.success(request, '¡Cliente creado correctamente!')
                return redirect('cliente')  # Redirecciona a la URL de la página principal
            
            else:
                # print(f"Errores: {form.errors}")
                # errores_formato = list(form.errors.as_data()[list(form.errors.as_data().keys())[0]][0])[0]
                # print(f"Errores: {errores_formato}")

                for error in form.errors.as_data():
                    print(error)
                    print(list(form.errors.as_data()[error][0])[0])
                    messages.error(request, list(form.errors.as_data()[error][0])[0])

                # return render(request, 'html/new_client.html', {'form': form, 'error_message': errores_formato})

        else:
            form = ClienteForm()

        # Si no es una petición POST, muestra la página con el formulario vacío
        return render(request, 'html/new_client.html', {'form': form})
    
    # Edit client view
    def edit_cliente(request, id):
        cliente = get_object_or_404(Cliente, pk=id)
        if request.method == "POST":
            form = ClienteForm(request.POST, instance=cliente)
            if form.is_valid():
                form.save()
                return redirect('cliente')  # Redirigir a la lista de clientes después de guardar
            
        else:
            form = ClienteForm(instance=cliente)
        return render(request, 'html/edit_cliente.html', {'form': form, 'cliente': cliente})
    
    # Delete client view
    def delete_cliente(request, id):
        cliente = get_object_or_404(Cliente, id=id)
        if request.method == 'POST':
            cliente.delete()
            messages.success(request, 'Cliente eliminado con éxito.')
            return redirect('cliente')
        return render(request, 'html/confirm_cliente_delete.html', {'cliente': cliente})
    


# Trazability view
def trazability(request):
    trazability = Trazabilidad.objects.all()
    return render(request ,"html/trazability.html", {'trazabilities': trazability})

# NECESITO CONECTAR MAQUINARIA CON CLIENTE CADA VEZ QUE SE AGREGE UNA MAQUINA NUEVA
""" 
def edit_trazability(request, id):
    trazability = get_object_or_404(Trazabilidad, pk=id)
    if request.method == "POST":
        form = TrazabilityForm(request.POST, instance=trazability)
        if form.is_valid():
            form.save()
            return redirect('trazability')  # Redirigir a la lista de clientes después de guardar
        
    else:
        form = TrazabilityForm(instance=trazability)
    return render(request, 'html/edit_trazability.html', {'form': form, 'trazability': trazability})
"""

class Machine_view:
    # Machine view
    def machine(request):
        maquinas = Maquinaria.objects.all()
        return render(request ,"html/machine.html", {'maquinas': maquinas})
    # New machine view
    def new_machine(request):
        if request.method == 'POST':
            maquinariaform = MaquinariaForm(request.POST)
            print(f"Formulario: {request.POST}")
            print(f"Formulario: {(maquinariaform.errors)}")
            print(f"Formulario valido: {(maquinariaform.is_valid())}")
            if maquinariaform.is_valid():
                maquinariaform.save()
                messages.success(request, '¡Maquinaria creada correctamente!')
                return redirect('maquinaria')
        return render(request ,"html/new_machine.html")
    
    # Edit machine view
    def edit_maquinaria(request, id):
        maquinaria = get_object_or_404(Maquinaria, pk=id)
        if request.method == "POST":
            form = MaquinariaForm(request.POST, instance=maquinaria)
            if form.is_valid():
                form.save()
                messages.success(request, '¡Maquinaria editada correctamente!')
                return redirect('maquinaria')
        else:
            form = MaquinariaForm(instance=maquinaria)
        return render(request, 'html/edit_maquinaria.html', {'form': form, 'maquinaria': maquinaria})
    
    # Delete machine view
    def delete_maquinaria(request, id):
        maquinaria = get_object_or_404(Maquinaria, id=id)
        if request.method == 'POST':
            maquinaria.delete()
            messages.success(request, 'Maquinaria eliminada con éxito.')
            return redirect('maquinaria')
        return render(request, 'html/confirm_maquinaria_delete.html', {'maquinaria': maquinaria})
    

class Config_view:
    # Config view
    def config(request):
        users = User.objects.all()
        print
        return render(request ,"html/config.html", {'usuarios': users})
    
    # New config view
    def new_user(request):
        if request.method == 'POST':
            # Crea un formulario de cliente y rellénalo con los datos de la petición
            form = UserForm(request.POST)
            # print(f"Formulario: {request.POST}")
            # Verifica si el formulario es válido
            # print(f"Formulario: {(form.is_valid())}")
            re_password = dict(request.POST)['confirm_password'][0]
            # print(f"re_password: {re_password}")
            clean_data = form.cleaned_data
            # print(f"cleandata:{clean_data}")
            if form.is_valid() and clean_data['password'] == re_password:
                # Aquí podrías hacer alguna lógica de negocio adicional si es necesario
                form.save()
                messages.success(request, '¡Usuario creado correctamente!')
                return redirect('configuracion')
            elif clean_data['password'] != re_password:
                messages.error(request, 'Las contraseñas no coinciden.')
            else:
                # print(f"Errores: {form.errors}")
                # errores_formato = list(form.errors.as_data()[list(form.errors.as_data().keys())[0]][0])[0]
                # print(f"Errores: {errores_formato}")

                for error in form.errors.as_data():
                    # print(error)
                    # print(list(form.errors.as_data()[error][0])[0])
                    messages.error(request, list(form.errors.as_data()[error][0])[0])

                # return render(request, 'html/new_client.html', {'form': form, 'error_message': errores_formato})
        return render(request ,"html/new_user.html")
    
    # Edit config view
    def edit_user(request, id):
        user = get_object_or_404(User, pk=id)
        if request.method == "POST":
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('configuracion')
        else:
            form = UserForm(instance=user)
        return render(request, 'html/edit_user.html', {'form': form, 'user': user})
    
    # Delete config view
    def delete_user(request, id):
        user = get_object_or_404(User, id=id)
        if request.method == 'POST':
            user.delete()
            messages.success(request, 'Usuario eliminado con éxito.')
            return redirect('configuracion')
        return render(request, 'html/confirm_user_delete.html', {'user': user})
    
class Manual_view:

    # Manual view
    def manual(request):
        manuales = Manual.objects.all()
        return render(request ,"html/manual.html", {'manuales': manuales})
    
    def new_manual(request):
        if request.method == 'POST':
            # Crea un formulario de cliente y rellénalo con los datos de la petición
            print(f"Formulario: {request.POST}")
            form = ManualesForm(request.POST, request.FILES)
            print(f"Formulario: {(request.FILES)}")
            # Verifica si el formulario es válido
            print(f"Formulario: {(form.is_valid())}")
            clean_data = form.cleaned_data
            print(f"cleandata:{clean_data}")

            if form.is_valid():
                # Aquí podrías hacer alguna lógica de negocio adicional si es necesario
                form.save()
                messages.success(request, '¡Manual creado correctamente!')
                return redirect('manuales')

            else:
                print(f"Errores: {form.errors}")
                for error in form.errors.as_data():
                    print(error)
                    messages.error(request, list(form.errors.as_data()[error][0])[0])

        return render(request ,"html/new_manual.html", {'form': ManualesForm()})
    
    def download_manual(request, id):
        manual = get_object_or_404(Manual, id=id)
        pdf_file = manual.pdf_manual.path  # Asegúrate de que 'pdf_manual' es el nombre de tu campo FileField

        if os.path.exists(pdf_file):
            # No uses 'with' aquí para evitar cerrar el archivo
            try:
                fh = open(pdf_file, 'rb')
                response = FileResponse(fh, content_type='application/pdf')
                response['Content-Disposition'] = f'inline; filename="{os.path.basename(pdf_file)}"'
                return response
            except IOError:
                # Manejar el error si el archivo no puede ser abierto
                return HttpResponseNotFound('<h1>Error al abrir el archivo</h1>')
        else:
            # Manejar el caso donde el archivo no existe
            return HttpResponseNotFound('<h1>Archivo no encontrado</h1>')
    
    def edit_manual(request, id):
        manual = get_object_or_404(Manual, pk=id)
        if request.method == "POST":
            form = ManualesForm(request.POST, request.FILES, instance=manual)
            if form.is_valid():
                form.save()
                return redirect('manuales')  # Redirigir a la lista de manuales después de guardar
        else:
            form = ManualesForm(instance=manual)
        return render(request, 'html/edit_manual.html', {'form': form, 'manual': manual})
    
    def delete_manual(request, id):
        manual = get_object_or_404(Manual, id=id)
        if request.method == 'POST':  # Asegúrate de que la solicitud sea POST para evitar la eliminación accidental
            manual.delete()
            messages.success(request, 'Manual eliminado con éxito.')
            return redirect('manuales')  # Redirigir a la lista de manuales después de eliminar
        return render(request, 'html/confirm_manual_delete.html', {'manual': manual})