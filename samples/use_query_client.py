import textwrap

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

# Connect to the database.
azure_pipeline_client.connect_to_database(
    server='trading-robot',
    database='stock-financials'
)

# Grab the News Client.
cnbc_client = azure_pipeline_client.news_client.cnbc

# Grab the Query Client.
query_client = azure_pipeline_client.query_client

# Grab the top news.
top_news = cnbc_client.news_feed(topic='top_news')

# Build the Insert Query and Recordset.
query_and_records = query_client.dict_to_query(
    source='cnbc',
    content=top_news,
    table_name='news_articles_cnbc'
)

# Insert the data.
query_client.azure_cursor.executemany(
    query_and_records[0],
    query_and_records[1]
)

# sql = "INSERT INTO product (item, price) VALUES (?, ?)"
# params = [('bicycle', 499.99), ('ham', 17.95)]
# # specify that parameters are for NVARCHAR(50) and DECIMAL(18,4) columns
# crsr.setinputsizes([(pyodbc.SQL_WVARCHAR, 50, 0), (pyodbc.SQL_DECIMAL, 18, 4)])
# crsr.executemany(sql, params)