# luminesce.CertificateManagementApi

All URIs are relative to *https://www.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_certificate**](CertificateManagementApi.md#download_certificate) | **GET** /api/Certificate/certificate | [EXPERIMENTAL] DownloadCertificate: Download domain or your personal certificates
[**list_certificates**](CertificateManagementApi.md#list_certificates) | **GET** /api/Certificate/certificates | [EXPERIMENTAL] ListCertificates: List previously minted certificates
[**manage_certificate**](CertificateManagementApi.md#manage_certificate) | **PUT** /api/Certificate/manage | [EXPERIMENTAL] ManageCertificate: Create / Renew / Revoke a certificate


# **download_certificate**
> file download_certificate(type=type, file_type=file_type, may_auto_create=may_auto_create)

[EXPERIMENTAL] DownloadCertificate: Download domain or your personal certificates

 Downloads your latest Domain or your User certificate's public or private key - if any.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - certificate is not available for some reason - 401 Unauthorized - 403 Forbidden 

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
    api_instance = luminesce.CertificateManagementApi(api_client)
    type = luminesce.CertificateType() # CertificateType | User or Domain level cert (Domain level requires additional entitlements) (optional)
file_type = luminesce.CertificateFileType() # CertificateFileType | Should the public key or private key be downloaded? (both must be in place to run providers) (optional)
may_auto_create = False # bool | If no matching cert is available, should an attempt be made to Create/Renew it with default options? (optional) (default to False)

    try:
        # [EXPERIMENTAL] DownloadCertificate: Download domain or your personal certificates
        api_response = api_instance.download_certificate(type=type, file_type=file_type, may_auto_create=may_auto_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CertificateManagementApi->download_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**CertificateType**](.md)| User or Domain level cert (Domain level requires additional entitlements) | [optional] 
 **file_type** | [**CertificateFileType**](.md)| Should the public key or private key be downloaded? (both must be in place to run providers) | [optional] 
 **may_auto_create** | **bool**| If no matching cert is available, should an attempt be made to Create/Renew it with default options? | [optional] [default to False]

### Return type

**file**

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificates**
> list[CertificateState] list_certificates()

[EXPERIMENTAL] ListCertificates: List previously minted certificates

 Lists all the certificates previously minted to which you have access.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

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
    api_instance = luminesce.CertificateManagementApi(api_client)
    
    try:
        # [EXPERIMENTAL] ListCertificates: List previously minted certificates
        api_response = api_instance.list_certificates()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CertificateManagementApi->list_certificates: %s\n" % e)
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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_certificate**
> CertificateState manage_certificate(action=action, type=type, version=version, validity_start=validity_start, validity_end=validity_end, dry_run=dry_run)

[EXPERIMENTAL] ManageCertificate: Create / Renew / Revoke a certificate

 Manages a certificate.  This could be creating a new one, renewing an old one or revoking one explicitly.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something about the request cannot be processed - 401 Unauthorized - 403 Forbidden 

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
    api_instance = luminesce.CertificateManagementApi(api_client)
    action = luminesce.CertificateAction() # CertificateAction | The Action to perform, e.g. Create / Renew / Revoke (optional)
type = luminesce.CertificateType() # CertificateType | User or Domain level cert (Domain level requires additional entitlements) (optional)
version = 1 # int | Version number of the cert, the request will fail to validate if incorrect (optional) (default to 1)
validity_start = '2013-10-20T19:20:30+01:00' # datetime | When should the cert first be valid (defaults to the current time in UTC) (optional)
validity_end = '2013-10-20T19:20:30+01:00' # datetime | When should the cert no longer be valid (defaults to 13 months from now) (optional)
dry_run = True # bool | True will just validate the request, but perform no changes to any system (optional) (default to True)

    try:
        # [EXPERIMENTAL] ManageCertificate: Create / Renew / Revoke a certificate
        api_response = api_instance.manage_certificate(action=action, type=type, version=version, validity_start=validity_start, validity_end=validity_end, dry_run=dry_run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CertificateManagementApi->manage_certificate: %s\n" % e)
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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

