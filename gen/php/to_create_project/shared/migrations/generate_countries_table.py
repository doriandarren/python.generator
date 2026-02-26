import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_countries_table(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "database", "migrations")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "0002_02_02_000003_create_countries_table.php")

    # Contenido por defecto
    content = """<?php

use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;


return new class extends Migration
{
	/**
	* Run the migrations.
	*
	* @return void
	*/
	public function up()
	 {
		// common_name iso_name code_alpha_2 code_alpha_3 numerical_code phone_code
		if (!Schema::connection('api')->hasTable('countries')) {

			Schema::connection('api')->create('countries', function (Blueprint $table) {

				$table->id();
				$table->string('common_name')->nullable();
				$table->string('iso_name')->nullable();
				$table->string('code_alpha_2')->nullable();
				$table->string('code_alpha_3')->nullable();
				$table->string('numerical_code')->nullable();
				$table->string('phone_code')->nullable();
				$table->timestamps();
				$table->softDeletes();
			});
		}
	}

	/**
	* Reverse the migrations.
	*
	* @return void
	*/
	public function down()
	{
		Schema::connection('api')->dropIfExists('countries');		
	}

};
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
