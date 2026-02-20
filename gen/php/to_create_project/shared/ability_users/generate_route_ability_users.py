import os
from gen.helpers.helper_print import print_message, GREEN, CYAN






def generate_route_ability_users(full_path):
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
    file_path = os.path.join(styles_path, "ability_users.php")

    # Contenido por defecto
    content = """<?php

use App\\Enums\\EnumAbilitySuffix;
use App\\Http\\Controllers\\SHARED\\AbilityUsers\\AbilityUserListController;
use App\\Http\\Controllers\\SHARED\\AbilityUsers\\AbilityUserShowController;
use App\\Http\\Controllers\\SHARED\\AbilityUsers\\AbilityUserStoreController;
use App\\Http\\Controllers\\SHARED\\AbilityUsers\\AbilityUserUpdateController;
use App\\Http\\Controllers\\SHARED\\AbilityUsers\\AbilityUserDestroyController;
use Illuminate\\Support\\Facades\\Route;

/**
* AbilityUsers
*/


Route::group(['prefix' => 'ability-users/'], function () {

	Route::group(['middleware' => 'auth:sanctum'], function() {

		Route::get('list', [AbilityUserListController::class, '__invoke'])->middleware('abilities:ability_users' . EnumAbilitySuffix::LIST);
		Route::get('show/{ability_user:id}', [AbilityUserShowController::class, '__invoke'])->middleware('abilities:ability_users' . EnumAbilitySuffix::SHOW);
		Route::post('store', [AbilityUserStoreController::class, '__invoke'])->middleware('abilities:ability_users' . EnumAbilitySuffix::STORE);
		Route::put('update/{ability_user:id}', [AbilityUserUpdateController::class, '__invoke'])->middleware('abilities:ability_users' . EnumAbilitySuffix::UPDATE);
		Route::delete('delete/{ability_user:id}', [AbilityUserDestroyController::class, '__invoke'])->middleware('abilities:ability_users' . EnumAbilitySuffix::DESTROY);

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
