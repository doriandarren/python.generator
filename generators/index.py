# generator/index.py

from repositories.python.to_api.create_model_file import generate_model_file
from repositories.python.to_api.create_repository_file import generate_repository_file
from repositories.python.to_api.create_url_file import create_url_file
from repositories.python.to_api.create_controller_list_file import generate_controller_list_file
from repositories.python.to_api.create_controller_show_file import generate_controller_show_file
from repositories.python.to_api.create_controller_store_file import generate_controller_store_file
from repositories.python.to_api.create_controller_update_file import generate_controller_update_file



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
    base_path = os.path.dirname(os.path.dirname(__file__))  # Navegar un nivel hacia arriba desde la ubicación de 'index.py'
    ruta = os.path.join(base_path, 'api_project/invoices')

    # Settings :
    namespace = "api_project"
    app_name = 'invoices'

    # Definir el nombre singular y plural de la tabla
    singular_name = 'InvoiceHeader'
    plural_name = 'InvoiceHeaders'

    # singular_name = 'Invoice'
    # plural_name = 'Invoices'




    # Definir las columnas adicionales de la tabla
    columns = [
        {"name": "name", "type": "CharField(max_length=255)"},
        {"name": "amount", "type": "DecimalField(max_digits=10, decimal_places=2)"},
        {"name": "description", "type": "TextField(null=True, blank=True)"}
    ]



    # Convertir singular_name y plural_name a kebab-case para las URLs
    singular_name_kebab = camel_to_kebab(singular_name)
    plural_name_kebab = camel_to_kebab(plural_name)
    singular_name_snake = camel_to_snake(singular_name)
    plural_name_snake = camel_to_snake(plural_name)


    # Verificar si la ruta proporcionada es válida
    if os.path.isdir(ruta):
        generate_model_file(ruta, singular_name, plural_name, columns, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake)
        generate_repository_file(ruta, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, namespace, app_name, columns)
        create_url_file(ruta, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, namespace, app_name)

        generate_controller_list_file(ruta, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, namespace, app_name)
        generate_controller_show_file(ruta, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, namespace, app_name)
        generate_controller_store_file(ruta, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, namespace, app_name)
        generate_controller_update_file(ruta, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, namespace, app_name)



    else:
        print("La ruta proporcionada no es válida o no existe. Por favor, verifica y vuelve a intentarlo.")
