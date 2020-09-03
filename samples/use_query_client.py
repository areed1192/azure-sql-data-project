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

# Grab the News Client.
cnn_finance_client = azure_pipeline_client.news_client.cnn_finance

# Grab the news topic.
content = cnn_finance_client.colleges()

# Build the Insert Query and Recordset.
query_and_records = query_client.dict_to_query(
    source='cnn',
    content=content,
    table_name='news_articles_cnn'
)

# Insert the data.
query_client.azure_cursor.executemany(
    query_and_records[0],
    query_and_records[1]
)

# Grab the News Client.
market_watch_finance_client = azure_pipeline_client.news_client.market_Watch

# Grab the news topic.
content = market_watch_finance_client.banking_and_finance()

# Build the Insert Query and Recordset.
query_and_records = query_client.dict_to_query(
    source='market_watch',
    content=content,
    table_name='news_articles_market_watch'
)

# Insert the data.
query_client.azure_cursor.executemany(
    query_and_records[0],
    query_and_records[1]
)

# Grab the News Client.
seeking_alpha_client = azure_pipeline_client.news_client.seeking_alpha

# Grab the news topic.
content = seeking_alpha_client.editors_picks()

# Build the Insert Query and Recordset.
query_and_records = query_client.dict_to_query(
    source='seeking_alpha',
    content=content,
    table_name='news_articles_seeking_alpha'
)

# Insert the data.
query_client.azure_cursor.executemany(
    query_and_records[0],
    query_and_records[1]
)

# Grab the News Client.
sp_global_client = azure_pipeline_client.news_client.sp_global

# Grab the news topic.
content = sp_global_client.corporate_news()

# Build the Insert Query and Recordset.
query_and_records = query_client.dict_to_query(
    source='sp_global',
    content=content,
    table_name='news_articles_sp_global'
)

# Insert the data.
query_client.azure_cursor.executemany(
    query_and_records[0],
    query_and_records[1]
)

# Grab the News Client.
nasdaq_client = azure_pipeline_client.news_client.nasdaq

# Grab the news topic.
content = nasdaq_client.commodities_feed()

# Build the Insert Query and Recordset.
query_and_records = query_client.dict_to_query(
    source='nasdaq',
    content=content,
    table_name='news_articles_nasdaq'
)

# Insert the data.
query_client.azure_cursor.executemany(
    query_and_records[0],
    query_and_records[1]
)

# print(query_and_records[0])
# pprint(query_and_records[1])

# for record in query_and_records[1]:
#     print(len(record))
#     pprint(tuple(record._asdict().values()))

# sql = "INSERT INTO product (item, price) VALUES (?, ?)"
# params = [('bicycle', 499.99), ('ham', 17.95)]
# # specify that parameters are for NVARCHAR(50) and DECIMAL(18,4) columns
# crsr.setinputsizes([(pyodbc.SQL_WVARCHAR, 50, 0), (pyodbc.SQL_DECIMAL, 18, 4)])
# crsr.executemany(sql, params)
