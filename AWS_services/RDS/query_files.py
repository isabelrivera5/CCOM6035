# Imports
# Library
from Library.Params import RDS
from Library.RDS import connect_to_rds

# 3rd Party
import pymysql


def query_files(selections: dict):
    # Create Connection
    connection = connect_to_rds(RDS['DB_ENDPOINT'], RDS['DB_PORT'], RDS['DB_USERNAME'], RDS['DB_PASSWORD'], RDS['DB_IDENTIFIER'])

    # Initial query
    query = "SELECT * FROM tareas WHERE 1=1"  # 1=1 ensures that the WHERE clause is valid even when no conditions are added
    values = []

    # Add conditions to the query based on non-empty dictionary values
    if selections['materia']:
        query += " AND materia = %s"
        values.append(selections['materia'])

    if selections['grado']:
        query += " AND grado = %s"
        values.append(selections['grado'])

    if selections['destreza']:
        query += " AND destreza = %s"
        values.append(selections['destreza'])

    if selections['nivel']:
        query += " AND nivel = %s"
        values.append(selections['nivel'])

    # Add LIMIT 10 at the end
    query += " LIMIT 10;"

    try:
        with connection.cursor() as cursor:
            # Execute the query with the parameter
            print(query)
            cursor.execute(query, values)

            # Get all Results
            result = cursor.fetchall()

            return result

    except pymysql.MySQLError as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        if connection:
            connection.close()


if __name__ == "__main__":
    _tmp_selections = {'materia': '', 'grado': '', 'destreza': '', 'nivel': ''}
    response = query_files(_tmp_selections)
    print(response)