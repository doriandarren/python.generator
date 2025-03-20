from databases.settings.connection import get_connection
from helpers.helper_string import convert_word

def list_tables_and_columns(host, user, password, database, port=3306, input_tables=None):
    """
    Retrieves and displays all tables along with their columns in the database.
    """

    connection = get_connection(host, user, password, database, port)

    if connection is None:
        print("❌ Failed to connect to the database.")
        return

    cursor = connection.cursor()

    try:
        # Obtener todas las tablas
        cursor.execute("SHOW TABLES")
        tables = {table[0] for table in cursor.fetchall()}  # Convertir en set para búsqueda rápida



        # Si el usuario especificó tablas, filtrar solo esas
        if input_tables:
            input_tables_set = set(input_tables) # Convertir entrada del usuario en un set
            tables_to_list = tables.intersection(input_tables_set)  # Mantener solo las que existen en la BD
        else:
            tables_to_list = tables  # Si no se especifican, listar todas

        if not tables_to_list:
            print("❌ No se encontraron las tablas especificadas.")
            return


        # Recorrer y procesar cada tabla seleccionada
        for table_name in tables_to_list:
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()

            # Filtrar columnas no deseadas
            filtered_columns = [column[0] for column in columns if column[0] not in {"id", "created_at", "updated_at", "deleted_at"}]

            # Convertir nombre de tabla a singular/plural
            table_name_format = convert_word(table_name)

            # Mostrar el resultado
            print(f"[{table_name}] {table_name_format['singular']} *** {table_name_format['plural']} : {' '.join(filtered_columns)}")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
