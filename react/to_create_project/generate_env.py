import os
from .utils import print_message, GREEN, CYAN, run_command



def generate_env(full_path):
    create_env_file(full_path)
    create_env_example_file(full_path)


def create_env_file(project_path):
    """
    Genera el archivo
    """
    file_path = os.path.join(project_path, ".env")



    # Contenido del archivo
    content = """VITE_APP_NAME=SiteLocal
VITE_APP_ENV=local
VITE_URL_API_BASE=http://project.test/v1/api/
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")

def create_env_example_file(project_path):
    """
    Genera el archivo
    """
    file_path = os.path.join(project_path, ".env.example")

    # Contenido del archivo
    content = """VITE_APP_NAME=SiteLocal
VITE_APP_ENV=local
VITE_URL_API_BASE=http://project.test/v1/api/
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")