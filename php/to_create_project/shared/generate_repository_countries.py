import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_model_countries(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Repositories", "Countries")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "CountryRepository.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Repositories\\Countries;

use App\\Enums\\EnumApiSetup;
use App\\Models\\Countries\\Country;


class CountryRepository
{

	/**
	* By Admin
	* @return mixed
	*/
	public function list(): mixed
	{
		return Country::latest()
					->limit(EnumApiSetup::QUERY_LIMIT)
					->get();
	}

	/**
	* By Manager
	* @param $company_id
	* @return mixed
	*/
	public function listByRoleManager($company_id): mixed
	{
		return Country::where('company_id', $company_id)
					->latest()
					->limit(EnumApiSetup::QUERY_LIMIT)
					->get();
	}

	/**
	* By User
	* @param $company_id
	* @param $employee_id
	* @return mixed
	*/
	public function listByRoleUser($company_id, $employee_id): mixed
	{
		return Country::where('employee_id', $employee_id)
					->where('company_id', $company_id)
					->latest()
					->limit(EnumApiSetup::QUERY_LIMIT)
					->get();
	}

	/**
	* By Driver
	* @param $company_id
	* @return mixed
	*/
	public function listByRoleDriver($company_id): mixed
	{
		return Country::where('company_id', $company_id)
					->latest()
					->limit(EnumApiSetup::QUERY_LIMIT)
					->get();
	}

	/**
	* @param $id
	* @return mixed
	*/
	public function show($id): mixed
	{
		return Country::where('id', $id)->first();
	}

	/**
	* @param $company_id
	* @param $id
	* @return mixed
	*/
	public function showByRoleManager($company_id, $id): mixed
	{
		return Country::where('id', $id)
					->where('company_id', $company_id)
					->first();

	}

	/**
	* @param $employee_id
	* @param $id
	* @return mixed
	*/
	public function showByRoleUser($employee_id, $id): mixed
	{
		return Country::where('id', $id)
					->where('employee_id', $employee_id)
					->first();

	}

	/**
	* @param $company_id
	* @param $id
	* @return mixed
	*/
	public function showByRoleDriver($company_id, $id): mixed
	{
		return Country::where('id', $id)
					->where('company_id', $company_id)
					->first();

	}

	/**
	* @param $data
	* @return Country
	*/
	public function store($data): Country
	{
		$objNew = new Country();
		$objNew->common_name = $data->common_name;
		$objNew->iso_name = $data->iso_name;
		$objNew->code_alpha_2 = $data->code_alpha_2;
		$objNew->code_alpha_3 = $data->code_alpha_3;
		$objNew->numerical_code = $data->numerical_code;
		$objNew->phone_code = $data->phone_code;
		$objNew->save();
		return $objNew;
	}

	/**
	* @param $id
	* @param $data
	* @return mixed
	*/
	public function update($id, $data): mixed
	{
		if(is_array($data)){
			$obj = json_decode(json_encode($data), FALSE);
		}else{
			$obj = $data;
		}
		$objOld = Country::find($id);

		if(isset($obj->common_name)){
			if($obj->common_name != '' && !empty($obj->common_name)){
				$objOld->common_name = $obj->common_name;
			}
		}

		if(isset($obj->iso_name)){
			if($obj->iso_name != '' && !empty($obj->iso_name)){
				$objOld->iso_name = $obj->iso_name;
			}
		}

		if(isset($obj->code_alpha_2)){
			if($obj->code_alpha_2 != '' && !empty($obj->code_alpha_2)){
				$objOld->code_alpha_2 = $obj->code_alpha_2;
			}
		}

		if(isset($obj->code_alpha_3)){
			if($obj->code_alpha_3 != '' && !empty($obj->code_alpha_3)){
				$objOld->code_alpha_3 = $obj->code_alpha_3;
			}
		}

		if(isset($obj->numerical_code)){
			if($obj->numerical_code != '' && !empty($obj->numerical_code)){
				$objOld->numerical_code = $obj->numerical_code;
			}
		}

		if(isset($obj->phone_code)){
			if($obj->phone_code != '' && !empty($obj->phone_code)){
				$objOld->phone_code = $obj->phone_code;
			}
		}

		$objOld->save();

		return $objOld;

	}

	/**	
	* @param $id
	* @return bool
	*/
	public function destroy($id): bool
	{
		$data = Country::find($id);
		$data->delete();
		return true;
	}


	/** 
	* Template
	 * @param $common_name
	 * @param $iso_name
	 * @param $code_alpha_2
	 * @param $code_alpha_3
	 * @param $numerical_code
	 * @param $phone_code
	 * @return Country
	 */
	public function setCountry($common_name, $iso_name, $code_alpha_2, $code_alpha_3, $numerical_code, $phone_code): Country
	{
		$obj = new Country();
		$obj->common_name = $common_name;
		$obj->iso_name = $iso_name;
		$obj->code_alpha_2 = $code_alpha_2;
		$obj->code_alpha_3 = $code_alpha_3;
		$obj->numerical_code = $numerical_code;
		$obj->phone_code = $phone_code;
		return $obj;
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




