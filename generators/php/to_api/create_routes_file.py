import os

def create_routes_structure(base_ruta, path_routes, namespace):
    """
    Crea la estructura de carpetas 'base_ruta/path_routes/namespace' en la ruta especificada.
    """
    # Crear la ruta completa base_ruta/path_routes/namespace
    routes_folder_path = os.path.join(base_ruta, path_routes, namespace)

    if not os.path.exists(routes_folder_path):
        os.makedirs(routes_folder_path)
        print(f"Estructura de carpetas '{routes_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{routes_folder_path}' ya existe.")

    return routes_folder_path


def generate_routes_file(base_ruta, namespace, path_routes, plural_name, singular_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake):
    """
    Genera un archivo de rutas PHP basado en los nombres proporcionados y crea la estructura path_routes/namespace dentro de base_ruta.
    """
    # Crear la estructura de carpetas llamando a create_routes_structure
    routes_folder_path = create_routes_structure(base_ruta, path_routes, namespace)

    # Nombre del archivo PHP será plural_name_snake.php
    file_name = f'{plural_name_snake}.php'
    routes_file_path = os.path.join(routes_folder_path, file_name)

    # Contenido del archivo PHP de las rutas adaptado
    routes_content = f"""<?php

use App\\Enums\\EnumAbilitySuffix;
use App\\Enums\\EnumApiSetup;
use App\\Http\\Controllers\\{namespace}\\{plural_name}\\{singular_name}ListController;
use App\\Http\\Controllers\\{namespace}\\{plural_name}\\{singular_name}ShowController;
use App\\Http\\Controllers\\{namespace}\\{plural_name}\\{singular_name}StoreController;
use App\\Http\\Controllers\\{namespace}\\{plural_name}\\{singular_name}UpdateController;
use App\\Http\\Controllers\\{namespace}\\{plural_name}\\{singular_name}DestroyController;
use Illuminate\\Support\\Facades\\Route;

/**
* {plural_name}
*/

Route::get(EnumApiSetup::API_VERSION. 'invoice-headers/list', [InvoiceHeaderListController::class, '__invoke']);


Route::group(['prefix' => EnumApiSetup::API_VERSION . '{plural_name_kebab}/'], function () {{

	Route::group(['middleware' => 'auth:sanctum'], function() {{
        
        /*
		Route::get('list', [{singular_name}ListController::class, '__invoke'])->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::LIST);
		Route::get('show/{{{singular_name_snake}:id}}', [{singular_name}ShowController::class, '__invoke'])->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::SHOW);
		Route::post('store', [{singular_name}StoreController::class, '__invoke'])->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::STORE);
		Route::put('update/{{{singular_name_snake}:id}}', [{singular_name}UpdateController::class, '__invoke'])->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::UPDATE);
		Route::delete('delete/{{{singular_name_snake}:id}}', [{singular_name}DestroyController::class, '__invoke'])->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::DESTROY);
		*/
		
	}});
}});
"""

    # Escribir el archivo PHP con el contenido de las rutas
    try:
        with open(routes_file_path, 'w') as routes_file:
            routes_file.write(routes_content)
            print(f"Archivo de rutas PHP '{file_name}' creado en: {routes_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo de rutas PHP '{file_name}': {e}")
