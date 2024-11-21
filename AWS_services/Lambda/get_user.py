# Imports
# Built-In
import json
from datetime import datetime

# Library
from Library.Params import RDS
from Library.RDS import connect_to_rds

# 3rd Party
import pymysql

# TODO Move to Utils
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super(DateTimeEncoder, self).default(obj)


def lambda_handler(event, context):
    # Provide your database credentials
    db_username = RDS['DB_USERNAME']
    db_password = RDS['DB_PASSWORD']
    endpoint = RDS['DB_ENDPOINT']
    port = RDS['DB_PORT']
    database = RDS['DB_IDENTIFIER']

    # Extract user_id to find
    user_id = event['queryStringParameters']['user_id']

    # Create Connection
    connection = connect_to_rds(endpoint, port, db_username, db_password, database)

    try:
        with connection.cursor() as cursor:
            # Prepare the SQL query to fetch the first row
            query = "SELECT * FROM users WHERE email = %s LIMIT 1"

            # Execute the query with the parameter
            cursor.execute(query, (user_id,))

            # Fetch the first matching row
            result = cursor.fetchone()

            # Check if a result was found
            if result:
                # Return the Data for the given user
                return {
                    "isBase64Encoded": False,
                    'statusCode': 200,
                    'body': json.dumps(result, cls=DateTimeEncoder)
                }
            else:
                # Return status code 204 No Content
                return {
                    "isBase64Encoded": False,
                    'statusCode': 204,
                    'body': json.dumps(result, cls=DateTimeEncoder)
                }


    except pymysql.MySQLError as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        if connection:
            connection.close()


if __name__ == "__main__":
    test_event = {'queryStringParameters': {'user_id': 'jgwilson1997@gmail.com'}}
    response = lambda_handler(test_event, None)
    print(response)