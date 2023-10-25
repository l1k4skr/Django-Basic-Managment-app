from django.db.models import *
"""
Debemos crear un modelo para cada tabla que queramos crear en la base de datos.

"""


class User(Model):
    name = CharField(max_length=100)
    email = CharField(max_length=100)
    password = CharField(max_length=20)