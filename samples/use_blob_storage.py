import json
from pprint import pprint

from azure.identity import DefaultAzureCredential

from azure.storage.blob import BlobClient
from azure.storage.blob import ContainerClient
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobProperties
from azure.storage.blob import ContainerProperties

from azure.keyvault.secrets import SecretClient

# Initialize the Credentials.
default_credential = DefaultAzureCredential()

# Define the URL to our Blob Client Service.
account_url = 'https://sigmafunctionnews.blob.core.windows.net/'

# Create a Secret Client.
secret_client = SecretClient(
    vault_url='https://sigma-key-vault.vault.azure.net/',
    credential=default_credential
)

# Grab the Blob Connection String
blob_conn_string = secret_client.get_secret(
    name='blob-storage-connection-string'
)

# Connection: Method 1 - Connect to the `BlobServiceClient`.
blob_service_client = BlobServiceClient(
    account_url=account_url,
    credential=default_credential
)

# Connection: Method 2 - Connect to the `BlobServiceClient`.
blob_service_client = BlobServiceClient.from_connection_string(
    conn_str=blob_conn_string.value
)

# Connection: Method 3 - Connect to a `ContainerClient`.
container_client = ContainerClient.from_connection_string(
    conn_str=blob_conn_string.value,
    container_name='finance-news-articles'
)

# Connection: Method 4 - Connect to a `BlobClient`.
blob_client = BlobClient.from_connection_string(
    conn_str=blob_conn_string.value,
    container_name='finance-news-articles',
    blob_name='News Articles/cnbc_blog_news.jsonc'
)

# Grab the Account Properties, and print the details.
account_info = blob_service_client.get_service_properties()
pprint(account_info)

# Loop through each container.
for container in blob_service_client.list_containers():

    container_properties: ContainerProperties = container
    pprint(container_properties.items())

# Grab the Blob Container Client.
container_client = blob_service_client.get_container_client(
    'finance-news-articles'
)
print(container_client.container_name)

# Loop through each Blob in the Container.
for blob in container_client.list_blobs():

    blob_properties: BlobProperties = blob
    pprint(blob_properties.items())

# Grab a Blob.
blob_client = container_client.get_blob_client(
    'News Articles/cnbc_blog_news.jsonc'
)
print(blob_client.account_name)
print(blob_client.blob_name)

# Define a Destination File.
dest_file = 'samples/data_dumps/blob_dump.jsonc'

# Open a file.
with open(file=dest_file, mode='wb+') as my_blob:

    # Start the download.
    download_stream = blob_client.download_blob()

    # Write to the file.
    my_blob.write(download_stream.readall())

    content = json.loads(download_stream.readall())

# Load the Data.
blob_client.upload_blob(
    data=json.dumps(content),
    blob_type="BlockBlob",
    overwrite=True
)

# Create a new Blob.
container_client.upload_blob(
    name="News Articles/blob_data_cleaned",
    data=json.dumps(content),
    blob_type="BlockBlob"
)
