from to_create_project.utils import print_message, GREEN, CYAN
from react.to_create_project.generate_components import generate_components
from react.to_create_project.generate_react_router import generate_react_router
from react.to_create_project.generate_images import generate_images
from to_create_project.generate_by_command_line import generate_by_command_line
from to_create_project.generate_project_structure import generate_project_structure
from to_create_project.generate_styles import generate_styles
from to_create_project.generate_layouts import generate_layouts
from to_create_project.generate_public_pages import generate_public_pages
from to_create_project.generate_dashboard_pages import generate_dashboard_pages
from to_create_project.generate_auth_pages import generate_auth_pages
from to_create_project.generate_redux import generate_redux
from to_create_project.generate_helpers import generate_helpers
from to_create_project.generate_translate import generate_translate




def start():
    # Ruta predeterminada
    default_path = "/Users/dorian/ReactProjects"

    project_name = input("Introduce el nombre del proyecto React: ")
    project_path = input(f"Introduce la ruta donde deseas crear el proyecto (por defecto: {default_path}): ").strip()

    # Si no se introduce una ruta, usar la predeterminada
    if not project_path:
        project_path = default_path

    # Combinar la ruta y el nombre del proyecto
    full_path = f"{project_path}/{project_name}"


    generate_by_command_line(full_path)

    generate_project_structure(full_path)

    generate_styles(full_path)
    generate_images(full_path)



    ## generate MainLayout
    generate_layouts(full_path)

    ## generate Public
    generate_public_pages(full_path)

    ## React Router
    generate_react_router(full_path)


    generate_components(full_path)


    # Dashboard
    generate_dashboard_pages(full_path)

    # Auth
    generate_auth_pages(full_path)

    # Redux
    generate_redux(full_path)


    # Helpers
    generate_helpers(full_path)

    # Translate
    generate_translate(full_path)


    # Mensaje final
    print_message(f"¡Proyecto React creado exitosamente en {full_path}!", GREEN)
    print_message(f"Para empezar: cd {full_path} && npm run dev", CYAN)





if __name__ == "__main__":
    start()
