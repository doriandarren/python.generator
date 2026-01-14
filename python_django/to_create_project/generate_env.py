import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command
from python_django.helpers.helper_file import helper_add_import, helper_append_content, helper_replace_block


def generate_env(full_path, project_name_format, app_name, venv_python):
    
    install_env(full_path, venv_python)
    update_settings(full_path, app_name)
    
    create_env(full_path, project_name_format)
    create_env_example(full_path, project_name_format)



def install_env(full_path, venv_python):
    print_message("Instalando python-dotenv...", CYAN)
    run_command(f'"{venv_python}" -m pip install python-dotenv', cwd=full_path)
    print_message("python-dotenv instalado correctamente.", GREEN)



def update_settings(full_path, app_name):
    
    
    helper_add_import(
        full_path, 
        f"{app_name}/settings.py", 
        "from dotenv import load_dotenv"
    )
    
    
    helper_append_content(
        full_path,
        f"{app_name}/settings.py",
        f'load_dotenv(BASE_DIR / ".env")                          # Enviroment',
        end_line=19
    )
    
    
    str = f"""\n## ENV
APP_NAME = os.getenv("APP_NAME", "splytin")
APP_ENV = os.getenv("APP_ENV", "local")
MESSAGE_CHANNEL_URL = os.getenv("MESSAGE_CHANNEL_URL")
    """
    
    helper_append_content(
        full_path, 
        f"{app_name}/settings.py", 
        str
    )
    
    
    

def create_env(full_path, project_name_format):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path)
    file_path = os.path.join(folder_path, ".env")

    os.makedirs(folder_path, exist_ok=True)
    
    content = f'''APP_NAME={project_name_format}
APP_ENV=local
MESSAGE_CHANNEL_URL=

# Debug
DEBUG=true

# DB
DB_NAME={project_name_format}_db
DB_USER={project_name_format}_user
DB_PASSWORD={project_name_format}_pass
DB_HOST=127.0.0.1
DB_PORT=5432
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        

def create_env_example(full_path, project_name_format):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path)
    file_path = os.path.join(folder_path, ".env.example")

    os.makedirs(folder_path, exist_ok=True)
    

    content = f'''APP_NAME={project_name_format}
APP_ENV=local
MESSAGE_CHANNEL_URL=

# Debug
DEBUG=true

# DB
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=5432
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
