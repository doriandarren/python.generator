# import sys
# import os
# print("Rutas en sys.path:", sys.path)
# print("Ruta actual:", os.getcwd())

from to_create_project.generate_by_command_line import *
from to_create_project.utils import print_message, GREEN, CYAN
from to_create_project.generate_project_structure import generate_project_structure



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
    setup_tailwind(full_path)
    setup_index_css(full_path)
    setup_app_jsx(full_path)
    update_main_jsx(full_path)
    delete_app_css(full_path)


    generate_project_structure(full_path)


    # Mensaje final
    print_message(f"¡Proyecto React creado exitosamente en {full_path}!", GREEN)
    print_message(f"Para empezar: cd {full_path} && npm run dev", CYAN)


if __name__ == "__main__":
    start()
