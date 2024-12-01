# Imports
# Library
from Library.Params import RDS
from Library.RDS import connect_to_rds

# 3rd Party
import pymysql


def query_files(sql_query_string: str):
    # Create Connection
    connection = connect_to_rds(RDS['DB_ENDPOINT'], RDS['DB_PORT'], RDS['DB_USERNAME'], RDS['DB_PASSWORD'], RDS['DB_IDENTIFIER'])

    try:
        with connection.cursor() as cursor:
            # Execute the query with the parameter
            cursor.execute(sql_query_string)

            # Get all Results
            result = cursor.fetchall()

            # TODO Once Decided on Results Limit, we can Limit number of results returned with LIMIT N

            return result

    except pymysql.MySQLError as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        if connection:
            connection.close()


if __name__ == "__main__":
    sql_string = "SELECT * FROM users LIMIT 1"
    response = query_files(sql_string)
    print(response)