# luminesce.CurrentTableFieldCatalogApi

All URIs are relative to *https://www.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog**](CurrentTableFieldCatalogApi.md#get_catalog) | **GET** /api/Catalog | GetCatalog: Shows Table and Field level information on Providers that are currently running that you have access to (in Json format)


# **get_catalog**
> str get_catalog(free_text_search=free_text_search, json_proper=json_proper)

GetCatalog: Shows Table and Field level information on Providers that are currently running that you have access to (in Json format)

 The following LuminesceSql is executed to return this information:  ```sql @reg = select     r.Name,     min(r.Description) as Description from     Sys.Registration r where     r.Type in ('DirectProvider', 'DataProvider')     and      r.ShowAll = false group by     1     ;  @fld = select     f.TableName,     f.FieldName,     f.DataType,     f.FieldType,     f.IsPrimaryKey,     f.IsMain,     f.Description,     f.ParamDefaultValue,     f.TableParamColumns from     Sys.Field f     ;  @x = select     coalesce(f.TableName, r.Name) as TableName,     coalesce(f.FieldName, 'N/A') as FieldName,     f.DataType,     f.FieldType,     f.IsPrimaryKey,     f.IsMain,     case          when f.TableName is not null              then f.Description         else             r.Name || ' returns a different set of columns depending on use.'         end as Description,     f.ParamDefaultValue,     f.TableParamColumns,     r.Description as ProviderDescription from     @reg r     left outer join @fld f         on r.Name = f.TableName order by     1, 5 desc, 6 desc, 2     ;     ```  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized 

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

    try:
        # GetCatalog: Shows Table and Field level information on Providers that are currently running that you have access to (in Json format)
        api_response = api_instance.get_catalog(free_text_search=free_text_search, json_proper=json_proper)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentTableFieldCatalogApi->get_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_text_search** | **str**| Limit the catalog to only things in some way dealing with the passed in text string | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

