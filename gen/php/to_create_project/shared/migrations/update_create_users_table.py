import os
from gen.helpers.helper_print import print_message, GREEN, CYAN


def update_create_users_table(full_path):
    """
    Actualiza el archivo
    """
    main_jsx_path = os.path.join(full_path, "database", "migrations", "0001_01_01_000000_create_users_table.php")

    # Verificar si el archivo existe
    if not os.path.exists(main_jsx_path):
        print_message(f"Error: {main_jsx_path} no existe.", CYAN)
        return

    try:

        # Leer el contenido del archivo
        with open(main_jsx_path, "r") as f:
            content = f.read()


        # Reemplazos
        content = content.replace(
            """Schema::create('users', function (Blueprint $table) {""",
            """Schema::create('user_statuses', function (Blueprint $table) {
            $table->id();
            $table->string('name')->unique();
            $table->timestamps();
            $table->softDeletes();
        });
        
        Schema::create('users', function (Blueprint $table) {"""
        )

        # Reemplazos
        content = content.replace(
            """Schema::create('users', function (Blueprint $table) {
            $table->id();""",
            """Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('user_status_id');
            $table->foreign('user_status_id')->references('id')->on('user_statuses')->onDelete("cascade");"""
        )

        # Reemplazos
        content = content.replace(
            """$table->string('password');""",
            """$table->string('password');
            $table->string('image_url')->nullable();"""
        )


        # Reemplazos
        content = content.replace(
            """Schema::dropIfExists('users');""",
            """Schema::dropIfExists('user_statuses');
        Schema::dropIfExists('users');"""
        )

        # Escribir el contenido actualizado
        with open(main_jsx_path, "w") as f:
            f.write(content)

        print_message("0001_01_01_000000_create_users_table.php Actulizado correctamente.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {main_jsx_path}: {e}", CYAN)



