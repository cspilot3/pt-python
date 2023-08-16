from fastapi import File, UploadFile
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from app.core.config import settings

def upload_file_to_blob_storage(file: UploadFile, client_code: str) -> (bool, str):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(settings.STORAGE_ACCOUNT_CS)
        container_client = blob_service_client.get_container_client(settings.CONTAINER_NAME)
        
        client_folder = f"unprocessed-files/{client_code}"
        file.file.seek(0)
        container_client.upload_blob(client_folder + "/" + file.filename, file.file.read(), overwrite=True)
        
        return True, ""
    except Exception as e:
        return False, f"Error al subir el archivo al Blob Storage: {str(e)}"
    
    
def move_blob_within_storage(source_blob_path: str, destination_blob_path: str):
    blob_service_client = BlobServiceClient.from_connection_string(settings.STORAGE_ACCOUNT_CS)
    source_blob_client = blob_service_client.get_blob_client(container=settings.CONTAINER_NAME, blob=source_blob_path)
    destination_blob_client = blob_service_client.get_blob_client(container=settings.CONTAINER_NAME, blob=destination_blob_path)
    
    destination_blob_client.start_copy_from_url(source_blob_client.url)
    source_blob_client.delete_blob()

def move_blob_to_processed_folder(filename: str, gln_cliente: str):
    try:
        source_blob_path = f"unprocessed-files/{gln_cliente}/{filename}"
        destination_blob_path = f"processed-files/{gln_cliente}/{filename}"
        move_blob_within_storage(source_blob_path, destination_blob_path)
        return True, ""
    except Exception as e:
        return False, f"Error al mover el archivo en el Blob Storage: {str(e)}"
