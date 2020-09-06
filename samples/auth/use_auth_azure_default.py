from pprint import pprint
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Create the Azure Default Credentials.
#  -------------------
#  Optional Arguments:
#  -------------------
#       1. exclude_cli_credential (bool) – Whether to exclude the Azure CLI from the credential.
#           Defaults to False.
#       2. exclude_environment_credential (bool) – Whether to exclude a service principal configured by environment variables from the credential.
#           Defaults to False.
#       3. exclude_managed_identity_credential (bool) – Whether to exclude managed identity from the credential.
#           Defaults to False.
#       4. exclude_visual_studio_code_credential (bool) – Whether to exclude stored credential from VS Code.
#           Defaults to False.
#       5. exclude_shared_token_cache_credential (bool) – Whether to exclude the shared token cache.
#           Defaults to False.
#       6. exclude_interactive_browser_credential (bool) – Whether to exclude interactive browser authentication (see InteractiveBrowserCredential).
#           Defaults to True.

# Initialize the Credentials.
default_credential = DefaultAzureCredential()

# Define the URL to our Blob Service.
account_url = "https://sigmafunctionnews.blob.core.windows.net/"

# Connect to the Blob Service Client.
blob_service_client = BlobServiceClient(
    account_url=account_url,
    credential=default_credential
)

# Grab the Account Properties, and print the details.
account_info = blob_service_client.get_service_properties()
pprint(account_info)
