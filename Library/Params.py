# Imports
# Built-In
import os

# Default Shared Params
# AWS Account Region
REGION: str = 'us-east-1'

# RDS Params
RDS: dict[str, str | None | int]  = {
    'DB_IDENTIFIER': 'asiste-tareas',
    'DB_ENDPOINT': os.environ['DB_ENDPOINT'],
    'DB_PORT': int(os.environ['DB_PORT']),
    'DB_USERNAME': os.environ['DB_USERNAME'],
    'DB_PASSWORD': os.environ['DB_PASSWORD']
}

S3: dict[str,str | None] = {
    'BUCKET_IDENTIFIER': None
}
