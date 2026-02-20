import os
from gen.helpers.helper_print import print_message, GREEN, CYAN




def generate_route_user_statuses(full_path):
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
    file_path = os.path.join(styles_path, "user_statuses.php")

    # Contenido por defecto
    content = """<?php

use App\\Enums\\EnumAbilitySuffix;
use App\\Http\\Controllers\\SHARED\\UserStatuses\\UserStatusListController;
use App\\Http\\Controllers\\SHARED\\UserStatuses\\UserStatusShowController;
use App\\Http\\Controllers\\SHARED\\UserStatuses\\UserStatusStoreController;
use App\\Http\\Controllers\\SHARED\\UserStatuses\\UserStatusUpdateController;
use App\\Http\\Controllers\\SHARED\\UserStatuses\\UserStatusDestroyController;
use Illuminate\\Support\\Facades\\Route;

/**
* UserStatuses
*/


Route::group(['prefix' => 'user-statuses/'], function () {

	Route::group(['middleware' => 'auth:sanctum'], function() {

		Route::get('list', [UserStatusListController::class, '__invoke'])->middleware('abilities:user_statuses' . EnumAbilitySuffix::LIST);
		Route::get('show/{user_status:id}', [UserStatusShowController::class, '__invoke'])->middleware('abilities:user_statuses' . EnumAbilitySuffix::SHOW);
		Route::post('store', [UserStatusStoreController::class, '__invoke'])->middleware('abilities:user_statuses' . EnumAbilitySuffix::STORE);
		Route::put('update/{user_status:id}', [UserStatusUpdateController::class, '__invoke'])->middleware('abilities:user_statuses' . EnumAbilitySuffix::UPDATE);
		Route::delete('delete/{user_status:id}', [UserStatusDestroyController::class, '__invoke'])->middleware('abilities:user_statuses' . EnumAbilitySuffix::DESTROY);

	});
});
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
