import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command




def generate_by_command_line(full_path):

    create_project(full_path)





def create_project(full_path):
    """Crea el proyecto Node.js inicial."""

    project_dir = os.path.dirname(full_path)
    project_name = os.path.basename(full_path)

    # Verificar si el directorio base existe
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
        print_message(f"Directorio base {project_dir} creado.", GREEN)

    # Crear la carpeta del proyecto
    project_path = os.path.join(project_dir, project_name)
    if not os.path.exists(project_path):
        os.makedirs(project_path)
        print_message(f"Directorio del proyecto {project_path} creado.", GREEN)

    print_message("Inicializando el proyecto Node.js...", CYAN)
    run_command("npm init -y", cwd=project_path)

    print_message("Proyecto Node.js creado con éxito.", GREEN)