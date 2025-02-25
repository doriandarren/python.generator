import os
from .utils import print_message, GREEN, CYAN


def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print_message(f"Carpeta creada: {path}", GREEN)
    else:
        print_message(f"Carpeta ya existe: {path}", CYAN)




def generate_project_structure(project_path):
    create_project_structure(project_path)
    create_env_file(project_path)
    create_env_example_file(project_path)



def create_project_structure(project_path):
    """
    Genera la estructura de carpetas para el proyecto React.
    """
    print_message("Generando estructura de carpetas...", CYAN)

    # Define la estructura
    structure = [
        "src/assets/images",
        "src/assets/fonts",
        "src/components",
        "src/router",
        "src/store",
        "src/hooks",
        "src/layouts",
        "src/modules/dashboard/components",
        "src/modules/dashboard/pages",
        "src/modules/dashboard/hooks",
        "src/modules/dashboard/styles",
        "src/modules/dashboard/routes",
        "src/modules/auth/components",
        "src/modules/auth/pages",
        "src/modules/auth/hooks",
        "src/modules/auth/styles",
        "src/modules/auth/routes",
        "src/modules/public/pages",
        "src/modules/public/routes",
        ##"src/services",
        ##"src/store/slices",
        "src/helpers",
        "src/styles",
    ]

    # Crear carpetas
    for folder in structure:
        full_path = os.path.join(project_path, folder)
        create_folder(full_path)

    print_message("Estructura de carpetas generada con éxito.", GREEN)




def create_env_file(project_path):
    """
    Genera el archivo
    """
    file_path = os.path.join(project_path, ".env")



    # Contenido del archivo
    content = """VITE_APP_TITLE=SiteLocal
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
    content = """VITE_APP_TITLE=SiteLocal
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