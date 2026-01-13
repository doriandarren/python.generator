import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command
from python_django.helpers.helper_file import helper_append_content, helper_replace_block, helper_update_list

def generate_cors(full_path, project_name_format, app_name, venv_python):
    """
    Genera el archivo
    """
    install_cors(full_path, venv_python)
    update_settings(full_path, project_name_format, app_name)
    
    
    
    
def install_cors(full_path, venv_python):
    print_message("Instalando django-cors-headers...", CYAN)
    run_command(f'"{venv_python}" -m pip install django-cors-headers', cwd=full_path)
    print_message("django-cors-headers instalado correctamente.", GREEN)
    

def update_settings(full_path, project_name_format, app_name):
    
    helper_update_list(
        full_path, 
        f"{app_name}/settings.py", 
        "INSTALLED_APPS", 
        f"'corsheaders',                      # required for cors"
    )
    
    
    
    helper_update_list(
        full_path, 
        f"{app_name}/settings.py", 
        "MIDDLEWARE", 
        f"'corsheaders.middleware.CorsMiddleware',                            # required for cors"
    ) 
    
    helper_replace_block(
        full_path,
        f"{app_name}/settings.py",
        "ALLOWED_HOSTS",
        f"ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '{project_name_format}.com']"
    )
    
    
    helper_append_content(
        full_path, 
        f"{app_name}/settings.py", 
        "\n## CORS"
    )
    
    helper_append_content(
        full_path, 
        f"{app_name}/settings.py", 
        "CORS_ORIGIN_ALLOW_ALL = True"
    )
   
    helper_append_content(
        full_path, 
        f"{app_name}/settings.py", 
        "CORS_ALLOW_CREDENTIALS = True"
    )
    
    print_message("settings.py actualizado correctamente.", GREEN)
   