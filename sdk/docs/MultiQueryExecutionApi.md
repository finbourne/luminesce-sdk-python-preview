# luminesce.MultiQueryExecutionApi

All URIs are relative to *https://www.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_multi_query**](MultiQueryExecutionApi.md#cancel_multi_query) | **DELETE** /api/MultiQueryBackground/{executionId} | CancelMultiQuery: Cancels (if running) or clears the data from (if completed) a previously started query-set
[**get_progress_of_multi_query**](MultiQueryExecutionApi.md#get_progress_of_multi_query) | **GET** /api/MultiQueryBackground/{executionId} | GetProgressOfMultiQuery: View progress information (up until this point) for the entire query-set
[**start_queries**](MultiQueryExecutionApi.md#start_queries) | **PUT** /api/MultiQueryBackground | StartQueries: Starts to Execute the LuminesceSql statements in the background.


# **cancel_multi_query**
> BackgroundQueryCancelResponse cancel_multi_query(execution_id)

CancelMultiQuery: Cancels (if running) or clears the data from (if completed) a previously started query-set

Cancel the query-set (if still running) / clear the data (if already returned) The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 404 Not Found : The requested query result doesn't exist and is not running. 

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
    api_instance = luminesce.MultiQueryExecutionApi(api_client)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query

    try:
        # CancelMultiQuery: Cancels (if running) or clears the data from (if completed) a previously started query-set
        api_response = api_instance.cancel_multi_query(execution_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MultiQueryExecutionApi->cancel_multi_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 

### Return type

[**BackgroundQueryCancelResponse**](BackgroundQueryCancelResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_progress_of_multi_query**
> BackgroundMultiQueryProgressResponse get_progress_of_multi_query(execution_id)

GetProgressOfMultiQuery: View progress information (up until this point) for the entire query-set

View progress information (up until this point) for the entire query-set The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 404 Not Found : The requested query result doesn't exist and is not running. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

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
    api_instance = luminesce.MultiQueryExecutionApi(api_client)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query

    try:
        # GetProgressOfMultiQuery: View progress information (up until this point) for the entire query-set
        api_response = api_instance.get_progress_of_multi_query(execution_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MultiQueryExecutionApi->get_progress_of_multi_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 

### Return type

[**BackgroundMultiQueryProgressResponse**](BackgroundMultiQueryProgressResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_queries**
> BackgroundMultiQueryResponse start_queries(type, body, as_at=as_at, effective_at=effective_at, limit1=limit1, limit2=limit2, input1=input1, input2=input2, input3=input3, timeout_seconds=timeout_seconds, keep_for_seconds=keep_for_seconds)

StartQueries: Starts to Execute the LuminesceSql statements in the background.

 Allow for starting a potentially long running query and getting back an immediate response with how to  - fetch the data in various formats (if available, or if not simply being informed it is not yet ready), on a per result basis - view progress information (up until this point), for all results in one go - cancel the queries (if still running) / clear the data (if already returned)  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - there was something wrong with your query syntax (the issue was detected at parse-time) - 401 Unauthorized 

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
    api_instance = luminesce.MultiQueryExecutionApi(api_client)
    type = luminesce.MultiQueryDefinitionType() # MultiQueryDefinitionType | An enum value defining the set of statements being executed
body = 'body_example' # str | A \"search\" value (e.g. 'Apple' on an instrument search, a `Finbourne.Filtering` expression of Insights, etc.)  In the cases where \"Nothing\" is valid for a `Finbourne.Filtering` expression, pass `True`.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt time used by any bitemporal provider in the queries. (optional)
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The EffectiveAt time used by any bitemporal provider in the queries. (optional)
limit1 = 56 # int | A limit that is applied to first-level queries (e.g. Instruments themselves) (optional)
limit2 = 56 # int | A limit that is applied to second-level queries (e.g. Holdings based on the set of Instruments found) (optional)
input1 = 'input1_example' # str | A value available to queries, these vary by 'type' and are only used by some types at all.  e.g. a start-date of some sort (optional)
input2 = 'input2_example' # str | A second value available to queries, these vary by 'type' and are only used by some types at all. (optional)
input3 = 'input3_example' # str | A third value available to queries, these vary by 'type' and are only used by some types at all. (optional)
timeout_seconds = 0 # int | Maximum time the query may run for, in seconds: <0 → ∞, 0 → 1200s (20m) (optional) (default to 0)
keep_for_seconds = 0 # int | Maximum time the result may be kept for, in seconds: <0 → 1200 (20m), 0 → 28800 (8h), max = 2,678,400 (31d) (optional) (default to 0)

    try:
        # StartQueries: Starts to Execute the LuminesceSql statements in the background.
        api_response = api_instance.start_queries(type, body, as_at=as_at, effective_at=effective_at, limit1=limit1, limit2=limit2, input1=input1, input2=input2, input3=input3, timeout_seconds=timeout_seconds, keep_for_seconds=keep_for_seconds)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MultiQueryExecutionApi->start_queries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**MultiQueryDefinitionType**](.md)| An enum value defining the set of statements being executed | 
 **body** | **str**| A \&quot;search\&quot; value (e.g. &#39;Apple&#39; on an instrument search, a &#x60;Finbourne.Filtering&#x60; expression of Insights, etc.)  In the cases where \&quot;Nothing\&quot; is valid for a &#x60;Finbourne.Filtering&#x60; expression, pass &#x60;True&#x60;. | 
 **as_at** | **datetime**| The AsAt time used by any bitemporal provider in the queries. | [optional] 
 **effective_at** | **datetime**| The EffectiveAt time used by any bitemporal provider in the queries. | [optional] 
 **limit1** | **int**| A limit that is applied to first-level queries (e.g. Instruments themselves) | [optional] 
 **limit2** | **int**| A limit that is applied to second-level queries (e.g. Holdings based on the set of Instruments found) | [optional] 
 **input1** | **str**| A value available to queries, these vary by &#39;type&#39; and are only used by some types at all.  e.g. a start-date of some sort | [optional] 
 **input2** | **str**| A second value available to queries, these vary by &#39;type&#39; and are only used by some types at all. | [optional] 
 **input3** | **str**| A third value available to queries, these vary by &#39;type&#39; and are only used by some types at all. | [optional] 
 **timeout_seconds** | **int**| Maximum time the query may run for, in seconds: &lt;0 → ∞, 0 → 1200s (20m) | [optional] [default to 0]
 **keep_for_seconds** | **int**| Maximum time the result may be kept for, in seconds: &lt;0 → 1200 (20m), 0 → 28800 (8h), max &#x3D; 2,678,400 (31d) | [optional] [default to 0]

### Return type

[**BackgroundMultiQueryResponse**](BackgroundMultiQueryResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

