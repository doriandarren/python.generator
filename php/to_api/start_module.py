from helpers.helper_print import input_with_validation
from php.to_api.generator import generate


def start_module():

    ruta = input_with_validation("Proyecto ", "/Users/dorian/PhpstormProjects81/docker-laravel/projects/laravel_test/")
    namespace = input_with_validation("Namespace (ERP / API / INVOICES) ", "API")
    singular_name = input_with_validation("Tabla singular (EX: AgendaUnloading): ", None)
    plural_name = input_with_validation("Tabla plural (EX: AgendaUnloadings): ", None)
    input_columns = input_with_validation("Columnas (separdo por espacio): ", None)

    columns = [{"name": column} for column in input_columns.split()]

    generate(namespace, ruta, singular_name, plural_name, columns)