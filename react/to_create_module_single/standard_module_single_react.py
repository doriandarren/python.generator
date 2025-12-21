import os
from helpers.helper_menu import pause
from helpers.helper_print import camel_to_kebab, camel_to_snake
from helpers.helper_string import normalize_project_name
from react.to_create_module_single.generate_barrel_file import generate_barrel_file
from react.to_create_module_single.generate_routes import generate_routes
from react.to_create_module_single.generate_service_file import generate_service_file
from react.to_create_module_single.generate_single_page import generate_single_page


def standard_module_single_react(full_path, singular_name, plural_name, columns, input_menu_checkbox=None):

    # Input Default
    if input_menu_checkbox is None:
        input_menu_checkbox = ["route", "list", "create", "edit", "barrel", "service"]

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


    if "route" in input_menu_checkbox:
        generate_routes(full_path, singular_name, plural_name_snake)

    if "single_page" in input_menu_checkbox:
        generate_single_page(
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



    if "barrel" in input_menu_checkbox:
        generate_barrel_file(full_path, singular_name, plural_name_snake)

    if "service" in input_menu_checkbox:
        generate_service_file(
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
    
    pause()

