import os
from helpers.helper_print import create_folder, camel_to_kebab, camel_to_snake
from helpers.helpers import dd
from react.to_create_module.generate_list_page import create_list_page
from react.to_create_module.generate_routes import create_routes
from react.to_create_module.generate_create_page import create_create_page
from react.to_create_module.generate_edit_page import create_edit_page
from react.to_create_module.generate_barrel_file import create_barrel_file
from react.to_create_module.generate_service_file import create_service_file


def generate_module_standard_react(project_path, singular_name, plural_name, columns, input_menu_checkbox=None):

    ## Input Default
    if input_menu_checkbox is None:
        input_menu_checkbox = [ "route", "list", "create", "edit", "create", "barrel", "service"]


    # Convertir singular_name y plural_name a kebab-case para las URLs
    singular_name_kebab = camel_to_kebab(singular_name)
    plural_name_kebab = camel_to_kebab(plural_name)
    singular_name_snake = camel_to_snake(singular_name)
    plural_name_snake = camel_to_snake(plural_name)
    singular_first_camel = singular_name[:1].lower() + singular_name[1:]

    if "route" in input_menu_checkbox:
        create_routes(project_path, singular_name, plural_name_snake)

    if "list" in input_menu_checkbox:
        create_list_page(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, singular_first_camel, columns)

    if "create" in input_menu_checkbox:
        create_create_page(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, singular_first_camel, columns)

    if "edit" in input_menu_checkbox:
        create_edit_page(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, singular_first_camel, columns)

    if "barrel" in input_menu_checkbox:
        create_barrel_file(project_path, singular_name, plural_name_snake)

    if "service" in input_menu_checkbox:
        create_service_file(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, singular_first_camel, columns)



