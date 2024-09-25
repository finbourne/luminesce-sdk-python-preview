# luminesce.CurrentTableFieldCatalogApi

All URIs are relative to *https://www.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog**](CurrentTableFieldCatalogApi.md#get_catalog) | **GET** /api/Catalog | GetCatalog: Get a Flattened Table/Field Catalog
[**get_fields**](CurrentTableFieldCatalogApi.md#get_fields) | **GET** /api/Catalog/fields | GetFields: List field and parameters for providers
[**get_providers**](CurrentTableFieldCatalogApi.md#get_providers) | **GET** /api/Catalog/providers | GetProviders: List available providers


# **get_catalog**
> str get_catalog(free_text_search=free_text_search, json_proper=json_proper, use_cache=use_cache)

GetCatalog: Get a Flattened Table/Field Catalog

 Returns the User's full version of the catalog (Providers, their fields and associated information) that are currently running that you have access to (in Json format).  This is the entire catalog flattened, which is often quite large and always a bit repetitive.   The internal results are cached for several minutes.  Consider using `api/Catalog/providers` and `api/Catalog/fields` for a more granular and incremental loading flow.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

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
    api_instance = luminesce.CurrentTableFieldCatalogApi(api_client)
    free_text_search = 'free_text_search_example' # str | Limit the catalog to only things in some way dealing with the passed in text string (optional)
json_proper = False # bool | Should this be text/json (not json-encoded-as-a-string) (optional) (default to False)
use_cache = False # bool | Should the available cache be used? false is effectively to pick up a change in the catalog (optional) (default to False)

    try:
        # GetCatalog: Get a Flattened Table/Field Catalog
        api_response = api_instance.get_catalog(free_text_search=free_text_search, json_proper=json_proper, use_cache=use_cache)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentTableFieldCatalogApi->get_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_text_search** | **str**| Limit the catalog to only things in some way dealing with the passed in text string | [optional] 
 **json_proper** | **bool**| Should this be text/json (not json-encoded-as-a-string) | [optional] [default to False]
 **use_cache** | **bool**| Should the available cache be used? false is effectively to pick up a change in the catalog | [optional] [default to False]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields**
> str get_fields(table_like=table_like)

GetFields: List field and parameters for providers

 Returns the User's full version of the catalog but only the field/parameter-level information  (as well as the TableName they refer to, of course) for tables matching the `tableLike` (manually include wildcards if desired).  The internal results are cached for several minutes.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

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
    api_instance = luminesce.CurrentTableFieldCatalogApi(api_client)
    table_like = '%' # str |  (optional) (default to '%')

    try:
        # GetFields: List field and parameters for providers
        api_response = api_instance.get_fields(table_like=table_like)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentTableFieldCatalogApi->get_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_like** | **str**|  | [optional] [default to &#39;%&#39;]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers**
> str get_providers(free_text_search=free_text_search, use_cache=use_cache)

GetProviders: List available providers

 Returns the User's full version of the catalog but only the table/provider-level information they have access to.  The internal results are cached for several minutes.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

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
    api_instance = luminesce.CurrentTableFieldCatalogApi(api_client)
    free_text_search = 'free_text_search_example' # str | Limit the catalog to only things in some way dealing with the passed in text string (optional)
use_cache = True # bool | Should the available cache be used? false is effectively to pick up a change in the catalog (optional) (default to True)

    try:
        # GetProviders: List available providers
        api_response = api_instance.get_providers(free_text_search=free_text_search, use_cache=use_cache)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentTableFieldCatalogApi->get_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_text_search** | **str**| Limit the catalog to only things in some way dealing with the passed in text string | [optional] 
 **use_cache** | **bool**| Should the available cache be used? false is effectively to pick up a change in the catalog | [optional] [default to True]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

