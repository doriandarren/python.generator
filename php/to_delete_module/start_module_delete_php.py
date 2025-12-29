from helpers.helper_menu import menu_checkbox, pause
from helpers.helper_print import input_with_validation


def start_module_delete_php():

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

    project_path = input_with_validation("Carpeta Proyecto", "/Users/dorian/ReactProjects/app-1")
    namespace = input_with_validation("Namespace (ERP / API / INVOICES)", "API")
    singular_name = input_with_validation("Nombre singular", "AgendaUnloading")

    

    # TODO Hacer el proceso inverso para eliminar el CRUD 
    # generate_module_standard_XXX(project_path, singular_name, plural_name, columns, input_menu_checkbox)
    
    
    
