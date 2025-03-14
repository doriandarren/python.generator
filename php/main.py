import os
import re

## Agregue "php." por si acaso no funciona esto con el kt:

from php.to_api.create_model_file import generate_model_file
from php.to_api.create_repository_file import generate_repository_file
from php.to_api.create_routes_file import generate_routes_file
from php.to_api.create_migration_file import generate_migration_file
from php.to_api.create_controller_list_file import generate_controller_list_file
from php.to_api.create_controller_show_file import generate_controller_show_file
from php.to_api.create_controller_store_file import generate_controller_store_file
from php.to_api.create_controller_update_file import generate_controller_update_file
from php.to_api.create_controller_destroy_file import generate_controller_destroy_file
from php.to_api.create_seeder_file import generate_seeder_file
from php.to_api.create_factory_file import generate_factory_file
from php.to_api.create_postman_file import generate_postman_file



def camel_to_kebab(name):
    """Convierte un string CamelCase a kebab-case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()


def camel_to_snake(name):
    """Convierte un string CamelCase a snake_case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()




def generate(namespace, ruta, singular_name, plural_name, columns):
    # Obtener la ruta base automáticamente
    ## base_path = os.path.dirname(os.path.dirname(__file__))  # Navegar un nivel hacia arriba desde la ubicación de 'main.py'
    ## ruta = os.path.join(base_path, 'api_project/invoices')



    # Path model
    path_model = "Models/" + plural_name
    path_repository = "Repositories/" + plural_name
    path_routes = "routes/"
    path_controller = "Http/Controllers/" + namespace + "/" + plural_name
    path_migration = "database/migrations/"
    path_seeder = "database/seeders"
    path_factory = "database/factories"
    path_script = "public/Script"


    # Convertir singular_name y plural_name a kebab-case para las URLs
    singular_name_kebab = camel_to_kebab(singular_name)
    plural_name_kebab = camel_to_kebab(plural_name)
    singular_name_snake = camel_to_snake(singular_name)
    plural_name_snake = camel_to_snake(plural_name)


    if os.path.isdir(ruta):
        generate_model_file(ruta, path_model, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake)
        generate_repository_file(ruta, path_repository, singular_name, plural_name, singular_name_snake, plural_name_snake, columns)
        generate_routes_file(ruta, namespace, path_routes, plural_name, singular_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake)
        generate_migration_file(ruta, namespace, path_migration, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns)
        generate_controller_list_file(ruta, namespace, path_controller, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake)
        generate_controller_show_file(ruta, namespace, path_controller, singular_name, plural_name, singular_name_snake, plural_name_snake)
        generate_controller_store_file(ruta, namespace, path_controller, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns)
        generate_controller_update_file(ruta, namespace, path_controller, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns)
        generate_controller_destroy_file(ruta, namespace, path_controller, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns)

        generate_seeder_file(ruta, path_seeder, singular_name, plural_name, singular_name_snake, plural_name_snake, columns)
        generate_factory_file(ruta, path_factory, singular_name, plural_name, singular_name_snake, plural_name_snake, columns)
        generate_postman_file(ruta, singular_name, plural_name, singular_name_kebab, plural_name_kebab, columns)

    else:
        print("La ruta proporcionada no es válida o no existe. Por favor, verifica y vuelve a intentarlo.")






# Función para manejar input con validación y valores por defecto
def input_with_validation(prompt, default_value=None):
    while True:  # Bucle para solicitar una entrada válida
        if default_value:  # Si hay un valor por defecto, se muestra
            user_input = input(f"{prompt} [{default_value}]: ").strip()
            if user_input:  # Si el usuario escribe algo, lo retorna
                return user_input
            return default_value  # Si presiona Enter, usa el valor por defecto
        else:  # Si no hay un valor por defecto
            user_input = input(f"{prompt}").strip()
            if user_input:  # Si el usuario escribe algo, lo retorna
                return user_input
            print("La entrada no puede estar en blanco. Por favor, inténtalo de nuevo.")




"""
Activar directamente. Si no usar el "mainTK" para activar la interfaz gráfica.
"""

if __name__ == "__main__":

    namespace = input_with_validation("Namespace ( ERP / API / INVOICES ) ", "API")
    ruta = input_with_validation("Ruta proyecto ( /Users/dorian/PhpstormProjects81/laravel_test/ ) ", "/Users/dorian/PhpstormProjects81/laravel_test/")
    singular_name = input_with_validation("Nombre singular (AgendaUnloading): ", None)
    plural_name = input_with_validation("Nombre plural (AgendaUnloadings): ", None)

    input_columns = input_with_validation("Columnas: ", None)

    columns = [{"name": column} for column in input_columns.split()]

    generate(namespace, ruta, singular_name, plural_name, columns)




# def load():
#
#     # Namespace
#     # namespace = "INVOICES"
#     # namespace = "API"
#     namespace = "ERP"
#
#
#     # Ruta del proyecto
#     # ruta = "/Users/dorian/PhpstormProjects81/php84/api.splytin.com/"
#     # ruta = "/Users/dorian/PhpstormProjects81/portuarios.globalfleet.es/"
#     ruta = "/Users/dorian/PhpstormProjects81/harineras-api.globalfleet.es/"
#
#
#     # Definir tabla
#     ##singular_name = 'AgendaUnloading'
#     singular_name = 'Device'
#     plural_name = 'Devices'
#
#     columns = [
#         {"name": "company_id"},
#         {"name": "vehicle_id"},
#         {"name": "box_id"},
#         {"name": "unit_id"},
#         {"name": "model"},
#         {"name": "model_ver"},
#         {"name": "installed"},
#         {"name": "imei"},
#         {"name": "serial"},
#         {"name": "phone"},
#     ]
#
#     generate(namespace, ruta, singular_name, plural_name, columns)












