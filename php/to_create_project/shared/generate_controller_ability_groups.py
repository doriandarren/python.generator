import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_controller_ability_groups(full_path):
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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "SHARED", "AbilityGroups")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, ".php")

    # Contenido por defecto
    content = """
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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "SHARED", "AbilityGroups")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AbilityGroupController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\AbilityGroups;

use App\\Http\\Controllers\\Controller;
use App\\Repositories\\AbilityGroups\\AbilityGroupRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;

class AbilityGroupListController extends Controller
{

	private AbilityGroupRepository $repository;


	public function __construct()
	{
		$this->repository = new AbilityGroupRepository();
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
		return $this->respondWithData('AbilityGroups list', $data);
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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "SHARED", "AbilityGroups")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AbilityGroupController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\AbilityGroups;

use App\\Http\\Controllers\\Controller;
use App\\Models\\AbilityGroups\\AbilityGroup;
use App\\Repositories\\AbilityGroups\\AbilityGroupRepository;
use Illuminate\\Http\\JsonResponse;

class AbilityGroupShowController extends Controller
{

	private AbilityGroupRepository $repository;


	public function __construct()
	{
		$this->repository = new AbilityGroupRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @param AbilityGroup $abilityGroup
	* @return JsonResponse
	*/
	public function __invoke(AbilityGroup $abilityGroup): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			$data = $this->repository->show($abilityGroup->id);
			return $this->respondWithData('AbilityGroup show', $data);

		}elseif($this->isManager(auth()->user()->roles)){

			$data = $this->repository->showByRoleManager(auth()->user()->employee->company_id, $abilityGroup->id);
			return $this->respondWithData('AbilityGroup show', $data);

		}else{

			$data = $this->repository->showByRoleUser(auth()->user()->employee->id, $abilityGroup->id);
			return $this->respondWithData('AbilityGroup show', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "SHARED", "AbilityGroups")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AbilityGroupController.php")

    # Contenido por defecto
    content = """<?php

namespace App\Http\Controllers\SHARED\AbilityGroups;

use App\\Http\\Controllers\\Controller;
use App\\Repositories\\AbilityGroups\\AbilityGroupRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Validator;

class AbilityGroupStoreController extends Controller
{

	private AbilityGroupRepository $repository;


	public function __construct()
	{
		$this->repository = new AbilityGroupRepository();
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
			$abilityGroup = $this->repository->setAbilityGroup($request->name);

			$data = $this->repository->store($abilityGroup);

			return $this->respondWithData('AbilityGroup created', $data);

		}else if($this->isManager(auth()->user()->roles)){

			// By Manager

			$validator = Validator::make($request->all(), [
				'name'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$abilityGroup = $this->repository->setAbilityGroup($request->name);

			$data = $this->repository->store($abilityGroup);

			return $this->respondWithData('AbilityGroup created', $data);

		}else{

			// By Role User

			$validator = Validator::make($request->all(), [
				'name'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$abilityGroup = $this->repository->setAbilityGroup($request->name);

			$data = $this->repository->store($abilityGroup);

			return $this->respondWithData('AbilityGroup created', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "SHARED", "AbilityGroups")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AbilityGroupController.php")

    # Contenido por defecto
    content = """<?php

namespace App\Http\Controllers\SHARED\AbilityGroups;

use App\\Http\\Controllers\\Controller;
use App\\Models\\AbilityGroups\\AbilityGroup;
use App\\Repositories\\AbilityGroups\\AbilityGroupRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Validator;

class AbilityGroupUpdateController extends Controller
{

	private AbilityGroupRepository $repository;


	public function __construct()
	{
		$this->repository = new AbilityGroupRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	* @bodyParam name string required
	*
	* @param Request $request
	* @param AbilityGroup $abilityGroup
	* @return JsonResponse
	*/
	public function __invoke(Request $request, AbilityGroup $abilityGroup): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){
			// By Admin

			$validator = Validator::make($request->all(), [
				'name'=>'required',
			]);

			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}

			$data = $this->repository->update($abilityGroup->id, $request->all());
			return $this->respondWithData('AbilityGroup updated', $data);

		}else{

			// By Role User

			$validator = Validator::make($request->all(), [
				'name'=>'required',
			]);

			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}

			if($abilityGroup->company_id == auth()->user()->employee->company_id){

				$data = $this->repository->update($abilityGroup->id, $request->all());

				return $this->respondWithData('AbilityGroup updated', $data);

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