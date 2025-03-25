import os
from helpers.helper_print import print_message, GREEN, CYAN


def generate_route_test(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "routes", "SHARED")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "dev.php")

    # Contenido por defecto
    content = """<?php

use App\\Http\\Controllers\\Dev\\ExecuteController;
use App\\Http\\Controllers\\Dev\\TestController;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Route;

/*
|--------------------------------------------------------------------------
| DEV
|--------------------------------------------------------------------------
|
*/

Route::get('v1/dev/execute', ExecuteController::class . '@__invoke')->name('v1/dev/execute');

Route::get('v1/dev/test', TestController::class . '@__invoke')->name('v1/dev/test');


"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
