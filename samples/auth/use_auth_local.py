from pprint import pprint
from configparser import ConfigParser

from azure.mgmt.sql import SqlManagementClient
from azure.mgmt.resource import SubscriptionClient
from azure.common.credentials import ServicePrincipalCredentials

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Grab the Azure Credentials needed.
subscription_id = config.get('azure_credentials', 'azure_subscription_id')
tenant_id = config.get('azure_credentials', 'azure_tenant_id')
client_id = config.get('azure_credentials', 'azure_client_id')
client_secret = config.get('azure_credentials', 'azure_client_secret')

# Define the Credentials.
credential = ServicePrincipalCredentials(
    tenant=tenant_id,
    client_id=client_id,
    secret=client_secret
)

# Pass through the credential.
subscription_client = SubscriptionClient(credential)

# Grab the Subscription.
subscription = next(subscription_client.subscriptions.list())
print(subscription.subscription_id)

# Initialize the SQL Management Client.
sql_management_client = SqlManagementClient(
    credentials=credential,
    subscription_id=subscription_id
)

# Grab a server using the Resource Group Name.
server = sql_management_client.servers.get(
    resource_group_name='resource_group_test',
    server_name='trading-robot'
)
print(server)

# Grab the master database from the `trading-robot` server.
database = sql_management_client.databases.get(
    resource_group_name='resource_group_test',
    server_name='trading-robot',
    database_name='master'
)
print(database)
print(database.name)
print(database.id)
print(database.status)

# Create a new database called `financial-news` on the `trading-robot` server.
operation_result = sql_management_client.databases.create_or_update(
    resource_group_name='resource_group_test',
    server_name='trading-robot',
    database_name='financial-news',
    parameters={
        'location': 'eastus'
    }
)
print(operation_result.result())

# Delete a database from my server.
operation_result = sql_management_client.databases.delete(
    resource_group_name='resource_group_test',
    server_name='trading-robot',
    database_name='financial-news'
)
