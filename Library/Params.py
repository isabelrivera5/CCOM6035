# Imports
# Built-In
import os

# Default Shared Params
# AWS Account Region
REGION: str = 'us-east-1'

LOCAL: bool = True

# RDS Params
if not LOCAL:
    RDS: dict[str, str | None | int]  = {
        'DB_IDENTIFIER': 'asiste-tareas',
        'DB_ENDPOINT': os.environ['DB_ENDPOINT'],
        'DB_PORT': int(os.environ['DB_PORT']),
        'DB_USERNAME': os.environ['DB_USERNAME'],
        'DB_PASSWORD': os.environ['DB_PASSWORD']
    }
else:
    RDS: dict[str, str | None | int]  = {
        'DB_IDENTIFIER': 'asiste-tareas',
        'DB_ENDPOINT': 'asiste-tareas-prod.c58a0wuwsogu.us-east-1.rds.amazonaws.com',
        'DB_PORT': 3306,
        'DB_USERNAME': 'admin',
        'DB_PASSWORD': 'HOGaKEkrh1d2WgGO3wzh'
    }

S3: dict[str,str | None] = {
    'BUCKET_IDENTIFIER': None
}
