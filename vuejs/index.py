# generator/index.py
import os
import re

from to_front.create_list_file import generate_list_file
from to_front.create_store_file import generate_store_file
from to_front.create_update_file import generate_update_file
from to_front.create_composable_file import generate_composable_file



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
    namespace = "Invoices"
    # Ruta del proyecto
    ruta = "/Users/dorian/VueJsProjects/example"
    #ruta = "/Users/dorian/VueJsProjects/splytin.com"



    # Definir tabla
    singular_name = 'InvoiceHeader'
    plural_name = 'InvoiceHeaders'

    # singular_name = 'Invoice'
    # plural_name = 'Invoices'



    # Convertir singular_name y plural_name a kebab-case para las URLs
    singular_name_kebab = camel_to_kebab(singular_name)
    plural_name_kebab = camel_to_kebab(plural_name)
    singular_name_snake = camel_to_snake(singular_name)
    plural_name_snake = camel_to_snake(plural_name)
    singular_name_first_lower = singular_name[0].lower() + singular_name[1:]
    plural_name_first_lower = plural_name[0].lower() + plural_name[1:]

    # Path model
    path_views = "src/modules/" + namespace.lower() + "/views/" + plural_name_snake
    path_component = "src/modules/" + namespace.lower() + "/components/" + plural_name_snake
    path_composable = "src/modules/" + namespace.lower() + "/composables/"


    ## invoice_counter_id own_company_id customer_id total_with_vat description
    columns = [
        {"name": "invoice_counter_id"},
        {"name": "own_company_id"},
        {"name": "customer_id"},
        {"name": "total_with_vat"},
        {"name": "description"}
    ]



    if os.path.isdir(ruta):
        generate_list_file(ruta, path_views, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns, singular_name_first_lower, plural_name_first_lower)
        generate_store_file(ruta, path_component, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns, singular_name_first_lower, plural_name_first_lower)
        generate_update_file(ruta, path_component, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns, singular_name_first_lower, plural_name_first_lower)
        generate_composable_file(ruta, path_composable, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns, singular_name_first_lower, plural_name_first_lower)


    else:
        print("La ruta proporcionada no es válida o no existe. Por favor, verifica y vuelve a intentarlo.")
