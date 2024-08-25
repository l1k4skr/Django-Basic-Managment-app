
# Gestor de Maquinaria Médica

Este proyecto es un sistema de gestión para maquinaria médica implementado con Django, HTML y CSS. Facilita la gestión de maquinarias defectuosas, trazabilidad, configuración y documentación técnica a través de una interfaz web.

## Funcionalidades

- **Registro e Inicio de Sesión**: Autenticación completa para usuarios, permitiendo el registro y el acceso al sistema.
- **Gestión de Clientes**: Automatización en la creación de registros de clientes conforme se ingresan nuevas maquinarias.
- **Administración de Maquinarias**: Permite ingresar maquinarias con detalles como número de serie, cliente asignado, marca, año, fecha de creación, y problemas identificados. Cada registro es editable y eliminable.
- **Manejo de Manuales**: Funcionalidad para subir, editar y eliminar manuales en formato PDF.
- **Configuración del Sistema**: Sección dedicada para la creación y gestión de usuarios del sistema.

## Tecnologías Utilizadas

- **Backend**: Django
- **Frontend**: HTML, CSS
- **Base de Datos**: SQLite (Por defecto con Django)

## Configuración e Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/l1k4skr/Django-Basic-Managment-app.git
   cd Django-Basic-Managment-app
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Migraciones de la base de datos**:
   ```bash
   python manage.py migrate
   ```

4. **Crear superusuario**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Ejecutar el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

## Uso

Accede a `http://127.0.0.1:8000` en tu navegador para iniciar la aplicación y comenzar a gestionar la maquinaria médica.

## Contribuciones

Las contribuciones son bienvenidas. Para cambios mayores, por favor abre un issue primero para discutir lo que te gustaría cambiar.

## Licencia

Este proyecto está licenciado bajo [Nombre de la Licencia] - ve el archivo LICENSE para más detalles.
