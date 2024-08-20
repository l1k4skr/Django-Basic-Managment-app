from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from django.http import FileResponse, HttpResponseNotFound
from django.db import transaction
from .models import User, Cliente, Maquinaria, Trazabilidad, Manual
from .forms import LoginForm, ClienteForm, MaquinariaForm, UserForm, ManualesForm
import os
import time

# VIEWS
# Home view
def home(request):
    return render(request, "html/home.html")

# Index view
def index(request):
    return render(request, "html/index.html")


# Login view
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if password == user.password:
                auth_login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'La contraseña es incorrecta.')
        except User.DoesNotExist:
            messages.error(request, 'No existe un usuario con ese correo electrónico.')

    return render(request, "html/login.html", {"form": LoginForm()})

# Reset_password view
def reset_password(request):
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
            messages.error(request, 'No existe un usuario con ese correo electrónico.')
        except Exception as e:
            messages.error(request, 'Algo salió mal.')
            print(e)
    return render(request, "html/reset_password.html")

# Client views
def client(request):
    clientes = Cliente.objects.all()
    return render(request, "html/client.html", {'clientes': clientes})

def new_client(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cliente creado correctamente!')
            return redirect('cliente')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')
    else:
        form = ClienteForm()

    return render(request, 'html/new_client.html', {'form': form})

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

def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado con éxito.')
        return redirect('cliente')
    return render(request, 'html/confirm_cliente_delete.html', {'cliente': cliente})

# Trazability view
def trazability(request):
    trazabilities = Trazabilidad.objects.all()
    return render(request, "html/trazability.html", {'trazabilities': trazabilities})

def boleta(request, id):
    trazability = get_object_or_404(Trazabilidad, pk=id)
    maquinaria = Maquinaria.objects.get(orden=trazability.n_orden_trazabilidad, fecha_creacion_m=trazability.fecha_creacion_t)
    usuario = User.objects.get(orden=trazability.n_orden_trazabilidad)
    return render(request, "html/boleta.html", {'trazabilidad': trazability, 'maquinaria': maquinaria, 'usuario': usuario})

# Machine views
def machine(request):
    maquinas = Maquinaria.objects.all()
    return render(request, "html/machine.html", {'maquinas': maquinas})

def new_machine(request):
    if request.method == 'POST':
        maquinariaform = MaquinariaForm(request.POST)
        if maquinariaform.is_valid():
            clean_data = maquinariaform.cleaned_data
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

            orden = user.orden
            time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            trazabilidad = Trazabilidad(
                n_orden_trazabilidad=orden,
                cliente_trazabilidad=clean_data['cliente'],
                maquinaria_trazabilidad=clean_data['maquinaria'],
                marca_trazabilidad=clean_data['marca'],
                año_trazabilidad=clean_data['año'],
                fecha_trazabilidad=clean_data['fecha'],
                descripcion_problema_trazabilidad=clean_data['problema'],
                fecha_creacion_t=time_now
            )
            trazabilidad.save()

            maquinaria = Maquinaria(
                orden=orden,
                numero_serie=clean_data['numero_serie'],
                cliente=clean_data['cliente'],
                maquinaria=clean_data['maquinaria'],
                marca=clean_data['marca'],
                año=clean_data['año'],
                fecha=clean_data['fecha'],
                problema=clean_data['problema'],
                fecha_creacion_m=time_now
            )
            maquinaria.save()

            messages.success(request, '¡Maquinaria creada correctamente!')
            return redirect('maquinaria')
        else:
            for field, errors in maquinariaform.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')
    return render(request, "html/new_machine.html", {'form': MaquinariaForm()})

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

def delete_maquinaria(request, id):
    maquinaria = get_object_or_404(Maquinaria, id=id)
    if request.method == 'POST':
        with transaction.atomic():
            Trazabilidad.objects.filter(n_orden_trazabilidad=maquinaria.orden, fecha_creacion_t=maquinaria.fecha_creacion_m).delete()
            maquinaria.delete()
            messages.success(request, 'Maquinaria eliminada con éxito.')
            return redirect('maquinaria')
    return render(request, 'html/confirm_maquinaria_delete.html', {'maquinaria': maquinaria})

# Config views
def config(request):
    users = User.objects.all()
    return render(request, "html/config.html", {'usuarios': users})

def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        re_password = request.POST.get('confirm_password')
        password = request.POST.get('password')
        if form.is_valid() and password == re_password:
            form.save()
            user = User.objects.get(username=request.POST.get('username'))
            user.orden = user.get_orden()
            user.save()
            messages.success(request, '¡Usuario creado correctamente!')
            return redirect('configuracion')
        elif password != re_password:
            messages.error(request, 'Las contraseñas no coinciden.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')
    return render(request, "html/new_user.html")

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

def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Usuario eliminado con éxito.')
        return redirect('configuracion')
    return render(request, 'html/confirm_user_delete.html', {'user': user})

# Manual views
def manual(request):
    manuales = Manual.objects.all()
    return render(request, "html/manual.html", {'manuales': manuales})

def new_manual(request):
    if request.method == 'POST':
        form = ManualesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Manual creado correctamente!')
            return redirect('manuales')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')
    return render(request, "html/new_manual.html", {'form': ManualesForm()})

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
        return redirect('manuales')
    return render(request, 'html/confirm_manual_delete.html', {'manual': manual})
