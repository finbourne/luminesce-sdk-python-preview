# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.638
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


class HealthCheckingEndpointApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fake_node_reclaim(self, **kwargs):  # noqa: E501
        """[INTERNAL] FakeNodeReclaim: Helps testing of AWS node reclaim behaviour  # noqa: E501

         An internal Method used to mark the next SIGTERM as though an Aws Node reclaim were about to take place. Simulates having received an AWS node reclaim warning, or similar.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fake_node_reclaim(async_req=True)
        >>> result = thread.get()

        :param seconds_until_reclaim: the number of seconds from which to assume node termination
        :type seconds_until_reclaim: int
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
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.fake_node_reclaim_with_http_info(**kwargs)  # noqa: E501

    def fake_node_reclaim_with_http_info(self, **kwargs):  # noqa: E501
        """[INTERNAL] FakeNodeReclaim: Helps testing of AWS node reclaim behaviour  # noqa: E501

         An internal Method used to mark the next SIGTERM as though an Aws Node reclaim were about to take place. Simulates having received an AWS node reclaim warning, or similar.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fake_node_reclaim_with_http_info(async_req=True)
        >>> result = thread.get()

        :param seconds_until_reclaim: the number of seconds from which to assume node termination
        :type seconds_until_reclaim: int
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
        :rtype: (object, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'seconds_until_reclaim'
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
                    " to method fake_node_reclaim" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seconds_until_reclaim' in local_var_params and local_var_params['seconds_until_reclaim'] is not None:  # noqa: E501
            query_params.append(('secondsUntilReclaim', local_var_params['seconds_until_reclaim']))  # noqa: E501

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
        header_params['X-LUSID-SDK-Version'] = '1.16.638'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "object",
        }

        return self.api_client.call_api(
            '/fakeNodeReclaim', 'GET',
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
