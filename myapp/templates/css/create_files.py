from os import getcwd
from os import path
from io import TextIOWrapper
from os.path import join
# Crear una funcion para crear archivos html en esta carpeta y que contengan este str: 

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><: nombre :></title>  
    <link rel="stylesheet" href="style_<: nombre :>.css">  
    <style id="applicationStylesheet" type="text/css">

    </style>
</head>
<body>
	<h2>
        This is the <nombre> page
    </h2>
</body>
</html>
"""
BASE="myapp/"
lista_archivos = ["home.html", "login.html", "reset_password.html", "client.html", "new_client.html", "trazability.html", "machine.html", "new_machine.html", "manual.html", "new_manual.html", "about.html"]

def obtener_nombre(cadena:str) -> str:
    return cadena.split(".")[0] 

def añadir_html(cadena) -> str:
    return cadena + '.html'

def añadir_css(cadena) -> str:
    return cadena + '.css'

def crear_archivo(file_name, html=False, css=False) -> None:
    # Obtiene el directorio donde se encuentra el script actual
    script_directory = path.dirname(__file__) # <-- absolute dir the script is in
    current_directory =script_directory
    if html:
        file_path = path.join(current_directory, file_name + '.html')
    elif css:
        file_path = path.join(current_directory, "style_"+file_name + '.css')
    else:
        raise ValueError("No se ha especificado el tipo de archivo a crear")


    # Escribir el contenido al archivo HTML
    with open(file_path, 'w') as html_file:
        html_file.write("""
/* Reset básico para eliminar los márgenes y padding por defecto */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Estilos para el cuerpo del documento */
body {
    font-family: Arial, sans-serif; /* Fuente por defecto */
    line-height: 1.6; /* Altura de línea para una mejor lectura */
    padding: 20px; /* Un poco de padding para no tocar los bordes de la ventana */
    background-color: #f4f4f4; /* Un color de fondo suave */
    color: #333; /* Color de texto principal */
}

/* Estilos para el contenedor principal */
.container {
    width: 80%; /* Ancho del contenedor */
    margin: auto; /* Centrar el contenedor */
    overflow: hidden; /* Manejar el desbordamiento */
}

/* Estilos para los encabezados */
h1, h2, h3, h4, h5, h6 {
    margin-bottom: 20px; /* Margen inferior para separar de los siguientes elementos */
}

/* Estilos para los párrafos */
p {
    margin-bottom: 10px; /* Margen inferior para separar párrafos */
}

/* Clase de utilidad para añadir un margen superior */
.mt {
    margin-top: 20px;
}

/* Clase de utilidad para añadir un margen inferior */
.mb {
    margin-bottom: 20px;
}

/* Estilos para los enlaces */
a {
    color: #333;
    text-decoration: none; /* Remover el subrayado de los enlaces */
}

a:hover {
    color: #555;
    text-decoration: underline; /* Subrayado al pasar el mouse para indicar clickeabilidad */
}

/* Estilos para los botones */
button {
    display: inline-block;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
    border-radius: 5px;
    border: none;
    background-color: #333;
    color: white;
}

button:hover {
    background-color: #555;
}

/* Media query para la responsividad */
@media (max-width: 768px) {
    .container {
        width: 95%;
    }
}
""")  


# def texto(file:file)


lista_nombres = [ obtener_nombre(i) for i in lista_archivos ]
lista_css = [ añadir_css(obtener_nombre(i)) for i in lista_archivos ]


for i in lista_nombres:
    crear_archivo(i, css=True)
    print(f"Archivo {i}.css creado con exito")
