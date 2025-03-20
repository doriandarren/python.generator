from databases.settings.connection import get_connection
from helpers.helper_string import convert_word
from php.to_api.generator import generate


def list_tables_and_columns_and_generate(host, user, password, database, port):
    """
    Generate Retrives and displays all tables along with their columns in the settings.
    """

    connection = get_connection(host, user, password, database, port)


    if connection is None:
        print("Failed to connect to the settings.")
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


