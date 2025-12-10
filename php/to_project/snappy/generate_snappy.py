import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command




def generate_snappy(full_path):
    install_snappy(full_path)
    install_publish(full_path)



def install_snappy(full_path):
    print_message("Instalando Snappy...", CYAN)
    run_command("composer require barryvdh/laravel-snappy", cwd=full_path)
    print_message("Snappy instalado correctamente.", GREEN)



def install_publish(full_path):
    print_message("Publicando Snappy...", CYAN)
    run_command("php artisan vendor:publish --provider='Barryvdh\Snappy\ServiceProvider'", cwd=full_path)
    print_message("Snappy publicado correctamente.", GREEN)


