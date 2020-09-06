import time
import textwrap
import datetime

from typing import List
from typing import Dict
from typing import Union

from azure.cosmos import documents
from azure.cosmos import cosmos_client
from azure.cosmos import ContainerProxy
from azure.cosmos import DatabaseProxy
from azure.cosmos import exceptions
from azure.cosmos.partition_key import PartitionKey

from azure.mgmt.resource import SubscriptionClient
from azure.common.credentials import ServicePrincipalCredentials

from finnews.client import News
from azure_data_pipeline.query import QueryBuilder


class AzureCosmosClient():

    def __init__(self, account_uri: str, account_key: str) -> None:
        """Initializes the `AzureCosmosClient` object.

        Arguments:
        ----
        account_uri (str): Your Azure Cosmos Account ID.

        account_key (str): Your Azure Cosmos Account Key.
        """

        self.connected = False
        self.authenticated = False

        # Define the client info.
        self.account_uri = account_uri
        self.account_key = account_key

        self._database_name = None
        self._database_client: DatabaseProxy = None

        self._container_name = None
        self._container_client: ContainerProxy = None

        # Create the News Client object.
        self._news_client = News()
        self._query_client: QueryBuilder = None

        self._cosmos_client: cosmos_client.CosmosClient = self.connect()
        self._cosmos_client_connection: cosmos_client.CosmosClientConnection = self._cosmos_client.client_connection

    def __repr__(self):
        """String representation of our `AzureSQLClient` instance."""

        # define the string representation
        str_representation = '<AzureCosmosClient (connected={login_state}, authorized={auth_state})>'.format(
            login_state=self.connected,
            auth_state=self.authenticated
        )

        return str_representation

    @property
    def news_client(self) -> News:
        """Returns the `NewsClient` object.

        Returns:
        ----
        News: A `NewsClient` object.
        """

        return self._news_client

    @property
    def query_client(self) -> QueryBuilder:
        """Returns the `QueryBuilder` client object.

        Returns:
        ----
        QueryBuilder: The query builder client.
        """

        # Initialize the Client.
        self._query_client = QueryBuilder()

        return self._query_client

    def connect(self) -> cosmos_client.CosmosClient:
        """Connects to the Cosmos Database.

        Returns:
        ----
        cosmos_client.CosmosClient: A cosmos client object.
        """

        client = cosmos_client.CosmosClient(
            url=self.account_uri,
            credential={"masterKey": self.account_key}
        )

        return client

    def grab_database(self, database_name: str) -> DatabaseProxy:
        """Used to query the a database using it's name.

        Arguments:
        ----
        database_name (str): The database name (ID).

        Returns:
        ----
        DatabaseProxy: A database proxy object which can be used to
            query other items.
        """

        # Set the name attribute.
        self._database_name = database_name

        # Get the database.
        database = self._cosmos_client.get_database_client(
            database=self._database_name
        )

        self._database_client = database

        return self._database_client

    def grab_container(self, container_id: str) -> ContainerProxy:
        """Used to grab a container from the database.

        Arguments:
        ----
        container_id (str): The name of the container (ID).

        Returns:
        ----
        ContainerProxy: A container proxy object.
        """

        container = self._database_client.get_container_client(
            container=container_id
        )

        self._container_client = container

        return self._container_client

    def upsert_article(self, article: dict) -> dict:
        """Used to upsert an article to our database.

        Arguments:
        ----
        article (dict): An article resource, in the form of
            a dictionary.

        Returns:
        ----
        dict: A dictionary representing the upserted item.
        """

        # Add the item.
        response = self._container_client.upsert_item(
            body=article
        )

        return response

    def grab_all_items(self, container_id: str) -> List[dict]:
        """Used to grab all the items from a container.

        Overview:
        ----
        If no container ID is speicified then will use the
        container queried from the `grab_container` method.

        Arguments:
        ----
        container_id (str): The name of the container (ID).

        Returns:
        ----
        (List[Dict]):  A collection of documents.
        """

        # Add the item.
        documents = self._container_client.read_all_items()

        return documents
