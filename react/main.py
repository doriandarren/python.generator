from react.to_create_project.generate_file_routes import generate_file_routes
from react.to_create_project.generate_images import generate_images
from to_create_project.generate_by_command_line import *
from to_create_project.utils import print_message, GREEN, CYAN
from to_create_project.generate_project_structure import generate_project_structure
from to_create_project.generate_styles import generate_styles
from to_create_project.generate_layouts import generate_layouts
from to_create_project.generate_public_pages import generate_pages




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

    # Crear proyecto y configurar
    create_project(full_path)
    install_dependencies(full_path)
    setup_react_router(full_path)
    setup_classname(full_path)
    setup_headlessui(full_path)             ## Estilos UI
    setup_heroicons(full_path)              ## Icons
    setup_clsx(full_path)                   ## utilidad para construir cadenas de clases condicionalmente
    setup_framer_motion(full_path)          ## utilidad para construir cadenas de clases condicionalmente
    setup_app_jsx(full_path)
    update_main_jsx(full_path)
    delete_app_and_index_css(full_path)


    generate_project_structure(full_path)

    generate_styles(full_path)

    generate_images(full_path)

    ## generate MainLayout
    generate_layouts(full_path)

    ## generate HomePages
    generate_pages(full_path)

    ## generate Routes
    generate_file_routes(full_path)





    # Mensaje final
    print_message(f"¡Proyecto React creado exitosamente en {full_path}!", GREEN)
    print_message(f"Para empezar: cd {full_path} && npm run dev", CYAN)


if __name__ == "__main__":
    start()
