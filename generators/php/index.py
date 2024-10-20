# generator/index.py

from to_api.create_model_file import generate_model_file
from to_api.create_repository_file import generate_repository_file
from to_api.create_routes_file import generate_routes_file
from to_api.create_controller_list_file import generate_controller_list_file
from to_api.create_migration_file import generate_migration_file




import os
import re


def camel_to_kebab(name):
    """Convierte un string CamelCase a kebab-case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()


def camel_to_snake(name):
    """Convierte un string CamelCase a snake_case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()




if __name__ == "__main__":
    # Obtener la ruta base automáticamente
    ## base_path = os.path.dirname(os.path.dirname(__file__))  # Navegar un nivel hacia arriba desde la ubicación de 'index.py'
    ## ruta = os.path.join(base_path, 'api_project/invoices')


    # Namespace
    namespace = "API"
    # Ruta del proyecto
    ruta = "/Users/dorian/PhpstormProjects81/php84/api-kitchen.famindex.com/"





    # Definir tabla
    singular_name = 'InvoiceHeader'
    plural_name = 'InvoiceHeaders'

    # singular_name = 'Invoice'
    # plural_name = 'Invoices'

    # Path model
    path_model = "Models/" + plural_name
    path_repository = "Repositories/" + plural_name
    path_routes = "routes/"
    path_controller = "Http/Controllers/" + namespace + "/" + plural_name
    path_migration = "database/migrations/"


    # Convertir singular_name y plural_name a kebab-case para las URLs
    singular_name_kebab = camel_to_kebab(singular_name)
    plural_name_kebab = camel_to_kebab(plural_name)
    singular_name_snake = camel_to_snake(singular_name)
    plural_name_snake = camel_to_snake(plural_name)


    columns = [
        {"name": "invoice_counter_id"},
        {"name": "own_company_id"},
        {"name": "customer_id"},
        {"name": "total_with_vat"},
        {"name": "description"}
    ]

    if os.path.isdir(ruta):
        generate_model_file(ruta, path_model, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake)

        generate_repository_file(ruta, path_repository, singular_name, plural_name, singular_name_snake, plural_name_snake, columns)

        generate_routes_file(ruta, namespace, path_routes, plural_name, singular_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake)

        generate_controller_list_file(ruta, namespace, path_controller, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake)

        generate_migration_file(ruta, namespace, path_migration, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns)


    else:
        print("La ruta proporcionada no es válida o no existe. Por favor, verifica y vuelve a intentarlo.")
