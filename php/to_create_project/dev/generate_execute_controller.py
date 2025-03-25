import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command




def generate_execute_controller(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "Dev")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "ExecuteController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\Dev;

use App\\Http\\Controllers\\Controller;
use Illuminate\\Http\\Request;

class ExecuteController extends Controller
{

    public function __invoke(Request $request)
    {

        dd("pasa");

    }
    
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

