# coding: utf-8

"""
    Alertmanager API

    API of the Prometheus Alertmanager (https://github.com/prometheus/alertmanager)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AlertApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_alerts(self, **kwargs):  # noqa: E501
        """get_alerts  # noqa: E501

        Get a list of alerts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alerts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool active: Show active alerts
        :param bool silenced: Show silenced alerts
        :param bool inhibited: Show inhibited alerts
        :param bool unprocessed: Show unprocessed alerts
        :param list[str] filter: A list of matchers to filter alerts by
        :param str receiver: A regex matching receivers to filter alerts by
        :return: GettableAlerts
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alerts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_alerts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_alerts_with_http_info(self, **kwargs):  # noqa: E501
        """get_alerts  # noqa: E501

        Get a list of alerts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alerts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool active: Show active alerts
        :param bool silenced: Show silenced alerts
        :param bool inhibited: Show inhibited alerts
        :param bool unprocessed: Show unprocessed alerts
        :param list[str] filter: A list of matchers to filter alerts by
        :param str receiver: A regex matching receivers to filter alerts by
        :return: GettableAlerts
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['active', 'silenced', 'inhibited', 'unprocessed', 'filter', 'receiver']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alerts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'active' in params:
            query_params.append(('active', params['active']))  # noqa: E501
        if 'silenced' in params:
            query_params.append(('silenced', params['silenced']))  # noqa: E501
        if 'inhibited' in params:
            query_params.append(('inhibited', params['inhibited']))  # noqa: E501
        if 'unprocessed' in params:
            query_params.append(('unprocessed', params['unprocessed']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'multi'  # noqa: E501
        if 'receiver' in params:
            query_params.append(('receiver', params['receiver']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/alerts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GettableAlerts',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_alerts(self, alerts, **kwargs):  # noqa: E501
        """post_alerts  # noqa: E501

        Create new Alerts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_alerts(alerts, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostableAlerts alerts: The alerts to create (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_alerts_with_http_info(alerts, **kwargs)  # noqa: E501
        else:
            (data) = self.post_alerts_with_http_info(alerts, **kwargs)  # noqa: E501
            return data

    def post_alerts_with_http_info(self, alerts, **kwargs):  # noqa: E501
        """post_alerts  # noqa: E501

        Create new Alerts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_alerts_with_http_info(alerts, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostableAlerts alerts: The alerts to create (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alerts']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_alerts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alerts' is set
        if ('alerts' not in params or
                params['alerts'] is None):
            raise ValueError("Missing the required parameter `alerts` when calling `post_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'alerts' in params:
            body_params = params['alerts']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/alerts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)