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
    """
    Genera la estructura de carpetas para el proyecto React.
    """
    print_message("Generando estructura de carpetas...", CYAN)

    # Define la estructura
    structure = [
        "src/assets/images",
        "src/assets/fonts",
        "src/components/Button",
        #"src/components/Modal",
        "src/hooks",
        "src/layouts",
        "src/layouts/components",
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
        "src/utils",
        "src/styles",
    ]

    # Crear carpetas
    for folder in structure:
        full_path = os.path.join(project_path, folder)
        create_folder(full_path)

    print_message("Estructura de carpetas generada con éxito.", GREEN)
