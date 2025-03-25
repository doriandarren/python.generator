import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command



def update_route_api_php(full_path):
    update_use(full_path)
    update_route(full_path)





def update_use(full_path):
    """
    Actualiza el archivo
    """
    main_jsx_path = os.path.join(full_path, "routes", "api.php")

    # Verificar si el archivo existe
    if not os.path.exists(main_jsx_path):
        print_message(f"Error: {main_jsx_path} no existe.", CYAN)
        return

    try:

        # Leer el contenido del archivo
        with open(main_jsx_path, "r") as f:
            content = f.read()


        # Reemplazos
        content = content.replace(
            """<?php
""",
            """<?php

use App\\Enums\\EnumApiSetup;"""
        )

        # Escribir el contenido actualizado
        with open(main_jsx_path, "w") as f:
            f.write(content)

        print_message("use api.php correctamente.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {main_jsx_path}: {e}", CYAN)







def update_route(full_path):
    """
    Agrega un bloque de contenido al final del archivo
    """
    file_path = os.path.join(full_path, "routes", "api.php")

    if not os.path.exists(file_path):
        print_message(f"Error: {file_path} no existe.", CYAN)
        return

    block_to_add = """Route::prefix(EnumApiSetup::API_VERSION )->group(function () {
    require base_path('routes/SHARED/abilities.php');
    require base_path('routes/SHARED/ability_groups.php');
    require base_path('routes/SHARED/ability_users.php');
    require base_path('routes/SHARED/countries.php');
    require base_path('routes/SHARED/dev.php');
    require base_path('routes/SHARED/role_users.php');
    require base_path('routes/SHARED/roles.php');
    require base_path('routes/SHARED/user_statuses.php');
    // ...
});
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
            print_message(f"Actualizo el archivo api.php", GREEN)
        else:
            print_message(f"No hay nuevas líneas que agregar", CYAN)

    except Exception as e:
        print_message(f"Error al actualizar {file_path}: {e}", CYAN)