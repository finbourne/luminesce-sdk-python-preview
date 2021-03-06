# luminesce.SqlExecutionApi

All URIs are relative to *https://www.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_by_query_csv**](SqlExecutionApi.md#get_by_query_csv) | **GET** /api/Sql/csv/{query} | [EXPERIMENTAL] GetByQueryCsv: Executes Sql, returned in CSV format, where the sql is simply in the url.
[**get_by_query_excel**](SqlExecutionApi.md#get_by_query_excel) | **GET** /api/Sql/excel/{query} | [EXPERIMENTAL] GetByQueryExcel: Executes Sql, returned in Excel (xlsx) format (as a file to be downloaded) format, where the sql is simply in the url.
[**get_by_query_json**](SqlExecutionApi.md#get_by_query_json) | **GET** /api/Sql/json/{query} | [EXPERIMENTAL] GetByQueryJson: Executes Sql, returned in JSON format, where the sql is simply in the url.
[**get_by_query_pipe**](SqlExecutionApi.md#get_by_query_pipe) | **GET** /api/Sql/pipe/{query} | [EXPERIMENTAL] GetByQueryPipe: Executes Sql, returned in pipe-delimited format, where the sql is simply in the url.
[**get_by_query_sqlite**](SqlExecutionApi.md#get_by_query_sqlite) | **GET** /api/Sql/sqlite/{query} | [EXPERIMENTAL] GetByQuerySqlite: Executes Sql, returned in SqLite DB (sqlite3) format (as a file to be downloaded) format, where the sql is simply in the url.
[**put_by_query_csv**](SqlExecutionApi.md#put_by_query_csv) | **PUT** /api/Sql/csv | [EXPERIMENTAL] PutByQueryCsv: Executes Sql, returned in CSV format, where the sql is the post-body url.
[**put_by_query_excel**](SqlExecutionApi.md#put_by_query_excel) | **PUT** /api/Sql/excel | [EXPERIMENTAL] PutByQueryExcel: Executes Sql, returned in Excel (xlsx) format (as a file to be downloaded), where the sql is the post-body url.
[**put_by_query_json**](SqlExecutionApi.md#put_by_query_json) | **PUT** /api/Sql/json | [EXPERIMENTAL] PutByQueryJson: Executes Sql, returned in JSON format, where the sql is the post-body url.
[**put_by_query_pipe**](SqlExecutionApi.md#put_by_query_pipe) | **PUT** /api/Sql/pipe | [EXPERIMENTAL] PutByQueryPipe: Executes Sql, returned in pipe-delimited format, where the sql is the post-body url.
[**put_by_query_sqlite**](SqlExecutionApi.md#put_by_query_sqlite) | **PUT** /api/Sql/sqlite | [EXPERIMENTAL] PutByQuerySqlite: Executes Sql, returned in SqLite DB (sqlite3) format (as a file to be downloaded), where the sql is the post-body url.
[**put_query_to_format**](SqlExecutionApi.md#put_query_to_format) | **PUT** /api/Sql/pretty | [EXPERIMENTAL] PutQueryToFormat: Executes Sql, returned in JSON format, where the sql is the post-body url.


# **get_by_query_csv**
> str get_by_query_csv(query, query_name=query_name, download=download, timeout=timeout)

[EXPERIMENTAL] GetByQueryCsv: Executes Sql, returned in CSV format, where the sql is simply in the url.

 For simple single-line query execution via the url. e.g. `select ^ from Sys.Field order by 1, 2`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/honeycomb
# See configuration.py for a list of all supported configuration parameters.
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with luminesce.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luminesce.SqlExecutionApi(api_client)
    query = 'select ^ from Sys.Field order by 1, 2' # str | HoneycombSql to Execute (must be one line only)
query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
timeout = 0 # int | In seconds: <0 ??? ???, 0 ??? 120s (optional) (default to 0)

    try:
        # [EXPERIMENTAL] GetByQueryCsv: Executes Sql, returned in CSV format, where the sql is simply in the url.
        api_response = api_instance.get_by_query_csv(query, query_name=query_name, download=download, timeout=timeout)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SqlExecutionApi->get_by_query_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| HoneycombSql to Execute (must be one line only) | 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout** | **int**| In seconds: &lt;0 ??? ???, 0 ??? 120s | [optional] [default to 0]

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_query_excel**
> str get_by_query_excel(query, query_name=query_name, timeout=timeout)

[EXPERIMENTAL] GetByQueryExcel: Executes Sql, returned in Excel (xlsx) format (as a file to be downloaded) format, where the sql is simply in the url.

 For simple single-line query execution via the url. e.g. `select ^ from Sys.Field order by 1, 2`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/honeycomb
# See configuration.py for a list of all supported configuration parameters.
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with luminesce.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luminesce.SqlExecutionApi(api_client)
    query = 'select ^ from Sys.Field order by 1, 2' # str | HoneycombSql to Execute (must be one line only)
query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
timeout = 0 # int | In seconds: <0 ??? ???, 0 ??? 120s (optional) (default to 0)

    try:
        # [EXPERIMENTAL] GetByQueryExcel: Executes Sql, returned in Excel (xlsx) format (as a file to be downloaded) format, where the sql is simply in the url.
        api_response = api_instance.get_by_query_excel(query, query_name=query_name, timeout=timeout)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SqlExecutionApi->get_by_query_excel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| HoneycombSql to Execute (must be one line only) | 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout** | **int**| In seconds: &lt;0 ??? ???, 0 ??? 120s | [optional] [default to 0]

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_query_json**
> str get_by_query_json(query, query_name=query_name, timeout=timeout, json_proper=json_proper)

[EXPERIMENTAL] GetByQueryJson: Executes Sql, returned in JSON format, where the sql is simply in the url.

 For simple single-line query execution via the url. e.g. `select ^ from Sys.Field order by 1, 2`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/honeycomb
# See configuration.py for a list of all supported configuration parameters.
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with luminesce.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luminesce.SqlExecutionApi(api_client)
    query = 'select ^ from Sys.Field order by 1, 2' # str | HoneycombSql to Execute (must be one line only)
query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
timeout = 0 # int | In seconds: <0 ??? ???, 0 ??? 120s (optional) (default to 0)
json_proper = False # bool | Should this be text/json (not json-encoded-as-a-string) (optional) (default to False)

    try:
        # [EXPERIMENTAL] GetByQueryJson: Executes Sql, returned in JSON format, where the sql is simply in the url.
        api_response = api_instance.get_by_query_json(query, query_name=query_name, timeout=timeout, json_proper=json_proper)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SqlExecutionApi->get_by_query_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| HoneycombSql to Execute (must be one line only) | 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout** | **int**| In seconds: &lt;0 ??? ???, 0 ??? 120s | [optional] [default to 0]
 **json_proper** | **bool**| Should this be text/json (not json-encoded-as-a-string) | [optional] [default to False]

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_query_pipe**
> str get_by_query_pipe(query, query_name=query_name, download=download, timeout=timeout)

[EXPERIMENTAL] GetByQueryPipe: Executes Sql, returned in pipe-delimited format, where the sql is simply in the url.

 For simple single-line query execution via the url. e.g. `select ^ from Sys.Field order by 1, 2`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/honeycomb
# See configuration.py for a list of all supported configuration parameters.
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with luminesce.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luminesce.SqlExecutionApi(api_client)
    query = 'select ^ from Sys.Field order by 1, 2' # str | HoneycombSql to Execute (must be one line only)
query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
timeout = 0 # int | In seconds: <0 ??? ???, 0 ??? 120s (optional) (default to 0)

    try:
        # [EXPERIMENTAL] GetByQueryPipe: Executes Sql, returned in pipe-delimited format, where the sql is simply in the url.
        api_response = api_instance.get_by_query_pipe(query, query_name=query_name, download=download, timeout=timeout)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SqlExecutionApi->get_by_query_pipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| HoneycombSql to Execute (must be one line only) | 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout** | **int**| In seconds: &lt;0 ??? ???, 0 ??? 120s | [optional] [default to 0]

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_query_sqlite**
> str get_by_query_sqlite(query, query_name=query_name, timeout=timeout)

[EXPERIMENTAL] GetByQuerySqlite: Executes Sql, returned in SqLite DB (sqlite3) format (as a file to be downloaded) format, where the sql is simply in the url.

 For simple single-line query execution via the url. e.g. `select ^ from Sys.Field order by 1, 2`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/honeycomb
# See configuration.py for a list of all supported configuration parameters.
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with luminesce.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luminesce.SqlExecutionApi(api_client)
    query = 'select ^ from Sys.Field order by 1, 2' # str | HoneycombSql to Execute (must be one line only)
query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
timeout = 0 # int | In seconds: <0 ??? ???, 0 ??? 120s (optional) (default to 0)

    try:
        # [EXPERIMENTAL] GetByQuerySqlite: Executes Sql, returned in SqLite DB (sqlite3) format (as a file to be downloaded) format, where the sql is simply in the url.
        api_response = api_instance.get_by_query_sqlite(query, query_name=query_name, timeout=timeout)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SqlExecutionApi->get_by_query_sqlite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| HoneycombSql to Execute (must be one line only) | 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout** | **int**| In seconds: &lt;0 ??? ???, 0 ??? 120s | [optional] [default to 0]

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_by_query_csv**
> str put_by_query_csv(body, query_name=query_name, download=download, timeout_seconds=timeout_seconds)

[EXPERIMENTAL] PutByQueryCsv: Executes Sql, returned in CSV format, where the sql is the post-body url.

 For more complex HoneycombSql a PUT will allow for longer Sql. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/honeycomb
# See configuration.py for a list of all supported configuration parameters.
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with luminesce.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luminesce.SqlExecutionApi(api_client)
    body = 'body_example' # str | HoneycombSql to Execute (may be multi-line)
query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
timeout_seconds = 0 # int | In seconds: <0 ??? ???, 0 ??? 120s (optional) (default to 0)

    try:
        # [EXPERIMENTAL] PutByQueryCsv: Executes Sql, returned in CSV format, where the sql is the post-body url.
        api_response = api_instance.put_by_query_csv(body, query_name=query_name, download=download, timeout_seconds=timeout_seconds)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SqlExecutionApi->put_by_query_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| HoneycombSql to Execute (may be multi-line) | 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout_seconds** | **int**| In seconds: &lt;0 ??? ???, 0 ??? 120s | [optional] [default to 0]

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_by_query_excel**
> str put_by_query_excel(body, query_name=query_name, timeout_seconds=timeout_seconds)

[EXPERIMENTAL] PutByQueryExcel: Executes Sql, returned in Excel (xlsx) format (as a file to be downloaded), where the sql is the post-body url.

 For more complex HoneycombSql a PUT will allow for longer Sql. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/honeycomb
# See configuration.py for a list of all supported configuration parameters.
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with luminesce.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luminesce.SqlExecutionApi(api_client)
    body = 'body_example' # str | HoneycombSql to Execute (may be multi-line)
query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
timeout_seconds = 0 # int | In seconds: <0 ??? ???, 0 ??? 120s (optional) (default to 0)

    try:
        # [EXPERIMENTAL] PutByQueryExcel: Executes Sql, returned in Excel (xlsx) format (as a file to be downloaded), where the sql is the post-body url.
        api_response = api_instance.put_by_query_excel(body, query_name=query_name, timeout_seconds=timeout_seconds)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SqlExecutionApi->put_by_query_excel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| HoneycombSql to Execute (may be multi-line) | 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout_seconds** | **int**| In seconds: &lt;0 ??? ???, 0 ??? 120s | [optional] [default to 0]

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_by_query_json**
> str put_by_query_json(body, query_name=query_name, timeout_seconds=timeout_seconds, json_proper=json_proper)

[EXPERIMENTAL] PutByQueryJson: Executes Sql, returned in JSON format, where the sql is the post-body url.

 For more complex HoneycombSql a PUT will allow for longer Sql. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/honeycomb
# See configuration.py for a list of all supported configuration parameters.
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with luminesce.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luminesce.SqlExecutionApi(api_client)
    body = 'body_example' # str | HoneycombSql to Execute (may be multi-line)
query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
timeout_seconds = 0 # int | In seconds: <0 ??? ???, 0 ??? 120s (optional) (default to 0)
json_proper = False # bool | Should this be text/json (not json-encoded-as-a-string) (optional) (default to False)

    try:
        # [EXPERIMENTAL] PutByQueryJson: Executes Sql, returned in JSON format, where the sql is the post-body url.
        api_response = api_instance.put_by_query_json(body, query_name=query_name, timeout_seconds=timeout_seconds, json_proper=json_proper)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SqlExecutionApi->put_by_query_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| HoneycombSql to Execute (may be multi-line) | 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout_seconds** | **int**| In seconds: &lt;0 ??? ???, 0 ??? 120s | [optional] [default to 0]
 **json_proper** | **bool**| Should this be text/json (not json-encoded-as-a-string) | [optional] [default to False]

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_by_query_pipe**
> str put_by_query_pipe(body, query_name=query_name, download=download, timeout_seconds=timeout_seconds)

[EXPERIMENTAL] PutByQueryPipe: Executes Sql, returned in pipe-delimited format, where the sql is the post-body url.

 For more complex HoneycombSql a PUT will allow for longer Sql. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/honeycomb
# See configuration.py for a list of all supported configuration parameters.
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with luminesce.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luminesce.SqlExecutionApi(api_client)
    body = 'body_example' # str | HoneycombSql to Execute (may be multi-line)
query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
timeout_seconds = 0 # int | In seconds: <0 ??? ???, 0 ??? 120s (optional) (default to 0)

    try:
        # [EXPERIMENTAL] PutByQueryPipe: Executes Sql, returned in pipe-delimited format, where the sql is the post-body url.
        api_response = api_instance.put_by_query_pipe(body, query_name=query_name, download=download, timeout_seconds=timeout_seconds)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SqlExecutionApi->put_by_query_pipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| HoneycombSql to Execute (may be multi-line) | 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout_seconds** | **int**| In seconds: &lt;0 ??? ???, 0 ??? 120s | [optional] [default to 0]

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_by_query_sqlite**
> str put_by_query_sqlite(body, query_name=query_name, timeout_seconds=timeout_seconds)

[EXPERIMENTAL] PutByQuerySqlite: Executes Sql, returned in SqLite DB (sqlite3) format (as a file to be downloaded), where the sql is the post-body url.

 For more complex HoneycombSql a PUT will allow for longer Sql. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/honeycomb
# See configuration.py for a list of all supported configuration parameters.
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with luminesce.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luminesce.SqlExecutionApi(api_client)
    body = 'body_example' # str | HoneycombSql to Execute (may be multi-line)
query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
timeout_seconds = 0 # int | In seconds: <0 ??? ???, 0 ??? 120s (optional) (default to 0)

    try:
        # [EXPERIMENTAL] PutByQuerySqlite: Executes Sql, returned in SqLite DB (sqlite3) format (as a file to be downloaded), where the sql is the post-body url.
        api_response = api_instance.put_by_query_sqlite(body, query_name=query_name, timeout_seconds=timeout_seconds)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SqlExecutionApi->put_by_query_sqlite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| HoneycombSql to Execute (may be multi-line) | 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout_seconds** | **int**| In seconds: &lt;0 ??? ???, 0 ??? 120s | [optional] [default to 0]

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_query_to_format**
> str put_query_to_format(body, trailing_commas=trailing_commas, uppercase_keywords=uppercase_keywords, break_join_on_sections=break_join_on_sections, space_after_expanded_comma=space_after_expanded_comma, keyword_standardization=keyword_standardization, expand_comma_lists=expand_comma_lists, expand_in_lists=expand_in_lists, expand_boolean_expressions=expand_boolean_expressions, expand_between_conditions=expand_between_conditions, expand_case_statements=expand_case_statements, max_line_width=max_line_width)

[EXPERIMENTAL] PutQueryToFormat: Executes Sql, returned in JSON format, where the sql is the post-body url.

 This formats SQL (given a set of options as to how to do so). It takes some SQL (or a fragment thereof, it need not fully parse as yet and certainly need not execute correctly) and returns the reformatted version. e.g. ```sql select x,y,z from a inner join b on a.x=b.x where x>y or y!=z ``` becomes ```sql select x, y, z from a inner join b    on a.x = b.x where x > y    or y != z ``` 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/honeycomb
# See configuration.py for a list of all supported configuration parameters.
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luminesce.Configuration(
    host = "https://www.lusid.com/honeycomb"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with luminesce.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luminesce.SqlExecutionApi(api_client)
    body = 'body_example' # str | HoneycombSql to Pretty-Print. Even if it doesn't parse an attempt will be made to format it
trailing_commas = True # bool | Should commas be after an expression (as opposed to before) (optional) (default to True)
uppercase_keywords = False # bool | Should key words be capitalized (optional) (default to False)
break_join_on_sections = True # bool | Should clauses on joins be given line breaks? (optional) (default to True)
space_after_expanded_comma = True # bool | Should comma-lists have spaces after the commas? (optional) (default to True)
keyword_standardization = True # bool | Should the \"nicest\" key words be used? (e.g. JOIN -> INNER JOIN) (optional) (default to True)
expand_comma_lists = False # bool | Should comma-lists (e.g. select a,b,c) have line breaks added? (optional) (default to False)
expand_in_lists = False # bool | Should IN-lists have line breaks added? (optional) (default to False)
expand_boolean_expressions = True # bool | Should boolean expressions have line breaks added? (optional) (default to True)
expand_between_conditions = True # bool | Should between conditions have line breaks added? (optional) (default to True)
expand_case_statements = True # bool | Should case-statements have line breaks added? (optional) (default to True)
max_line_width = 120 # int | Maximum number of characters to allow on one line (if possible) (optional) (default to 120)

    try:
        # [EXPERIMENTAL] PutQueryToFormat: Executes Sql, returned in JSON format, where the sql is the post-body url.
        api_response = api_instance.put_query_to_format(body, trailing_commas=trailing_commas, uppercase_keywords=uppercase_keywords, break_join_on_sections=break_join_on_sections, space_after_expanded_comma=space_after_expanded_comma, keyword_standardization=keyword_standardization, expand_comma_lists=expand_comma_lists, expand_in_lists=expand_in_lists, expand_boolean_expressions=expand_boolean_expressions, expand_between_conditions=expand_between_conditions, expand_case_statements=expand_case_statements, max_line_width=max_line_width)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SqlExecutionApi->put_query_to_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| HoneycombSql to Pretty-Print. Even if it doesn&#39;t parse an attempt will be made to format it | 
 **trailing_commas** | **bool**| Should commas be after an expression (as opposed to before) | [optional] [default to True]
 **uppercase_keywords** | **bool**| Should key words be capitalized | [optional] [default to False]
 **break_join_on_sections** | **bool**| Should clauses on joins be given line breaks? | [optional] [default to True]
 **space_after_expanded_comma** | **bool**| Should comma-lists have spaces after the commas? | [optional] [default to True]
 **keyword_standardization** | **bool**| Should the \&quot;nicest\&quot; key words be used? (e.g. JOIN -&gt; INNER JOIN) | [optional] [default to True]
 **expand_comma_lists** | **bool**| Should comma-lists (e.g. select a,b,c) have line breaks added? | [optional] [default to False]
 **expand_in_lists** | **bool**| Should IN-lists have line breaks added? | [optional] [default to False]
 **expand_boolean_expressions** | **bool**| Should boolean expressions have line breaks added? | [optional] [default to True]
 **expand_between_conditions** | **bool**| Should between conditions have line breaks added? | [optional] [default to True]
 **expand_case_statements** | **bool**| Should case-statements have line breaks added? | [optional] [default to True]
 **max_line_width** | **int**| Maximum number of characters to allow on one line (if possible) | [optional] [default to 120]

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

