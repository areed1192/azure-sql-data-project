from pprint import pprint
from configparser import ConfigParser
from azure_data_pipeline.client import AzureSQLClient
from azure_data_pipeline.cosmos import AzureCosmosClient

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Grab the Azure Management Credentials.
account_uri = config.get('azure_cosmos', 'account_host')
account_key = config.get('azure_cosmos', 'account_key')

# Connect to a Cosmos Database.
pipeline_cosmos_client = AzureCosmosClient(
    account_uri=account_uri,
    account_key=account_key
)

# Grab a database.
cosmos_database = pipeline_cosmos_client.grab_database(
    database_name='FinancialNewsArticles'
)
print(cosmos_database.id)
print(cosmos_database.database_link)
print(cosmos_database.client_connection.url_connection)

# Grab a Container.
cosmos_container = pipeline_cosmos_client.grab_container(
    container_id='FinancialNewsContainer'
)
print(cosmos_container.id)
print(cosmos_container.container_link)
print(cosmos_container.client_connection)
