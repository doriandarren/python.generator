from helpers.helper_columns import parse_columns_input
from helpers.helper_menu import menu_checkbox, pause
from helpers.helper_print import input_with_validation
from php.to_module_crud.standard_module_crud_php import standard_module_crud_php


def start_module_php():

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

    ##full_path = input_with_validation("Proyecto ", "/Users/dorian/PhpstormProjects81/app-1")
    full_path = input_with_validation("Proyecto ", "/Users/dorian/PhpstormProjects81/docker-laravel-84/projects/services.avanzaoil.eu")
    namespace = input_with_validation("Namespace (ERP / API / INVOICES) ", "EFIDATA")
    singular_name = input_with_validation("Tabla singular (EX: AgendaUnloading): ", "AgendaUnloading")
    plural_name = input_with_validation("Tabla plural (EX: AgendaUnloadings): ", "AgendaUnloadings")
    input_columns = input_with_validation(
        "Columnas (separdo por espacio): ", "customer_id:fk name:string amount:float description has_active:boolean")

    ##columns = [{"name": column} for column in input_columns.split()]
    
    columns = parse_columns_input(input_columns)
    
    standard_module_crud_php(namespace, full_path, singular_name, plural_name, columns, input_menu_checkbox)
    
    pause()
