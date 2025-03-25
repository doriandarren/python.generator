import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_route_role_users(full_path):
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
    file_path = os.path.join(styles_path, "role_users.php")

    # Contenido por defecto
    content = """<?php

use App\\Enums\\EnumAbilitySuffix;
use App\\Http\\Controllers\\SHARED\\RoleUsers\\RoleUserListController;
use App\\Http\\Controllers\\SHARED\\RoleUsers\\RoleUserShowController;
use App\\Http\\Controllers\\SHARED\\RoleUsers\\RoleUserStoreController;
use App\\Http\\Controllers\\SHARED\\RoleUsers\\RoleUserUpdateController;
use App\\Http\\Controllers\\SHARED\\RoleUsers\\RoleUserDestroyController;
use Illuminate\\Support\\Facades\\Route;

/**
* RoleUsers
*/


Route::group(['prefix' => 'role-users/'], function () {

	Route::group(['middleware' => 'auth:sanctum'], function() {

		Route::get('list', [RoleUserListController::class, '__invoke'])->middleware('abilities:role_users' . EnumAbilitySuffix::LIST);
		Route::get('show/{role_user:id}', [RoleUserShowController::class, '__invoke'])->middleware('abilities:role_users' . EnumAbilitySuffix::SHOW);
		Route::post('store', [RoleUserStoreController::class, '__invoke'])->middleware('abilities:role_users' . EnumAbilitySuffix::STORE);
		Route::put('update/{role_user:id}', [RoleUserUpdateController::class, '__invoke'])->middleware('abilities:role_users' . EnumAbilitySuffix::UPDATE);
		Route::delete('delete/{role_user:id}', [RoleUserDestroyController::class, '__invoke'])->middleware('abilities:role_users' . EnumAbilitySuffix::DESTROY);

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
