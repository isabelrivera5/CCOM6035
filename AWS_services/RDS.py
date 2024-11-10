# Imports
# Built In
from Params import REGION, RDS

# 3rd Party
import boto3
import pymysql
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Extract Top Level DB Identifier for DB Connection
DB_INSTANCE_IDENTIFIER: str = RDS['DB_INSTANCE_IDENTIFIER']

# Get the RDS instance endpoint and credentials from boto3
# NOTE: this requires an actual configured AWS Credentials File, won't be used most of the time except for DEV Purposes
def get_rds_endpoint(instance_identifier: str):
    rds_client = boto3.client('rds', region_name=REGION)
    try:
        response = rds_client.describe_db_instances(DBInstanceIdentifier=instance_identifier)
        _endpoint = response['DBInstances'][0]['Endpoint']['Address']
        _port = response['DBInstances'][0]['Endpoint']['Port']
        return _endpoint, _port
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error: {e}")
        return None, None
    except Exception as e:
        print(f"Error retrieving RDS instance info: {e}")
        return None, None

# Connect to the RDS MySQL database
def connect_to_rds(_endpoint, _port, username, password):
    try:
        _connection = pymysql.connect(
            host=_endpoint,
            port=_port,
            user=username,
            password=password,
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

# Example usage
if __name__ == "__main__":
    # Provide your database credentials
    db_username = RDS['DB_USERNAME']
    db_password = RDS['DB_PASSWORD']

    # Get the RDS instance endpoint and port
    if not RDS['DB_PORT'] and not RDS['DB_ENDPOINT']:
        endpoint, port = get_rds_endpoint(DB_INSTANCE_IDENTIFIER)
    else:
        endpoint = RDS['DB_ENDPOINT']
        port = RDS['DB_PORT']

    if endpoint and port:
        # Connect to the RDS MySQL instance
        connection = connect_to_rds(endpoint, port, db_username, db_password)

        if connection:
            # List all databases
            list_databases(connection)

            # Close the connection
            connection.close()
