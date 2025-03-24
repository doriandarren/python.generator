import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command



def generate_by_command_line(full_path):
    create_project(full_path)
    create_console(full_path)
    create_route_service_provider(full_path)



def create_project(full_path):
    # Verifica si el directorio ya existe
    if os.path.exists(full_path):
        print_message(f'El directorio {full_path} ya existe. Abortando.', GREEN)
        return

    # Comando para crear un nuevo proyecto Laravel
    command = f'composer create-project --prefer-dist laravel/laravel {full_path}'
    run_command(command)
    print_message(f'Proyecto Laravel creado en: {full_path}', GREEN)




def create_console(full_path):
    print_message("Instalando TestCommand...", CYAN)
    run_command("php artisan make:command TestCommand", cwd=full_path)
    print_message("TestCommand instalado correctamente.", GREEN)



def create_route_service_provider(full_path):
    print_message("Instalando RouteServiceProvider...", CYAN)
    run_command("php artisan make:provider RouteServiceProvider", cwd=full_path)
    print_message("RouteServiceProvider instalado correctamente.", GREEN)