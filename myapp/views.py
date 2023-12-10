from django.shortcuts import render, redirect, get_object_or_404
import time
from .models import User, Cliente, Maquinaria, Trazabilidad, Manual
from .forms import LoginForm, ClienteForm, MaquinariaForm, UserForm, ManualesForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from django.http import FileResponse
import os
from django.conf import settings
from django.http import HttpResponseNotFound
from django.db import transaction


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
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:    
            # Aquí que el campo de correo electrónico es único
            user = User.objects.get(email=email)
            if password== user.password:
                auth_login(request, user)
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
        new_password = request.POST.get('new-password')
        re_new_password = request.POST.get('re-new-password')

        try:
            user = User.objects.get(email=email)
            if new_password == re_new_password:
                user.password = new_password
                user.save()
                messages.success(request, 'Se ha cambiado la contraseña correctamente.')
            else:
                messages.error(request, 'Las contraseñas no coinciden.')
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

            # Crea un formulario de cliente y rellena con los datos de la petición
            form = ClienteForm(request.POST)
        
            # Verifica si el formulario es válido
            print(f"Formulario: {(form.is_valid())}")

            if form.is_valid():
                form.save()
                messages.success(request, '¡Cliente creado correctamente!')
                return redirect('cliente')  
            
            else:
                for error in form.errors.as_data():
                    print(error)
                    print(list(form.errors.as_data()[error][0])[0])
                    messages.error(request, list(form.errors.as_data()[error][0])[0])
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
                return redirect('cliente')
            
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
def boleta(request, id):
    trazability = get_object_or_404(Trazabilidad, pk=id)
    maquinaria = Maquinaria.objects.get(orden=trazability.n_orden_trazabilidad, fecha_creacion_m=trazability.fecha_creacion_t)
    usuario = User.objects.get(orden=trazability.n_orden_trazabilidad)
    return render(request ,"html/boleta.html", {'trazabilidad': trazability, 'maquinaria': maquinaria, 'usuario': usuario})


# Machine view
class Machine_view:
    def machine(request):
        print(request.user)
        maquinas = Maquinaria.objects.all()
        return render(request ,"html/machine.html", {'maquinas': maquinas})
    
    # New machine view
    def new_machine(request):
        print(request.user)
        if request.method == 'POST':
            maquinariaform = MaquinariaForm(request.POST)
            if maquinariaform.is_valid():
                # Extrayendo el valor de 'orden' del formulario
                clean_data = maquinariaform.cleaned_data
                print(f"cleandata:{clean_data}")

                email = request.POST.get('email')
                password = request.POST.get('password1')

                try:
                    user = User.objects.get(email=email)
                    if password == user.password:
                        pass
                    else:
                        messages.error(request, 'La contraseña es incorrecta.')
                        return redirect('nueva_maquinaria')
                except User.DoesNotExist:
                    messages.error(request, 'No existe un usuario con ese correo electrónico.')
                    return redirect('nueva_maquinaria')
                except Exception as e:
                    messages.error(request, 'Algo salió mal.')
                    print(e)
                    return redirect('nueva_maquinaria')
                
                orden= user.get_orden()
                time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                # Creando la trazabilidad
                trazabilidad = Trazabilidad(
                    n_orden_trazabilidad = orden,
                    cliente_trazabilidad = clean_data['cliente'],
                    maquinaria_trazabilidad = clean_data['maquinaria'],
                    marca_trazabilidad = clean_data['marca'],
                    año_trazabilidad = clean_data['año'],
                    fecha_trazabilidad = clean_data['fecha'],
                    descripcion_problema_trazabilidad = clean_data['problema'],
                    fecha_creacion_t = time_now
                )
                trazabilidad.save()

                # Creando la maquinaria
                maquinaria = Maquinaria(
                    orden = orden,
                    numero_serie = clean_data['numero_serie'],
                    cliente = clean_data['cliente'],
                    maquinaria = clean_data['maquinaria'],
                    marca = clean_data['marca'],
                    año = clean_data['año'],
                    fecha = clean_data['fecha'],
                    problema = clean_data['problema'],
                    fecha_creacion_m = time_now
                )
                maquinaria.save()
                # Verificar si existe la trazabilidad, si no, crearla
                messages.success(request, '¡Maquinaria creada correctamente!')
                return redirect('maquinaria')

            else:
                print(f"Errores: {maquinariaform.errors}")
                for error in maquinariaform.errors.as_data():
                    print(error)
                    print(list(maquinariaform.errors.as_data()[error][0])[0])
                    messages.error(request, list(maquinariaform.errors.as_data()[error][0])[0])
                    messages.error(request, "Error al crear maquinaria.")

        return render(request ,"html/new_machine.html", {'form': MaquinariaForm()})
    
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
            with transaction.atomic():  
                Trazabilidad.objects.filter(n_orden_trazabilidad=maquinaria.orden,fecha_creacion_t = maquinaria.fecha_creacion_m).delete()
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
            form = UserForm(request.POST)
            re_password = dict(request.POST)['confirm_password'][0]
            password = dict(request.POST)['password'][0]
            if form.is_valid() and password == re_password:
                form.save()
                user = User.objects.get(username=dict(request.POST)['username'][0])
                user.orden = user.get_orden()
                user.save()
                messages.success(request, '¡Usuario creado correctamente!')
                return redirect('configuracion')
            elif password != re_password:
                messages.error(request, 'Las contraseñas no coinciden.')
            else:
                for error in form.errors.as_data():
                    messages.error(request, list(form.errors.as_data()[error][0])[0])
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
            form = ManualesForm(request.POST, request.FILES)
            if form.is_valid():
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
        pdf_file = manual.pdf_manual.path 

        if os.path.exists(pdf_file):
            try:
                fh = open(pdf_file, 'rb')
                response = FileResponse(fh, content_type='application/pdf')
                response['Content-Disposition'] = f'inline; filename="{os.path.basename(pdf_file)}"'
                return response
            except IOError:
                return HttpResponseNotFound('<h1>Error al abrir el archivo</h1>')
        else:
            return HttpResponseNotFound('<h1>Archivo no encontrado</h1>')
    
    def edit_manual(request, id):
        manual = get_object_or_404(Manual, pk=id)
        if request.method == "POST":
            form = ManualesForm(request.POST, request.FILES, instance=manual)
            if form.is_valid():
                form.save()
                return redirect('manuales') 
        else:
            form = ManualesForm(instance=manual)
        return render(request, 'html/edit_manual.html', {'form': form, 'manual': manual})
    
    def delete_manual(request, id):
        manual = get_object_or_404(Manual, id=id)
        if request.method == 'POST': 
            manual.delete()
            messages.success(request, 'Manual eliminado con éxito.')
            return redirect('manuales')  # Redirigir a la lista de manuales después de eliminar
        return render(request, 'html/confirm_manual_delete.html', {'manual': manual})
    
