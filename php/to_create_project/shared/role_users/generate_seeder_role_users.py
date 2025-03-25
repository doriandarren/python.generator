import os
from helpers.helper_print import print_message, GREEN, CYAN





def generate_seeder_role_users(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "database", "seeders")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "RoleUserSeeder.php")

    # Contenido por defecto
    content = """<?php

namespace Database\\Seeders;

use App\\Models\\RoleUsers\\RoleUser;
use Illuminate\\Database\\Seeder;


class RoleUserSeeder extends Seeder
{

	/**
	* Run the database seeds.
	*
	* @return void
	*/
	public function run()
	{
		// php artisan make:seeder RoleUserSeeder

		RoleUser::factory()->create([
			'user_id' => 'user_id',
			'role_id' => 'role_id',
		]);

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
