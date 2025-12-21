import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_barrel_file(full_path, singular_name, plural_name_snake):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "src", "modules", plural_name_snake, 'pages')
    file_path = os.path.join(folder_path, "index.js")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''
export * from './{singular_name}Page';
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)