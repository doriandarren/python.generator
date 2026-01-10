import os
from helpers.helper_print import print_message, GREEN, CYAN


def generate_env(full_path, project_name_format):
    create_env(full_path, project_name_format)
    create_env_example(full_path, project_name_format)


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
        
