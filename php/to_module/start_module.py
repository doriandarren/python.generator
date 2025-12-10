from helpers.helper_menu import menu_checkbox, pause
from helpers.helper_print import input_with_validation
from php.to_module.generator import generate


def start_module():

    opt = [
        ("Modelo", "model"),
        ("Controlador - List", "controller_list"),
        ("Controlador - Show", "controller_show"),
        ("Controlador - Store", "controller_store"),
        ("Controlador - Update", "controller_update"),
        ("Controlador - Destroy", "controller_destroy"),
        ("Repositorio", "repository"),
        ("Rutas", "routes"),
        ("Migración", "migration"),
        ("Seeder", "seeder"),
        ("Factory", "factory"),
        ("Archivo Postman", "postman"),
    ]

    input_menu_checkbox = menu_checkbox("Componentes: ", opt)

    pause()

    full_path = input_with_validation(
        "Proyecto ", "/Users/dorian/PhpstormProjects81/app-1")
    namespace = input_with_validation(
        "Namespace (ERP / API / INVOICES) ", "EFIDATA")
    singular_name = input_with_validation(
        "Tabla singular (EX: AgendaUnloading): ", None)
    plural_name = input_with_validation(
        "Tabla plural (EX: AgendaUnloadings): ", None)
    input_columns = input_with_validation(
        "Columnas (separdo por espacio): ", None)

    columns = [{"name": column} for column in input_columns.split()]

    print(columns)

    # generate(namespace, full_path, singular_name, plural_name, columns, input_menu_checkbox)
