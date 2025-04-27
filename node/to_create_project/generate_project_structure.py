import os
from helpers.helper_print import print_message, GREEN, CYAN, create_folder


def generate_project_structure(full_path):
    create_project_structure(full_path)




def create_project_structure(project_path):
    """
    Genera la estructura de carpetas para el proyecto React.
    """
    print_message("Generando estructura de carpetas...", CYAN)

    structure = [
        "public",
        "src",

    ]
    # Define la estructura

    # Crear carpetas
    for folder in structure:
        full_path = os.path.join(project_path, folder)
        create_folder(full_path)

    print_message("Estructura de carpetas generada con éxito.", GREEN)