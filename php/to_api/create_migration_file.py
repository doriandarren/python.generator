import os
from datetime import datetime

from .string_helpers import get_plural  # Importar el helper de pluralización

def create_migration_structure(base_ruta, path_migration):
    """
    Crea la estructura de carpetas 'base_ruta/database/migrations/' en la ruta especificada.
    """
    migration_folder_path = os.path.join(base_ruta, path_migration)

    if not os.path.exists(migration_folder_path):
        os.makedirs(migration_folder_path)
        print(f"Estructura de carpetas '{migration_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{migration_folder_path}' ya existe.")

    return migration_folder_path


def generate_migration_file(base_ruta, namespace, path_migration, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns):
    """
    Genera un archivo de migración PHP basado en los nombres proporcionados y crea la estructura database/migrations/ dentro de base_ruta.
    """
    # Crear la estructura de carpetas llamando a create_migration_structure
    migration_folder_path = create_migration_structure(base_ruta, path_migration)

    # Obtener la fecha y hora actual en el formato deseado: año_mes_dia_hora_min_seg
    current_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

    # Nombre del archivo PHP será año_mes_dia_hora_min_seg_create_invoice_headers_table.php
    file_name = f'{current_time}_create_{singular_name_snake}_table.php'
    migration_file_path = os.path.join(migration_folder_path, file_name)

    # Contenido del archivo PHP de la migración adaptado
    migration_content = f"""<?php

use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;

return new class extends Migration
{{
    /**
    * Run the migrations.
    *
    * @return void
    */
    public function up()
    {{
        if (!Schema::connection('api')->hasTable('{plural_name_snake}')) {{

            Schema::connection('api')->create('{plural_name_snake}', function (Blueprint $table) {{

                $table->id();
"""

    # Agregar las columnas dinámicamente en el método `up`
    for column in columns:
        if "_id" in column["name"]:
            # Si es una clave foránea, usar el helper para obtener el plural del nombre de la tabla
            table_name = get_plural(column["name"].replace("_id", ""))  # Obtener el plural de la tabla sin el _id
            migration_content += f"""                $table->unsignedBigInteger('{column['name']}');
                $table->foreign('{column['name']}')->references('id')->on('{table_name}')->onDelete('cascade');
"""
        else:
            # Si es una columna normal
            migration_content += f"                $table->string('{column['name']}')->nullable();\n"

    # Agregar las líneas $table->timestamps() y $table->softDeletes() después de las columnas
    migration_content += f"""
                $table->timestamps();
                $table->softDeletes();
            }});
        }}
    }}

    /**
    * Reverse the migrations.
    *
    * @return void
    */
    public function down()
    {{
"""

    # Agregar las claves foráneas a eliminar en el método `down`
    for column in columns:
        if "_id" in column["name"]:
            migration_content += f"""        if (Schema::connection('api')->hasColumn('{plural_name_snake}', '{column['name']}')) {{
            Schema::connection('api')->table('{plural_name_snake}', function (Blueprint $table) {{
                $table->dropForeign(['{column['name']}']);
                $table->dropColumn('{column['name']}');
            }});
        }}
"""

    # Completar el método `down` con la eliminación de la tabla
    migration_content += f"""        Schema::connection('api')->dropIfExists('{plural_name_snake}');
    }}
}};
"""

    # Escribir el archivo PHP con el contenido de la migración
    try:
        with open(migration_file_path, 'w') as migration_file:
            migration_file.write(migration_content)
            print(f"Archivo de migración PHP '{file_name}' creado en: {migration_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo de migración PHP '{file_name}': {e}")
