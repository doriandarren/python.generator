import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command



def update_gitignore(full_path):
    """
    Agrega un bloque de contenido al final del archivo .gitignore.
    - Agrega líneas en blanco aunque existan.
    - Agrega solo líneas nuevas con contenido.
    - Evita duplicados.
    """
    file_path = os.path.join(full_path, ".gitignore")

    if not os.path.exists(file_path):
        print_message(f"Error: {file_path} no existe.", CYAN)
        return

    # Bloque de contenido
    block_to_add = """.DS_Store
app/Http/Controllers/Dev/TestController.php
src/Api/Dev/
"""

    lines_to_add = block_to_add.splitlines()

    try:
        # Leer contenido existente
        with open(file_path, "r") as f:
            existing_lines = f.read().splitlines()

        new_lines = []

        for line in lines_to_add:
            if line.strip() == "":
                # Siempre agregar líneas en blanco
                new_lines.append("")
                print_message("Línea en blanco agregada.", GREEN)
            elif line not in existing_lines:
                new_lines.append(line)
                print_message(f"Línea agregada: {line}", GREEN)
            else:
                print_message(f"Línea ya existe: {line}", CYAN)

        if new_lines:
            with open(file_path, "a") as f:
                f.write("\n" + "\n".join(new_lines) + "\n")
        else:
            print_message("No hay nuevas líneas que agregar.", CYAN)

    except Exception as e:
        print_message(f"Error al actualizar {file_path}: {e}", CYAN)
