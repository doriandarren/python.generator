from helpers.helper_menu import pause
from helpers.helper_print import input_with_validation


def start_project_cpp():
    
    # Defaults
    default_path = "/Users/dorian/ReactProjects"
    default_name = "app-1"
    
    # Inputs
    project_name = input_with_validation(f"Nombre del proyecto (defacto: {default_name}): ", default_name)
    project_path = input_with_validation(f"Ruta para crear el proyecto (defecto: {default_path}): ",  default_path)


    # Split
    full_path = f"{project_path}/{project_name}"
    
    
    ## TODO llamadas a los "generate_"
    # generate_by_command_line(full_path)
    
    pause()
    
    
