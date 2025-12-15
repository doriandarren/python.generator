# Generator Project


# TODOS:

- Crear React_TS
- Crear Python






import os

def generate_(project_path):
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
