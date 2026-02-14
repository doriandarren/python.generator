import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command
from python_django.helpers.helper_file import helper_add_import, helper_append_content, helper_replace_block



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

    folder_path = os.path.join(full_path, "docker")
    file_path = os.path.join(folder_path, "docker-compose.yml")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''## docker compose down    --> Eliminar los contenedores
## docker compose up -d   --> Levantar los contenedores
name: {project_name_format}_posgrest
services:
  postgres:
    image: postgres:16
    container_name: {project_name_format}_postgres
    restart: on-failure
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
#####################################
# Uncomment to use PostgreSQL
#####################################
#DATABASES = {{
#    "default": {{
#        "ENGINE": "django.db.backends.postgresql",
#        "NAME": os.getenv("DB_NAME", "{project_name_format}_db"),
#        "USER": os.getenv("DB_USER", "{project_name_format}_user"),
#        "PASSWORD": os.getenv("DB_PASSWORD", "{project_name_format}_pass"),
#        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
#        "PORT": os.getenv("DB_PORT", "5432"),
#    }}
#}}
    '''

    relative_path = f"{app_name}/settings.py"
    
    ok = helper_add_import(full_path, relative_path, "import os")
    ok = helper_append_content(full_path, relative_path, content_to_append=new_databases, end_line=84)
    
    
    
    str = """\n# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'"""
    
    helper_append_content(
        full_path,
        f"{app_name}/settings.py", 
        str
    )
    

    print_message(f"Archivo settings.py Reemplazado: {ok}", GREEN)