import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_controller_ability_users(full_path):
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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "AbilityUsers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AbilityUserDestroyController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\AbilityUsers;

use App\\Http\\Controllers\\Controller;
use App\\Models\\AbilityUsers\\AbilityUser;
use App\\Repositories\\AbilityUsers\\AbilityUserRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;

class AbilityUserDestroyController extends Controller
{

	private AbilityUserRepository $repository;


	public function __construct()
	{
		$this->repository = new AbilityUserRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	*
	* @param Request $request
	* @param AbilityUser $abilityUser
	* @return JsonResponse
	*/
	public function __invoke(Request $request, AbilityUser $abilityUser): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			$data = $this->repository->destroy($abilityUser->id);

			return $this->respondWithData('AbilityUser deleted', $data);

		}else{

			if($abilityUser->company_id == auth()->user()->employee->company_id){

				$data = $this->repository->destroy($abilityUser->id);

				return $this->respondWithData('AbilityUser deleted', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "AbilityUsers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AbilityUserListController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\AbilityUsers;

use App\\Http\\Controllers\\Controller;
use App\\Repositories\\AbilityUsers\\AbilityUserRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;

class AbilityUserListController extends Controller
{

	private AbilityUserRepository $repository;


	public function __construct()
	{
		$this->repository = new AbilityUserRepository();
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
		return $this->respondWithData('AbilityUsers list', $data);
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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "AbilityUsers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AbilityUserShowController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\AbilityUsers;

use App\\Http\\Controllers\\Controller;
use App\\Models\\AbilityUsers\\AbilityUser;
use App\\Repositories\\AbilityUsers\\AbilityUserRepository;
use Illuminate\\Http\\JsonResponse;

class AbilityUserShowController extends Controller
{

	private AbilityUserRepository $repository;


	public function __construct()
	{
		$this->repository = new AbilityUserRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @param AbilityUser $abilityUser
	* @return JsonResponse
	*/
	public function __invoke(AbilityUser $abilityUser): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			$data = $this->repository->show($abilityUser->id);
			return $this->respondWithData('AbilityUser show', $data);

		}elseif($this->isManager(auth()->user()->roles)){

			$data = $this->repository->showByRoleManager(auth()->user()->employee->company_id, $abilityUser->id);
			return $this->respondWithData('AbilityUser show', $data);

		}else{

			$data = $this->repository->showByRoleUser(auth()->user()->employee->id, $abilityUser->id);
			return $this->respondWithData('AbilityUser show', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "AbilityUsers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AbilityUserStoreController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\AbilityUsers;

use App\\Http\\Controllers\\Controller;
use App\\Repositories\\AbilityUsers\\AbilityUserRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Validator;

class AbilityUserStoreController extends Controller
{

	private AbilityUserRepository $repository;


	public function __construct()
	{
		$this->repository = new AbilityUserRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @bodyParam user_id string required
	* @bodyParam ability_id string required
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
				'ability_id'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$abilityUser = $this->repository->setAbilityUser($request->user_id, $request->ability_id);

			$data = $this->repository->store($abilityUser);

			return $this->respondWithData('AbilityUser created', $data);

		}else if($this->isManager(auth()->user()->roles)){

			// By Manager

			$validator = Validator::make($request->all(), [
				'user_id'=>'required',
				'ability_id'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$abilityUser = $this->repository->setAbilityUser($request->user_id, $request->ability_id);

			$data = $this->repository->store($abilityUser);

			return $this->respondWithData('AbilityUser created', $data);

		}else{

			// By Role User

			$validator = Validator::make($request->all(), [
				'user_id'=>'required',
				'ability_id'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$abilityUser = $this->repository->setAbilityUser($request->user_id, $request->ability_id);

			$data = $this->repository->store($abilityUser);

			return $this->respondWithData('AbilityUser created', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "AbilityUsers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AbilityUserUpdateController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\AbilityUsers;

use App\\Http\\Controllers\\Controller;
use App\\Models\\AbilityUsers\\AbilityUser;
use App\\Repositories\\AbilityUsers\\AbilityUserRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Validator;

class AbilityUserUpdateController extends Controller
{

	private AbilityUserRepository $repository;


	public function __construct()
	{
		$this->repository = new AbilityUserRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @bodyParam user_id string required
	* @bodyParam ability_id string required
	*
	* @param Request $request
	* @param AbilityUser $abilityUser
	* @return JsonResponse
	*/
	public function __invoke(Request $request, AbilityUser $abilityUser): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){
			// By Admin

			$validator = Validator::make($request->all(), [
				'user_id'=>'required',
				'ability_id'=>'required',
			]);

			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}

			$data = $this->repository->update($abilityUser->id, $request->all());
			return $this->respondWithData('AbilityUser updated', $data);

		}else{

			// By Role User

			$validator = Validator::make($request->all(), [
				'user_id'=>'required',
				'ability_id'=>'required',
			]);

			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}

			if($abilityUser->company_id == auth()->user()->employee->company_id){

				$data = $this->repository->update($abilityUser->id, $request->all());

				return $this->respondWithData('AbilityUser updated', $data);

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