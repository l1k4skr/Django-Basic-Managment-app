from django.db.models import *

class User(Model):
    name = CharField(max_length=100)
    email = CharField(max_length=100)
    password = CharField(max_length=20)
    def __str__(self):
        return self.name

class Cliente(Model):
    """Modelo que representa a un cliente que posee maquinaria médica."""
    nombre = CharField(max_length=100)
    direccion = CharField(max_length=100)
    rut = CharField(max_length=20)
    razon_social = CharField(max_length=100)
    email = EmailField()
    telefono = CharField(max_length=15)
    # Agregar Maquinaria > ForeignKey(Maquinaria, on_delete=CASCADE) 1 a muchos <    
    def __str__(self):
        return self.nombre

class Maquinaria(Model):
    """Modelo que representa una máquina médica de un cliente."""
    n_serie = CharField(max_length=100)
    modelo = CharField(max_length=100)
    año = PositiveIntegerField()
    # Cliente > ForeignKey(Cliente, related_name='maquinarias', on_delete=CASCADE) 1 a 1 >
    cliente = ForeignKey(Cliente, related_name='maquinarias', on_delete=CASCADE)
    descripcion = TextField()
    cotizacion = CharField(max_length=100)
    historial = TextField(blank=True)
    
    def __str__(self):
        return self.modelo

class Trazabilidad(Model):
    """Modelo que representa la trazabilidad de una máquina médica."""
    n_orden = CharField(max_length=10, unique=True)  # RR00000001
    cliente = ForeignKey(Cliente, on_delete=CASCADE)
    maquinaria = ForeignKey(Maquinaria, on_delete=CASCADE, null=True, blank=True)  # Permitir valores nulos
    tipo = CharField(max_length=100)
    fecha = DateField()
    descripcion = TextField()

    class Meta:
        unique_together = ['cliente', 'maquinaria']
    
    def __str__(self):
        return f"{self.cliente} - {self.maquinaria} - {self.fecha}"
