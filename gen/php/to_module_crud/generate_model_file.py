import os


def create_model_structure(base_ruta, path_model):
    """
    Crea la estructura de carpetas 'base_ruta/app/path_model' en la ruta especificada.
    """
    # Crear la ruta completa base_ruta/app/path_model
    model_folder_path = os.path.join(base_ruta, 'app', path_model)

    if not os.path.exists(model_folder_path):
        os.makedirs(model_folder_path)
        print(f"Estructura de carpetas '{model_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{model_folder_path}' ya existe.")

    return model_folder_path


def generate_model_file(base_ruta, namespace, path_model, singular_name, plural_name, plural_name_snake):
    """
    Genera un archivo de modelo PHP basado en los nombres proporcionados y crea la estructura app/path_model dentro de base_ruta.
    El nombre del archivo será igual a 'singular_name'.
    """
    # Crear la estructura de carpetas llamando a create_model_structure
    model_folder_path = create_model_structure(base_ruta, path_model)

    # Nombre del archivo PHP será igual a singular_name
    file_name = f'{singular_name}.php'
    model_file_path = os.path.join(model_folder_path, file_name)

    # Contenido del archivo PHP del modelo adaptado
    model_content = f"""<?php

namespace App\\Models\\{namespace}\\{plural_name};

use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;

class {singular_name} extends Model
{{
    use HasFactory;
    // use SoftDeletes;

    protected $connection = '{namespace.lower()}';
    protected $table = '{plural_name_snake}';

    /***********************
    * RELATIONS
    ***********************/

    // TODO add relation tables
    // public function classrelacion()
    // {{
    //     return $this->hasMany(ClassRelacion::class, 'classrelacion_id', 'id');
    // }}
}}
"""

    # Crear el archivo PHP con el contenido del modelo
    try:
        with open(model_file_path, 'w') as model_file:
            model_file.write(model_content)
            print(f"Archivo PHP modelo '{file_name}' creado en: {model_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo PHP del modelo '{file_name}': {e}")
