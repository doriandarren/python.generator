import os
from gen.helpers.helper_print import print_message, GREEN, CYAN




def generate_code_file_init(full_path):
    """
    Genera el archivo init
    """
    folder_path = os.path.join(full_path, "core")
    file_path = os.path.join(folder_path, "__init__.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f''''''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)