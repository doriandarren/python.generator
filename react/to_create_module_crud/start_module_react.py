from helpers.helper_columns import parse_columns_input
from helpers.helper_menu import menu_checkbox, pause
from helpers.helper_print import input_with_validation
from react.to_create_module_crud.standard_module_crud_react import standard_module_crud_react


def start_module_react():

    opt = [
        ("Route", "route"),
        ("List", "list"),
        ("Create", "create"),
        ("Edit", "edit"),
        ("Barril", "barrel"),
        ("Service", "service"),
    ]

    input_menu_checkbox = menu_checkbox("Componentes: ", opt)

    # project_path = input_with_validation("Carpeta Proyecto (defecto es: /Users/dorian/ReactProjects/app-1): ", "/Users/dorian/ReactProjects")
    project_path = input_with_validation(
        "Carpeta Proyecto", 
        "/Users/dorian/ReactProjects/Avanza/prices.avanzaoil.eu"
    )
    singular_name = input_with_validation("Nombre singular", "AgendaUnloading")
    plural_name = input_with_validation("Nombre plural ", "AgendaUnloadings")
    input_columns = input_with_validation("Columnas (separdo por espacio)", "user_id:fk name age:integer description")
    
    columns = parse_columns_input(input_columns)
    
    standard_module_crud_react(project_path, singular_name, plural_name, columns, input_menu_checkbox)

