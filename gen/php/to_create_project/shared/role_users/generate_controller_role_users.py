import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_controller_role_users(full_path):
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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "RoleUsers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleUserDestroyController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\RoleUsers;

use App\\Http\\Controllers\\Controller;
use App\\Models\\RoleUsers\\RoleUser;
use App\\Repositories\\RoleUsers\\RoleUserRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;

class RoleUserDestroyController extends Controller
{

	private RoleUserRepository $repository;


	public function __construct()
	{
		$this->repository = new RoleUserRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	*
	* @param Request $request
	* @param RoleUser $roleUser
	* @return JsonResponse
	*/
	public function __invoke(Request $request, RoleUser $roleUser): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			$data = $this->repository->destroy($roleUser->id);

			return $this->respondWithData('RoleUser deleted', $data);

		}else{

			if($roleUser->company_id == auth()->user()->employee->company_id){

				$data = $this->repository->destroy($roleUser->id);

				return $this->respondWithData('RoleUser deleted', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "RoleUsers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleUserListController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\RoleUsers;

use App\\Http\\Controllers\\Controller;
use App\\Repositories\\RoleUsers\\RoleUserRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;

class RoleUserListController extends Controller
{

	private RoleUserRepository $repository;


	public function __construct()
	{
		$this->repository = new RoleUserRepository();
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
		return $this->respondWithData('RoleUsers list', $data);
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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "RoleUsers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleUserShowController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\RoleUsers;

use App\\Http\\Controllers\\Controller;
use App\\Models\\RoleUsers\\RoleUser;
use App\\Repositories\\RoleUsers\\RoleUserRepository;
use Illuminate\\Http\\JsonResponse;

class RoleUserShowController extends Controller
{

	private RoleUserRepository $repository;


	public function __construct()
	{
		$this->repository = new RoleUserRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @param RoleUser $roleUser
	* @return JsonResponse
	*/
	public function __invoke(RoleUser $roleUser): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			$data = $this->repository->show($roleUser->id);
			return $this->respondWithData('RoleUser show', $data);

		}elseif($this->isManager(auth()->user()->roles)){

			$data = $this->repository->showByRoleManager(auth()->user()->employee->company_id, $roleUser->id);
			return $this->respondWithData('RoleUser show', $data);

		}else{

			$data = $this->repository->showByRoleUser(auth()->user()->employee->id, $roleUser->id);
			return $this->respondWithData('RoleUser show', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "RoleUsers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleUserStoreController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\RoleUsers;

use App\\Http\\Controllers\\Controller;
use App\\Repositories\\RoleUsers\\RoleUserRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Validator;

class RoleUserStoreController extends Controller
{

	private RoleUserRepository $repository;


	public function __construct()
	{
		$this->repository = new RoleUserRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @bodyParam user_id string required
	* @bodyParam role_id string required
	*
	* @param Request $request
	* @return JsonResponse
	*/
	public function __invoke(Request $request): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			// By Admin

			$validator = Validator::make($request->all(), [
				'user_id'=>'required',
				'role_id'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$roleUser = $this->repository->setRoleUser($request->user_id, $request->role_id);

			$data = $this->repository->store($roleUser);

			return $this->respondWithData('RoleUser created', $data);

		}else if($this->isManager(auth()->user()->roles)){

			// By Manager

			$validator = Validator::make($request->all(), [
				'user_id'=>'required',
				'role_id'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$roleUser = $this->repository->setRoleUser($request->user_id, $request->role_id);

			$data = $this->repository->store($roleUser);

			return $this->respondWithData('RoleUser created', $data);

		}else{

			// By Role User

			$validator = Validator::make($request->all(), [
				'user_id'=>'required',
				'role_id'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$roleUser = $this->repository->setRoleUser($request->user_id, $request->role_id);

			$data = $this->repository->store($roleUser);

			return $this->respondWithData('RoleUser created', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "RoleUsers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleUserUpdateController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\RoleUsers;

use App\\Http\\Controllers\\Controller;
use App\\Models\\RoleUsers\\RoleUser;
use App\\Repositories\\RoleUsers\\RoleUserRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Validator;

class RoleUserUpdateController extends Controller
{

	private RoleUserRepository $repository;


	public function __construct()
	{
		$this->repository = new RoleUserRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @bodyParam user_id string required
	* @bodyParam role_id string required
	*
	* @param Request $request
	* @param RoleUser $roleUser
	* @return JsonResponse
	*/
	public function __invoke(Request $request, RoleUser $roleUser): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){
			// By Admin

			$validator = Validator::make($request->all(), [
				'user_id'=>'required',
				'role_id'=>'required',
			]);

			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}

			$data = $this->repository->update($roleUser->id, $request->all());
			return $this->respondWithData('RoleUser updated', $data);

		}else{

			// By Role User

			$validator = Validator::make($request->all(), [
				'user_id'=>'required',
				'role_id'=>'required',
			]);

			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}

			if($roleUser->company_id == auth()->user()->employee->company_id){

				$data = $this->repository->update($roleUser->id, $request->all());

				return $this->respondWithData('RoleUser updated', $data);

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