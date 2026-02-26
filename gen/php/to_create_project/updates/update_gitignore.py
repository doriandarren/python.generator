import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command



def update_gitignore(full_path):
    """
       Agrega un bloque de contenido al final del archivo .gitignore.
       - Agrega líneas en blanco aunque existan.
       - Agrega solo líneas nuevas con contenido.
       - Evita duplicados.
       - No deja línea en blanco antes del bloque añadido.
       """
    file_path = os.path.join(full_path, ".gitignore")

    if not os.path.exists(file_path):
        print_message(f"Error: {file_path} no existe.", CYAN)
        return

    block_to_add = """.DS_Store
app/Http/Controllers/Dev/TestController.php
"""

    lines_to_add = block_to_add.splitlines()

    try:
        with open(file_path, "r") as f:
            existing_lines = f.read().splitlines()

        # Eliminar líneas en blanco al final
        while existing_lines and existing_lines[-1].strip() == "":
            existing_lines.pop()

        new_lines = []

        for line in lines_to_add:
            if line.strip() == "" or line not in existing_lines:
                new_lines.append(line)

        if new_lines:
            with open(file_path, "w") as f:
                f.write("\n".join(existing_lines + new_lines) + "\n")
            print_message(f"Actualizo el archivo gitignore", GREEN)
        else:
            print_message(f"No hay nuevas líneas que agregar", CYAN)

    except Exception as e:
        print_message(f"Error al actualizar {file_path}: {e}", CYAN)