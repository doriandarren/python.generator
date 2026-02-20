import mysql.connector

def get_connection(host, user, password, database, port=3306):
    """
    Establishes and returns a connection to the MySQL database with given credentials.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            collation = "utf8mb4_general_ci",
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Connection error: {err}")
        return None