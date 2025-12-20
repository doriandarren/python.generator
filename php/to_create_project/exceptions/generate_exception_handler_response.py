import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command





def generate_exception_handler_response(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Exceptions")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "HandlerResponse.php")

    # Contenido por defecto
    content = r"""<?php

namespace App\Exceptions;

use Illuminate\Http\JsonResponse;

class HandlerResponse
{

    /**
     * @param $message
     * @param $statusCode
     * @param null $errors
     * @return JsonResponse
     */
    public static function respondWithError($message, $statusCode, $errors=null): JsonResponse
    {
        $data = [
            'message' => $message,
            'data' => null,
            'errors' => $errors,
            'success' => FALSE,
            'status_code' => $statusCode
        ];
        return response()->json($data, $statusCode);
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
