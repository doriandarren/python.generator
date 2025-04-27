from helpers.helper_print import print_message, GREEN, CYAN
from react.to_create_project.generate_components import generate_components
from react.to_create_project.generate_react_router import generate_react_router
from react.to_create_project.generate_images import generate_images
from react.to_create_project.generate_by_command_line import generate_by_command_line
from react.to_create_project.generate_project_structure import generate_project_structure
from react.to_create_project.generate_styles import generate_styles
from react.to_create_project.generate_public_layouts import generate_public_layouts
from react.to_create_project.generate_private_layouts import generate_private_layouts
from react.to_create_project.generate_module_public import generate_module_public
from react.to_create_project.generate_module_dashboard import generate_module_dashboard
from react.to_create_project.generate_module_auth import generate_module_auth
from react.to_create_project.generate_redux import generate_redux
from react.to_create_project.generate_helpers import generate_helpers
from react.to_create_project.generate_translate import generate_translate
from react.to_create_project.generate_env import generate_env
from react.to_create_project.generate_gitignore import generate_gitignore
from react.to_create_project.generate_readme import generate_readme
from react.to_create_project.generate_index_html import generate_index_html
from react.to_create_project.generate_folder_api import generate_folder_api
from react.to_create_project.generate_module_teams import generate_module_teams
from react.to_create_project.generate_module_profile import generate_module_profile





def start_project():
    # Ruta predeterminada
    default_path = "/Users/dorian/ReactProjects"

    project_name = input("Nombre del proyecto React: ")
    project_path = input(f"Ruta para crear el proyecto (por defecto: {default_path}): ").strip()

    # Si no se introduce una ruta, usar la predeterminada
    if not project_path:
        project_path = default_path

    # Combinar la ruta y el nombre del proyecto
    full_path = f"{project_path}/{project_name}"


    generate_by_command_line(full_path)

    generate_project_structure(full_path)

    generate_styles(full_path)
    generate_images(full_path)



    ## Layouts
    generate_public_layouts(full_path)
    generate_private_layouts(full_path)


    ## generate Public
    generate_module_public(full_path)

    ## React Router
    generate_react_router(full_path)

    generate_components(full_path)

    # Dashboard
    generate_module_dashboard(full_path)

    # Auth
    generate_module_auth(full_path)

    ## Profile
    generate_module_profile(full_path)

    # Teams
    generate_module_teams(full_path)

    # Redux
    generate_redux(full_path)

    # Helpers
    generate_helpers(full_path)

    # Translate
    generate_translate(full_path)

    generate_env(full_path)

    generate_gitignore(full_path)

    generate_readme(full_path)

    ## index.html
    generate_index_html(full_path)

    generate_folder_api(full_path)

    # Mensaje final
    print_message(f"¡Proyecto React creado exitosamente en {full_path}!", GREEN)
    print_message(f"Para empezar: cd {full_path} && npm run dev", CYAN)
