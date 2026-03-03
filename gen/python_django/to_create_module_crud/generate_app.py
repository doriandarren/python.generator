import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command, run_command_debug


def generate_app(full_path,plural_name_snake,venv_python,manage_py_path):
    install_app(full_path, plural_name_snake, manage_py_path, venv_python)


def install_app(full_path, plural_name_snake, manage_py_path, venv_python):
    print_message("Instalando app...", CYAN)
    run_command_debug(f'"{venv_python}" manage.py startapp {plural_name_snake} apps/{plural_name_snake}', cwd=full_path)
    print_message("App instalada correctamente.", GREEN)
    
    