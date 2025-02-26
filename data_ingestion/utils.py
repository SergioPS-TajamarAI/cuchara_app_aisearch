from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

from cuchara_webapp import settings

BLOB_CLIENT = settings.BLOB_CLIENT 
BLOB_KEY = settings.BLOB_KEY
BLOB_CONTAINER = settings.BLOB_CONTAINER

def get_container_client():
    blob_service_client = BlobServiceClient(account_url=BLOB_CLIENT, credential=BLOB_KEY)
    container_client = blob_service_client.get_container_client(BLOB_CONTAINER)
    if not container_client.exists():
        container_client.create_container()
    return container_client

def upload_file_to_blob_storage(file, blob_name, company):
    try:
        container_client = get_container_client()
        # Create a blob client using the local file name as the name for the blob
        blob_client = container_client.get_blob_client(blob=blob_name)
        
        # Upload the file with metadata
        blob_client.upload_blob(file.read(), metadata={'company_name': company.name, 'longitude': str(company.longitude), 'latitude': str(company.latitude)})
        
        print(f"File uploaded to blob storage as {blob_name}")
        return blob_client.url
    except Exception as ex:
        print(f"Exception: {ex}")
        return None

def blob_exists(blob_name):
    try:
        container_client = get_container_client()
        blob_client = container_client.get_blob_client(blob=blob_name)
        return blob_client.exists()
    except Exception as ex:
        print(f"Exception: {ex}")
        return False

def get_pdf(file_name):
    blob_service_client = BlobServiceClient(account_url=settings.BLOB_CLIENT, credential=settings.BLOB_KEY)
    container_client = blob_service_client.get_container_client(settings.BLOB_CONTAINER)
    blob_client = container_client.get_blob_client(file_name)
    download_stream = blob_client.download_blob()
    return download_stream.readall()

