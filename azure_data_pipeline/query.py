
import time
import json
import pyodbc
import textwrap

from typing import List
from typing import Dict
from typing import Union
from typing import Any


class QueryBuilder():

    def __init__(self, azure_connection: pyodbc.Connection, azure_cursor: pyodbc.Cursor, azure_client: object) -> None:
        """Initializes the `QueryBuilder` object."""

        from azure_data_pipeline.client import AzureSQLClient

        self.connected = True
        self.authenticated = True
        self.azure_connection = azure_connection
        self.azure_cursor = azure_cursor
        self.azure_client: AzureSQLClient = azure_client

        with open(file='azure_data_pipeline/fields.jsonc', mode='r') as fields:
            self.fields = json.load(fp=fields)

    def set_executemany_fast(self) -> None:
        """Sets the Cursor to execute Insert Queries in a fast manner."""

        self.azure_cursor.fast_executemany = True

    def __repr__(self):
        """String representation of our `QueryBuilder` instance."""

        # define the string representation
        str_representation = '<QueryBuilder (connected={login_state}, authorized={auth_state})>'.format(
            login_state=self.connected,
            auth_state=self.authenticated
        )

        return str_representation

    def grab_column_names(self, table_name: str) -> str:
        """Returns the column names from a table in Insert Format.

        Arguments:
        ----
        table_name (str): The table to grab column names from.

        Returns:
        ----
        str: The column names from the table organized for an Insert query.
        """

        # Grab the table Column Names.
        column_names = """
        SELECT [COLUMN_NAME]
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = N'{tbl_name}'
        """.format(tbl_name=table_name)

        # Create the Column Names.
        column_names = ','.join(
            [
                '[{name}]'.format(name=item[0])
                for item in self.azure_cursor.execute(column_names)
            ]
        )

        return column_names

    def sanitize_row(self, row: dict) -> Dict:
        """Removes all characters from the string that will cause Insert Issues.

        Arguments:
        ----
        row (dict): A row of elements in the form of a dictionary.

        Returns:
        Dict: A cleaned row.
        """

        for row_key in row:

            # If we have a string, remove the bad characters.
            if isinstance(row[row_key], str):

                row[row_key] = row[row_key].replace(',', '')
                row[row_key] = row[row_key].replace('"', "")
                row[row_key] = row[row_key].replace("'", "")

        return row

    def remove_empty_keys(self, source: str, row: dict) -> Dict:
        """Removes Keys that aren't to be inserted.

        Arguments:
        ----
        source (str): The News Client source of the articles.

        row (dict): A row representing a single News article, as a dictionary.

        Returns:
        ----
        Dict: A dictionary with the keys removed.
        """

        # Remove Unecessary Keys.
        for key_to_remove in self.fields[source]['removes']:
            row.pop(key_to_remove)

        return row

    def build_placeholders(self, row: tuple) -> str:
        """Builds the placeholders (?,), used in an insert Query.

        Arguments:
        ----
        row (tuple): An example of a row to be inserted.

        Returns:
        ----
        str: The placeholder, with number of needed elements.
        """

        # Define the number of elements.
        num_of_elements = len(row)

        # Create the place holders.
        placeholders = '?, '*num_of_elements

        # Cleanup the ending characters.
        placeholders = placeholders[:-2]

        return placeholders

    def build_recordset(self, data: List[dict], source: str) -> List[tuple]:
        """Used to build the recordset from a List of dictionaries.

        Arguments:
        ----
        data (List[dict]): The raw data in JSON form.

        source (str): The News Client source from which the data originated.

        Returns:
        ----
        List[tuple]: A list of sanitized tuples.
        """

        # Grab the Default values used in every query.
        source_name = self.fields[source]['source']
        source_id = self.fields[source]['id']

        records = []

        # Loop through each article.
        for article in data:

            # Remove the empty keys.
            article = self.remove_empty_keys(
                source=source,
                row=article
            )

            # Remove bad characters.
            article = self.sanitize_row(
                row=article
            )

            # Define the Source Specific Elements.
            default_elem = [article[source_id], source_name]

            # Define the row.
            new_row = default_elem + list(article.values())

            records.append(tuple(new_row))

        return records

    def dict_to_query(self, source: str, content: List[dict], table_name: str) -> tuple:
        """Converts a Dictionary to an Insert Query.

        Arguments:
        ----
        source (str): The News Source of the articles.

        content (List[dict]): The JSON content returned from the feed.

        table_name (str): The table where the data is being inserted.

        Returns:
        ----
        tuple: A tuple where the first element is the query, and the second element is the records.
        """

        # Create the records.
        records = self.build_recordset(data=content, source=source)

        # Define the Column Names.
        column_names = self.grab_column_names(table_name=table_name)

        # Define the place holders.
        placeholders = self.build_placeholders(row=records[0])

        # Define the Insert Query.
        insert_query = textwrap.dedent("""
        INSERT INTO [dbo].[{table_name}]
            (
                {column_names}
            )
        VALUES
            (
                {record_tuples}
            )
        """.format(
            table_name=table_name,
            column_names=column_names,
            record_tuples=placeholders
        ))

        return (insert_query, records)
