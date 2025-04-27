from helpers.helper_print import print_message, GREEN, CYAN
from node.to_create_project.generate_app import generate_app
from node.to_create_project.generate_by_command_line import generate_by_command_line
from node.to_create_project.generate_database import generate_database
from node.to_create_project.generate_enums import generate_enums
from node.to_create_project.generate_env import generate_env
from node.to_create_project.generate_gitignore import generate_gitignore
from node.to_create_project.generate_helpers import generate_helpers
from node.to_create_project.generate_middleware import generate_middleware
from node.to_create_project.generate_module_auth import generate_module_auth
from node.to_create_project.generate_postman_file import generate_postman_file
from node.to_create_project.generate_project_structure import generate_project_structure
from node.to_create_project.generate_public import generate_public
from node.to_create_project.generate_readme import generate_readme
from node.to_create_project.generate_scripts import generate_scripts
from node.to_create_project.generate_server import generate_server


def start_project():
    # Ruta predeterminada
    default_path = "/Users/dorian/NodejsProjects"

    project_name = input("Nombre del proyecto Node: ")
    project_path = input(f"Ruta para crear el proyecto (por defecto: {default_path}): ").strip()

    # Si no se introduce una ruta, usar la predeterminada
    if not project_path:
        project_path = default_path

    # Combinar la ruta y el nombre del proyecto
    full_path = f"{project_path}/{project_name}"


    generate_by_command_line(full_path)

    # Generar la estructura de carpetas
    generate_project_structure(full_path)


    generate_env(full_path)
    generate_readme(full_path)
    generate_gitignore(full_path)
    generate_postman_file(full_path)
    generate_app(full_path)
    generate_public(full_path)
    generate_server(full_path)
    generate_scripts(full_path)
    generate_middleware(full_path)
    generate_helpers(full_path)
    generate_enums(full_path)
    generate_database(full_path)



    ## Modules



    ##generate_module_auth(full_path)








    # Mensaje final
    print_message(f"¡Proyecto Node creado exitosamente en {full_path}!", GREEN)
    print_message(f"Para empezar: cd {full_path} && npm run dev", CYAN)