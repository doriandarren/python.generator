import pprint
import sys
import os  # Importar os para trabajar con rutas

# Añadir la carpeta raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database_connection import get_connection
from helpers.helper_string import convert_word
from helpers.helpers import dd

from php.main import generate


def list_tables_and_columns(host, user, password, database):
    """
    Retrives and displays all tables along with their columns in the database.
    """

    connection = get_connection(host, user, password, database)

    if connection is None:
        print("Failed to connect to the database.")
        return

    cursor = connection.cursor()

    try:

        # Get all tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        # Loop through each table to get its columns
        for (table_name,) in tables:

            #if table_name == 'items':

            # Get column details for each table
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()

            c = ''

            for column in columns:
                # print(f" - {column[0]} ({column[1]})")

                if column[0] not in {"created_at", "updated_at", "deleted_at"}:
                    c = c + column[0] + " "

            table_name_format = convert_word(table_name)

            print(f"{table_name_format['singular']} / {table_name_format['plural']} {table_name}: {c}")


    except Exception as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()




def list_tables_and_columns_and_generate(host, user, password, database):
    """
    Generate Retrives and displays all tables along with their columns in the database.
    """

    connection = get_connection(host, user, password, database)


    if connection is None:
        print("Failed to connect to the database.")
        return

    cursor = connection.cursor()

    try:

        # Get all tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()


        # Loop through each table to get its columns
        for (table_name,) in tables:
            print(f"\nTable: {table_name}")

            # Get column details for each table
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()

            for column in columns:
                print(f" - {column[0]} ({column[1]})")

            cols = [{"name":column[0]} for column in columns]

            table_name_format = convert_word(table_name)

            generate(
                "API",
                "/Users/dorian/PhpstormProjects81/laravel_test/",
                table_name_format['singular'],
                table_name_format['plural'],
                cols
            )




    except Exception as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()









if __name__ == "__main__":

    # Your credentials
    host = "127.0.0.1"
    user = "root"
    password = "123456"
    database = "portuarios_api"

    ## Listar Tablas solamente
    list_tables_and_columns(host, user, password, database)


    ## Listar Tablas y Columnas y Generar
    ## list_tables_and_columns_and_generate(host, user, password, database)