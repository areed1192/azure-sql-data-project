# Setting Up an Azure Account

Link: <https://www.testpreptraining.com/tutorial/microsoft-azure-fundamentals-az-900/creating-an-azure-account/>

## Azure Free Subscription

An Azure free subscription includes a \$200 credit to spend on any service for the first 30 days,
free access to the most popular Azure products for 12 months, and access to more than 25 products
that are always free. This is an excellent way for new users to get started. To set up a free
subscription, you need a phone number, a credit card, and a Microsoft account.

## Azure Pay-As-You-Go subscription

A Pay-As-You-Go (PAYG) subscription charges you monthly for the services you used in that billing
period. This subscription type is appropriate for a wide range of users, from individuals to small
businesses, and many large organizations as well.

## Azure Enterprise Agreement

An Enterprise Agreement provides flexibility to buy cloud services and software licenses under one
agreement, with discounts for new licenses and Software Assurance. It’s targeted at enterprise-scale
organizations.

## Azure for Students subscription

An Azure for Students subscription includes \$100 in Azure credits to be used within the first 12
months plus select free services without requiring a credit card at sign-up. You must verify your
student status through your organizational email address.

## Using multiple Azure subscriptions

You can create multiple subscriptions under a single Azure account. This is particularly useful
for businesses because access control and billing occur at the subscription level, not the
account level.

## Authenticate access with Azure Active Directory

As you’ve seen, your Azure account is a globally unique entity that gives you access to your Azure
subscriptions and services. Authentication for your account is performed using Azure Active Directory
(Azure AD). Azure AD is a modern identity provider that supports multiple authentication protocols to
secure applications and services in the cloud.

Users, applications, and other entities registered in Azure AD aren’t all lumped into a single global
service. Instead, Azure AD is partitioned into separate tenants. A tenant is a dedicated, isolated
instance of the Azure Active Directory service, owned and managed by an organization. When you sign
up for a Microsoft cloud service subscription such as Microsoft Azure, Microsoft Intune, or Office 365,
a dedicated instance of Azure AD is automatically created for your organization.

When it comes to Azure AD tenants, there is no concrete definition of “organization” — tenants can
be owned by individuals, teams, companies, or any other group of people. Tenants are commonly associated
with companies. If you sign up for Azure with an email address that’s not associated with an existing
tenant, the sign-up process will walk you through creating a tenant, owned entirely by you.

Azure AD tenants and subscriptions have a many-to-one trust relationship: A tenant can be associated
with multiple Azure subscriptions, but every subscription is associated with only one tenant. This
structure allows organizations to manage multiple subscriptions and set security rules across all
the resources contained within them.
