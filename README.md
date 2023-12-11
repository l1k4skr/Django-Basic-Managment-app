# Django-Web
# Proyecto de Gestión de Maquinaria Médica

Este es un proyecto de gestión de maquinaria médica desarrollado en Django. Permite a los usuarios gestionar clientes, máquinas médicas, manuales y más.

## Funcionalidades

- **Inicio de sesión:** Los usuarios pueden iniciar sesión utilizando su correo electrónico y contraseña.

- **Gestión de Usuarios:** Los administradores pueden agregar, editar y eliminar usuarios. Cada usuario tiene un nombre de usuario único, siglas, dirección, correo electrónico, teléfono y cargo.

- **Gestión de Clientes:** Se pueden agregar, editar y eliminar clientes. Los detalles del cliente incluyen nombre, razón social, RUT, dirección, correo electrónico y teléfono.

- **Gestión de Maquinaria:** Permite registrar máquinas médicas, incluyendo número de serie, cliente asociado, tipo de máquina, marca, año de fabricación, fecha de adquisición y descripción de problemas.

- **Trazabilidad:** Registra la trazabilidad de las máquinas médicas, incluyendo número de orden, cliente, tipo de máquina, marca, año y descripción de problemas.

- **Manuales:** Los usuarios pueden cargar manuales de máquinas médicas, incluyendo nombre, tipo, año y archivo PDF.

## Requisitos

- Python 3.x
- Django 3.x
- Otros requisitos específicos de tu proyecto

## Instalación

1. Clona este repositorio en tu máquina local:

git clone https://github.com/tu-usuario/proyecto-gestion-maquinaria.git


2. Instala las dependencias:

pip install -r requirements.txt


3. Ejecuta las migraciones de la base de datos:

python manage.py makemigrations
python manage.py migrate


4. Inicia el servidor:

python manage.py runserver


5. Accede al proyecto en tu navegador web:

http://localhost:8000/


## Uso

- Inicia sesión con tu correo electrónico y contraseña.
- Explora las diferentes funcionalidades de gestión de usuarios, clientes, máquinas médicas y manuales.
- Añade, edita o elimina registros según sea necesario.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu contribución.
3. Realiza tus cambios y asegúrate de que los tests pasen.
4. Envía un pull request a la rama principal del proyecto.

## Autor

- Nombre: [Andres Perez]
- Correo Electrónico: [andres.antonio2000@hotmail.com]

## Licencia

Este proyecto está bajo la Licencia MIT