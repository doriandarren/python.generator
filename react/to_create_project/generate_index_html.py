import os
from react.utils.utils import print_message, GREEN, CYAN


def generate_index_html(full_path):
    update_main_jsx(full_path)




def update_main_jsx(full_path):
    """
    Actualiza el archivo
    """
    file_path = os.path.join(full_path, "index.html")

    # Verificar si el archivo existe
    if not os.path.exists(file_path):
        print_message(f"Error: {file_path} no existe.", CYAN)
        return

    try:

        # Leer el contenido del archivo
        with open(file_path, "r") as f:
            content = f.read()


        # Reemplazos
        content = content.replace(
            "<html lang=\"en\">",
            "<html lang=\"es\">"
        )

        # Reemplazos
        content = content.replace(
            "<title>Vite + React</title>",
            "<title>Site</title>"
        )



        # Escribir el contenido actualizado
        with open(file_path, "w") as f:
            f.write(content)

        print_message("index.html configurado correctamente.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {file_path}: {e}", CYAN)
