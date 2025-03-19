import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command





def generate_by_command_line(full_path):

    print(f'Fillpa: {full_path}')

    create_project(full_path)





def create_project(full_path):
    # Verifica si el directorio ya existe
    if os.path.exists(full_path):
        print_message(f'El directorio {full_path} ya existe. Abortando.', GREEN)
        return

    # Comando para crear un nuevo proyecto Laravel
    command = f'composer create-project --prefer-dist laravel/laravel {full_path}'
    run_command(command)

    print_message(f'Proyecto Laravel creado en: {full_path}', GREEN)