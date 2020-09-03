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

# Grab the Cosmos Credentials.
account_uri = config.get('azure_cosmos', 'account_host')
account_key = config.get('azure_cosmos', 'account_key')

# Initialize the client.
azure_pipeline_client = AzureSQLClient(
    client_id=client_id,
    client_secret=client_secret,
    subscription_id=subscription_id,
    tenant_id=tenant_id,
    username=server_username,
    password=server_password,
    cosmos_account_uri=account_uri,
    cosmos_account_key=account_key
)

# Grab the News Client.
finnews_client = azure_pipeline_client.news_client

# Set the Server Name.
azure_pipeline_client.server_name = 'trading-robot'

# Set the Database Name.
azure_pipeline_client.database_name = 'master'

# Set the Resource Group Name.
azure_pipeline_client.resource_group_name = 'sigma-coding-tutorials'

# Grab the server.
server = azure_pipeline_client.get_server()

# I can also grab it like this, if I didn't set the properties.
server = azure_pipeline_client.get_server(
    resource_group='sigma-coding-tutorials',
    server_name='trading-robot.database.windows.net'
)

# Grab the database.
database = azure_pipeline_client.get_database()

# I can also grab it like this, if I didn't set the properties..
database = azure_pipeline_client.get_database(
    resource_group='sigma-coding-tutorials',
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

# Define the query to create all the tables.
create_all_tables = """
IF Object_ID('news_articles_cnbc') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_cnbc]
(
    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [link] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [type] NVARCHAR(MAX) NULL,
    [article_id] NVARCHAR(MAX) NULL,
    [sponsored] NVARCHAR(MAX) NULL,
    [title] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL
);

IF Object_ID('news_articles_cnn') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_cnn]
(
    [news_id] NVARCHAR(MAX) NOT NULL,
    [news_source] NVARCHAR(MAX) NOT NULL,
    [link] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [thumbnail] NVARCHAR(MAX) NULL,
    [title] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL
);

IF Object_ID('news_articles_market_watch') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_market_watch]
(
    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [link] NVARCHAR(MAX) NULL,
    [origin_link] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [title] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL
);

IF Object_ID('news_articles_seeking_alpha') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_seeking_alpha]
(
    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [title] NVARCHAR(MAX) NULL,
    [link] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL,
    [category] NVARCHAR(MAX) NULL

);

IF Object_ID('news_articles_sp_global') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_sp_global]
(
    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [title] NVARCHAR(MAX) NULL,
    [link] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL,
    [source] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [category] NVARCHAR(MAX) NULL

);

IF Object_ID('news_articles_wsj') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_wsj]
(
    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [title] NVARCHAR(MAX) NULL,
    [link] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [encoded] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL,
    [category] NVARCHAR(MAX) NULL,
    [article_type] NVARCHAR(MAX) NULL

);

IF Object_ID('news_articles_yahoo_finance') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_yahoo_finance]
(
    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [title] NVARCHAR(MAX) NULL,
    [link] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [text] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL,
    [content] NVARCHAR(MAX) NULL,
    [article_type] NVARCHAR(MAX) NULL,
    [source] NVARCHAR(MAX) NULL,
    [credit] NVARCHAR(MAX) NULL

);

IF Object_ID('news_articles_nasdaq') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_nasdaq]
(
    [news_id] NVARCHAR(MAX) NOT NULL,
    [news_source] NVARCHAR(MAX) NOT NULL,
    [title] NVARCHAR(MAX) NULL,
    [link] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [creator] NVARCHAR(MAX) NULL,
    [category] NVARCHAR(MAX) NULL,
    [tickers] NVARCHAR(MAX) NULL,
    [partner_link] NVARCHAR(MAX) NULL
);
"""

# Create the table.
create_result = azure_pipeline_client.cursor_object.execute(
    create_all_tables
)
