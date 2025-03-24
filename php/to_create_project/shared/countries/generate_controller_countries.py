import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_controller_countries(full_path):
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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "Countries")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "CountryDestroyController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\Countries;

use App\\Models\\Countries\\Country;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use App\\Http\\Controllers\\Controller;
use App\\Repositories\\Countries\\CountryRepository;

class CountryDestroyController extends Controller
{

	private CountryRepository $repository;


	public function __construct()
	{
		$this->repository = new CountryRepository();
	}

	/**
	* @header Authorization Bearer TOKEN 
	* @urlParam id required The ID of the table.
	*
	*
	* @param Request $request
	* @param Country $country
	* @return JsonResponse
	*/
	public function __invoke(Request $request, Country $country): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			$data = $this->repository->destroy($country->id);

			return $this->respondWithData('Country deleted', $data);

		}else{

			if($country->company_id == auth()->user()->employee->company_id){

				$data = $this->repository->destroy($country->id);

				return $this->respondWithData('Country deleted', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "Countries")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "CountryListController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\Countries;

use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use App\\Http\\Controllers\\Controller;
use App\\Repositories\\Countries\\CountryRepository;

class CountryListController extends Controller
{

	private CountryRepository $repository;


	public function __construct()
	{
		$this->repository = new CountryRepository();
	}

	/**
	* @header Authorization Bearer TOKEN 
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
		return $this->respondWithData('Countries list', $data);
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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "Countries")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "CountryShowController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\Countries;

namespace App\\Http\\Controllers\\SHARED\\Countries;

use App\\Models\\Countries\\Country;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use App\\Http\\Controllers\\Controller;
use App\\Repositories\\Countries\\CountryRepository;

class CountryShowController extends Controller
{

	private CountryRepository $repository;


	public function __construct()
	{
		$this->repository = new CountryRepository();
	}

	/**
	* @header Authorization Bearer TOKEN 
	* @urlParam id required The ID of the table.
	*
	* @param Country $country
	* @return JsonResponse
	*/
	public function __invoke(Country $country): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			$data = $this->repository->show($country->id);
			return $this->respondWithData('Country show', $data);

		}elseif($this->isManager(auth()->user()->roles)){

			$data = $this->repository->showByRoleManager(auth()->user()->employee->company_id, $country->id);
			return $this->respondWithData('Country show', $data);

		}else{

			$data = $this->repository->showByRoleUser(auth()->user()->employee->id, $country->id);
			return $this->respondWithData('Country show', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "Countries")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "CountryStoreController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\Countries;

use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use App\\Http\\Controllers\\Controller;
use Illuminate\\Support\\Facades\\Validator;
use Illuminate\\Validation\\Rule;
use App\\Repositories\\Countries\\CountryRepository;

class CountryStoreController extends Controller
{

	private CountryRepository $repository;


	public function __construct()
	{
		$this->repository = new CountryRepository();
	}

	/**
	* @header Authorization Bearer TOKEN 
	*
	* @bodyParam common_name string required
	* @bodyParam iso_name string required
	* @bodyParam code_alpha_2 string required
	* @bodyParam code_alpha_3 string required
	* @bodyParam numerical_code string required
	* @bodyParam phone_code string required
	*
	* @param Request $request
	* @return JsonResponse
	*/
	public function __invoke(Request $request): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			// By Admin

			$validator = Validator::make($request->all(), [
				'common_name'=>'required',
				'iso_name'=>'required',
				'code_alpha_2'=>'required',
				'code_alpha_3'=>'required',
				'numerical_code'=>'required',
				'phone_code'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$country = $this->repository->setCountry($request->common_name, $request->iso_name, $request->code_alpha_2, $request->code_alpha_3, $request->numerical_code, $request->phone_code);

			$data = $this->repository->store($country);

			return $this->respondWithData('Country created', $data);

		}else if($this->isManager(auth()->user()->roles)){

			// By Manager

			$validator = Validator::make($request->all(), [
				'common_name'=>'required',
				'iso_name'=>'required',
				'code_alpha_2'=>'required',
				'code_alpha_3'=>'required',
				'numerical_code'=>'required',
				'phone_code'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$country = $this->repository->setCountry($request->common_name, $request->iso_name, $request->code_alpha_2, $request->code_alpha_3, $request->numerical_code, $request->phone_code);

			$data = $this->repository->store($country);

			return $this->respondWithData('Country created', $data);

		}else{

			// By Role User

			$validator = Validator::make($request->all(), [
				'common_name'=>'required',
				'iso_name'=>'required',
				'code_alpha_2'=>'required',
				'code_alpha_3'=>'required',
				'numerical_code'=>'required',
				'phone_code'=>'required',
			]);
			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}
			$country = $this->repository->setCountry($request->common_name, $request->iso_name, $request->code_alpha_2, $request->code_alpha_3, $request->numerical_code, $request->phone_code);

			$data = $this->repository->store($country);

			return $this->respondWithData('Country created', $data);

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
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "SHARED", "Countries")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "CountryUpdateController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\Countries;

use App\\Models\\Countries\\Country;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use App\\Http\\Controllers\\Controller;
use Illuminate\\Support\\Facades\\Validator;
use Illuminate\\Validation\\Rule;
use App\\Repositories\\Countries\\CountryRepository;

class CountryUpdateController extends Controller
{

	private CountryRepository $repository;


	public function __construct()
	{
		$this->repository = new CountryRepository();
	}

	/**
	* @header Authorization Bearer TOKEN 
	* @urlParam id required The ID of the table.
	*
	* @bodyParam common_name string required
	* @bodyParam iso_name string required
	* @bodyParam code_alpha_2 string required
	* @bodyParam code_alpha_3 string required
	* @bodyParam numerical_code string required
	* @bodyParam phone_code string required
	*
	* @param Request $request
	* @param Country $country
	* @return JsonResponse
	*/
	public function __invoke(Request $request, Country $country): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){
			// By Admin

			$validator = Validator::make($request->all(), [
				'common_name'=>'required',
				'iso_name'=>'required',
				'code_alpha_2'=>'required',
				'code_alpha_3'=>'required',
				'numerical_code'=>'required',
				'phone_code'=>'required',
			]);

			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}

			$data = $this->repository->update($country->id, $request->all());
			return $this->respondWithData('Country updated', $data);

		}else{

			// By Role User

			$validator = Validator::make($request->all(), [
				'common_name'=>'required',
				'iso_name'=>'required',
				'code_alpha_2'=>'required',
				'code_alpha_3'=>'required',
				'numerical_code'=>'required',
				'phone_code'=>'required',
			]);

			if($validator->fails()){
				return $this->respondWithError('Error', $validator->errors());
			}

			if($country->company_id == auth()->user()->employee->company_id){

				$data = $this->repository->update($country->id, $request->all());

				return $this->respondWithData('Country updated', $data);

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




