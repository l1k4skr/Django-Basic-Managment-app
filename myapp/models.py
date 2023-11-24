from django.db.models import *

class User(Model):
    username = CharField(max_length=100)
    siglas  = CharField(max_length=2) # -> AA -> BB -> CC -> siglas de tecnicos
    rut = CharField(max_length=20)
    direccion = CharField(max_length=100) 
    email = CharField(max_length=100)
    telefono = CharField(max_length=15)
    cargo = CharField(max_length=100)
    password = CharField(max_length=20)

    def __str__(self):
        return self.username

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
    orden = CharField(max_length=100)
    numero_serie = CharField(max_length=100) # agregar numero de serie > CharField(max_length=100)
    cliente = CharField(max_length=100)
    maquinaria =  CharField(max_length=100)  #ForeignKey(Cliente, on_delete=CASCADE)
    marca = CharField(max_length=100)  # Cliente > ForeignKey(Cliente, related_name='maquinarias', on_delete=CASCADE) 1 a 1 >
    año = PositiveIntegerField()
    fecha = DateField()
    problema = TextField(blank=True)
    
    def __str__(self):
        return self.MARCA

class Trazabilidad(Model):
    """Modelo que representa la trazabilidad de una máquina médica."""
    n_orden = CharField(max_length=10, unique=True)  # RR00000001
    cliente = CharField(max_length=100) #ForeignKey(Cliente, on_delete=CASCADE)
    maquinaria = CharField(max_length=100) #ForeignKey(Maquinaria, on_delete=CASCADE, null=True, blank=True)  # Permitir valores nulos
    marca= CharField(max_length=100)
    año = PositiveIntegerField()
    fecha = DateField()
    descripcion_problema = TextField()

    # class Meta:
    #     unique_together = ['cliente', 'maquinaria']
    
    def __str__(self):
        return f"{self.cliente} - {self.maquinaria} - {self.fecha}"

class Manual(Model):
    """Modelo que representa un manual de una máquina médica."""
    nombre_manual = CharField(max_length=100)
    tipo_manual = CharField(max_length=100)
    año_manual = PositiveIntegerField()
    pdf_manual = FileField(upload_to='pdfs/')
