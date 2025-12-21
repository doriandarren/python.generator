

from helpers.helper_columns import parse_columns_input
from helpers.helper_menu import menu_checkbox, pause
from helpers.helper_print import input_with_validation


def start_project_cpp():
    
    # Ruta predeterminada
    default_path = "/Users/dorian/PhpstormProjects81"

    project_name = input_with_validation("Nombre del proyecto: ", None)
    project_path = input(f"Ruta para crear el proyecto (por defecto: {default_path}): ").strip()

    # Si no se introduce una ruta, usar la predeterminada
    if not project_path:
        project_path = default_path

    # Combinar la ruta y el nombre del proyecto
    full_path = f"{project_path}/{project_name}"
    
    
    ## TODO irian las llamadas a los metodos para crear el proyecto

    
