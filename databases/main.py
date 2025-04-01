import os
from helpers.helper_print import input_with_validation, print_header
from databases.to_list.list_tables import list_tables_and_columns
from databases.to_generate.generate_tables_columns import list_tables_and_columns_and_generate
from dotenv import load_dotenv



load_dotenv()

if __name__ == "__main__":


    print_header("DATABASE")

    port = 3306
    database_name = "portuarios_api"
    password = ""

    generator_type = input_with_validation("[1]Listar - [2]Generar: ")
    input_db_type = input_with_validation("Basedatos [1]Local - [2]Docker(3307) - [3]Docker(3308): ")
    input_db_name = input("Nombre Basedatos [portuarios_api]: ")
    input_tables = input("Nombre(s) Tabla(s) [separado por espacio / vacio todos]: ")
    print("\n\n")


    if input_db_type.lower() == '1':
        port = 3306
        password = os.getenv("DATABASE_LOCAL_PASSWORD")
    elif input_db_type.lower() == '2':
        port = 3307
        password = os.getenv("DATABASE_DOCKER_PASSWORD")
    elif input_db_type.lower() == '3':
        port = 3308
        password = os.getenv("DATABASE_DOCKER_PASSWORD")





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
            port,
            input_tables
        )

    print("\n\nBye...")

