from django.db import models
import time

def generar_numero_aleatorio() -> str:
    tiempo_actual = int(time.time())
    numero_aleatorio = tiempo_actual % 100000000  # Aseguramos 8 dígitos
    return f"{numero_aleatorio:08d}"

class User(models.Model):
    username = models.CharField(max_length=100)
    siglas = models.CharField(max_length=2)  # Ejemplo: AA, BB, CC (siglas de técnicos)
    rut = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=15)
    cargo = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    last_login = models.DateTimeField(auto_now=True)
    orden = models.CharField(max_length=100)

    def __str__(self):
        return self.username # print(User.objects.all()[0]) -> "Juan perez"

    def get_orden(self):
        return self.siglas + generar_numero_aleatorio() # BB12345678

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    rut = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Maquinaria(models.Model):
    orden = models.CharField(max_length=100, default=generar_numero_aleatorio)
    numero_serie = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    maquinaria = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    fecha = models.DateField() # Fecha de creación de la orden: 2021-01-01
    fecha_creacion_m = models.DateTimeField() # Fecha de creación de la orden: 2021-01-01 12:00:00
    problema = models.TextField(blank=True)

    def __str__(self):
        return self.marca

class Trazabilidad(models.Model):
    n_orden_trazabilidad = models.CharField(max_length=100)
    cliente_trazabilidad = models.CharField(max_length=100)
    maquinaria_trazabilidad = models.CharField(max_length=100)
    marca_trazabilidad = models.CharField(max_length=100)
    año_trazabilidad = models.PositiveIntegerField()
    fecha_trazabilidad = models.DateField()
    descripcion_problema_trazabilidad = models.TextField()
    fecha_creacion_t = models.DateTimeField()

    def __str__(self):
        return f"{self.cliente_trazabilidad} - {self.maquinaria_trazabilidad} - {self.fecha_trazabilidad}" # Juan Perez - Maquina 1 - 2021-01-01

class Manual(models.Model):
    nombre_manual = models.CharField(max_length=100)
    tipo_manual = models.CharField(max_length=100)
    año_manual = models.PositiveIntegerField()
    pdf_manual = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.nombre_manual
