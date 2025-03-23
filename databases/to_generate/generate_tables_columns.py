from databases.settings.connection import get_connection
from helpers.helper_string import convert_word
from php.to_api.generator import generate
from helpers.helper_print import input_with_validation




def list_tables_and_columns_and_generate(host, user, password, database, port=3306, input_tables=None):
    """
    Generates code for all tables in the database or only for the specified tables.
    """

    full_path = "/Users/dorian/PhpstormProjects81/docker-laravel/projects/laravel_test/"


    input_full_path = input_with_validation(
        "Ruta del proyecto a Generar: [/Users/dorian/PhpstormProjects81/docker-laravel/projects/laravel_test/]: ")

    if input_full_path:
        full_path = input_full_path



    connection = get_connection(host, user, password, database, port)

    if connection is None:
        print("❌ Failed to connect to the database.")
        return

    cursor = connection.cursor()

    try:
        # Obtener todas las tablas disponibles en la base de datos
        cursor.execute("SHOW TABLES")
        tables = {table[0] for table in cursor.fetchall()}  # Convertir en un conjunto para búsqueda rápida

        # Si el usuario especificó tablas, filtrar solo esas
        if input_tables:
            input_tables_set = set(input_tables)  # `input_tables` ya es una lista
            tables_to_generate = tables.intersection(input_tables_set)  # Mantener solo las existentes
        else:
            tables_to_generate = tables  # Si no se especifican, generar para todas

        if not tables_to_generate:
            print("❌ No se encontraron las tablas especificadas.")
            return

        # Loop a través de las tablas seleccionadas
        for table_name in tables_to_generate:
            print(f"\n⚙️ Generando código para la tabla: {table_name}")

            # Obtener columnas de la tabla
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()

            # Mostrar detalles de las columnas
            for column in columns:
                print(f" - {column[0]} ({column[1]})")

            cols = [{"name": column[0]} for column in columns]

            table_name_format = convert_word(table_name)

            # Llamar al generador
            generate(
                "API",
                full_path,
                table_name_format['singular'],
                table_name_format['plural'],
                cols
            )

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
