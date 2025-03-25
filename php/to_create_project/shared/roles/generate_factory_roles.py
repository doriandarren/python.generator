import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_factory_roles(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "database", "factories", "Roles")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleFactory.php")

    # Contenido por defecto
    content = """<?php

namespace Database\\Factories\\Roles;

use App\\Models\\Roles\\Role;
use Illuminate\\Database\\Eloquent\\Factories\\Factory;


/**
* @extends Factory<Role>
*/
class RoleFactory extends Factory
{

	/**
	* Define the model's default state.
	*
	* @return array<string, mixed>
	*/
	public function definition()
	{
		// php artisan make:factory RoleFactory

		return [
			'description' => $this->faker->word(),
		];

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
