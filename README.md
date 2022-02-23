# LUMINECSE<sup>®</sup> Python Preview SDK
This is the Python Preview SDK for [LUMINESCE by FINBOURNE](https://www.finbourne.com/luminesce/), a data virtualisation platform that lets you explore, query, fetch and combine data from multiple sources and systems, including LUSID, into an integrated view for interrogation. To use it you'll need a LUSID account. [Sign up for free at lusid.com](https://www.lusid.com/app/signup)

<a href="https://www.lusid.com/app/signup"><img src="https://content.finbourne.com/LUSID_repo.png" alt="LUSID_by_Finbourne"></a>

## Build Status

| branch | status |
| --- | --- |
| `master` |  ![PyPI](https://img.shields.io/pypi/v/luminesce-sdk-preview?color=blue) ![build](https://github.com/finbourne/luminesce-sdk-python-preview/workflows/luminesce-sdk-python-preview-test/badge.svg) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=finbourne_luminesce-sdk-python-preview&metric=alert_status)](https://sonarcloud.io/dashboard?id=finbourne_luminesce-sdk-python-preview) |
| `develop` | ![luminesce-sdk-python-preview-test](https://github.com/finbourne/luminesce-sdk-python-preview/workflows/luminesce-sdk-python-preview-test/badge.svg?branch=develop) |


## Installation

The PyPi package for the LUMINESCE SDK can installed using the following:

```
pip install luminesce-sdk-preview finbourne-sdk-utilities
```

For more information on the LUMINESCE API, see [LUMINESCE API Documentation](https://www.lusid.com/honeycomb/swagger/index.html).


## Documentation 

For further documentation on building the SDK, running the tutorials and using the SDK please see the [wiki](https://github.com/finbourne/luminesce-sdk-python-preview/wiki).

Documentation for classes, methods, attributes and other members of the SDK is [available to view online](https://luminesce-sdk-python-preview.readthedocs.io/en/latest/_autosummary/sdk.luminesce.html).


## Usage

```python
import luminesce
from fbnsdkutilities import ApiClientFactory

factory = ApiClientFactory(luminesce, api_secrets_filename='/path/to/secrets.json')
sql_exec_api = factory.build(luminesce.api.SqlExecutionApi)

sql_exec_api.put_by_query_csv("""
    select * from lusid.portfolio limit 10
""")
```