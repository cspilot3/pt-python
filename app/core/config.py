import os
from pydantic import BaseSettings

credentials = {
    "dbname": 'postgres',
    "user": 'admin123',
    "host": 'db-prueba-tecnica.postgres.database.azure.com',
    "password": 'a12345678*',
    "storage_cs": 'DefaultEndpointsProtocol=https;AccountName=pruebastoragecs;AccountKey=Al/eI3H2VqWEEzHBh1LUNCOzMe+vdnocHMxy8i6+52OcZuXBZb4qmUxWKsEKjhJ0J5CzmBsUXh8T+AStY+0wDg==;EndpointSuffix=core.windows.net',
    "container_name": 'blob-container'
}


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = f"postgresql+psycopg2://{credentials['user']}:{credentials['password']}@{credentials['host']}/{credentials['dbname']}"
    STORAGE_ACCOUNT_CS: str = credentials['storage_cs']
    CONTAINER_NAME: str = credentials['container_name']
    CONTAINER_NAME: str = "frontier-documents"
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "Prueba Tecnica - Python"
    DESCRIPTION: str = "Restful API"


settings = Settings()

