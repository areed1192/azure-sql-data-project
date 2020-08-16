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
        'pyodbc',
        'azure-mgmt-sql',
        'azure.identity',
        'requests',
        'azure.mgmt.resource'
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
