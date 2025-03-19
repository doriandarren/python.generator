from helpers.helper_print import input_with_validation
from php.to_create_project.generate_by_command_line import generate_by_command_line


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








