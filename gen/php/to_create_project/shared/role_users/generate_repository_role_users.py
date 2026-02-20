import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_repository_role_users(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Repositories", "RoleUsers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleUserRepository.php")

    # Contenido por defecto
    content = r"""<?php

namespace App\Repositories\RoleUsers;

use App\Enums\EnumApiSetup;
use App\Models\RoleUsers\RoleUser;


final class RoleUserRepository
{
    /**
     * By Admin
     * @return mixed
     */
    public function list(): mixed
    {
        return RoleUser::latest()
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
        return RoleUser::where('company_id', $company_id)
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
        return RoleUser::where('employee_id', $employee_id)
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
        return RoleUser::where('id', $id)->first();
    }

    /**
     * @param $company_id
     * @param $id
     * @return mixed
     */
    public function showByRoleManager($company_id, $id): mixed
    {
        return RoleUser::where('id', $id)
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
        return RoleUser::where('id', $id)
            ->where('employee_id', $employee_id)
            ->first();

    }

    /**
     * @param $data
     * @return RoleUser
     */
    public function store($data): RoleUser
    {
        $objNew = new RoleUser();
        $objNew->role_id = $data->role_id;
        $objNew->user_id = $data->user_id;
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
        $objOld = RoleUser::find($id);

        if(isset($obj->role_id)){
            if($obj->role_id != '' && !empty($obj->role_id)){
                $objOld->role_id = $obj->role_id;
            }
        }

        if(isset($obj->user_id)){
            if($obj->user_id != '' && !empty($obj->user_id)){
                $objOld->user_id = $obj->user_id;
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
        $data = RoleUser::find($id);
        $data->delete();
        return true;
    }


    /**
     * Template
     * @param $role_id
     * @param $user_id
     * @return RoleUser
     */
    public function setRoleUser($role_id, $user_id): RoleUser
    {
        $obj = new RoleUser();
        $obj->role_id = $role_id;
        $obj->user_id = $user_id;
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




