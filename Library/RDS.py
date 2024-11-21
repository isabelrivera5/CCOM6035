# Imports
# 3rd Party
import pymysql

# Connect to the RDS MySQL database
def connect_to_rds(_endpoint, _port, username, password, database):
    try:
        _connection = pymysql.connect(
            host=_endpoint,
            port=_port,
            user=username,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connection to RDS MySQL instance successful!")
        return _connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to database: {e}")
        return None

# List all databases in the connected MySQL RDS instance
def list_databases(_connection):
    try:
        with _connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES;")
            databases = cursor.fetchall()
            print("Databases on the RDS MySQL instance:")
            for db in databases:
                print(db[0])
    except pymysql.MySQLError as e:
        print(f"Error executing query: {e}")
