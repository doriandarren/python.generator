from helpers.helper_menu import pause
from helpers.helper_print import input_with_validation
from helpers.helper_string import normalize_project_name
from python_django.helpers.helper_virtual_env import get_venv_python
from python_django.to_create_project.core.generate_core_file_init import generate_code_file_init
from python_django.to_create_project.core.generate_core_models import generate_core_models
from python_django.to_create_project.core.generate_file_helpers import generate_file_helpers
from python_django.to_create_project.core.generate_http import generate_http
from python_django.to_create_project.core.generate_message_channel import generate_message_channel
from python_django.to_create_project.generate_api_doc import generate_api_doc
from python_django.to_create_project.generate_by_command_line import generate_by_command_line
from python_django.to_create_project.generate_cors import generate_cors
from python_django.to_create_project.generate_cron import generate_cron
from python_django.to_create_project.generate_django import generate_django
from python_django.to_create_project.generate_env import generate_env
from python_django.to_create_project.generate_gitignore import generate_gitignore
from python_django.to_create_project.generate_passenger_wsgi import generate_passenger_wsgi
from python_django.to_create_project.generate_postgres import generate_postgres
from python_django.to_create_project.generate_readme import generate_readme
from python_django.to_create_project.generate_simplejwt import generate_simplejwt
from python_django.to_create_project.generate_static_files import generate_static_files
from python_django.to_create_project.generate_todo_md import generate_todo_md


def start_project_python_django():
    
    # Defaults
    default_path = "/Users/dorian/PythonProjects"
    default_project_name = "app1.com"
    default_app_name = "main"

    # Inputs
    project_name = input_with_validation(
        f"Nombre del proyecto",
        default_project_name
    )
    project_path = input_with_validation(
        f"Ruta del proyecto",
        default_path
    )
    
    app_name = input_with_validation(
        f"Nombre de la aplicación principal",
        default_app_name
    )

    # Join Full Path
    full_path = f"{project_path}/{project_name}"
    
    project_name_format = normalize_project_name(project_name)
    
    # Crear el proyecto
    generate_by_command_line(full_path, project_name_format, app_name)
    
    # Generar archivos
    generate_gitignore(full_path)
    generate_passenger_wsgi(full_path, app_name)
    generate_readme(full_path, project_name)
    generate_todo_md(full_path, project_name)
    
    
    # Load virtualenv
    venv_python = get_venv_python(full_path)
    
    
    
    # Django
    generate_django(full_path, project_name_format, app_name, venv_python)
    
    
    # Env
    generate_env(full_path, project_name_format, app_name, venv_python)
    
    
    # Folder uploads
    generate_static_files(full_path, app_name)
    
    # DB
    generate_postgres(full_path, project_name_format, app_name, venv_python)
    
    
    generate_api_doc(full_path, project_name_format, app_name, venv_python)
    
    
    ## TODO crear users app
    ## TODO Pendiente de agregar en la ruta de users para la validacion
    generate_simplejwt(full_path, project_name_format, app_name, venv_python)
    
    generate_code_file_init(full_path)
    
    generate_cors(full_path, project_name_format, app_name, venv_python)
    
    
    # Core Files
    generate_cron(full_path, project_name_format, app_name, venv_python)
    generate_file_helpers(full_path)
    generate_http(full_path)
    generate_message_channel(full_path)
    generate_core_models(full_path)
    
    
    

    pause()