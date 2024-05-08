# luminesce.BinaryDownloadingApi

All URIs are relative to *https://www.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_binary**](BinaryDownloadingApi.md#download_binary) | **GET** /api/Download/download | [EXPERIMENTAL] DownloadBinary: Downloads the latest version (or specific if needs be) of the specified Luminesce Binary, given the required entitlements.


# **download_binary**
> file download_binary(type=type, version=version)

[EXPERIMENTAL] DownloadBinary: Downloads the latest version (or specific if needs be) of the specified Luminesce Binary, given the required entitlements.

 Downloads the latest version (or specific if needs be) of the specified Luminesce Binary, given the required entitlements.  *NOTE:* This endpoint is an alternative to time-consuming manual distribution via Drive or Email. > it relies on as underlying datastore that is not quite as \"Highly Available\" to the degree  > that FINBOURNE services generally are.   > Thus it is not subject to the same SLAs as other API endpoints are. > *If you perceive an outage, please try again later.*  Once a file has been downloaded the following steps can be used to install it (for the dotnet tools at least):  1. Open a terminal and cd to the directory you downloaded it to 2. Install / extract files from that package via: ``` dotnet tool install NameOfFileWithoutVersionNumberOrExtension -g --add-source \".\" ``` e.g. ``` dotnet tool install Finbourne.Luminesce.DbProviders.Oracle_Snowflake -g --add-source \".\" ``` 3. Execute them (see documentation for specific binary)...  The installed binaries can then be found in - Windows - `%USERPROFILE%\\.dotnet\\tools\\.store\\` - Linux/macOS - `$HOME/.dotnet/tools/.store/`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - binary file is not available for some reason (e.g. permissions or invalid version) - 401 Unauthorized - 403 Forbidden 

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
    api_instance = luminesce.BinaryDownloadingApi(api_client)
    type = luminesce.LuminesceBinaryType() # LuminesceBinaryType | Type of binary to download (each requires separate licenses and entitlements) (optional)
version = 'version_example' # str | An explicit version of the binary.  Leave blank to get the latest version (recommended) (optional)

    try:
        # [EXPERIMENTAL] DownloadBinary: Downloads the latest version (or specific if needs be) of the specified Luminesce Binary, given the required entitlements.
        api_response = api_instance.download_binary(type=type, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BinaryDownloadingApi->download_binary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**LuminesceBinaryType**](.md)| Type of binary to download (each requires separate licenses and entitlements) | [optional] 
 **version** | **str**| An explicit version of the binary.  Leave blank to get the latest version (recommended) | [optional] 

### Return type

**file**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The .nupkg file of the requested binary |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

