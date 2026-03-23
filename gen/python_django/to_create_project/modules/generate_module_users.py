import os
from gen.helpers.helper_columns import parse_columns_input
from gen.python_django.helpers.helper_file import helper_append_content
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import standard_module_crud_python_django
from helpers.helper_print import print_message, GREEN, CYAN



def generate_module_users(full_path, project_name_format, app_name):
    create_module_users(full_path, project_name_format, app_name)
    update_setting_auth_user_model(full_path, project_name_format, app_name)
    
    update_model(full_path, project_name_format, app_name)
    
    ## TODO Actializar el urls.py
    
    


def create_module_users(full_path, project_name_format, app_name):
    
    print_message(f"Generando el modulo de Users", CYAN)
    singular_name = "User"
    plural_name = "Users"
    columns = "email password"
    input_menu_checkbox = ['api_route', 'api_serializer', 'api_wiewset', 'api_model', 'api_service']
    formatColumns = parse_columns_input(columns)
    
    standard_module_crud_python_django(full_path, app_name, singular_name, plural_name, formatColumns, input_menu_checkbox)
    


def update_setting_auth_user_model(full_path, project_name_format, app_name):
    
    helper_append_content(
        full_path,
        f"{app_name}/settings.py",
        "\n# USERS"
    )
    
    helper_append_content(
        full_path,
        f"{app_name}/settings.py",
        "AUTH_USER_MODEL = 'users.User'"
    )

    print_message("settings.py actualizado correctamente.", GREEN)
    
    

def update_model(full_path, project_name_format, app_name):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "apps", "users")
    file_path = os.path.join(folder_path, "models.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)