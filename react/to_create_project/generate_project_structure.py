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



def create_project_structure(project_path):
    """
    Genera la estructura de carpetas para el proyecto React.
    """
    print_message("Generando estructura de carpetas...", CYAN)

    structure = [
        "src/assets/images",
        "src/assets/fonts",
        "src/components",
        "src/router",
        "src/store",
        "src/hooks",
        "src/layouts",

        ## Public
        "src/modules/public/pages",
        "src/modules/public/routes",

        ## Auth
        "src/modules/auth/pages",
        "src/modules/auth/routes",
        "src/modules/auth/api",

        ## Dashboard
        "src/modules/dashboard/components",
        "src/modules/dashboard/pages",
        "src/modules/dashboard/routes",
        "src/modules/dashboard/api",
        "src/helpers",
        "src/styles",

        ## "src/modules/auth/styles",
        ## "src/modules/auth/hooks",
        ## "src/modules/dashboard/hooks",
        ## "src/modules/auth/components",
        ## "src/services",
        ## "src/store/slices",
        ## "src/modules/dashboard/styles",
    ]
    # Define la estructura

    # Crear carpetas
    for folder in structure:
        full_path = os.path.join(project_path, folder)
        create_folder(full_path)

    print_message("Estructura de carpetas generada con éxito.", GREEN)



