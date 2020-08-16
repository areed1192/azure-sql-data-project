from azure.mgmt.sql import SqlManagementClient
from azure.common.client_factory import get_client_from_auth_file

# Grab the subscription client.
sql_management_client: SqlManagementClient = get_client_from_auth_file(
    client_class=SqlManagementClient,
    auth_path="config/azure_sigma_auth_sp.jsonc"
)

# Print out all the servers associated with my Subscription.
server = next(sql_management_client.servers.list())
print(server)
