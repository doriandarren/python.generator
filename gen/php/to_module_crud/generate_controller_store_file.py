import os


def first_letter_lower(name):
    """Convierte la primera letra de un string a minúscula."""
    return name[0].lower() + name[1:]


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


def generate_controller_store_file(base_ruta, namespace, path_controller, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns):
    """
    Genera un archivo de controlador PHP para el método 'store' basado en los nombres proporcionados y crea la estructura app/path_controller dentro de base_ruta.
    """
    # Crear la estructura de carpetas llamando a create_controller_structure
    controller_folder_path = create_controller_structure(base_ruta, path_controller)

    # Nombre del archivo PHP será igual a singular_name
    file_name = f'{singular_name}StoreController.php'
    controller_file_path = os.path.join(controller_folder_path, file_name)

    # Construir los comentarios dinámicos para @bodyParam usando las columnas
    body_param_comments = ""
    for i, column in enumerate(columns):
        body_param_comments += f"    * @bodyParam {column['name']} string required"
        if i < len(columns) - 1:
            body_param_comments += "\n"

    # Contenido del archivo PHP del controlador para 'store'
    controller_content = f"""<?php

namespace App\\Http\\Controllers\\{namespace}\\{plural_name};

use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Support\\Facades\\Validator;
use App\\Http\\Controllers\\Controller;
use App\\Repositories\\{namespace}\\{plural_name}\\{singular_name}Repository;

class {singular_name}StoreController extends Controller
{{
    private {singular_name}Repository $repository;

    public function __construct()
    {{
        $this->repository = new {singular_name}Repository();
    }}

    /**
    * @header Authorization Bearer TOKEN 
    *
{body_param_comments}
    *
    * @param Request $request
    * @return JsonResponse
    */
    public function __invoke(Request $request): JsonResponse
    {{
        if($this->isAdmin(Auth::user()->roles)){{

            $validator = Validator::make($request->all(), [
"""

    # Agregar validaciones dinámicas para las columnas en la parte de Admin
    for column in columns:
        controller_content += f"                '{column['name']}'=>'required',\n"

    controller_content += f"""            ]); 
            if($validator->fails()){{
                return $this->respondWithError('Error', $validator->errors());
            }}
            ${ first_letter_lower(singular_name)} = $this->repository->set{singular_name}(
                {', '.join([f'$request->{column["name"]}' for column in columns])}
            );

            $data = $this->repository->store(${first_letter_lower(singular_name)});
            return $this->respondWithData('{singular_name} created', $data);

        }} else if($this->isManager(Auth::user()->roles)){{
            // By Manager
            $validator = Validator::make($request->all(), [
"""

    # Agregar validaciones dinámicas para las columnas en la parte de Manager
    for column in columns:
        controller_content += f"                '{column['name']}'=>'required',\n"

    controller_content += f"""            ]);
            if($validator->fails()){{
                return $this->respondWithError('Error', $validator->errors());
            }}
            ${first_letter_lower(singular_name)} = $this->repository->set{singular_name}(
                {', '.join([f'$request->{column["name"]}' for column in columns])}
            );

            $data = $this->repository->store(${first_letter_lower(singular_name)});
            return $this->respondWithData('{singular_name} created', $data);

        }} else {{
            // By User
            $validator = Validator::make($request->all(), [
"""

    # Agregar validaciones dinámicas para las columnas en la parte de User
    for column in columns:
        controller_content += f"                '{column['name']}'=>'required',\n"

    controller_content += f"""            ]);
            if($validator->fails()){{
                return $this->respondWithError('Error', $validator->errors());
            }}
            ${first_letter_lower(singular_name)} = $this->repository->set{singular_name}(
                {', '.join([f'$request->{column["name"]}' for column in columns])}
            );

            $data = $this->repository->store(${first_letter_lower(singular_name)});
            return $this->respondWithData('{singular_name} created', $data);
        }}
    }}
}}
"""

    # Escribir el archivo PHP con el contenido del controlador
    try:
        with open(controller_file_path, 'w') as controller_file:
            controller_file.write(controller_content)
            print(f"Archivo PHP controlador '{file_name}' creado en: {controller_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo PHP del controlador '{file_name}': {e}")
