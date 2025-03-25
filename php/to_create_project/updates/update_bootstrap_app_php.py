import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command



def update_bootstrap_app_php(full_path):
    update_abilities(full_path)



def update_abilities(full_path):
    """
    Actualiza el archivo
    """
    main_jsx_path = os.path.join(full_path, "bootstrap", "app.php")

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

use Laravel\\Sanctum\\Http\\Middleware\\CheckAbilities;
use Laravel\\Sanctum\\Http\\Middleware\\CheckForAnyAbility;
"""
        )


        # Reemplazos
        content = content.replace(
            """->withMiddleware(function (Middleware $middleware) {
        //
    })""",
            """->withMiddleware(function (Middleware $middleware) {
        $middleware->alias([
            'abilities' => CheckAbilities::class,
            'ability' => CheckForAnyAbility::class,
        ]);
    })"""
        )

        # Escribir el contenido actualizado
        with open(main_jsx_path, "w") as f:
            f.write(content)

        print_message("boostrap/app.php Actulizado correctamente.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {main_jsx_path}: {e}", CYAN)




