from pprint import pprint
from configparser import ConfigParser

from azure_data_pipeline.client import AzureSQLClient

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Grab the Azure Management Credentials.
subscription_id = config.get('azure_credentials', 'azure_subscription_id')
tenant_id = config.get('azure_credentials', 'azure_tenant_id')
client_id = config.get('azure_credentials', 'azure_client_id')
client_secret = config.get('azure_credentials', 'azure_client_secret')

# Grab the Azure SQL Server Credentials.
server_username = config.get('server_info', 'administrator_login')
server_password = config.get('server_info', 'administrator_login_password')

# Initialize the client.
azure_pipeline_client = AzureSQLClient(
    client_id=client_id,
    client_secret=client_secret,
    subscription_id=subscription_id,
    tenant_id=tenant_id,
    username=server_username,
    password=server_password
)

# Set the Server Name.
azure_pipeline_client.server_name = 'trading-robot'

# Set the Database Name.
azure_pipeline_client.database_name = 'master'

# Set the Resource Group Name.
azure_pipeline_client.resource_group_name = 'resource_group_test'

# Grab the server.
server = azure_pipeline_client.get_server()

# I can also grab it like this, if I didn't set the properties.
server = azure_pipeline_client.get_server(
    resource_group='resource_group_test',
    server_name='trading-robot'
)

# Grab the database.
database = azure_pipeline_client.get_database()

# I can also grab it like this, if I didn't set the properties..
database = azure_pipeline_client.get_database(
    resource_group='resource_group_test',
    server_name='trading-robot',
    database_name='stock-financials'
)
print("DATABASE ID: {db_id}".format(db_id=database.database_id))
print("DATABASE NAME: {db_name}".format(db_name=database.name))

# Connect to the database.
database_connection = azure_pipeline_client.connect_to_database(
    server=server.name,
    database=database.name
)
print(database_connection)

# Perform a Query.
result = azure_pipeline_client.cursor_object.execute(
    "SELECT @@version;"
).fetchone()

# Print the results.
while result:
    print("Result: {res}".format(res=result[0]))
    result = azure_pipeline_client.cursor_object.fetchone()

# Here is another way to do the same Query.
cursor = database_connection.cursor()
result = cursor.execute("SELECT @@version;").fetchone()

# Print the results.
while result:
    print("Result: {res}".format(res=result[0]))
    result = cursor.fetchone()
