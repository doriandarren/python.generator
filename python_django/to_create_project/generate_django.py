import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command

def generate_django(full_path, project_name_format, app_name, venv_python):
    """
    Genera el archivo
    """
    install_dependencies(full_path, venv_python)
    
    create_django_project(full_path, app_name, venv_python)
    create_migrate(full_path, venv_python)
    
    # TODO falta configuracion de django
    
    
    

    
def install_dependencies(full_path, venv_python):
    print_message("Instalando dependencias en el venv...", CYAN)
    run_command(f'"{venv_python}" -m pip install django', cwd=full_path)
    print_message("Dependencias instaladas correctamente.", GREEN)




def create_django_project(full_path, app_name, venv_python):
    print_message("Creando proyecto Django...", CYAN)

    # Esto crea el proyecto dentro del directorio actual
    run_command(f'"{venv_python}" -m django startproject {app_name} .', cwd=full_path)

    print_message("Proyecto Django creado correctamente.", GREEN)



def create_migrate(full_path, venv_python):
    print_message("Generando requirements.txt...", CYAN)
    run_command(f'"{venv_python}" manage.py migrate', cwd=full_path)
    print_message("requirements.txt generado correctamente.", GREEN)



