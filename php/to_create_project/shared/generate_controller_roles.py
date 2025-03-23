import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_controller_roles(full_path):
    create_destroy(full_path)
    create_list(full_path)
    create_show(full_path)
    create_store(full_path)
    create_update(full_path)
    


def create_destroy(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "SHARED", "Roles")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleDestroyController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\Roles;

use App\\Http\\Controllers\\Controller;
use App\\Models\\Roles\\Role;
use App\\Repositories\\Roles\\RoleRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;

class RoleDestroyController extends Controller
{

	private RoleRepository $repository;


	public function __construct()
	{
		$this->repository = new RoleRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	*
	* @param Request $request
	* @param Role $role
	* @return JsonResponse
	*/
	public function __invoke(Request $request, Role $role): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			$data = $this->repository->destroy($role->id);

			return $this->respondWithData('Role deleted', $data);

		}else{

			if($role->company_id == auth()->user()->employee->company_id){

				$data = $this->repository->destroy($role->id);

				return $this->respondWithData('Role deleted', $data);

			}else{

				return $this->respondWithError('Error', ['e' => trans('validation.user_not_belong_company')]);

			}

		}

	}

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

def create_list(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "SHARED", "Roles")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleListController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\Roles;

use App\\Http\\Controllers\\Controller;
use App\\Repositories\\Roles\\RoleRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;

class RoleListController extends Controller
{

	private RoleRepository $repository;


	public function __construct()
	{
		$this->repository = new RoleRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @param Request $request
	* @return JsonResponse
	*/
	public function __invoke(Request $request): JsonResponse
	{
		if($this->isAdmin(auth()->user()->roles)){
			$data = $this->repository->list();
		}elseif($this->isManager(auth()->user()->roles)){
			$data = $this->repository->listByRoleManager(auth()->user()->employee->company_id);
		}else{
			$data = $this->repository->listByRoleUser(auth()->user()->employee->company_id, auth()->user()->employee->id);
		}
		return $this->respondWithData('Roles list', $data);
	}

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

def create_show(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "SHARED", "Roles")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleShowController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\Roles;

use App\\Http\\Controllers\\Controller;
use App\\Models\\Roles\\Role;
use App\\Repositories\\Roles\\RoleRepository;
use Illuminate\\Http\\JsonResponse;

class RoleShowController extends Controller
{

	private RoleRepository $repository;


	public function __construct()
	{
		$this->repository = new RoleRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @param Role $role
	* @return JsonResponse
	*/
	public function __invoke(Role $role): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			$data = $this->repository->show($role->id);
			return $this->respondWithData('Role show', $data);

		}elseif($this->isManager(auth()->user()->roles)){

			$data = $this->repository->showByRoleManager(auth()->user()->employee->company_id, $role->id);
			return $this->respondWithData('Role show', $data);

		}else{

			$data = $this->repository->showByRoleUser(auth()->user()->employee->id, $role->id);
			return $this->respondWithData('Role show', $data);

		}

	}

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

def create_store(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "SHARED", "Roles")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleStoreController.php")

    # Contenido por defecto
    content = """<?php

namespace App\Http\Controllers\SHARED\Roles;

use App\\Http\\Controllers\\Controller;
use App\\Repositories\\Roles\\RoleRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Validator;

class RoleStoreController extends Controller
{

	private RoleRepository $repository;


	public function __construct()
	{
		$this->repository = new RoleRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @bodyParam name string required
	* @bodyParam description string
	*
	* @param Request $request
	* @return JsonResponse
	*/
	public function __invoke(Request $request): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			// By Admin

			$validator = Validator::make($request->all(), [
				'name'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$role = $this->repository->setRole($request->name, $request->description);

			$data = $this->repository->store($role);

			return $this->respondWithData('Role created', $data);

		}else if($this->isManager(auth()->user()->roles)){

			// By Manager

			$validator = Validator::make($request->all(), [
				'name'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$role = $this->repository->setRole($request->name, $request->description);

			$data = $this->repository->store($role);

			return $this->respondWithData('Role created', $data);

		}else{

			// By Role User

			$validator = Validator::make($request->all(), [
				'name'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$role = $this->repository->setRole($request->name, $request->description);

			$data = $this->repository->store($role);

			return $this->respondWithData('Role created', $data);

		}

	}

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

def create_update(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "SHARED", "Roles")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleUpdateController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\Roles;

use App\\Http\\Controllers\\Controller;
use App\\Models\\Roles\\Role;
use App\\Repositories\\Roles\\RoleRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Validator;

class RoleUpdateController extends Controller
{

	private RoleRepository $repository;


	public function __construct()
	{
		$this->repository = new RoleRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @bodyParam description string required
	*
	* @param Request $request
	* @param Role $role
	* @return JsonResponse
	*/
	public function __invoke(Request $request, Role $role): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){
			// By Admin

			$validator = Validator::make($request->all(), [
				'description'=>'required',
			]);

			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}

			$data = $this->repository->update($role->id, $request->all());
			return $this->respondWithData('Role updated', $data);

		}else{

			// By Role User

			$validator = Validator::make($request->all(), [
				'description'=>'required',
			]);

			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}

			if($role->company_id == auth()->user()->employee->company_id){

				$data = $this->repository->update($role->id, $request->all());

				return $this->respondWithData('Role updated', $data);

			}else{

				return $this->respondWithError('Error', ['e' => trans('validation.user_not_belong_company')]);

			}

		}

	}

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)