import os
from pydantic import BaseSettings

credentials = {
    "dbname": os.environ.get('DB_NAME'),
    "user": os.environ.get('DB_USER'),
    "host": os.environ.get('DB_HOST'),
    "password": os.environ.get('DB_PASSWORD'),
    "storage_cs": os.environ.get('STORAGE_CS'),
    "container_name": os.environ.get('CONTAINER_NAME')
}


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = f"postgresql+psycopg2://{credentials['user']}:{credentials['password']}@{credentials['host']}/{credentials['dbname']}"
    STORAGE_ACCOUNT_CS: str = credentials['storage_cs']
    CONTAINER_NAME: str = credentials['container_name']
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "Prueba Tecnica - Python"
    DESCRIPTION: str = """Sistema en el cual el usuario por medio de una archivo plano (.csv) cargue 
una plantilla de inventario aun DB PostgreSQL,\n El archivo es cargado a un BlobStorage de Azure y luego de su cargue se crean o actualizan los 
datos en el modelo de la DB """


settings = Settings()

