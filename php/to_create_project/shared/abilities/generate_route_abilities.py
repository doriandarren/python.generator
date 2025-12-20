import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_route_abilities(full_path):
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
    file_path = os.path.join(styles_path, "abilities.php")

    # Contenido por defecto
    content = """<?php

use App\\Enums\\EnumAbilitySuffix;
use App\\Http\\Controllers\\SHARED\\Abilities\\AbilityListController;
use App\\Http\\Controllers\\SHARED\\Abilities\\AbilityShowController;
use App\\Http\\Controllers\\SHARED\\Abilities\\AbilityStoreController;
use App\\Http\\Controllers\\SHARED\\Abilities\\AbilityUpdateController;
use App\\Http\\Controllers\\SHARED\\Abilities\\AbilityDestroyController;
use Illuminate\\Support\\Facades\\Route;

/**
* Abilities
*/


Route::group(['prefix' => 'abilities/'], function () {

	Route::group(['middleware' => 'auth:sanctum'], function() {

		Route::get('list', [AbilityListController::class, '__invoke'])->middleware('abilities:abilities' . EnumAbilitySuffix::LIST);
		Route::get('show/{ability:id}', [AbilityShowController::class, '__invoke'])->middleware('abilities:abilities' . EnumAbilitySuffix::SHOW);
		Route::post('store', [AbilityStoreController::class, '__invoke'])->middleware('abilities:abilities' . EnumAbilitySuffix::STORE);
		Route::put('update/{ability:id}', [AbilityUpdateController::class, '__invoke'])->middleware('abilities:abilities' . EnumAbilitySuffix::UPDATE);
		Route::delete('delete/{ability:id}', [AbilityDestroyController::class, '__invoke'])->middleware('abilities:abilities' . EnumAbilitySuffix::DESTROY);

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
