# luminesce.LuminesceCertificateManagementApi

All URIs are relative to *https://www.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_certificates**](LuminesceCertificateManagementApi.md#get_certificates) | **GET** /api/Certificate/certificates | [EXPERIMENTAL] GetCertificates: Shows Table and Field level information on Providers that are currently running that you have access to (in Json format)
[**manage_certificate**](LuminesceCertificateManagementApi.md#manage_certificate) | **PUT** /api/Certificate/manage | [EXPERIMENTAL] ManageCertificate: Manages a new certificate (Create / Renew / Revoke)


# **get_certificates**
> list[CertificateState] get_certificates()

[EXPERIMENTAL] GetCertificates: Shows Table and Field level information on Providers that are currently running that you have access to (in Json format)

 Lists all the certificates previously minted to which you have access.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized 

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
    api_instance = luminesce.LuminesceCertificateManagementApi(api_client)
    
    try:
        # [EXPERIMENTAL] GetCertificates: Shows Table and Field level information on Providers that are currently running that you have access to (in Json format)
        api_response = api_instance.get_certificates()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LuminesceCertificateManagementApi->get_certificates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CertificateState]**](CertificateState.md)

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

# **manage_certificate**
> CertificateState manage_certificate(action=action, type=type, version=version, validity_start=validity_start, validity_end=validity_end, dry_run=dry_run)

[EXPERIMENTAL] ManageCertificate: Manages a new certificate (Create / Renew / Revoke)

 Manages a certificate.  This could be creating a new one, renewing an old one or revoking one explicitly.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something about the request cannot be processed - 401 Unauthorized 

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
    api_instance = luminesce.LuminesceCertificateManagementApi(api_client)
    action = luminesce.CertificateAction() # CertificateAction | The Action to perform, e.g. Create / Renew / Revoke (optional)
type = luminesce.CertificateType() # CertificateType | User or Domain level cert (Domain level requires additional entitlements) (optional)
version = 1 # int | Version number of the cert, the request will fail to validate if incorrect (optional) (default to 1)
validity_start = '2013-10-20T19:20:30+01:00' # datetime | When should the cert first be valid (defaults to the current time in UTC) (optional)
validity_end = '2013-10-20T19:20:30+01:00' # datetime | When should the cert no longer be valid (defaults to 13 months from now) (optional)
dry_run = True # bool | True will just validate the request, but perform no changes to any system (optional) (default to True)

    try:
        # [EXPERIMENTAL] ManageCertificate: Manages a new certificate (Create / Renew / Revoke)
        api_response = api_instance.manage_certificate(action=action, type=type, version=version, validity_start=validity_start, validity_end=validity_end, dry_run=dry_run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LuminesceCertificateManagementApi->manage_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | [**CertificateAction**](.md)| The Action to perform, e.g. Create / Renew / Revoke | [optional] 
 **type** | [**CertificateType**](.md)| User or Domain level cert (Domain level requires additional entitlements) | [optional] 
 **version** | **int**| Version number of the cert, the request will fail to validate if incorrect | [optional] [default to 1]
 **validity_start** | **datetime**| When should the cert first be valid (defaults to the current time in UTC) | [optional] 
 **validity_end** | **datetime**| When should the cert no longer be valid (defaults to 13 months from now) | [optional] 
 **dry_run** | **bool**| True will just validate the request, but perform no changes to any system | [optional] [default to True]

### Return type

[**CertificateState**](CertificateState.md)

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

