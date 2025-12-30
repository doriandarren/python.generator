from helpers.helper_columns import parse_columns_input
from helpers.helper_menu import menu_checkbox, pause
from helpers.helper_print import input_with_validation
from react.to_create_module_single.standard_module_single_react import standard_module_single_react


def start_module_single_react():

    opt = [
        ("Route", "route"),
        ("Página", "single_page"),
        ("Barril", "barrel"),
        ("Service", "service"),
    ]

    input_menu_checkbox = menu_checkbox("Componentes: ", opt)

    #project_path = input_with_validation("Carpeta Proyecto", "/Users/dorian/ReactProjects/app-1")
    project_path = input_with_validation("Carpeta Proyecto", "/Users/dorian/ReactProjects/Truckwash/office.truckwashvilamalla.eu")
    singular_name = input_with_validation("Nombre singular", "AgendaUnloading")
    plural_name = input_with_validation("Nombre plural", "AgendaUnloadings")
    input_columns = input_with_validation("Columnas (separdo por espacio)", "user_id:fk name age:integer description")

    columns = parse_columns_input(input_columns)
    
    standard_module_single_react(project_path, singular_name, plural_name, columns, input_menu_checkbox)
    
