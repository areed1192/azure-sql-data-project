from setuptools import setup
from setuptools import find_namespace_packages

# Open the README File.
with open(file="README.md", mode="r") as readme_file:
    long_description = readme_file.read()

setup(
    name='azure-sql-project',
    author='Alex Reed',
    author_email='coding.sigma@gmail.com',
    version='0.0.1',
    description='A Microsoft Azure project used to send data to an Azure SQL Database.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/areed1192/azure-sql-data-project',
    install_requires=[
        'msrest==0.6.18',
        'msrestazure==0.6.4',
        'pyodbc==4.0.30',
        'fin-news==0.1.1',
        'azure-core==1.7.0',
        'azure-common==1.1.25',
        'azure-cosmos==4.0.0b6',
        'azure-identity==1.4.0',
        'azure-mgmt-sql==0.20.0',
        'azure-mgmt-core==1.2.0',
        'azure-mgmt-compute==13.0.0',
        'azure-storage-blob==12.4.0',
        'azure-keyvault-secrets==4.2.0'
    ],
    packages=find_namespace_packages(
        include=['azure_data_pipeline']
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>3.7'
)
