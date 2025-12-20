import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command



def generate_maatwebsite_excel(full_path):
    install_excel(full_path)
    install_publish(full_path)



def install_excel(full_path):
    print_message("Instalando Excel...", CYAN)
    run_command("composer require maatwebsite/excel", cwd=full_path)
    print_message("Excel instalado correctamente.", GREEN)


def install_publish(full_path):
    print_message("Publicando Excel...", CYAN)
    run_command("php artisan vendor:publish --provider=\"Maatwebsite\Excel\ExcelServiceProvider\"", cwd=full_path)
    print_message("Excel publicado correctamente.", GREEN)
