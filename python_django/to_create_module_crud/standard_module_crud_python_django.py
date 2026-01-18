import os
from helpers.helper_menu import pause
from helpers.helper_print import camel_to_kebab, camel_to_snake
from helpers.helper_string import normalize_project_name
from helpers.helpers import dd
from python_django.helpers.helper_virtual_env import get_venv_python
from python_django.to_create_module_crud.generate_app import generate_app


def standard_module_crud_python_django(full_path, singular_name, plural_name, columns, input_menu_checkbox=None):

    # Input Default
    if input_menu_checkbox is None:
        input_menu_checkbox = ["app", "route", "list", "create", "edit", "barrel", "service"]

    # Convertir nombres
    singular_name_kebab = camel_to_kebab(singular_name)
    plural_name_kebab = camel_to_kebab(plural_name)
    singular_name_snake = camel_to_snake(singular_name)
    plural_name_snake = camel_to_snake(plural_name)
    
    ## Project Name
    temp_name = os.path.basename(full_path.rstrip(os.sep))
    project_name = normalize_project_name(temp_name)
    

    # Camel (para services)
    singular_first_camel = singular_name[:1].lower() + singular_name[1:]
    plural_first_camel = plural_name[:1].lower() + plural_name[1:]
    
    
    # Load virtualenv
    venv_python = get_venv_python(full_path)
    
    
    manage_py_path = os.path.join(full_path, "manage.py")
    
    
    # print(f"Crear un: {venv_python} ")
    # dd(manage_py_path)
    
    
    
    if "app" in input_menu_checkbox:
        generate_app(
            full_path,
            singular_name,
            plural_name,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            singular_first_camel,
            plural_first_camel,
            columns,
            venv_python,
            manage_py_path
        )
    


    # if "list" in input_menu_checkbox:
    #     generate_model(
    #         full_path,
    #         singular_name,
    #         plural_name,
    #         singular_name_kebab,
    #         plural_name_kebab,
    #         singular_name_snake,
    #         plural_name_snake,
    #         singular_first_camel,
    #         plural_first_camel,
    #         columns,
    #     )


    # TODO refactor
    # if "route" in input_menu_checkbox:
    #     create_routes(full_path, singular_name, plural_name_snake)

    # if "list" in input_menu_checkbox:
    #     generate_list_page(
    #         full_path,
    #         singular_name,
    #         plural_name,
    #         singular_name_kebab,
    #         plural_name_kebab,
    #         singular_name_snake,
    #         plural_name_snake,
    #         singular_first_camel,
    #         plural_first_camel,
    #         columns,
    #     )

    # if "create" in input_menu_checkbox:
    #     generate_create_page(
    #         full_path,
    #         singular_name,
    #         plural_name,
    #         singular_name_kebab,
    #         plural_name_kebab,
    #         singular_name_snake,
    #         plural_name_snake,
    #         singular_first_camel,
    #         plural_first_camel,
    #         columns,
    #     )

    # if "edit" in input_menu_checkbox:
    #     generate_edit_page(
    #         full_path,
    #         singular_name,
    #         plural_name,
    #         singular_name_kebab,
    #         plural_name_kebab,
    #         singular_name_snake,
    #         plural_name_snake,
    #         singular_first_camel,
    #         plural_first_camel,
    #         columns,
    #     )

    # if "barrel" in input_menu_checkbox:
    #     generate_barrel_file(full_path, singular_name, plural_name_snake)

    # if "service" in input_menu_checkbox:
    #     generate_service_file(
    #         full_path,
    #         project_name,
    #         singular_name,
    #         plural_name,
    #         singular_name_kebab,
    #         plural_name_kebab,
    #         singular_name_snake,
    #         plural_name_snake,
    #         singular_first_camel,
    #         plural_first_camel,
    #         columns,
    #     )
    
    pause()