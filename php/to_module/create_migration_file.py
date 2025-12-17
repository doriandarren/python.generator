import os
from datetime import datetime
from php.to_module.helpers.helper_migrate_php import php_column_line
from .string_helpers import get_plural



def create_migration_structure(base_ruta, path_migration):
    """
    Crea la estructura de carpetas 'base_ruta/settings/migrations/' en la ruta especificada.
    """
    migration_folder_path = os.path.join(base_ruta, path_migration)

    if not os.path.exists(migration_folder_path):
        os.makedirs(migration_folder_path)
        print(f"Estructura de carpetas '{migration_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{migration_folder_path}' ya existe.")

    return migration_folder_path


def generate_migration_file(
    base_ruta,
    namespace,
    path_migration,
    singular_name,
    plural_name,
    singular_name_kebab,
    plural_name_kebab,
    singular_name_snake,
    plural_name_snake,
    columns
):
    """
    Genera un archivo de migración PHP basado en los nombres proporcionados
    y crea la estructura dentro de base_ruta.
    """

    migration_folder_path = create_migration_structure(base_ruta, path_migration)

    current_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    file_name = f'{current_time}_create_{plural_name_snake}_table.php'
    migration_file_path = os.path.join(migration_folder_path, file_name)

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
        if (!Schema::connection('{namespace.lower()}')->hasTable('{plural_name_snake}')) {{

            Schema::connection('{namespace.lower()}')->create('{plural_name_snake}', function (Blueprint $table) {{

                $table->id();
"""

    # ================== UP: columnas ==================
    for column in columns:
        name = column["name"]
        is_fk = column.get("is_fk") or column.get("type") == "fk"

        if is_fk:
            table_name = column.get("related_table")
            if not table_name:
                table_name = get_plural(name.replace("_id", ""))

            migration_content += php_column_line(column)
            migration_content += (
                f"                $table->foreign('{name}')"
                f"->references('id')->on('{table_name}')->onDelete('cascade');\n"
            )
        else:
            migration_content += php_column_line(column)

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

    # ================== DOWN: eliminar FKs ==================
    for column in columns:
        name = column["name"]
        is_fk = column.get("is_fk") or column.get("type") == "fk"

        if is_fk:
            migration_content += f"""        if (Schema::connection('{namespace.lower()}')->hasColumn('{plural_name_snake}', '{name}')) {{
            Schema::connection('{namespace.lower()}')->table('{plural_name_snake}', function (Blueprint $table) {{
                $table->dropForeign(['{name}']);
                $table->dropColumn('{name}');
            }});
        }}
"""

    migration_content += f"""        Schema::connection('{namespace.lower()}')->dropIfExists('{plural_name_snake}');
    }}
}};
"""

    try:
        with open(migration_file_path, 'w') as migration_file:
            migration_file.write(migration_content)
            print(f"Archivo de migración PHP '{file_name}' creado en: {migration_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo de migración PHP '{file_name}': {e}")
