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
        "src/modules/Dashboard/components",
        "src/modules/Dashboard/pages",
        "src/modules/Dashboard/hooks",
        "src/modules/Dashboard/styles",
        "src/modules/Auth/components",
        "src/modules/Auth/pages",
        "src/modules/Auth/hooks",
        "src/modules/Auth/styles",
        "src/pages",
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
