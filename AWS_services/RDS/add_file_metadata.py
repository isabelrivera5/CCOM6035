# Imports
# Library
from Library.Params import RDS
from Library.RDS import connect_to_rds

# 3rd Party
import pymysql


def add_file_metadata(values):
    # Create Connection
    connection = connect_to_rds(RDS['DB_ENDPOINT'], RDS['DB_PORT'], RDS['DB_USERNAME'], RDS['DB_PASSWORD'], RDS['DB_IDENTIFIER'])

    # Base SQL Query_String
    query = """INSERT INTO tareas (materia, grado, destreza, nivel, file_key, created_by) VALUES (%s, %s, %s, %s, %s, %s); """

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)  # Execute the query with the values
            connection.commit()  # Commit the transaction

    except pymysql.MySQLError as e:
        print(f"Error: {e}")
        return e

    finally:
        # Close the database connection
        if connection:
            connection.close()
            return 'success'


if __name__ == "__main__":
    _tmp_values = ('matematicas', 'grado 3', 'motor fino', 'nivel 1', '/uploads/some_file.jpeg', 'some_user_id_here')
    response = add_file_metadata(_tmp_values)
    print(response)