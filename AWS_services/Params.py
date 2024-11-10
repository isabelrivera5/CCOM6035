# Default Shared Params
# AWS Account Region
REGION: str = 'us-east-1'

# RDS Params
RDS: dict[str, str | None | int]  = {
    'DB_INSTANCE_IDENTIFIER': 'asiste-tareas',
    'DB_ENDPOINT': None,
    'DB_PORT': 3306,
    'DB_USERNAME': 'admin',
    'DB_PASSWORD': None
}

S3: dict[str,str | None] = {
    'BUCKET_IDENTIFIER': None
}

# TODO Setup the VPC Security Group to only allow access from the Github Pages URL
