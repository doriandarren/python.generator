import os
from gen.helpers.helper_columns import parse_columns_input
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import standard_module_crud_python_django
from helpers.helper_print import print_message, GREEN, CYAN


def generate_module_devs(full_path, project_name_format, app_name):
    create_module_devs(full_path, project_name_format, app_name)
    update_file_api_views(full_path, project_name_format, app_name)



def create_module_devs(full_path, project_name_format, app_name):
    
    print_message(f"Generando el modulo de Users", CYAN)
    singular_name = "Dev"
    plural_name = "Devs"
    columns = "test"
    input_menu_checkbox = ['api_route', 'api_serializer', 'api_wiewset']
    formatColumns = parse_columns_input(columns)
    
    standard_module_crud_python_django(full_path, app_name, singular_name, plural_name, formatColumns, input_menu_checkbox)
    


def update_file_api_views():
    pass