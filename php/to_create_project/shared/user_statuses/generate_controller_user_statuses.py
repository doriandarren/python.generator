import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_controller_user_statuses(full_path):
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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "UserStatuses")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "UserStatusDestroyController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\UserStatuses;

use App\\Http\\Controllers\\Controller;
use App\\Models\\UserStatuses\\UserStatus;
use App\\Repositories\\UserStatuses\\UserStatusRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;

class UserStatusDestroyController extends Controller
{

	private UserStatusRepository $repository;


	public function __construct()
	{
		$this->repository = new UserStatusRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	*
	* @param Request $request
	* @param UserStatus $userStatus
	* @return JsonResponse
	*/
	public function __invoke(Request $request, UserStatus $userStatus): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			$data = $this->repository->destroy($userStatus->id);

			return $this->respondWithData('UserStatus deleted', $data);

		}else{

			if($userStatus->company_id == auth()->user()->employee->company_id){

				$data = $this->repository->destroy($userStatus->id);

				return $this->respondWithData('UserStatus deleted', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "UserStatuses")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "UserStatusListController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\UserStatuses;

use App\\Http\\Controllers\\Controller;
use App\\Repositories\\UserStatuses\\UserStatusRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;

class UserStatusListController extends Controller
{

	private UserStatusRepository $repository;


	public function __construct()
	{
		$this->repository = new UserStatusRepository();
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
		return $this->respondWithData('UserStatuses list', $data);
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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "UserStatuses")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "UserStatusShowController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\UserStatuses;

use App\\Http\\Controllers\\Controller;
use App\\Models\\UserStatuses\\UserStatus;
use App\\Repositories\\UserStatuses\\UserStatusRepository;
use Illuminate\\Http\\JsonResponse;

class UserStatusShowController extends Controller
{

	private UserStatusRepository $repository;


	public function __construct()
	{
		$this->repository = new UserStatusRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @param UserStatus $userStatus
	* @return JsonResponse
	*/
	public function __invoke(UserStatus $userStatus): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			$data = $this->repository->show($userStatus->id);
			return $this->respondWithData('UserStatus show', $data);

		}elseif($this->isManager(auth()->user()->roles)){

			$data = $this->repository->showByRoleManager(auth()->user()->employee->company_id, $userStatus->id);
			return $this->respondWithData('UserStatus show', $data);

		}else{

			$data = $this->repository->showByRoleUser(auth()->user()->employee->id, $userStatus->id);
			return $this->respondWithData('UserStatus show', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "UserStatuses")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "UserStatusStoreController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\UserStatuses;

use App\\Http\\Controllers\\Controller;
use App\\Repositories\\UserStatuses\\UserStatusRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Validator;

class UserStatusStoreController extends Controller
{

	private UserStatusRepository $repository;


	public function __construct()
	{
		$this->repository = new UserStatusRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @bodyParam name string required
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
			$userStatus = $this->repository->setUserStatus($request->name);

			$data = $this->repository->store($userStatus);

			return $this->respondWithData('UserStatus created', $data);

		}else if($this->isManager(auth()->user()->roles)){

			// By Manager

			$validator = Validator::make($request->all(), [
				'name'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$userStatus = $this->repository->setUserStatus($request->name);

			$data = $this->repository->store($userStatus);

			return $this->respondWithData('UserStatus created', $data);

		}else{

			// By Role User

			$validator = Validator::make($request->all(), [
				'name'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$userStatus = $this->repository->setUserStatus($request->name);

			$data = $this->repository->store($userStatus);

			return $this->respondWithData('UserStatus created', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "UserStatuses")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "UserStatusUpdateController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\UserStatuses;

use App\\Http\\Controllers\\Controller;
use App\\Models\\UserStatuses\\UserStatus;
use App\\Repositories\\UserStatuses\\UserStatusRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Validator;

class UserStatusUpdateController extends Controller
{

	private UserStatusRepository $repository;


	public function __construct()
	{
		$this->repository = new UserStatusRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @bodyParam name string required
	*
	* @param Request $request
	* @param UserStatus $userStatus
	* @return JsonResponse
	*/
	public function __invoke(Request $request, UserStatus $userStatus): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){
			// By Admin

			$validator = Validator::make($request->all(), [
				'name'=>'required',
			]);

			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}

			$data = $this->repository->update($userStatus->id, $request->all());
			return $this->respondWithData('UserStatus updated', $data);

		}else{

			// By Role User

			$validator = Validator::make($request->all(), [
				'name'=>'required',
			]);

			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}

			if($userStatus->company_id == auth()->user()->employee->company_id){

				$data = $this->repository->update($userStatus->id, $request->all());

				return $this->respondWithData('UserStatus updated', $data);

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