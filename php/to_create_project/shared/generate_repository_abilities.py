import os
from helpers.helper_print import print_message, GREEN, CYAN




def generate_repository_abilities(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Repositories", "Abilities")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AbilityRepository.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Repositories\\Abilities;

use App\\Enums\\EnumApiSetup;
use App\\Models\\Abilities\\Ability;



final class AbilityRepository
{
    /**
     * By Admin
     * @return mixed
     */
    public function list(): mixed
    {
        return Ability::latest()
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
        return Ability::where('company_id', $company_id)
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
        return Ability::where('employee_id', $employee_id)
            ->where('company_id', $company_id)
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
        return Ability::where('id', $id)->first();
    }

    /**
     * @param $company_id
     * @param $id
     * @return mixed
     */
    public function showByRoleManager($company_id, $id): mixed
    {
        return Ability::where('id', $id)
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
        return Ability::where('id', $id)
            ->where('employee_id', $employee_id)
            ->first();

    }

    /**
     * @param $data
     * @return Ability
     */
    public function store($data): Ability
    {
        $objNew = new Ability();
        $objNew->name = $data->name;
        $objNew->label = $data->label;
        $objNew->ability_group_id = $data->ability_group_id;
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
        $objOld = Ability::find($id);

        if(isset($obj->name)){
            if($obj->name != '' && !empty($obj->name)){
                $objOld->name = $obj->name;
            }
        }

        if(isset($obj->label)){
            if($obj->label != '' && !empty($obj->label)){
                $objOld->label = $obj->label;
            }
        }

        if(isset($obj->ability_group_id)){
            if($obj->ability_group_id != '' && !empty($obj->ability_group_id)){
                $objOld->ability_group_id = $obj->ability_group_id;
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
        $data = Ability::find($id);
        $data->delete();
        return true;
    }


    /**
     * Template
     * @param $name
     * @param $label
     * @param $ability_group_id
     * @return Ability
     */
    public function setAbility($name, $label, $ability_group_id): Ability
    {
        $obj = new Ability();
        $obj->name = $name;
        $obj->label = $label;
        $obj->ability_group_id = $ability_group_id;
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







