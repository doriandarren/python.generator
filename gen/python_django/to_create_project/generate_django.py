import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command
from gen.python_django.helpers.helper_file import helper_update_list

def generate_django(full_path, project_name_format, app_name, venv_python):
    """
    Genera el archivo
    """
    install_django(full_path, venv_python)
    install_requests(full_path, venv_python)
    install_django_rest_framework(full_path, venv_python)
    create_django_project(full_path, app_name, venv_python)
    update_settings(full_path, app_name)
    


    
def install_django(full_path, venv_python):
    print_message("Instalando django...", CYAN)
    run_command(f'"{venv_python}" -m pip install django', cwd=full_path)
    print_message("django instalado correctamente.", GREEN)
    
    
def install_requests(full_path, venv_python):
    print_message("Instalando requests...", CYAN)
    run_command(f'"{venv_python}" -m pip install requests', cwd=full_path)
    print_message("requests instalado correctamente.", GREEN)



def install_django_rest_framework(full_path, venv_python):
    print_message("Instalando djangorestframework...", CYAN)
    run_command(f'"{venv_python}" -m pip install djangorestframework', cwd=full_path)
    print_message("djangorestframework instalado correctamente.", GREEN)




def create_django_project(full_path, app_name, venv_python):
    print_message("Creando proyecto Django...", CYAN)

    # Esto crea el proyecto dentro del directorio actual
    run_command(f'"{venv_python}" -m django startproject {app_name} .', cwd=full_path)

    print_message("Proyecto Django creado correctamente.", GREEN)



def update_settings(full_path, app_name):
    
    helper_update_list(
        full_path, 
        f"{app_name}/settings.py", 
        "INSTALLED_APPS", 
        f"'rest_framework',                   # required for DRF"
    )
    

