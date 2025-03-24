import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_model_roles(full_path):
    pass


def generate_repository_roles(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Repositories", "Roles")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleRepository.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Repositories\\Roles;

use App\\Enums\\EnumApiSetup;
use App\\Models\\Roles\\Role;


final class RoleRepository
{
    /**
     * By Admin
     * @return mixed
     */
    public function list(): mixed
    {
        return Role::latest()
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
        return Role::where('company_id', $company_id)
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
        return Role::where('employee_id', $employee_id)
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
        return Role::where('id', $id)->first();
    }

    /**
     * @param $company_id
     * @param $id
     * @return mixed
     */
    public function showByRoleManager($company_id, $id): mixed
    {
        return Role::where('id', $id)
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
        return Role::where('id', $id)
            ->where('employee_id', $employee_id)
            ->first();

    }

    /**
     * @param $data
     * @return Role
     */
    public function store($data): Role
    {
        $objNew = new Role();
        $objNew->name = $data->name;
        $objNew->description = $data->description;
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
        $objOld = Role::find($id);

        if(isset($obj->name)){
            if($obj->name != '' && !empty($obj->name)){
                $objOld->name = $obj->name;
            }
        }

        if(isset($obj->description)){
            if($obj->description != '' && !empty($obj->description)){
                $objOld->description = $obj->description;
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
        $data = Role::find($id);
        $data->delete();
        return true;
    }


    /**
     * Template
     * @param $name
     * @param $description
     * @return Role
     */
    public function setRole($name, $description): Role
    {
        $obj = new Role();
        $obj->name = $name;
        $obj->description = $description;
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






