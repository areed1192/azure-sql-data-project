import time
import textwrap
import datetime

from typing import List
from typing import Dict
from typing import Union

from finnews.client import News

from azure.cosmos import documents
from azure.cosmos import cosmos_client
from azure.cosmos import ContainerProxy
from azure.cosmos import DatabaseProxy
from azure.cosmos import exceptions
from azure.cosmos.partition_key import PartitionKey

from azure.mgmt.resource import SubscriptionClient
from azure.common.credentials import ServicePrincipalCredentials

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
        self._container_client: ContainerProxy = cosmos_client

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

    def connect(self) -> None:

        client = cosmos_client.CosmosClient(
            url=self.account_uri,
            credential=self.account_key
        )

        return client

    def grab_database(self, database_name: str):

        self._database_name = database_name
        
        database = self._cosmos_client.get_database_client(
            database=self._database_name
        )

        self._database_client = database

        return self._database_client

    def grab_container(self, container_id: str):

        container = self._database_client.get_container_client(
            container=container_id
        )

        self._container_client = container

        return self._container_client
