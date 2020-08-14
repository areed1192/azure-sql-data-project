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

# Grab the Server.
server = next(sql_management_client.servers.list())
print(server)