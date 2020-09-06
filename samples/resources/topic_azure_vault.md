# Azure Vault: Granting Access Policies

## Overview

Many of our applications will need to be able to access different information inside of our Azure Key Vault.
However, to access this information, the application must have access to our Key Vault. To change the access policy
of our application with respect to the Azure Key Vault run through the following steps:

## Steps

Link to Microsoft Documentation: [Assign Access Policy](https://docs.microsoft.com/en-us/azure/key-vault/general/assign-access-policy-portal)

1. In the Azure portal, navigate to the Key Vault resource.
2. Under Settings, select Access policies, then select Add Access Policy.
3. Select the permissions you want under Certificate permissions, Key permissions,
   and Secret permissions. You can also select a template that contains common
   permission combinations.
4. Under Select principal, choose the None selected link to open the Principal selection
   pane. Enter the name of the app or service principal in the search field, select the
   appropriate result, then choose Select.
5. Back in the Add access policy pane, select Add to save the access policy.
6. Back on the Access policies page, verify that your access policy is listed under Current
   Access Policies, then select Save. Access policies aren't applied until you save them.
