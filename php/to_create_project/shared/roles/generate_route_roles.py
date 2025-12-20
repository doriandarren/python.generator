import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_route_roles(full_path):
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
    file_path = os.path.join(styles_path, "roles.php")

    # Contenido por defecto
    content = """<?php

use App\\Enums\\EnumAbilitySuffix;
use App\\Http\\Controllers\\SHARED\\Roles\\RoleListController;
use App\\Http\\Controllers\\SHARED\\Roles\\RoleShowController;
use App\\Http\\Controllers\\SHARED\\Roles\\RoleStoreController;
use App\\Http\\Controllers\\SHARED\\Roles\\RoleUpdateController;
use App\\Http\\Controllers\\SHARED\\Roles\\RoleDestroyController;
use Illuminate\\Support\\Facades\\Route;

/**
* Roles
*/


Route::group(['prefix' => 'roles/'], function () {

	Route::group(['middleware' => 'auth:sanctum'], function() {

		Route::get('list', [RoleListController::class, '__invoke'])->middleware('abilities:roles' . EnumAbilitySuffix::LIST);
		Route::get('show/{role:id}', [RoleShowController::class, '__invoke'])->middleware('abilities:roles' . EnumAbilitySuffix::SHOW);
		Route::post('store', [RoleStoreController::class, '__invoke'])->middleware('abilities:roles' . EnumAbilitySuffix::STORE);
		Route::put('update/{role:id}', [RoleUpdateController::class, '__invoke'])->middleware('abilities:roles' . EnumAbilitySuffix::UPDATE);
		Route::delete('delete/{role:id}', [RoleDestroyController::class, '__invoke'])->middleware('abilities:roles' . EnumAbilitySuffix::DESTROY);

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
