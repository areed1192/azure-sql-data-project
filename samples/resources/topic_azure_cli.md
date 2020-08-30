# Using the Azure CLI

## Subscription Management

To access the resources for a subscription, switch your active subscription or use the `--subscription argument`. Switching your
subscription for all commands is done with az account set. To switch your active subscription:

To Get a list of your subscriptions with the `az account` use the following command:

```bash
az account list --output table
```

The output should be a table with the subscriptions that are associated with your account.

```bash
Name           CloudName    SubscriptionId                        State    IsDefault
-------------  -----------  ------------------------------------  -------  -----------
<SUB NAME>     AzureCloud   <THIS WILL BE YOUR SUBSCRIPTION ID>   Enabled  True
```

Use `az account set` command with the **subscription ID or name** you want to switch to.

```bash
az account set --subscription "MyOtherSubscription"
```

To run only a single command with a different subscription, use the --subscription argument. This argument takes either a
subscription ID or subscription name:

```bash
az vm create --subscription "MyOtherSubscription" --resource-group MyGroup --name NewVM --image Ubuntu
```

## Service Prinicapls

### Overview

As described in [How to manage service principals - Basics of authorization](https://docs.microsoft.com/en-us/azure/developer/python/how-to-manage-service-principals#basics-of-azure-authorization), each developer needs a service principal to use as the application
identity when testing app code locally.

The following sections describe how to create a service principal and the environment variables that provide the service principal's properties
to the Azure libraries when needed. Each developer in your organization should perform these steps individually.

### Step 1: Login to the Azure CLI

In a terminal or command prompt, sign in to your Azure subscription:

```bash
az login
```

The `az` command is the root command of the Azure CLI. What follows `az` is one or more specific commands, such as `login`. See the ([`az login`](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli) command reference. The Azure CLI normally maintains your sign-in across sessions, but it's a good
practice to run `az login` whenever you open a new terminal or command prompt.

### Step 2: Create a Service Principal

This command saves it output in `azure_sigma_auth_sp.json`. For more details on the command and its arguments, see What the [create-for-rbac](https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd#what-the-create-for-rbac-command-does)
command does. If you're in an organization, you may not have permission in the subscription to run this command. In that case, contact the
subscription owners to have them create the service principal for you.

```bash
az ad sp create-for-rbac --name SigmaCodingServicePrincipalAuth --skip-assignment --sdk-auth > azure_sigma_auth_sp.json
```

### What the `create-for-rbac` command does

The az ad create-for-rbac command creates a service principal for "role-based authentication" (RBAC).

- `ad` means Azure Active Directory; `sp` means "service principal," and `create-for-rbac` means "create for role-based access control," Azure's primary form of authorization.
- The `--name` argument should be unique within your organization and typically uses the name of the developer that uses the service principal. If you omit this argument, the Azure CLI uses a generic name of the form `azure-cli-<timestamp>`. You can rename the service principal on the Azure portal, if desired.
- The `--skip-assignment` argument creates a service principal with no default permissions. You must then assign specific permissions to the service principal to allow locally-run code to access any resources. Different quickstarts and tutorials provide details for authorizing a service principal for the resources involved.
- The command provides JSON output, which in the example is saved in a file named local-sp.json.
- The `--sdk-auth` argument generates JSON output similar to the following values. Your ID values and secret will all be different)

If you skip `--sdk-auth` argument the output will look like the following:

```json
{
  "appId": "12345678-1111-2222-3333-1234567890ab",
  "displayName": "localtest-sp-rbac",
  "name": "http://localtest-sp-rbac",
  "password": "abcdef00-4444-5555-6666-1234567890ab",
  "tenant": "00112233-7777-8888-9999-aabbccddeeff"
}
```

Note here, in this case, tenant is the tenant ID, appId is the client ID, and password is the client secret.If you don't skip `--sdk-auth` argument the output will look like the following:

```json
{
  "clientId": "12345678-1111-2222-3333-1234567890ab",
  "clientSecret": "abcdef00-4444-5555-6666-1234567890ab",
  "subscriptionId": "00000000-0000-0000-0000-000000000000",
  "tenantId": "00112233-7777-8888-9999-aabbccddeeff",
  "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
  "resourceManagerEndpointUrl": "https://management.azure.com/",
  "activeDirectoryGraphResourceId": "https://graph.windows.net/",
  "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
  "galleryEndpointUrl": "https://gallery.azure.com/",
  "managementEndpointUrl": "https://management.core.windows.net/"
}
```

Here is an example of creating a service prinicpal that I used:

```bash
az ad sp create-for-rbac --name SigmaCodingServicePrincipal
```

Then you can see the details of the this Service Prinicipal Object by using the `show --id` command
where the ID is the `appID` or also called the `clientId`.

```bash
az ad sp show --id <CLIENT_ID>
```
