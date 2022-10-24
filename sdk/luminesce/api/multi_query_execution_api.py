# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.11.389
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
from luminesce.models.background_multi_query_progress_response import BackgroundMultiQueryProgressResponse
from luminesce.models.background_multi_query_response import BackgroundMultiQueryResponse
from luminesce.models.background_query_cancel_response import BackgroundQueryCancelResponse
from luminesce.models.lusid_problem_details import LusidProblemDetails
from luminesce.models.multi_query_definition_type import MultiQueryDefinitionType


class MultiQueryExecutionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_multi_query(self, execution_id, **kwargs):  # noqa: E501
        """CancelMultiQuery: Cancels (if running) or clears the data from (if completed) a previously started query-set  # noqa: E501

        Cancel the query-set (if still running) / clear the data (if already returned) The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 404 Not Found : The requested query result doesn't exist and is not running.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cancel_multi_query(execution_id, async_req=True)
        >>> result = thread.get()

        :param execution_id: ExecutionId returned when starting the query (required)
        :type execution_id: str
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
        :rtype: BackgroundQueryCancelResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.cancel_multi_query_with_http_info(execution_id, **kwargs)  # noqa: E501

    def cancel_multi_query_with_http_info(self, execution_id, **kwargs):  # noqa: E501
        """CancelMultiQuery: Cancels (if running) or clears the data from (if completed) a previously started query-set  # noqa: E501

        Cancel the query-set (if still running) / clear the data (if already returned) The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 404 Not Found : The requested query result doesn't exist and is not running.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cancel_multi_query_with_http_info(execution_id, async_req=True)
        >>> result = thread.get()

        :param execution_id: ExecutionId returned when starting the query (required)
        :type execution_id: str
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
        :rtype: (BackgroundQueryCancelResponse, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'execution_id'
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
                    " to method cancel_multi_query" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'execution_id' is set
        if self.api_client.client_side_validation and ('execution_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['execution_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `execution_id` when calling `cancel_multi_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'execution_id' in local_var_params:
            path_params['executionId'] = local_var_params['execution_id']  # noqa: E501

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
        header_params['X-LUSID-SDK-Version'] = '1.11.389'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "BackgroundQueryCancelResponse",
        }

        return self.api_client.call_api(
            '/api/MultiQueryBackground/{executionId}', 'DELETE',
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

    def get_progress_of_multi_query(self, execution_id, **kwargs):  # noqa: E501
        """GetProgressOfMultiQuery: View progress information (up until this point) for the entire query-set  # noqa: E501

        View progress information (up until this point) for the entire query-set The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 404 Not Found : The requested query result doesn't exist and is not running. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_progress_of_multi_query(execution_id, async_req=True)
        >>> result = thread.get()

        :param execution_id: ExecutionId returned when starting the query (required)
        :type execution_id: str
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
        :rtype: BackgroundMultiQueryProgressResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_progress_of_multi_query_with_http_info(execution_id, **kwargs)  # noqa: E501

    def get_progress_of_multi_query_with_http_info(self, execution_id, **kwargs):  # noqa: E501
        """GetProgressOfMultiQuery: View progress information (up until this point) for the entire query-set  # noqa: E501

        View progress information (up until this point) for the entire query-set The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 404 Not Found : The requested query result doesn't exist and is not running. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_progress_of_multi_query_with_http_info(execution_id, async_req=True)
        >>> result = thread.get()

        :param execution_id: ExecutionId returned when starting the query (required)
        :type execution_id: str
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
        :rtype: (BackgroundMultiQueryProgressResponse, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'execution_id'
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
                    " to method get_progress_of_multi_query" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'execution_id' is set
        if self.api_client.client_side_validation and ('execution_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['execution_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `execution_id` when calling `get_progress_of_multi_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'execution_id' in local_var_params:
            path_params['executionId'] = local_var_params['execution_id']  # noqa: E501

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
        header_params['X-LUSID-SDK-Version'] = '1.11.389'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "BackgroundMultiQueryProgressResponse",
        }

        return self.api_client.call_api(
            '/api/MultiQueryBackground/{executionId}', 'GET',
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

    def start_queries(self, type, body, **kwargs):  # noqa: E501
        """StartQueries: Starts to Execute the LuminesceSql statements in the background.  # noqa: E501

         Allow for starting a potentially long running query and getting back an immediate response with how to  - fetch the data in various formats (if available, or if not simply being informed it is not yet ready), on a per result basis - view progress information (up until this point), for all results in one go - cancel the queries (if still running) / clear the data (if already returned)  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - there was something wrong with your query syntax (the issue was detected at parse-time) - 401 Unauthorized   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.start_queries(type, body, async_req=True)
        >>> result = thread.get()

        :param type: An enum value defining the set of statements being executed (required)
        :type type: MultiQueryDefinitionType
        :param body: A \"search\" value (e.g. 'Apple' on an instrument search, a `Finbourne.Filtering` expression of Insights, etc.)  In the cases where \"Nothing\" is valid for a `Finbourne.Filtering` expression, pass `True`. (required)
        :type body: str
        :param as_at: The AsAt time used by any bitemporal provider in the queries.
        :type as_at: datetime
        :param effective_at: The EffectiveAt time used by any bitemporal provider in the queries.
        :type effective_at: datetime
        :param limit1: A limit that is applied to first-level queries (e.g. Instruments themselves)
        :type limit1: int
        :param limit2: A limit that is applied to second-level queries (e.g. Holdings based on the set of Instruments found)
        :type limit2: int
        :param input1: A value available to queries, these vary by 'type' and are only used by some types at all.  e.g. a start-date of some sort
        :type input1: str
        :param input2: A second value available to queries, these vary by 'type' and are only used by some types at all.
        :type input2: str
        :param input3: A third value available to queries, these vary by 'type' and are only used by some types at all.
        :type input3: str
        :param timeout_seconds: Maximum time the query may run for, in seconds: <0 → ∞, 0 → 1200s (20m)
        :type timeout_seconds: int
        :param keep_for_seconds: Maximum time the result may be kept for, in seconds: <0 → 1200 (20m), 0 → 28800 (8h), max = 2,678,400 (31d)
        :type keep_for_seconds: int
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
        :rtype: BackgroundMultiQueryResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.start_queries_with_http_info(type, body, **kwargs)  # noqa: E501

    def start_queries_with_http_info(self, type, body, **kwargs):  # noqa: E501
        """StartQueries: Starts to Execute the LuminesceSql statements in the background.  # noqa: E501

         Allow for starting a potentially long running query and getting back an immediate response with how to  - fetch the data in various formats (if available, or if not simply being informed it is not yet ready), on a per result basis - view progress information (up until this point), for all results in one go - cancel the queries (if still running) / clear the data (if already returned)  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - there was something wrong with your query syntax (the issue was detected at parse-time) - 401 Unauthorized   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.start_queries_with_http_info(type, body, async_req=True)
        >>> result = thread.get()

        :param type: An enum value defining the set of statements being executed (required)
        :type type: MultiQueryDefinitionType
        :param body: A \"search\" value (e.g. 'Apple' on an instrument search, a `Finbourne.Filtering` expression of Insights, etc.)  In the cases where \"Nothing\" is valid for a `Finbourne.Filtering` expression, pass `True`. (required)
        :type body: str
        :param as_at: The AsAt time used by any bitemporal provider in the queries.
        :type as_at: datetime
        :param effective_at: The EffectiveAt time used by any bitemporal provider in the queries.
        :type effective_at: datetime
        :param limit1: A limit that is applied to first-level queries (e.g. Instruments themselves)
        :type limit1: int
        :param limit2: A limit that is applied to second-level queries (e.g. Holdings based on the set of Instruments found)
        :type limit2: int
        :param input1: A value available to queries, these vary by 'type' and are only used by some types at all.  e.g. a start-date of some sort
        :type input1: str
        :param input2: A second value available to queries, these vary by 'type' and are only used by some types at all.
        :type input2: str
        :param input3: A third value available to queries, these vary by 'type' and are only used by some types at all.
        :type input3: str
        :param timeout_seconds: Maximum time the query may run for, in seconds: <0 → ∞, 0 → 1200s (20m)
        :type timeout_seconds: int
        :param keep_for_seconds: Maximum time the result may be kept for, in seconds: <0 → 1200 (20m), 0 → 28800 (8h), max = 2,678,400 (31d)
        :type keep_for_seconds: int
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
        :rtype: (BackgroundMultiQueryResponse, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'type',
            'body',
            'as_at',
            'effective_at',
            'limit1',
            'limit2',
            'input1',
            'input2',
            'input3',
            'timeout_seconds',
            'keep_for_seconds'
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
                    " to method start_queries" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'type' is set
        if self.api_client.client_side_validation and ('type' not in local_var_params or  # noqa: E501
                                                        local_var_params['type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `type` when calling `start_queries`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in local_var_params or  # noqa: E501
                                                        local_var_params['body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `start_queries`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params and local_var_params['type'] is not None:  # noqa: E501
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'as_at' in local_var_params and local_var_params['as_at'] is not None:  # noqa: E501
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'effective_at' in local_var_params and local_var_params['effective_at'] is not None:  # noqa: E501
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501
        if 'limit1' in local_var_params and local_var_params['limit1'] is not None:  # noqa: E501
            query_params.append(('limit1', local_var_params['limit1']))  # noqa: E501
        if 'limit2' in local_var_params and local_var_params['limit2'] is not None:  # noqa: E501
            query_params.append(('limit2', local_var_params['limit2']))  # noqa: E501
        if 'input1' in local_var_params and local_var_params['input1'] is not None:  # noqa: E501
            query_params.append(('input1', local_var_params['input1']))  # noqa: E501
        if 'input2' in local_var_params and local_var_params['input2'] is not None:  # noqa: E501
            query_params.append(('input2', local_var_params['input2']))  # noqa: E501
        if 'input3' in local_var_params and local_var_params['input3'] is not None:  # noqa: E501
            query_params.append(('input3', local_var_params['input3']))  # noqa: E501
        if 'timeout_seconds' in local_var_params and local_var_params['timeout_seconds'] is not None:  # noqa: E501
            query_params.append(('timeoutSeconds', local_var_params['timeout_seconds']))  # noqa: E501
        if 'keep_for_seconds' in local_var_params and local_var_params['keep_for_seconds'] is not None:  # noqa: E501
            query_params.append(('keepForSeconds', local_var_params['keep_for_seconds']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/plain'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '1.11.389'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            202: "BackgroundMultiQueryResponse",
            400: "LusidProblemDetails",
        }

        return self.api_client.call_api(
            '/api/MultiQueryBackground', 'PUT',
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
