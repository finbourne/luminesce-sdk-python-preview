# luminesce.ApplicationMetadataApi

All URIs are relative to *https://www.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_services_as_access_controlled_resources**](ApplicationMetadataApi.md#get_services_as_access_controlled_resources) | **GET** /api/metadata/access/resources | GetServicesAsAccessControlledResources: Get resources available for access control


# **get_services_as_access_controlled_resources**
> ResourceListOfAccessControlledResource get_services_as_access_controlled_resources()

GetServicesAsAccessControlledResources: Get resources available for access control

Get the comprehensive set of resources that are available for access control

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
    api_instance = luminesce.ApplicationMetadataApi(api_client)
    
    try:
        # GetServicesAsAccessControlledResources: Get resources available for access control
        api_response = api_instance.get_services_as_access_controlled_resources()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationMetadataApi->get_services_as_access_controlled_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfAccessControlledResource**](ResourceListOfAccessControlledResource.md)

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

