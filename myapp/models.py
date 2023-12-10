from django.db.models import *
import time
def generar_numero_aleatorio() -> str:
    # Usamos el tiempo actual en segundos para generar números "aleatorios"
    tiempo_actual = int(time.time())
    numero_aleatorio = tiempo_actual % 100000000  # Aseguramos 8 dígitos
    return f"{numero_aleatorio:08d}"


class User(Model):
    username = CharField(max_length=100)
    siglas  = CharField(max_length=2) # -> AA -> BB -> CC -> siglas de tecnicos
    rut = CharField(max_length=20)
    direccion = CharField(max_length=100) 
    email = CharField(max_length=100)
    telefono = CharField(max_length=15)
    cargo = CharField(max_length=100)
    password = CharField(max_length=20)
    last_login = DateTimeField(auto_now=True)
    orden = CharField(max_length=100)

    def __str__(self):
        return self.username
    def get_orden(self):
        return self.siglas + generar_numero_aleatorio()

class Cliente(Model):
    """Modelo que representa a un cliente que posee maquinaria médica."""
    nombre = CharField(max_length=100)
    razon_social = CharField(max_length=100)
    rut = CharField(max_length=20)
    direccion = CharField(max_length=100)
    email = EmailField()
    telefono = CharField(max_length=15)
    # Agregar Maquinaria > ForeignKey(Maquinaria, on_delete=CASCADE) 1 a muchos <    
    def __str__(self):
        return self.nombre
    
class Maquinaria(Model):
    """Modelo que representa una máquina médica de un cliente."""
    orden = CharField(max_length=100, default=generar_numero_aleatorio)  # RR00000001
    numero_serie = CharField(max_length=100) 
    cliente = CharField(max_length=100)
    maquinaria =  CharField(max_length=100)  #ForeignKey(Cliente, on_delete=CASCADE)
    marca = CharField(max_length=100) 
    año = PositiveIntegerField()
    fecha = DateField( )
    fecha_creacion_m = DateTimeField()
    problema = TextField(blank=True)

    
    def __str__(self):
        return self.MARCA
    
class Trazabilidad(Model):
    """Modelo que representa la trazabilidad de una máquina médica."""
    n_orden_trazabilidad = CharField(max_length=100)  # RR00000001
    cliente_trazabilidad = CharField(max_length=100) 
    maquinaria_trazabilidad = CharField(max_length=100) 
    marca_trazabilidad= CharField(max_length=100)
    año_trazabilidad = PositiveIntegerField()
    fecha_trazabilidad = DateField()
    descripcion_problema_trazabilidad = TextField()
    fecha_creacion_t = DateTimeField()


    def __str__(self):
        return f"{self.cliente} - {self.maquinaria} - {self.fecha}"



class Manual(Model):
    """Modelo que representa un manual de una máquina médica."""
    nombre_manual = CharField(max_length=100)
    tipo_manual = CharField(max_length=100)
    año_manual = PositiveIntegerField()
    pdf_manual = FileField(upload_to='pdfs/')
