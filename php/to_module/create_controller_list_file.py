import os

def create_controllers_structure(base_ruta, path_model):
    """
    Crea la estructura de carpetas 'base_ruta/app/path_model' en la ruta especificada.
    """
    controllers_folder_path = os.path.join(base_ruta, 'app', path_model)

    if not os.path.exists(controllers_folder_path):
        os.makedirs(controllers_folder_path)
        print(f"Estructura de carpetas '{controllers_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{controllers_folder_path}' ya existe.")

    return controllers_folder_path


def generate_controller_list_file(base_ruta, namespace, path_model, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake):
    """
    Genera un archivo de controlador PHP basado en los nombres proporcionados y crea la estructura app/path_model dentro de base_ruta.
    """
    # Crear la estructura de carpetas llamando a create_controllers_structure
    controllers_folder_path = create_controllers_structure(base_ruta, path_model)

    # Nombre del archivo PHP será igual a singular_name
    file_name = f'{singular_name}ListController.php'
    controller_file_path = os.path.join(controllers_folder_path, file_name)

    # Contenido del archivo PHP del controlador adaptado
    controller_content = f"""<?php

namespace App\\Http\\Controllers\\{namespace}\\{plural_name};

use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Auth;
use App\\Http\\Controllers\\Controller;
use App\\Repositories\\{plural_name}\\{singular_name}Repository;

class {singular_name}ListController extends Controller
{{
    private {singular_name}Repository $repository;

    public function __construct()
    {{
        $this->repository = new {singular_name}Repository();
    }}

    /**
    * @header Authorization Bearer TOKEN 
    *
    * @param Request $request
    * @return JsonResponse
    */
    public function __invoke(Request $request): JsonResponse
    {{
        if ($this->isAdmin(Auth::user()->roles)) {{
            $data = $this->repository->list();
        }} elseif ($this->isManager(Auth::user()->roles)) {{
            $data = $this->repository->listByRoleManager();
        }} else {{
            $data = $this->repository->listByRoleUser();
        }}
        
        return $this->respondWithData('{plural_name} list', $data);
    }}
}}
"""

    # Escribir el archivo PHP con el contenido del controlador
    try:
        with open(controller_file_path, 'w') as controller_file:
            controller_file.write(controller_content)
            print(f"Archivo de controlador PHP '{file_name}' creado en: {controllers_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo de controlador PHP '{file_name}': {e}")
