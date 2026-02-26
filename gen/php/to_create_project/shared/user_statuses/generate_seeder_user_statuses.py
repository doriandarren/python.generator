import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_seeder_user_statuses(full_path):
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
    file_path = os.path.join(styles_path, "UserStatusSeeder.php")

    # Contenido por defecto
    content = """<?php

namespace Database\\Seeders;

use App\\Enums\\UserStatuses\\EnumUserStatus;
use App\\Models\\UserStatuses\\UserStatus;
use Illuminate\\Database\\Seeder;


class UserStatusSeeder extends Seeder
{

	/**
	* Run the database seeds.
	*
	* @return void
	*/
	public function run()
	{

        //Create UserStatus
        $userStatuses = [
            EnumUserStatus::STATUS_ACTIVE_NAME,
            EnumUserStatus::STATUS_INACTIVE_NAME,
        ];

        foreach ($userStatuses as $userStatus) {
            if (!UserStatus::where('name', $userStatus)->exists()) {

                UserStatus::factory()->create(['name' => $userStatus]);
            }
        }


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
