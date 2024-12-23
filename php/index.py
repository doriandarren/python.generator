# generator/index.py
import os
import re

from to_api.create_model_file import generate_model_file
from to_api.create_repository_file import generate_repository_file
from to_api.create_routes_file import generate_routes_file
from to_api.create_migration_file import generate_migration_file
from to_api.create_controller_list_file import generate_controller_list_file
from to_api.create_controller_show_file import generate_controller_show_file
from to_api.create_controller_store_file import generate_controller_store_file
from to_api.create_controller_update_file import generate_controller_update_file
from to_api.create_controller_destroy_file import generate_controller_destroy_file
from to_api.create_seeder_file import generate_seeder_file
from to_api.create_factory_file import generate_factory_file
from to_api.create_postman_file import generate_postman_file



def camel_to_kebab(name):
    """Convierte un string CamelCase a kebab-case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()


def camel_to_snake(name):
    """Convierte un string CamelCase a snake_case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()




def generate(namespace, ruta, singular_name, plural_name, columns):
    # Obtener la ruta base automáticamente
    ## base_path = os.path.dirname(os.path.dirname(__file__))  # Navegar un nivel hacia arriba desde la ubicación de 'index.py'
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




if __name__ == "__main__":

    # Namespace
    # namespace = "INVOICES"
    # namespace = "API"
    namespace = "ERP"


    # Ruta del proyecto
    # ruta = "/Users/dorian/PhpstormProjects81/php84/api.splytin.com/"
    # ruta = "/Users/dorian/PhpstormProjects81/portuarios.globalfleet.es/"
    ruta = "/Users/dorian/PhpstormProjects81/harineras-api.globalfleet.es/"


    # Definir tabla
    ##singular_name = 'AgendaUnloading'
    singular_name = 'Device'
    plural_name = 'Devices'


    # Definir las columnas:
    # columns = [
    #     {"name": "transporeon_code"},
    #     {"name": "name"},
    #     {"name": "msoft_code"},
    # ]

    columns = [
        {"name": "company_id"},
        {"name": "box_id"},
        {"name": "unit_id"},
        {"name": "model"},
        {"name": "model_ver"},
        {"name": "installed"},
        {"name": "imei"},
        {"name": "serial"},
        {"name": "phone"},
    ]



    generate(namespace, ruta, singular_name, plural_name, columns)
