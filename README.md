# Azure SQL Database Pipeline Project

## Table of Contents

- [Overview](#overview)
- [Resources](#resources)
- [Setup](#setup)
- [Usage](#usage)
- [Support These Projects](#support-these-projects)

## Overview

Microsoft Azure provides a wide number of services for managing and storing data. One
product is Microsoft Azure SQL. Which gives us the capability to create and manage
instances of SQL Servers hosted in the cloud. This project, demonstrates how to use these
services to manage data we collect from different sources.

## Resources

To use this project you will need to install some dependencies to connect to the database.
To download the drivers needed go to to [Microsoft SQL Drivers for Python](https://docs.microsoft.com/en-us/sql/connect/sql-connection-libraries?view=sql-server-ver15#anchor-20-drivers-relational-access). Once you download it, run through
the installation process.

**Resources - PYODBC with Azure:**

If you would like to read more on the topic of using PYODBC in conjunction with Microsoft
Azure, then I would refer you to the [documentation provided by Microsoft](https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver15).

## Setup

Right now, this project is not planned to be hosted on **PyPi** so you will need to do
a local install on your system if you plan to use it in other scrips you use. First,
clone this repo to your local system.

**Setup - Local Install:**

If you plan to use this project in other projects on your system, I would recommend you
either install this project in `editable` mode or do a `local install`. For those of you,
who want to make modifications to this project. I would recommend you install the library
in `editable` mode.

If you want to install the library in `editable` mode, make sure to run the `setup.py`
file, so you can install any dependencies you may need. To run the `setup.py` file,
run the following command in your terminal.

```console
pip install -e .
```

If you don't plan to make any modifications to the project but still want to use it across
your different projects, then do a local install.

```console
pip install .
```

This will install all the dependencies listed in the `setup.py` file. Once done
you can use the library wherever you want.

**Setup - Requirement Install:**

If you don't plan to use this project in any of your other projects, I would recommend you
just install the dependencies by using the `requirement.txt` file.

```console
pip install --requirement requirements.txt
```

## Usage

Here is a simple example of using the `azure_sql_pipeline` library to grab a specific
database from our SQL Server.

```python
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

# Initialize the client.
azure_pipeline_client = AzureSQLClient(
    client_id=client_id,
    client_secret=client_secret,
    subscription_id=subscription_id,
    tenant_id=tenant_id,
    username=server_username,
    password=server_password
)
```

## Support These Projects

**Patreon:**
Help support this project and future projects by donating to my [Patreon Page](https://www.patreon.com/sigmacoding)
. I'm always looking to add more content for individuals like yourself, unfortuantely some of the
APIs I would require me to pay monthly fees.

**YouTube:**
If you'd like to watch more of my content, feel free to visit my YouTube channel [Sigma Coding](https://www.youtube.com/c/SigmaCoding).
