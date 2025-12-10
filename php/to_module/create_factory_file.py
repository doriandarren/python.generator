import os

def create_factory_structure(base_ruta, path_factory, plural_name):
    """
    Crea la estructura de carpetas 'base_ruta/settings/factories/plural_name' en la ruta especificada.
    """
    # Crear la ruta completa base_ruta/settings/factories/plural_name
    factory_folder_path = os.path.join(base_ruta, path_factory, plural_name)

    if not os.path.exists(factory_folder_path):
        os.makedirs(factory_folder_path)
        print(f"Estructura de carpetas '{factory_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{factory_folder_path}' ya existe.")

    return factory_folder_path


def generate_factory_file(base_ruta, path_factory, singular_name, plural_name, singular_name_snake, plural_name_snake, columns):
    """
    Genera un archivo de Factory PHP basado en los nombres proporcionados y crea la estructura settings/factories/plural_name dentro de base_ruta.
    """
    # Crear la estructura de carpetas llamando a create_factory_structure
    factory_folder_path = create_factory_structure(base_ruta, path_factory, plural_name)

    # Nombre del archivo PHP será igual a singular_nameFactory
    file_name = f'{singular_name}Factory.php'
    factory_file_path = os.path.join(factory_folder_path, file_name)

    # Obtener los nombres de las columnas dinámicamente
    column_names = [column["name"] for column in columns]

    # Contenido del archivo PHP del Factory adaptado
    factory_content = f"""<?php

namespace Database\\Factories\\{plural_name};

use Illuminate\\Database\\Eloquent\\Factories\\Factory;

/**
* @extends \\Illuminate\\Database\\Eloquent\\Factories\\Factory<\\App\\Models\\{plural_name}\\{singular_name}>
*/
class {singular_name}Factory extends Factory
{{
    /**
    * Define the model's default state.
    *
    * @return array<string, mixed>
    */
    public function definition()
    {{
        // php artisan make:factory {singular_name}Factory

        return [
"""

    # Agregar las columnas dinámicamente en el método `definition`
    for column in column_names:
        factory_content += f"            '{column}' => $this->faker->word(),\n"

    factory_content += f"""        ];

    }}
}}
"""

    # Escribir el archivo PHP con el contenido del Factory
    try:
        with open(factory_file_path, 'w') as factory_file:
            factory_file.write(factory_content)
            print(f"Archivo PHP Factory '{file_name}' creado en: {factory_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo PHP del Factory '{file_name}': {e}")
