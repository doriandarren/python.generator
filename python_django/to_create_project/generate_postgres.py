import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command
from python_django.helpers.helper_file import helper_add_import, helper_replace_block



def generate_postgres(full_path, project_name_format, app_name, venv_python):
    """
    Genera el archivo
    """
    install_dependencies(full_path, venv_python)
    generate_docker_file(full_path, project_name_format)    
    replace_settings(full_path, project_name_format, app_name)
    


def install_dependencies(full_path, venv_python):
    print_message("Instalando dependencias en el venv...", CYAN)
    run_command(f'"{venv_python}" -m pip install "psycopg[binary]"', cwd=full_path)
    print_message("Dependencias instaladas correctamente.", GREEN)
    
    
    

def generate_docker_file(full_path, project_name_format):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path)
    file_path = os.path.join(folder_path, "docker-compose.yml")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''services:
  db:
    image: postgres:16-alpine
    container_name: {project_name_format}_postgres
    environment:
      POSTGRES_DB: {project_name_format}_db
      POSTGRES_USER: {project_name_format}_user
      POSTGRES_PASSWORD: {project_name_format}_pass
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)



def replace_settings(full_path, project_name_format, app_name):
    
    new_databases = f'''
DATABASES = {{
    "default": {{
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "{project_name_format}_db"),
        "USER": os.getenv("DB_USER", "{project_name_format}_user"),
        "PASSWORD": os.getenv("DB_PASSWORD", "{project_name_format}_pass"),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }}
}}
    '''

    relative_path = f"{app_name}/settings.py"
    
    ok = helper_add_import(full_path, relative_path, "import os")
    ok = helper_replace_block(full_path, relative_path, "DATABASES", new_databases)    

    print_message(f"Archivo settings.py Reemplazado: {ok}", GREEN)