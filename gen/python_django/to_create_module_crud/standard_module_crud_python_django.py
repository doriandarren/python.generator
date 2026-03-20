import os
from gen.helpers.helper_menu import pause
from gen.helpers.helper_print import camel_to_kebab, camel_to_snake
from gen.helpers.helper_string import normalize_project_name
from gen.helpers.helpers import dd
from gen.python_django.helpers.helper_virtual_env import get_venv_python
from gen.python_django.to_create_module_crud.generate_api_model import generate_api_model
from gen.python_django.to_create_module_crud.generate_api_route import generate_api_route
from gen.python_django.to_create_module_crud.generate_api_serializer import generate_api_serializer
from gen.python_django.to_create_module_crud.generate_api_service import generate_api_service
from gen.python_django.to_create_module_crud.generate_api_viewset import generate_api_viewset
from gen.python_django.to_create_module_crud.generate_app import generate_app
from gen.python_django.to_create_module_crud.update_installed_apps import update_installed_apps


def standard_module_crud_python_django(full_path, app_main, singular_name, plural_name, columns, input_menu_checkbox=None):

    # Input Default
    if input_menu_checkbox is None:
        input_menu_checkbox = ["api_route", "api_serializer", "api_wiewset"]

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
    
    
    # Update installed apps
    update_installed_apps(
        full_path, 
        app_main, 
        plural_name_snake,
        manage_py_path, 
        venv_python
    )
    
    
    # Generate app
    generate_app(
        full_path,
        plural_name_snake,
        venv_python,
        manage_py_path
    )
    

    

    if "api_route" in input_menu_checkbox:
        generate_api_route(
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
        
    
        
    if "api_serializer" in input_menu_checkbox:
        generate_api_serializer(
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
        
    
    
    if "api_wiewset" in input_menu_checkbox:
        generate_api_viewset(
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
    
        
    if "api_model" in input_menu_checkbox:
        generate_api_model(
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
        
        
    if "api_service" in input_menu_checkbox:
        generate_api_service(
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
    
    