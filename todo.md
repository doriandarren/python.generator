# Generator Project

# TODOS:

- En PHP: cuando se crea un proyecto, se tiene que cambiar en el ".env" y en el ".env.example" lo siguientes: "LOG_CHANNEL=daily"
- en el archivo para API de postman hay que agregar en el Dev: el "execute"
- En PHP: revisar el plural cambiar a inflect por que agrega una "s" al final de la palabra de las migraciones cuando es fk



- Crear React_TS
- Crear Python

import os

def generate\_(project_path):
"""
Genera el archivo
"""
file_path = os.path.join(project_path, "")

    # Contenido del archivo
    content = r"""

"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")
