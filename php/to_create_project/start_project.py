


def start_project():
    # Ruta predeterminada
    default_path = "/Users/dorian/ReactProjects"

    project_name = input("Nombre del proyecto PHP: ")
    project_path = input(f"Ruta para crear el proyecto (por defecto: {default_path}): ").strip()

    # Si no se introduce una ruta, usar la predeterminada
    if not project_path:
        project_path = default_path

    # Combinar la ruta y el nombre del proyecto
    full_path = f"{project_path}/{project_name}"


