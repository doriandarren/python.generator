import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_controller_roles(full_path):
    create_destroy(full_path)
    create_list(full_path)
    create_show(full_path)
    create_store(full_path)
    create_update(full_path)



def create_destroy(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "SHARED", "Roles")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RolesController.php")

    # Contenido por defecto
    content = """
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


