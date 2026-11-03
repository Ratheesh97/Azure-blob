import os
from azure.storage.blob import BlobServiceClient

try:
    # Azure Web App-ன் Environment Variable-ல் இருந்து பாதுகாப்பாக எடுக்கிறது
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

    if not connect_str:
        raise ValueError("Storage Connection String is missing!")

    # BlobServiceClient உருவாக்குதல்
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    # ஒரு புதிய கண்டெய்னர் உருவாக்குதல் (ஏற்கனவே இல்லை என்றால்)
    container_name = "staging-github-container"
    container_client = blob_service_client.get_container_client(container_name)
    if not container_client.exists():
        container_client.create_container()
        print(f"Container '{container_name}' created successfully!")
    
    # ஒரு சாம்பிள் டெக்ஸ்ட் ஃபைலை அப்லோட் செய்தல்
    blob_client = blob_service_client.get_blob_client(container=container_name, blob="staging-test.txt")
    blob_client.upload_blob("Hello! This file is uploaded from GitHub to Azure Staging Pipeline Automation.", overwrite=True)
    print("Test file uploaded successfully to Azure Blob Storage!")

except Exception as ex:
    print(f"Error occurred: {ex}")
