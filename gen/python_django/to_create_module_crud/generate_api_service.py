import os
from gen.python_django.helpers.helper_file import create_init_file
from helpers.helper_print import print_message, GREEN, CYAN





def generate_api_service(
        full_path,
        project_name,
        singular_name,
        plural_name,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        singular_first_camel,
        plural_first_camel,
        columns,
    ):
    
    create_init_file(full_path, plural_name_snake)
    
    
    create_file(
        full_path,
        project_name,
        singular_name,
        plural_name,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        singular_first_camel,
        plural_first_camel,
        columns,
    )



def create_init_file(full_path, plural_name_snake):
    print_message("Instalando app...", CYAN)

    apps_path = os.path.join(full_path, "apps", plural_name_snake, "services")
    os.makedirs(apps_path, exist_ok=True)

    create_init_file(apps_path) 




def create_file(
        full_path,
        project_name,
        singular_name,
        plural_name,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        singular_first_camel,
        plural_first_camel,
        columns,
    ):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "apps", plural_name_snake, "services")
    file_path = os.path.join(folder_path, singular_name_snake + "service_2.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''
    ## TODO Content
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)