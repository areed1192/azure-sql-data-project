from configparser import ConfigParser
from azure.mgmt.sql import SqlManagementClient
from azure.common.client_factory import get_client_from_json_dict

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Grab the Azure Credentials needed.
subscription_id = config.get('azure_credentials', 'azure_subscription_id')
tenant_id = config.get('azure_credentials', 'azure_tenant_id')
client_id = config.get('azure_credentials', 'azure_client_id')
client_secret = config.get('azure_credentials', 'azure_client_secret')

# Define the configuration dictionary.
config_dict = {
    "subscriptionId": subscription_id,
    "tenantId": tenant_id,
    "clientId": client_id,
    "clientSecret": client_secret,
    "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
    "resourceManagerEndpointUrl": "https://management.azure.com/",
    "activeDirectoryGraphResourceId": "https://graph.windows.net/",
    "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
    "galleryEndpointUrl": "https://gallery.azure.com/",
    "managementEndpointUrl": "https://management.core.windows.net/"
}

# Grab the subscription client.
sql_management_client: SqlManagementClient = get_client_from_json_dict(
    client_class=SqlManagementClient,
    config_dict=config_dict
)

# Print out all the servers associated with my Subscription.
server = next(sql_management_client.servers.list())
print(server)
