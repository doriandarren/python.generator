from helpers.helper_columns import parse_columns_input
from helpers.helper_menu import menu_checkbox, pause
from helpers.helper_print import input_with_validation
# TODO refactor
# from react.to_create_module_crud.generate_module_standard_X import generate_module_standard_X


def start_module_single():

    opt = [
        ("Route", "route"),
        ("List", "list"),
        ("Create", "create"),
        ("Edit", "edit"),
        ("Barril", "barrel"),
        ("Service", "service"),
    ]

    input_menu_checkbox = menu_checkbox("Componentes: ", opt)

    project_path = input_with_validation("Carpeta Proyecto (defecto es: /Users/dorian/ReactProjects/app-1): ", "/Users/dorian/ReactProjects/app-1")
    singular_name = input_with_validation("Nombre singular (AgendaUnloading): ", "AgendaUnloading")
    plural_name = input_with_validation("Nombre plural (AgendaUnloadings): ", "AgendaUnloadings")
    input_columns = input_with_validation("Columnas: ", "user_id:fk name age:integer description")

    columns = parse_columns_input(input_columns)

    # TODO refactor
    # generate_module_standard_X(project_path, singular_name, plural_name, columns, input_menu_checkbox)