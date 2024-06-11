# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.73
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from luminesce.api_client import ApiClient
from luminesce.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from luminesce.models.certificate_action import CertificateAction
from luminesce.models.certificate_file_type import CertificateFileType
from luminesce.models.certificate_state import CertificateState
from luminesce.models.certificate_type import CertificateType
from luminesce.models.lusid_problem_details import LusidProblemDetails


class CertificateManagementApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def download_certificate(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] DownloadCertificate: Downloads your latest Domain or User certificate's public or private key - if any  # noqa: E501

         Downloads your latest Domain or User certificate's public or private key - if any.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - certificate is not available for some reason - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_certificate(async_req=True)
        >>> result = thread.get()

        :param type: User or Domain level cert (Domain level requires additional entitlements)
        :type type: CertificateType
        :param file_type: Should the public key or private key be downloaded? (both must be in place to run providers)
        :type file_type: CertificateFileType
        :param may_auto_create: If no matching cert is available, should an attempt be made to Create/Renew it with default options?
        :type may_auto_create: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: file
        """
        kwargs['_return_http_data_only'] = True
        return self.download_certificate_with_http_info(**kwargs)  # noqa: E501

    def download_certificate_with_http_info(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] DownloadCertificate: Downloads your latest Domain or User certificate's public or private key - if any  # noqa: E501

         Downloads your latest Domain or User certificate's public or private key - if any.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - certificate is not available for some reason - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_certificate_with_http_info(async_req=True)
        >>> result = thread.get()

        :param type: User or Domain level cert (Domain level requires additional entitlements)
        :type type: CertificateType
        :param file_type: Should the public key or private key be downloaded? (both must be in place to run providers)
        :type file_type: CertificateFileType
        :param may_auto_create: If no matching cert is available, should an attempt be made to Create/Renew it with default options?
        :type may_auto_create: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (file, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'type',
            'file_type',
            'may_auto_create'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_certificate" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params and local_var_params['type'] is not None:  # noqa: E501
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'file_type' in local_var_params and local_var_params['file_type'] is not None:  # noqa: E501
            query_params.append(('fileType', local_var_params['file_type']))  # noqa: E501
        if 'may_auto_create' in local_var_params and local_var_params['may_auto_create'] is not None:  # noqa: E501
            query_params.append(('mayAutoCreate', local_var_params['may_auto_create']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '1.16.73'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "file",
            400: "LusidProblemDetails",
            403: "LusidProblemDetails",
        }

        return self.api_client.call_api(
            '/api/Certificate/certificate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def list_certificates(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListCertificates: Lists all the certificates previously minted to which you have access  # noqa: E501

         Lists all the certificates previously minted to which you have access.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_certificates(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[CertificateState]
        """
        kwargs['_return_http_data_only'] = True
        return self.list_certificates_with_http_info(**kwargs)  # noqa: E501

    def list_certificates_with_http_info(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListCertificates: Lists all the certificates previously minted to which you have access  # noqa: E501

         Lists all the certificates previously minted to which you have access.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_certificates_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (list[CertificateState], int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_certificates" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '1.16.73'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "list[CertificateState]",
            400: "LusidProblemDetails",
            403: "LusidProblemDetails",
        }

        return self.api_client.call_api(
            '/api/Certificate/certificates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def manage_certificate(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ManageCertificate: Manages a new certificate (Create / Renew / Revoke)  # noqa: E501

         Manages a certificate.  This could be creating a new one, renewing an old one or revoking one explicitly.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something about the request cannot be processed - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.manage_certificate(async_req=True)
        >>> result = thread.get()

        :param action: The Action to perform, e.g. Create / Renew / Revoke
        :type action: CertificateAction
        :param type: User or Domain level cert (Domain level requires additional entitlements)
        :type type: CertificateType
        :param version: Version number of the cert, the request will fail to validate if incorrect
        :type version: int
        :param validity_start: When should the cert first be valid (defaults to the current time in UTC)
        :type validity_start: datetime
        :param validity_end: When should the cert no longer be valid (defaults to 13 months from now)
        :type validity_end: datetime
        :param dry_run: True will just validate the request, but perform no changes to any system
        :type dry_run: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CertificateState
        """
        kwargs['_return_http_data_only'] = True
        return self.manage_certificate_with_http_info(**kwargs)  # noqa: E501

    def manage_certificate_with_http_info(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ManageCertificate: Manages a new certificate (Create / Renew / Revoke)  # noqa: E501

         Manages a certificate.  This could be creating a new one, renewing an old one or revoking one explicitly.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something about the request cannot be processed - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.manage_certificate_with_http_info(async_req=True)
        >>> result = thread.get()

        :param action: The Action to perform, e.g. Create / Renew / Revoke
        :type action: CertificateAction
        :param type: User or Domain level cert (Domain level requires additional entitlements)
        :type type: CertificateType
        :param version: Version number of the cert, the request will fail to validate if incorrect
        :type version: int
        :param validity_start: When should the cert first be valid (defaults to the current time in UTC)
        :type validity_start: datetime
        :param validity_end: When should the cert no longer be valid (defaults to 13 months from now)
        :type validity_end: datetime
        :param dry_run: True will just validate the request, but perform no changes to any system
        :type dry_run: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (CertificateState, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'action',
            'type',
            'version',
            'validity_start',
            'validity_end',
            'dry_run'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method manage_certificate" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params and local_var_params['action'] is not None:  # noqa: E501
            query_params.append(('action', local_var_params['action']))  # noqa: E501
        if 'type' in local_var_params and local_var_params['type'] is not None:  # noqa: E501
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'version' in local_var_params and local_var_params['version'] is not None:  # noqa: E501
            query_params.append(('version', local_var_params['version']))  # noqa: E501
        if 'validity_start' in local_var_params and local_var_params['validity_start'] is not None:  # noqa: E501
            query_params.append(('validityStart', local_var_params['validity_start']))  # noqa: E501
        if 'validity_end' in local_var_params and local_var_params['validity_end'] is not None:  # noqa: E501
            query_params.append(('validityEnd', local_var_params['validity_end']))  # noqa: E501
        if 'dry_run' in local_var_params and local_var_params['dry_run'] is not None:  # noqa: E501
            query_params.append(('dryRun', local_var_params['dry_run']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '1.16.73'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "CertificateState",
            400: "LusidProblemDetails",
            403: "LusidProblemDetails",
        }

        return self.api_client.call_api(
            '/api/Certificate/manage', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
