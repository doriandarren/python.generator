import pprint
import sys
import os
# Añadir la carpeta raíz del proyecto al sys.path
## sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helpers.helper_print import input_with_validation
from databases.to_list.list_tables import list_tables_and_columns
from databases.to_generate.generate_tables_columns import list_tables_and_columns_and_generate





if __name__ == "__main__":

    print("******************************************************")
    print("**********************  DATABASE   *******************")
    print("******************************************************")

    port = 3306
    database_name = "portuarios_api"
    password = ""
    full_path = "/Users/dorian/PhpstormProjects81/docker-laravel/projects/laravel_test/"

    generator_type = input_with_validation("[1]Listar - [2]Generar: ")
    input_db_type = input_with_validation("Basedatos [1]Local - [2]Docker: ")
    input_db_name = input("Nombre Basedatos [portuarios_api]: ")
    input_tables = input("Nombre(s) Tabla(s) [separado por espacio / vacio todos]: ")
    print("\n\n")


    if input_db_type.lower() == '1':
        port = 3306
        password = "123456"
    elif input_db_type.lower() == '2':
        port = 3307
        password = "root"

        input_full_path = input_with_validation("Ruta del proyecto a Generar: [/Users/dorian/PhpstormProjects81/docker-laravel/projects/laravel_test/]: ")

        if input_full_path:
            full_path = input_full_path





    if input_db_name:
        database_name = input_db_name

    # Convertir input_tables en lista, aunque sea un solo elemento
    input_tables = input_tables.split() if input_tables else []




    if generator_type.lower() == '1':
        list_tables_and_columns(
            "127.0.0.1",
            "root",
            password,
            database_name,
            port,
            input_tables
        )


    if generator_type.lower() == '2':
        list_tables_and_columns_and_generate(
            "127.0.0.1",
            "root",
            password,
            database_name,
            full_path,
            port,
            input_tables
        )

    print("\n\nBye...")

