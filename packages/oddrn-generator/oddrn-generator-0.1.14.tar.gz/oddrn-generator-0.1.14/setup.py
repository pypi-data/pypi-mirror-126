# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oddrn_generator']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.8.2,<2.0.0']

setup_kwargs = {
    'name': 'oddrn-generator',
    'version': '0.1.14',
    'description': 'Open Data Discovery Resource Name Generator',
    'long_description': '# Open Data Discovery Resource Name Generator\n## Requirements\nPython >= 3.7\n## Installation\n```\npoetry install\n```\n## Usage and configuration\n### Available generators\n* postgresql - PostgresqlGenerator\n* mysql - MysqlGenerator\n* glue - GlueGenerator\n* kafka - KafkaGenerator\n* kafkaconnect - KafkaConnectGenerator\n* snowflake - SnowflakeGenerator\n* airflow - AirflowGenerator\n* hive - HiveGenerator\n* dynamodb - DynamodbGenerator\n* odbc - OdbcGenerator\n* mssql - MssqlGenerator\n* oracle - OracleGenerator\n* redshift - RedshiftGenerator\n* clickhouse - ClickHouseGenerator\n* athena - AthenaGenerator\n* quicksight - QuicksightGenerator\n* dbt - DbtGenerator\n* prefect - PrefectGenerator\n* tableau - TableauGenerator\n### Work in progress generators\n* kubeflow - KubeflowGenerator\n* dvc - DVCGenerator\n* great_expectations - GreatExpectationsGenerator\n\n### Generator properties\n* base_oddrn - Get base oddrn (without path)\n* available_paths - Get all available path of generator \n\n### Generator methods\n* get_oddrn_by_path(path_name, new_value=None) - Get oddrn string by path. You also can set value for this path using \'new_value\' param\n* set_oddrn_paths(**kwargs) - Set or update values of oddrn path\n* get_data_source_oddrn() - Get datasouce oddrn \n\n### Generator parameters:\n* host_settings: str - optional. Hostname configuration\n* cloud_settings: dict - optional.  Cloud configuration\n* **kwargs - path\'s name and values\n\n### Example usage\n```python\n# postgresql\nfrom oddrn_generator import PostgresqlGenerator\noddrn_gen = PostgresqlGenerator(\n  host_settings=\'my.host.com:5432\', \n  schemas=\'schema_name\', databases=\'database_name\', tables=\'table_name\'\n)\n\noddrn_gen.base_oddrn\n# //postgresql/host/my.host.com:5432\noddrn_gen.available_paths\n# (\'schemas\', \'databases\', \'tables\', \'columns\')\n\noddrn_gen.get_data_source_oddrn()\n# //postgresql/host/my.host.com:5432/schemas/schema_name/databases/database_name\n\noddrn_gen.get_oddrn_by_path("schemas")\n# //postgresql/host/my.host.com:5432/schemas/schema_name\n\noddrn_gen.get_oddrn_by_path("databases")\n# //postgresql/host/my.host.com:5432/schemas/schema_name/databases/database_name\n\noddrn_gen.get_oddrn_by_path("tables")\n# //postgresql/host/my.host.com:5432/schemas/schema_name/databases/database_name/tables/table_name\n\n# you can set or change path:\noddrn_gen.set_oddrn_paths(tables=\'another_table_name\', columns=\'new_column_name\')\noddrn_gen.get_oddrn_by_path("columns")\n# //postgresql/host/my.host.com:5432/schemas/schema_name/databases/database_name/tables/another_table_name/columns/new_column_name\n\n# you can get path wih new values:\noddrn_gen.get_oddrn_by_path("columns", new_value="another_new_column_name")\n# //postgresql/host/my.host.com:5432/schemas/schema_name/databases/database_name/tables/another_table_name/columns/another_new_column_name\n\n\n# glue\nfrom oddrn_generator import GlueGenerator\noddrn_gen = GlueGenerator(\n  cloud_settings={\'account\': \'acc_id\', \'region\':\'reg_id\'}, \n  databases=\'database_name\', tables=\'table_name\', columns=\'column_name\', \n  jobs=\'job_name\', runs=\'run_name\', owners=\'owner_name\'\n)\n\noddrn_gen.available_paths\n# (\'databases\', \'tables\', \'columns\', \'owners\', \'jobs\', \'runs\')\n\noddrn_gen.get_oddrn_by_path("databases")\n# //glue/cloud/aws/account/acc_id/region/reg_id/databases/database_name\n\noddrn_gen.get_oddrn_by_path("tables")\n# //glue/cloud/aws/account/acc_id/region/reg_id/databases/database_name/tables/table_name\'\n\noddrn_gen.get_oddrn_by_path("columns")\n# //glue/cloud/aws/account/acc_id/region/reg_id/databases/database_name/tables/table_name/columns/column_name\n\noddrn_gen.get_oddrn_by_path("jobs")\n# //glue/cloud/aws/account/acc_id/region/reg_id/jobs/job_name\n\noddrn_gen.get_oddrn_by_path("runs")\n# //glue/cloud/aws/account/acc_id/region/reg_id/jobs/job_name/runs/run_name\n\noddrn_gen.get_oddrn_by_path("owners")\n# //glue/cloud/aws/account/acc_id/region/reg_id/owners/owner_name\n\n```\n\n### Exceptions\n* WrongPathOrderException - raises when trying set path that depends on another path\n```python\nfrom oddrn_generator import PostgresqlGenerator\noddrn_gen = PostgresqlGenerator(\n    host_settings=\'my.host.com:5432\', \n    schemas=\'schema_name\', databases=\'database_name\',\n    columns=\'column_without_table\'\n)\n# WrongPathOrderException: \'columns\' can not be without \'tables\' attribute\n```\n* EmptyPathValueException - raises when trying to get a path that is not set up\n```python\nfrom oddrn_generator import PostgresqlGenerator\noddrn_gen = PostgresqlGenerator(\n    host_settings=\'my.host.com:5432\', schemas=\'schema_name\', databases=\'database_name\',\n)\noddrn_gen.get_oddrn_by_path("tables")\n\n# EmptyPathValueException: Path \'tables\' is not set up\n```\n* PathDoestExistException - raises when trying to get not existing oddrn path\n```python\nfrom oddrn_generator import PostgresqlGenerator\noddrn_gen = PostgresqlGenerator(\n    host_settings=\'my.host.com:5432\', schemas=\'schema_name\', databases=\'database_name\',\n)\noddrn_gen.get_oddrn_by_path("jobs")\n\n# PathDoestExistException: Path \'jobs\' doesn\'t exist in generator\n```',
    'author': 'Open Data Discovery',
    'author_email': 'pypi@opendatadiscovery.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/opendatadiscovery/oddrn-generator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
