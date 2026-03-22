import os
from gen.helpers.helper_columns import parse_columns_input
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import standard_module_crud_python_django
from helpers.helper_print import print_message, GREEN, CYAN



def generate_module_users(full_path, project_name_format, app_name):
    create_module_users(full_path, project_name_format, app_name)

    ## TODO Actializar el settings.py
    ## TODO Actializar el urls.py



def create_module_users(full_path, project_name_format, app_name):
    
    print_message(f"Generando el modulo de Users", CYAN)
    singular_name = "User"
    plural_name = "Users"
    columns = "email password"
    input_menu_checkbox = ['api_route', 'api_serializer', 'api_wiewset', 'api_model', 'api_service']
    formatColumns = parse_columns_input(columns)
    
    standard_module_crud_python_django(full_path, "main", singular_name, plural_name, formatColumns, input_menu_checkbox)
    
    