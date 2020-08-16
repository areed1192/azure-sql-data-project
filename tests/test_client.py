import pyodbc
import unittest

from unittest import TestCase
from configparser import ConfigParser

from azure.mgmt.sql import SqlManagementClient
from azure.common.credentials import ServicePrincipalCredentials
from azure_data_pipeline.client import AzureSQLClient


class AzurePipelineSession(TestCase):

    """Will perform a unit test for the `AzureSQLClient` session."""

    def setUp(self) -> None:
        """Set up the Client."""

        # Initialize the Parser.
        config = ConfigParser()

        # Read the file.
        config.read('config/config.ini')

        # Grab the Azure Credentials needed.
        subscription_id = config.get(
            'azure_credentials', 'azure_subscription_id'
        )
        tenant_id = config.get(
            'azure_credentials', 'azure_tenant_id'
        )
        client_id = config.get(
            'azure_credentials', 'azure_client_id'
        )
        client_secret = config.get(
            'azure_credentials', 'azure_client_secret'
        )

        # Grab the Azure SQL Server Credentials.
        server_username = config.get(
            'server_info', 'administrator_login'
        )

        server_password = config.get(
            'server_info', 'administrator_login_password'
        )

        # Initialize the client.
        self.azure_pipeline_client = AzureSQLClient(
            client_id=client_id,
            client_secret=client_secret,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            username=server_username,
            password=server_password
        )

    def test_creates_instance_of_session(self):
        """Create an instance and make sure it's a `AzureSQLClient`."""

        # Make sure we have an `AzureSQLClient`.
        self.assertIsInstance(self.azure_pipeline_client, AzureSQLClient)

    def test_create_credentials(self):
        """Test whether the Credentials Object was created."""

        # Make sure we have a Credential Object.
        self.assertIsNotNone(self.azure_pipeline_client.credentials)

        # Make sure it's a `ServicePrincipalCredentials`.
        self.assertIsInstance(
            self.azure_pipeline_client.credentials,
            ServicePrincipalCredentials
        )

    def test_create_sql_client(self):
        """Test whether the SQL Management Client Object was created."""

        # Make sure we have a SQL Management Client Object.
        self.assertIsNotNone(self.azure_pipeline_client.sql_management_client)

        # Make sure it's a `SqlManagementClient`.
        self.assertIsInstance(
            self.azure_pipeline_client.sql_management_client,
            SqlManagementClient
        )

    def test_server_name_property(self):
        """Test setting and grabbing the `server_name` property."""

        # Set the property.
        self.azure_pipeline_client.server_name = 'my_server'

        # Make sure it matches.
        self.assertEqual(
            'my_server',
            self.azure_pipeline_client._server_name
        )

        # Make sure it matches.
        self.assertEqual(
            'my_server',
            self.azure_pipeline_client.server_name
        )

    def test_database_name_property(self):
        """Test setting and grabbing the `database_name` property."""

        # Set the property.
        self.azure_pipeline_client.database_name = 'my_database'

        # Make sure it matches.
        self.assertEqual(
            'my_database',
            self.azure_pipeline_client._database_name
        )

        # Make sure it matches.
        self.assertEqual(
            'my_database',
            self.azure_pipeline_client.database_name
        )

    def test_resource_group_name_property(self):
        """Test setting and grabbing the `resource_group_name` property."""

        # Set the property.
        self.azure_pipeline_client.resource_group_name = 'my_resource_group'

        # Make sure it matches.
        self.assertEqual(
            'my_resource_group',
            self.azure_pipeline_client._resource_group
        )

        # Make sure it matches.
        self.assertEqual(
            'my_resource_group',
            self.azure_pipeline_client.resource_group_name
        )

    def test_grab_server(self):
        """Test grabbing the Server object."""

        # Grab the server.
        server_object = self.azure_pipeline_client.get_server(
            resource_group='resource_group_test',
            server_name='trading-robot'
        )

        # Make sure it matches.
        self.assertEqual(
            'trading-robot',
            server_object.name
        )

    def test_grab_database(self):
        """Test grabbing the Database object."""

        # Grab the server.
        database_object = self.azure_pipeline_client.get_database(
            resource_group='resource_group_test',
            server_name='trading-robot',
            database_name='master'
        )

        # Make sure it matches.
        self.assertEqual(
            'master',
            database_object.name
        )

    def test_create_connection(self):
        """Test creating a connection to the Database."""

        # Create a connection object.
        self.azure_pipeline_client.connect_to_database(
            server='trading-robot',
            database='master'
        )

        # Make sure a have a Connection object.
        self.assertIsInstance(
            self.azure_pipeline_client.connection_object,
            pyodbc.Connection
        )

        # Make sure a have a Cursor object.
        self.assertIsInstance(
            self.azure_pipeline_client.cursor_object,
            pyodbc.Cursor
        )

        # Close the connection.
        self.azure_pipeline_client.connection_object.close()

    def tearDown(self) -> None:
        """Teardown the `AzureSQLClient`."""

        del self.azure_pipeline_client


if __name__ == '__main__':
    unittest.main()
