import os
from helpers.helper_menu import pause
from helpers.helper_print import camel_to_kebab, camel_to_snake
from php.to_module.create_model_file import generate_model_file
from php.to_module.create_repository_file import generate_repository_file
from php.to_module.create_routes_file import generate_routes_file
from php.to_module.create_migration_file import generate_migration_file
from php.to_module.create_controller_list_file import generate_controller_list_file
from php.to_module.create_controller_show_file import generate_controller_show_file
from php.to_module.create_controller_store_file import generate_controller_store_file
from php.to_module.create_controller_update_file import generate_controller_update_file
from php.to_module.create_controller_destroy_file import generate_controller_destroy_file
from php.to_module.create_seeder_file import generate_seeder_file
from php.to_module.create_factory_file import generate_factory_file
from php.to_module.create_postman_file import generate_postman_file


def generate_module_standard_php(namespace, ruta, singular_name, plural_name, columns, input_menu_checkbox=None):

    # Input Default
    if input_menu_checkbox is None:
        input_menu_checkbox = ["model", "controller_list", "controller_show", "controller_store", "controller_update",
                               "controller_destroy", "repository", "routes", "migration", "seeder", "factory", "postman"]


    ##TODO refactorizar esto a cada uno de las rutas

    path_model = "Models/" + namespace + "/" + plural_name
    path_repository = "Repositories/" + namespace + "/" + plural_name
    path_controller = "Http/Controllers/" + namespace + "/" + plural_name
    path_migration = "database/migrations/"
    path_routes = "routes/"
    path_seeder = "database/seeders"
    path_factory = "database/factories/" + namespace

    # Convertir singular_name y plural_name a kebab-case para las URLs
    singular_name_kebab = camel_to_kebab(singular_name)
    plural_name_kebab = camel_to_kebab(plural_name)
    singular_name_snake = camel_to_snake(singular_name)
    plural_name_snake = camel_to_snake(plural_name)
    

    if os.path.isdir(ruta):
        if "model" in input_menu_checkbox:
            generate_model_file(ruta, namespace, path_model,
                                singular_name, plural_name, plural_name_snake)

        if "controller_list" in input_menu_checkbox:
            generate_controller_list_file(ruta, namespace, path_controller, singular_name, plural_name,
                                          singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake)

        if "controller_show" in input_menu_checkbox:
            generate_controller_show_file(
                ruta, namespace, path_controller, singular_name, plural_name, singular_name_snake, plural_name_snake)

        if "controller_store" in input_menu_checkbox:
            generate_controller_store_file(ruta, namespace, path_controller, singular_name, plural_name,
                                           singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns)

        if "controller_update" in input_menu_checkbox:
            generate_controller_update_file(ruta, namespace, path_controller, singular_name, plural_name,
                                            singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns)

        if "controller_destroy" in input_menu_checkbox:
            generate_controller_destroy_file(ruta, namespace, path_controller, singular_name, plural_name,
                                             singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns)

        if "repository" in input_menu_checkbox:
            generate_repository_file(ruta, namespace, path_repository, singular_name,
                                     plural_name, singular_name_snake, plural_name_snake, columns)

        if "routes" in input_menu_checkbox:
            generate_routes_file(ruta, namespace, path_routes, plural_name, singular_name,
                                 singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake)

        if "migration" in input_menu_checkbox:
            generate_migration_file(ruta, namespace, path_migration, singular_name, plural_name,
                                    singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns)

        if "seeder" in input_menu_checkbox:
            generate_seeder_file(ruta, path_seeder, singular_name, plural_name,
                                 singular_name_snake, plural_name_snake, columns)

        if "factory" in input_menu_checkbox:
            generate_factory_file(ruta, namespace, path_factory, singular_name,
                                  plural_name, singular_name_snake, plural_name_snake, columns)

        if "postman" in input_menu_checkbox:
            generate_postman_file(ruta, singular_name, plural_name,
                                  singular_name_kebab, plural_name_kebab, columns)

    else:
        print("La ruta proporcionada no es válida o no existe. Por favor, verifica y vuelve a intentarlo.")
