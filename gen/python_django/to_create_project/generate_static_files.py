import os
from gen.helpers.helper_print import print_message, GREEN, CYAN
from gen.python_django.helpers.helper_file import helper_append_content, helper_replace_block



def generate_static_files(full_path, app_name):
    """
    Genera el archivo
    """
    create_static_files(full_path, app_name)
    create_folder(full_path)



def create_static_files(full_path, app_name):
    
    str = f"""STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
    """
    
    helper_append_content(
        full_path,
        f"{app_name}/settings.py",
        str
    )
    


def create_folder(full_path):
    folder_path = os.path.join(full_path, "uploads")
    os.makedirs(folder_path, exist_ok=True)
    print_message(f"Carpeta uploads creada", GREEN)
