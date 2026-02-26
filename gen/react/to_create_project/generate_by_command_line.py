import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command


def generate_by_command_line(full_path: str):
    create_project(full_path)
    install_dependencies(full_path)

    # Instalar librerías (declarativo y fácil de mantener)
    install_packages(full_path, [
        ("classnames", "ClassNames"),
        ("@headlessui/react", "Headless UI"),
        ("@heroicons/react", "Heroicons"),
        ("lucide-react", "Lucide React"),
        ("recharts", "Recharts"),
        ("animate.css", "Animate.css"),
        ("sweetalert2", "SweetAlert2"),
        ("clsx", "clsx"),
        ("framer-motion", "Framer Motion"),
        ("uuid", "UUID"),
        ("prop-types", "PropTypes"),
    ])

    # Form validation (tu stack actual)
    install_packages(full_path, [
        ("react-hook-form", "React Hook Form"),
        ("@hookform/resolvers", "Hookform Resolvers"),
        ("yup", "Yup"),
    ], label="Validación de formularios")

    delete_app_and_index_css(full_path)


def create_project(full_path: str):
    """Crea el proyecto React con Vite."""
    project_dir = os.path.dirname(full_path)
    project_name = os.path.basename(full_path)

    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
        print_message(f"Directorio base {project_dir} creado.", GREEN)

    print_message("Creando el proyecto React con Vite...", CYAN)
    run_command(
        f"npm create vite@latest {project_name} -- --template react --yes",
        cwd=project_dir
    )


def install_dependencies(full_path: str):
    """Instala las dependencias del proyecto."""
    print_message("Instalando dependencias (npm install)...", CYAN)
    run_command("npm install", cwd=full_path)
    print_message("Dependencias instaladas.", GREEN)


def install_packages(full_path: str, packages: list[tuple[str, str]], label: str | None = None):
    """
    Instala paquetes con npm.
    packages: [("pkg-name", "Nombre bonito"), ...]
    """
    if label:
        print_message(f"Instalando: {label}", CYAN)

    for pkg, nice_name in packages:
        print_message(f"Instalando {nice_name} ({pkg})...", CYAN)
        run_command(f"npm install {pkg}", cwd=full_path)
        print_message(f"{nice_name} instalado correctamente.", GREEN)


def delete_app_and_index_css(full_path: str):
    """Elimina los archivos src/App.css y src/index.css si existen."""
    files_to_delete = ["src/App.css", "src/index.css"]

    for rel in files_to_delete:
        file_path = os.path.join(full_path, rel)
        if os.path.exists(file_path):
            os.remove(file_path)
            print_message(f"{rel} eliminado correctamente.", GREEN)
        else:
            print_message(f"{rel} no existe, no es necesario eliminarlo.", CYAN)
