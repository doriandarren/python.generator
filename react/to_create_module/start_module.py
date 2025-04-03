from helpers.helper_menu import menu_checkbox, pause
from helpers.helper_print import input_with_validation
from react.to_create_module.generate_module_standard import generate_module_standard


def start_module():

    opt = [
        ("Route", "route"),
        ("List", "list"),
        ("Create", "create"),
        ("Edit", "edit"),
        ("Barril", "barrel"),
        ("Service", "service"),
    ]

    input_menu_checkbox = menu_checkbox("Componentes: ", opt)

    pause()

    project_path = "/Users/dorian/ReactProjects/"

    print("[Directorio por defecto es: /Users/dorian/ReactProjects/]")
    folder_project = input_with_validation("Carpeta Proyecto: ")
    singular_name = input_with_validation("Nombre singular (AgendaUnloading): ", None)
    plural_name = input_with_validation("Nombre plural (AgendaUnloadings): ", None)
    input_columns = input_with_validation("Columnas: ", None)

    columns = [{"name": column} for column in input_columns.split()]
    project_path = project_path + folder_project + "/"

    generate_module_standard(project_path, singular_name, plural_name, columns, input_menu_checkbox)

