import json
from pprint import pprint
from configparser import ConfigParser
from azure_data_pipeline.client import AzureSQLClient
from azure_data_pipeline.cosmos import AzureCosmosClient

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read("config/config.ini")

# Grab the Azure Management Credentials.
account_uri = config.get("azure_cosmos", "account_host")
account_key = config.get("azure_cosmos", "account_key")

# Connect to a Cosmos Database.
pipeline_cosmos_client = AzureCosmosClient(
    account_uri=account_uri,
    account_key=account_key
)

# Grab a database.
cosmos_database = pipeline_cosmos_client.grab_database(
    database_name="FinancialNewsArticles"
)
print(cosmos_database.id)
print(cosmos_database.database_link)
print(cosmos_database.client_connection.url_connection)
print('')

# Grab a Container.
cosmos_container = pipeline_cosmos_client.grab_container(
    container_id="FinanceNewsContainer"
)
print(cosmos_container.id)
print(cosmos_container.container_link)
print(cosmos_container.client_connection.url_connection)
print('')

# Grab the News Client.
cnbc_client = pipeline_cosmos_client.news_client.cnbc

# Grab the Query Client.
query_client = pipeline_cosmos_client.query_client

# Grab the top news.
top_news = cnbc_client.news_feed(topic="top_news")

# Build the Insert Query and Recordset.
records = query_client.dict_to_cosmos_query(
    source="cnbc",
    content=top_news
)

# Loop through the records.
for record in records:

    # Upsert the item.
    response = pipeline_cosmos_client.upsert_article(article=record)

    pprint(response)

# Grab the articles, this returns a paged item.
articles = pipeline_cosmos_client.grab_all_items(
    container_id="FinanceNewsContainer"
)

# Convert it to a list.
articles = [item for item in articles]

# Save to a file.
with open(file='samples/data_dumps/articles.jsonc', mode='w+') as json_file:
    json.dump(obj=articles, fp=json_file, indent=2)
