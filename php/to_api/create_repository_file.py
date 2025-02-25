import os

def create_repository_structure(base_ruta, path_model):
    """
    Crea la estructura de carpetas 'base_ruta/app/path_model' en la ruta especificada.
    """
    # Crear la ruta completa base_ruta/app/path_model
    repository_folder_path = os.path.join(base_ruta, 'app', path_model)

    if not os.path.exists(repository_folder_path):
        os.makedirs(repository_folder_path)
        print(f"Estructura de carpetas '{repository_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{repository_folder_path}' ya existe.")

    return repository_folder_path


def generate_repository_file(base_ruta, path_model, singular_name, plural_name, singular_name_snake, plural_name_snake, columns):
    """
    Genera un archivo de repositorio PHP basado en los nombres proporcionados y crea la estructura app/path_model dentro de base_ruta.
    """
    # Crear la estructura de carpetas llamando a create_repository_structure
    repository_folder_path = create_repository_structure(base_ruta, path_model)

    # Nombre del archivo PHP será igual a singular_name
    file_name = f'{singular_name}Repository.php'
    repository_file_path = os.path.join(repository_folder_path, file_name)

    # Obtener los nombres de las columnas dinámicamente
    column_names = [column["name"] for column in columns]

    # Contenido del archivo PHP del repositorio adaptado
    repository_content = f"""<?php

namespace App\\Repositories\\{plural_name};

use App\\Enums\\EnumApiSetup;
use App\\Models\\{plural_name}\\{singular_name};

class {singular_name}Repository
{{
    const WITH = [];

    /**
    * List by Admin
    * @return mixed
    */
    public function list(): mixed
    {{
        return {singular_name}::latest()
                            ->limit(EnumApiSetup::QUERY_LIMIT)
                            ->get();
    }}
    
    
    /**
    * List by Manager
    * @return mixed
    */
    public function listByRoleManager(): mixed
    {{
        return {singular_name}::latest()
                            ->limit(EnumApiSetup::QUERY_LIMIT)
                            ->get();
    }}
    
    
    /**
    * List by User
    * @return mixed
    */
    public function listByRoleUser(): mixed
    {{
        return {singular_name}::latest()
                            ->limit(EnumApiSetup::QUERY_LIMIT)
                            ->get();
    }}


    /**
    * Show by Admin
	* @param $id
	* @return mixed
	*/
    public function show($id): mixed
    {{
        return {singular_name}::where('id', $id)
                            ->first();
    }}
    
    
    /**
    * Show by Manager
	* @param $id
	* @return mixed
	*/
    public function showByRoleManager($id): mixed
    {{
        return {singular_name}::where('id', $id)
                            ->first();
    }}
    
    
    /**
    * Show by User
	* @param $id
	* @return mixed
	*/
    public function showByRoleUser($id): mixed
    {{
        return {singular_name}::where('id', $id)
                            ->first();
    }}


    /**
    * Store
    * @param $data
    * @return {singular_name}
    */
    public function store($data): {singular_name}
    {{
        $objNew = new {singular_name}();
"""

    # Agregar las columnas dinámicamente en el método `store`
    for column in column_names:
        repository_content += f"        $objNew->{column} = $data->{column};\n"

    repository_content += f"""
        $objNew->save();
        return $objNew;
    }}
    

    /**
    * Update
    * @param $id
    * @param $data
    * @return {singular_name}
    */
    public function update($id, $data): mixed
    {{
    
        if(is_array($data)){{
			$obj = json_decode(json_encode($data), FALSE);
		}}else{{
			$obj = $data;
		}}
        
        $objOld = {singular_name}::where('id', $id)->first();

"""

    # Separar las columnas dinámicamente en el método `update`
    for column in column_names:
        repository_content += f"""        if (isset($obj->{column})) {{
            if ($obj->{column} != '' && !empty($obj->{column})) {{
                $objOld->{column} = $obj->{column};
            }}
        }}

"""
    repository_content += f"""
        $objOld->save();
        return $objOld;
    }}


    /**
    * Destroy
    * @param $id
    * @return bool
    */
    public function destroy($id): bool
    {{
        $obj = {singular_name}::find($id);
        $obj->delete();
        return true;
    }}


    /**
    * Set {singular_name}
"""

    # Agregar los `@param` dinámicos para cada columna
    for column in column_names:
        repository_content += f"    * @param ${column}\n"

    repository_content += f"""    * @return {singular_name}
    */
    public function set{singular_name}({', '.join([f'${column}' for column in column_names])}): {singular_name}
    {{
        $obj = new {singular_name}();
"""

    # Agregar las columnas dinámicamente en el método `set`
    for column in column_names:
        repository_content += f"        $obj->{column} = ${column};\n"

    repository_content += f"""
        return $obj;
    }}
}}
"""

    # Escribir el archivo PHP con el contenido del repositorio
    try:
        with open(repository_file_path, 'w') as repository_file:
            repository_file.write(repository_content)
            print(f"Archivo PHP repositorio '{file_name}' creado en: {repository_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo PHP del repositorio '{file_name}': {e}")
