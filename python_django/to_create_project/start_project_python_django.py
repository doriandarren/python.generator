from helpers.helper_menu import pause
from helpers.helper_print import input_with_validation


def start_project_python_django():
    
    # Defaults
    default_path = "/Users/dorian/PythonProjects"
    default_name = "app-1"

    # Inputs
    project_name = input_with_validation(
        f"Nombre del proyecto (defecto: {default_name}): ",
        default_name
    )
    project_path = input_with_validation(
        f"Ruta del proyecto (defecto: {default_path}): ",
        default_path
    )

    # Split
    full_path = f"{project_path}/{project_name}"
    
    ## TODO llamadas a las funciones "generate_"
    # generate_by_command_line(full_path)

    pause()