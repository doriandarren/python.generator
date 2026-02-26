import os
from gen.helpers.helper_print import print_message, GREEN, CYAN


def generate_route_ability_groups(full_path):
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
    file_path = os.path.join(styles_path, "ability_groups.php")

    # Contenido por defecto
    content = """<?php

use App\\Enums\\EnumAbilitySuffix;
use App\\Http\\Controllers\\SHARED\\AbilityGroups\\AbilityGroupListController;
use App\\Http\\Controllers\\SHARED\\AbilityGroups\\AbilityGroupShowController;
use App\\Http\\Controllers\\SHARED\\AbilityGroups\\AbilityGroupStoreController;
use App\\Http\\Controllers\\SHARED\\AbilityGroups\\AbilityGroupUpdateController;
use App\\Http\\Controllers\\SHARED\\AbilityGroups\\AbilityGroupDestroyController;
use Illuminate\\Support\\Facades\\Route;

/**
* AbilityGroups
*/


Route::group(['prefix' => 'ability-groups/'], function () {

	Route::group(['middleware' => 'auth:sanctum'], function() {

		Route::get('list', [AbilityGroupListController::class, '__invoke'])->middleware('abilities:ability_groups' . EnumAbilitySuffix::LIST);
		Route::get('show/{ability_group:id}', [AbilityGroupShowController::class, '__invoke'])->middleware('abilities:ability_groups' . EnumAbilitySuffix::SHOW);
		Route::post('store', [AbilityGroupStoreController::class, '__invoke'])->middleware('abilities:ability_groups' . EnumAbilitySuffix::STORE);
		Route::put('update/{ability_group:id}', [AbilityGroupUpdateController::class, '__invoke'])->middleware('abilities:ability_groups' . EnumAbilitySuffix::UPDATE);
		Route::delete('delete/{ability_group:id}', [AbilityGroupDestroyController::class, '__invoke'])->middleware('abilities:ability_groups' . EnumAbilitySuffix::DESTROY);

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
