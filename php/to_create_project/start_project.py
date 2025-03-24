from helpers.helper_print import input_with_validation
from php.to_create_project.generate_base_controller import generate_base_controller
from php.to_create_project.generate_by_command_line import generate_by_command_line
from php.to_create_project.generate_controller_auth import generate_controller_auth
from php.to_create_project.generate_enums import generate_enums
from php.to_create_project.shared.generate_shared import generate_shared
from php.to_create_project.updates.update_app_php import update_app_php
from php.to_create_project.updates.update_model_user_php import update_model_user
from php.to_create_project.utilities.generate_utilities import generate_utilities


def start_project():
    # Ruta predeterminada
    default_path = "/Users/dorian/PhpstormProjects81"

    project_name = input_with_validation("Nombre del proyecto: ", None)
    project_path = input(f"Ruta para crear el proyecto (por defecto: {default_path}): ").strip()

    # Si no se introduce una ruta, usar la predeterminada
    if not project_path:
        project_path = default_path

    # Combinar la ruta y el nombre del proyecto
    full_path = f"{project_path}/{project_name}"

    # Crear el proyecto
    generate_by_command_line(full_path)
    generate_enums(full_path)


    # Controller & Base Controller
    generate_base_controller(full_path)




    # Controllers
    generate_controller_auth(full_path)

    # Shared
    generate_shared(full_path)


    # Utilities
    generate_utilities(full_path)



    # Updates
    update_model_user(full_path)
    update_app_php(full_path)

    # TODO Exceptions










