import os
from gen.python_django.helpers.helper_file import helper_update_list
from helpers.helper_print import print_message, GREEN, CYAN



def update_installed_apps(full_path, app_main, plural_name_snake, venv_python, manage_py_path):
    
    helper_update_list(
        full_path, 
        f"{app_main}/settings.py", 
        "INSTALLED_APPS", 
        f"'apps.{plural_name_snake}',                         # Module")