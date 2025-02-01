import json
import pprint
import sys

from database_connection import get_connection
##from php.main import generate
from helpers.helper_string import convert_word


def dd(data):
    pprint.pprint(data)
    sys.exit()



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
            print(f"\nTable: {table_name}")

            # Get column details for each table
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()

            for column in columns:
                print(f" - {column[0]} ({column[1]})")


            cols = [{"name":column[0]} for column in columns]


            table_name_format = convert_word(table_name)

            print(table_name_format['singular'])



            # generate(
            #     "API",
            #     "/Users/dorian/PhpstormProjects81/laravel_test/",
            #     table_name_format['singular'],
            #     table_name_format['plural'],
            #     cols
            # )

            dd("OK")



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
    database = "gtank"

    list_tables_and_columns(host, user, password, database)