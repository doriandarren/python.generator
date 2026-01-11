import os
import platform
from helpers.helper_print import print_message, GREEN, CYAN, run_command
from python_django.helpers.helper_file_block import replace_block_in_file
from python_django.helpers.helper_virtual_env import get_venv_python


def generate_by_command_line(full_path, project_name_format, app_name):
    create_folder(full_path)

    # Crear entorno virtual
    create_virtualenv(full_path)
    venv_python = get_venv_python(full_path)
    update_pip(full_path, venv_python)
    
    
    
    replace_settings(full_path, project_name_format, app_name)

    
    # requirements.txt
    ## create_requirements(full_path, venv_python)


def create_folder(full_path):
    os.makedirs(full_path, exist_ok=True)


def create_virtualenv(full_path):
    print_message("Creando entorno virtual (.venv)...", CYAN)
    cmd = "python3 -m venv .venv" if platform.system() != "Windows" else "python -m venv .venv"
    run_command(cmd, cwd=full_path)
    print_message("Entorno virtual creado correctamente.", GREEN)




def update_pip(full_path, venv_python):
    print_message("Actualizando PIP...", CYAN)
    run_command(f'"{venv_python}" -m pip install --upgrade pip', cwd=full_path)
    print_message("PIP actualizado correctamente.", GREEN)





# def create_requirements(full_path, venv_python):
#     print_message("Generando requirements.txt...", CYAN)
#     run_command(f'"{venv_python}" -m pip freeze > requirements.txt', cwd=full_path)
#     print_message("requirements.txt generado correctamente.", GREEN)
    


def replace_settings(full_path, project_name_format, app_name):
    
    new_databases = f'''
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "{project_name_format}_db"),
        "USER": os.getenv("DB_USER", "{project_name_format}_user"),
        "PASSWORD": os.getenv("DB_PASSWORD", "{project_name_format}_pass"),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}
    '''

    # OJO: ruta del settings relativa al proyecto real:
    relative_path = f"{app_name}/settings.py"

    ok = replace_block_in_file(full_path, relative_path, "DATABASES", new_databases)

    print("Reemplazado:", ok)