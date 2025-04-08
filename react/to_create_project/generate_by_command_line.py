import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command



def generate_by_command_line(full_path):
    # Crear proyecto y configurar
    create_project(full_path)
    install_dependencies(full_path)
    setup_classname(full_path)
    setup_headlessui(full_path)  ## Estilos UI
    setup_heroicons(full_path)  ## Icons
    setup_lucide_react(full_path)
    setup_animate_css(full_path)
    setup_sweetalert2(full_path)
    setup_validation_form(full_path) ## Validators Form
    setup_clsx(full_path)  ## utilidad para construir cadenas de clases condicionalmente
    setup_framer_motion(full_path)  ## utilidad para construir cadenas de clases condicionalmente
    delete_app_and_index_css(full_path)
    setup_uuid(full_path)





def create_project(full_path):
    """Crea el proyecto React con Vite."""

    project_dir = os.path.dirname(full_path)
    project_name = os.path.basename(full_path)

    # Verificar si el directorio base existe
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
        print_message(f"Directorio base {project_dir} creado.", GREEN)

    print_message("Creando el proyecto React con Vite...", CYAN)
    run_command(f"npm create vite@latest {project_name} -- --template react", cwd=project_dir)


def install_dependencies(full_path):
    """Instala las dependencias del proyecto."""
    print_message("Instalando dependencias...", CYAN)
    run_command("npm install", cwd=full_path)



def setup_classname(full_path):
    """Instala ClassNames."""
    print_message("Instalando ClassNames...", CYAN)
    run_command("npm install classnames", cwd=full_path)
    print_message("ClassNames instalado correctamente.", GREEN)


def setup_headlessui(full_path):
    """Instala Headlessui."""
    print_message("Instalando Headlessui...", CYAN)
    run_command("npm install @headlessui/react", cwd=full_path)
    print_message("Headlessui instalado correctamente.", GREEN)


def setup_heroicons(full_path):
    """Instala Heroicons."""
    print_message("Instalando Heroicons...", CYAN)
    run_command("npm install @heroicons/react", cwd=full_path)
    print_message("Heroicons instalado correctamente.", GREEN)



def setup_lucide_react(full_path):
    """Instala Heroicons."""
    print_message("Instalando LucideReact...", CYAN)
    run_command("npm install lucide-react", cwd=full_path)
    print_message("LucideReact instalado correctamente.", GREEN)


def setup_animate_css(full_path):
    """Instala FramerMotion."""
    print_message("Instalando AnimateCss...", CYAN)
    run_command("npm install animate.css --save", cwd=full_path)
    print_message("AnimateCss instalado correctamente.", GREEN)


def setup_sweetalert2(full_path):
    """Instala FramerMotion."""
    print_message("Instalando Sweetalert2...", CYAN)
    run_command("npm install sweetalert2", cwd=full_path)
    print_message("Sweetalert2 instalado correctamente.", GREEN)


def setup_clsx(full_path):
    """Instala Clsx."""
    print_message("Instalando Clsx...", CYAN)
    run_command("npm install clsx", cwd=full_path)
    print_message("Clsx instalado correctamente.", GREEN)


def setup_framer_motion(full_path):
    """Instala FramerMotion."""
    print_message("Instalando FramerMotion...", CYAN)
    run_command("npm install framer-motion", cwd=full_path)
    print_message("React FramerMotion instalado correctamente.", GREEN)



def setup_validation_form(full_path):
    """Instala FramerMotion."""
    print_message("Instalando FramerMotion...", CYAN)
    run_command("npm install react-hook-form @hookform/resolvers yup", cwd=full_path)
    print_message("React FramerMotion instalado correctamente.", GREEN)



def setup_uuid(full_path):
    """Instala FramerMotion."""
    print_message("Instalando UUID...", CYAN)
    run_command("npm i uuid", cwd=full_path)
    print_message("UUID instalado correctamente.", GREEN)







def delete_app_and_index_css(full_path):
    """
    Elimina los archivos src/App.css y src/index.css si existen.
    """
    files_to_delete = ["src/App.css", "src/index.css"]

    for file in files_to_delete:
        file_path = os.path.join(full_path, file)
        if os.path.exists(file_path):
            os.remove(file_path)
            print_message(f"{file} eliminado correctamente.", GREEN)
        else:
            print_message(f"{file} no existe, no es necesario eliminarlo.", CYAN)