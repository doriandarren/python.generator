from helpers.helper_columns import parse_columns_input
from helpers.helper_menu import menu_checkbox, pause
from helpers.helper_print import input_with_validation
from python_django.to_create_module_crud.standard_module_crud_python_django import standard_module_crud_python_django


def start_module_crud_python_django():

    opt = [
        ("Route", "route"),
        ("List", "list"),
        ("Create", "create"),
        ("Edit", "edit"),
        ("Barril", "barrel"),
        ("Service", "service"),
    ]
    
    full_path_default = "/Users/dorian/PythonProjects/app1.com"
    singular_name_default = "AgendaUnloading"
    plural_name_default = "AgendaUnloadings"
    columns_default = "user_id:fk name age:integer description"
    

    input_menu_checkbox = menu_checkbox("Componentes: ", opt)

    full_path = input_with_validation("Carpeta Proyecto", full_path_default)
    singular_name = input_with_validation("Nombre singular", singular_name_default)
    plural_name = input_with_validation("Nombre plural", plural_name_default)
    input_columns = input_with_validation("Columnas: ", columns_default)

    columns = parse_columns_input(input_columns)
    
    
    standard_module_crud_python_django(full_path, singular_name, plural_name, columns, input_menu_checkbox)

    pause()