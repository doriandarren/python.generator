import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_route_countries(full_path):
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
    file_path = os.path.join(styles_path, "countries.php")

    # Contenido por defecto
    content = """<?php

use App\\Enums\\EnumAbilitySuffix;
use App\\Http\\Controllers\\SHARED\\Countries\\CountryListController;
use App\\Http\\Controllers\\SHARED\\Countries\\CountryShowController;
//use App\\Http\\Controllers\\SHARED\\Countries\\CountryStoreController;
//use App\\Http\\Controllers\\SHARED\\Countries\\CountryUpdateController;
//use App\\Http\\Controllers\\SHARED\\Countries\\CountryDestroyController;
use Illuminate\\Support\\Facades\\Route;

/**
* Countries
*/

Route::group(['prefix' => 'countries/'], function () {

	Route::group(['middleware' => 'auth:sanctum'], function() {

		Route::get('list', [CountryListController::class, '__invoke']);
		Route::get('show/{country:id}', [CountryShowController::class, '__invoke']);


//		Route::post('store', [CountryStoreController::class, '__invoke'])->middleware('abilities:countries' . EnumAbilitySuffix::STORE);
//		Route::put('update/{country:id}', [CountryUpdateController::class, '__invoke'])->middleware('abilities:countries' . EnumAbilitySuffix::UPDATE);
//		Route::delete('delete/{country:id}', [CountryDestroyController::class, '__invoke'])->middleware('abilities:countries' . EnumAbilitySuffix::DESTROY);

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
