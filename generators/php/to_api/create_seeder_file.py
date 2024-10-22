import os

def create_seeder_structure(base_ruta, path_seeder):
    """
    Crea la estructura de carpetas 'base_ruta/database/migrations/sedeers' en la ruta especificada.
    """
    # Crear la ruta completa base_ruta/database/migrations/sedeers
    seeder_folder_path = os.path.join(base_ruta, path_seeder)

    if not os.path.exists(seeder_folder_path):
        os.makedirs(seeder_folder_path)
        print(f"Estructura de carpetas '{seeder_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{seeder_folder_path}' ya existe.")

    return seeder_folder_path


def generate_seeder_file(base_ruta, path_seeder, singular_name, plural_name, singular_name_snake, plural_name_snake, columns):
    """
    Genera un archivo de seeder PHP basado en los nombres proporcionados y crea la estructura database/migrations/sedeers dentro de base_ruta.
    """
    # Crear la estructura de carpetas llamando a create_seeder_structure
    seeder_folder_path = create_seeder_structure(base_ruta, path_seeder)

    # Nombre del archivo PHP será igual a singular_nameSeeder
    file_name = f'{singular_name}Seeder.php'
    seeder_file_path = os.path.join(seeder_folder_path, file_name)

    # Obtener los nombres de las columnas dinámicamente
    column_names = [column["name"] for column in columns]

    # Contenido del archivo PHP del seeder adaptado
    seeder_content = f"""<?php

namespace Database\\Seeders;

use Illuminate\\Database\\Seeder;
use App\\Models\\{plural_name}\\{singular_name};

class {singular_name}Seeder extends Seeder
{{
    /**
    * Run the database seeds.
    *
    * @return void
    */
    public function run()
    {{
        // php artisan make:seeder {singular_name}Seeder

        {singular_name}::factory()->create([
"""

    # Agregar las columnas dinámicamente en el método `run`
    for column in column_names:
        seeder_content += f"            '{column}' => '{column}',\n"

    seeder_content += f"""        ]);
    }}
}}
"""

    # Escribir el archivo PHP con el contenido del seeder
    try:
        with open(seeder_file_path, 'w') as seeder_file:
            seeder_file.write(seeder_content)
            print(f"Archivo PHP seeder '{file_name}' creado en: {seeder_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo PHP del seeder '{file_name}': {e}")
