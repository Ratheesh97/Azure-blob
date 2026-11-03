import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

try:
    # Azure Portal-ல் இருந்து உங்களது Connection String-ஐ இங்கே கொடுக்க வேண்டும்
    connect_str = "உங்களுடைய_CONNECTION_STRING_இங்கே_போடவும்"
    
    # BlobServiceClient உருவாக்குதல்
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    # ஒரு புதிய கண்டெய்னர் உருவாக்குதல்
    container_name = "github-test-container"
    container_client = blob_service_client.create_container(container_name)
    print(f"Container '{container_name}' created successfully!")
    
    # ஒரு டெக்ஸ்ட் ஃபைலை அப்லோட் செய்தல்
    blob_client = blob_service_client.get_blob_client(container=container_name, blob="sample.txt")
    blob_client.upload_blob("Hello from GitHub and Azure Blob Storage!")
    print("File uploaded successfully!")

except Exception as ex:
    print(f"Error: {ex}")
