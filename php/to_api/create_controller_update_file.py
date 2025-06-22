import os

def create_controller_structure(base_ruta, path_controller):
    """
    Crea la estructura de carpetas 'base_ruta/app/path_controller' en la ruta especificada.
    """
    # Crear la ruta completa base_ruta/app/path_controller
    controller_folder_path = os.path.join(base_ruta, 'app', path_controller)

    if not os.path.exists(controller_folder_path):
        os.makedirs(controller_folder_path)
        print(f"Estructura de carpetas '{controller_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{controller_folder_path}' ya existe.")

    return controller_folder_path




def generate_controller_update_file(base_ruta, namespace, path_controller, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns):
    """
    Genera el archivo de controlador PHP para el método Update.
    """
    # Crear la estructura de carpetas llamando a create_controller_structure
    controller_folder_path = create_controller_structure(base_ruta, path_controller)

    # Nombre del archivo PHP será igual a singular_name
    file_name = f'{singular_name}UpdateController.php'
    controller_file_path = os.path.join(controller_folder_path, file_name)

    # Crear comentarios dinámicos para @bodyParam
    body_param_comments = ""
    for i, column in enumerate(columns):
        body_param_comments += f"    * @bodyParam {column['name']} string required"
        if i < len(columns) - 1:
            body_param_comments += "\n"

    # Contenido del archivo PHP del controlador adaptado
    controller_content = f"""<?php

namespace App\\Http\\Controllers\\{namespace}\\{plural_name};

use App\\Models\\{plural_name}\\{singular_name};
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use App\\Http\\Controllers\\Controller;
use Illuminate\\Support\\Facades\\Validator;
use Illuminate\\Validation\\Rule;
use App\\Repositories\\{plural_name}\\{singular_name}Repository;

class {singular_name}UpdateController extends Controller
{{
    private {singular_name}Repository $repository;

    public function __construct()
    {{
        $this->repository = new {singular_name}Repository();
    }}

    /**
    * @header Authorization Bearer TOKEN 
    * @urlParam id required The ID of the table.
    *
{body_param_comments}
    *
    * @param Request $request
    * @param {singular_name} ${singular_name_snake}
    * @return JsonResponse
    */
    public function __invoke(Request $request, {singular_name} ${singular_name_snake}): JsonResponse
    {{

        if($this->isAdmin(auth()->user()->roles)){{
            // By Admin

            $validator = Validator::make($request->all(), [
{generate_validation_rules(columns)}
            ]);

            if($validator->fails()){{
                return $this->respondWithError('Error', $validator->errors());
            }}

            $data = $this->repository->update(${singular_name_snake}->id, $request->all());
            return $this->respondWithData('{singular_name} updated', $data);

        }}else{{

            // By Role Manager & User

            $validator = Validator::make($request->all(), [
{generate_validation_rules(columns)}
            ]);

            if($validator->fails()){{
                return $this->respondWithError('Error', $validator->errors());
            }}

            $data = $this->repository->update(${singular_name_snake}->id, $request->all());

            return $this->respondWithData('{singular_name} updated', $data);

        }}

    }}

}}"""

    # Escribir el archivo PHP con el contenido del controlador
    try:
        with open(controller_file_path, 'w') as controller_file:
            controller_file.write(controller_content)
            print(f"Archivo PHP controlador '{file_name}' creado en: {controller_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo de controlador '{file_name}': {e}")





# Función auxiliar para generar reglas de validación
def generate_validation_rules(columns):
    validation_rules = ""
    for column in columns:
        validation_rules += f"                '{column['name']}' => 'required',\n"
    return validation_rules
