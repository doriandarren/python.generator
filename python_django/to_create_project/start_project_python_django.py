from helpers.helper_menu import pause
from helpers.helper_print import input_with_validation
from helpers.helper_string import normalize_project_name
from python_django.helpers.helper_virtual_env import get_venv_python
from python_django.to_create_project.generate_by_command_line import generate_by_command_line
from python_django.to_create_project.generate_django import generate_django
from python_django.to_create_project.generate_env import generate_env
from python_django.to_create_project.generate_gitignore import generate_gitignore
from python_django.to_create_project.generate_passenger_wsgi import generate_passenger_wsgi
from python_django.to_create_project.generate_postgres import generate_postgres
from python_django.to_create_project.generate_readme import generate_readme
from python_django.to_create_project.generate_todo_md import generate_todo_md


def start_project_python_django():
    
    # Defaults
    default_path = "/Users/dorian/PythonProjects"
    default_project_name = "app1.com"
    default_app_name = "app"

    # Inputs
    project_name = input_with_validation(
        f"Nombre del proyecto (defecto: {default_project_name}): ",
        default_project_name
    )
    project_path = input_with_validation(
        f"Ruta del proyecto (defecto: {default_path}): ",
        default_path
    )
    
    app_name = input_with_validation(
        f"Nombre de la APP (defecto: {default_app_name}): ",
        default_app_name
    )

    # Join Full Path
    full_path = f"{project_path}/{project_name}"
    
    project_name_format = normalize_project_name(project_name)
    
    # Crear el proyecto
    generate_by_command_line(full_path, project_name_format, app_name)
    
    venv_python = get_venv_python(full_path)
    
    
    generate_env(full_path, project_name_format)
    generate_gitignore(full_path)
    generate_passenger_wsgi(full_path, app_name)
    
    # Django
    generate_django(full_path, project_name_format, app_name, venv_python)
    
    # DB
    generate_postgres(full_path, project_name_format, venv_python)
    
    
    
    generate_readme(full_path, project_name)
    
    generate_todo_md(full_path, project_name)
    
    

    pause()