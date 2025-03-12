import os
from react.utils.utils import print_message, GREEN, CYAN, create_folder



def generate_project_structure(project_path):
    create_project_structure(project_path)



def create_project_structure(project_path):
    """
    Genera la estructura de carpetas para el proyecto React.
    """
    print_message("Generando estructura de carpetas...", CYAN)

    structure = [
        "src/assets/images",
        "src/assets/fonts",
        "src/components",
        "src/api",
        "src/router",
        "src/store",
        "src/hooks",
        "src/layouts",

        ## Public
        "src/modules/public/pages",
        "src/modules/public/routes",

        ## Auth
        "src/modules/auth/pages",
        "src/modules/auth/routes",

        ## Dashboard
        "src/modules/dashboard/pages",
        "src/modules/dashboard/routes",
        "src/helpers",

        ## "src/modules/auth/styles",
        ## "src/modules/auth/hooks",
        ## "src/modules/dashboard/hooks",
        ## "src/modules/auth/components",
        ## "src/services",
        ## "src/store/slices",
        ## "src/modules/dashboard/styles",
    ]
    # Define la estructura

    # Crear carpetas
    for folder in structure:
        full_path = os.path.join(project_path, folder)
        create_folder(full_path)

    print_message("Estructura de carpetas generada con éxito.", GREEN)



