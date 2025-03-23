import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_controller_ability(full_path):
    create_destroy(full_path)



def create_destroy(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "SHARED", "Abilities")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AbilityDestroyController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\SHARED\\Abilities;

use App\\Http\\Controllers\\Controller;
use App\\Models\\Abilities\\Ability;
use App\\Repositories\\Abilities\\AbilityRepository;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;

class AbilityDestroyController extends Controller
{

	private AbilityRepository $repository;


	public function __construct()
	{
		$this->repository = new AbilityRepository();
	}

	/**
	* @header Bearer BEARER_AUTH
	*
	*
	* @param Request $request
	* @param Ability $ability
	* @return JsonResponse
	*/
	public function __invoke(Request $request, Ability $ability): JsonResponse
	{

		if($this->isAdmin(auth()->user()->roles)){

			$data = $this->repository->destroy($ability->id);

			return $this->respondWithData('Ability deleted', $data);

		}else{

			if($ability->company_id == auth()->user()->employee->company_id){

				$data = $this->repository->destroy($ability->id);

				return $this->respondWithData('Ability deleted', $data);

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

