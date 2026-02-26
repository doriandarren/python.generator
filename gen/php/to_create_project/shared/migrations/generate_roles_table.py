import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_roles_table(full_path):
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
    file_path = os.path.join(styles_path, "0002_02_02_000002_create_roles_table.php")

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

        if (!Schema::hasTable("roles")) {
            Schema::create('roles', function (Blueprint $table) {
                $table->bigIncrements('id');
                $table->string('name');
                $table->string('description')->nullable();
                $table->timestamps();
                $table->softDeletes();
            });
        }



        if (!Schema::hasTable("abilities")) {
            Schema::create('abilities', function (Blueprint $table) {
                $table->bigIncrements('id');
                $table->string('name')->unique();
                $table->string('label')->nullable();

                $table->unsignedBigInteger('ability_group_id')->unsigned();

                $table->foreign('ability_group_id')
                    ->references('id')
                    ->on('ability_groups')
                    ->onDelete('cascade');

                $table->timestamps();
                $table->softDeletes();

            });
        }


        if (!Schema::hasTable("ability_user")) {
            Schema::create('ability_user', function (Blueprint $table) {
                //$table->primary(['id', 'user_id', 'ability_id']);
                $table->bigIncrements('id');
                $table->unsignedBigInteger('user_id')->unsigned();
                $table->unsignedBigInteger('ability_id')->unsigned();
                $table->timestamps();
                $table->softDeletes();

                $table->foreign('user_id')
                    ->references('id')
                    ->on('users')
                    ->onDelete('cascade');

                $table->foreign('ability_id')
                    ->references('id')
                    ->on('abilities')
                    ->onDelete('cascade');

            });
        }


        if (!Schema::hasTable("role_user")) {
            Schema::create('role_user', function (Blueprint $table) {
                //$table->primary(['id', 'user_id', 'role_id']);
                $table->bigIncrements('id');
                $table->unsignedBigInteger('role_id')->unsigned();
                $table->unsignedBigInteger('user_id')->unsigned();
                $table->timestamps();
                $table->softDeletes();

                $table->foreign('user_id')
                    ->references('id')
                    ->on('users')
                    ->onDelete('cascade');

                $table->foreign('role_id')
                    ->references('id')
                    ->on('roles')
                    ->onDelete('cascade');
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

        if (Schema::hasColumn('role_user', 'role_id')) {
            Schema::table('role_user', function (Blueprint $table) {
                $table->dropForeign(['role_id']);
                $table->dropColumn('role_id');
            });
        }

        if (Schema::hasColumn('role_user', 'user_id')) {
            Schema::table('role_user', function (Blueprint $table) {
                $table->dropForeign(['user_id']);
                $table->dropColumn('user_id');
            });
        }



        if (Schema::hasColumn('ability_user', 'ability_id')) {
            Schema::table('ability_user', function (Blueprint $table) {
                $table->dropForeign(['ability_id']);
                $table->dropColumn('ability_id');
            });
        }


        if (Schema::hasColumn('abilities', 'ability_group_id')) {
            Schema::table('abilities', function (Blueprint $table) {
                $table->dropForeign(['ability_group_id']);
                $table->dropColumn('ability_group_id');
            });
        }


        if (Schema::hasColumn('ability_user', 'user_id')) {
            Schema::table('ability_user', function (Blueprint $table) {
                $table->dropForeign(['user_id']);
                $table->dropColumn('user_id');
            });
        }



        Schema::dropIfExists('ability_user');
        Schema::dropIfExists('role_user');
        Schema::dropIfExists('abilities');
        Schema::dropIfExists('roles');

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
