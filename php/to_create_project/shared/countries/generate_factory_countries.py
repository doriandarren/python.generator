import os
from helpers.helper_print import print_message, GREEN, CYAN





def generate_factory_countries(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "database", "factories", "Countries")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "CountryFactory.php")

    # Contenido por defecto
    content = """<?php

namespace Database\\Factories\\Countries;

use App\\Models\\Countries\\Country;
use Illuminate\\Database\\Eloquent\\Factories\\Factory;

/**
* @extends Factory<Country>
*/
class CountryFactory extends Factory
{

	/**
	* Define the model's default state.
	*
	* @return array<string, mixed>
	*/
	public function definition()
	{
		// php artisan make:factory CountryFactory

		return [
			'common_name' => $this->faker->word(),
			'iso_name' => $this->faker->word(),
			'code_alpha_2' => $this->faker->word(),
			'code_alpha_3' => $this->faker->word(),
			'numerical_code' => $this->faker->word(),
			'phone_code' => $this->faker->word(),
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
