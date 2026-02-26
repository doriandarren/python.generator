import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command



def update_app_php(full_path):
    """
    Actualiza el archivo
    """
    main_jsx_path = os.path.join(full_path, "config", "app.php")

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
            "'timezone' => 'UTC',",
            """'timezone' => 'Europe/Madrid',"""
        )

        # Escribir el contenido actualizado
        with open(main_jsx_path, "w") as f:
            f.write(content)

        print_message("app.php Actulizado correctamente.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {main_jsx_path}: {e}", CYAN)


