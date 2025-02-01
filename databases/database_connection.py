import mysql.connector

def get_connection(host, user, password, database):
    """
    Establishes and returns a connection to the MySQL database with given credentials.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            collation = "utf8mb4_general_ci"  # Usa una collation compatible
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Connection error: {err}")
        return None
