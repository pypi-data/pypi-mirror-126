# coding: utf-8

"""
    Products

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.products.api_client import ApiClient
from hubspot.crm.products.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class AssociationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, product_id, to_object_type, to_object_id, association_type, **kwargs):  # noqa: E501
        """Remove an association between two products  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive(product_id, to_object_type, to_object_id, association_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str product_id: (required)
        :param str to_object_type: (required)
        :param str to_object_id: (required)
        :param str association_type: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.archive_with_http_info(product_id, to_object_type, to_object_id, association_type, **kwargs)  # noqa: E501

    def archive_with_http_info(self, product_id, to_object_type, to_object_id, association_type, **kwargs):  # noqa: E501
        """Remove an association between two products  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_with_http_info(product_id, to_object_type, to_object_id, association_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str product_id: (required)
        :param str to_object_type: (required)
        :param str to_object_id: (required)
        :param str association_type: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["product_id", "to_object_type", "to_object_id", "association_type"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method archive" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ("product_id" not in local_var_params or local_var_params["product_id"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `product_id` when calling `archive`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and ("to_object_type" not in local_var_params or local_var_params["to_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `archive`")  # noqa: E501
        # verify the required parameter 'to_object_id' is set
        if self.api_client.client_side_validation and ("to_object_id" not in local_var_params or local_var_params["to_object_id"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_id` when calling `archive`")  # noqa: E501
        # verify the required parameter 'association_type' is set
        if self.api_client.client_side_validation and ("association_type" not in local_var_params or local_var_params["association_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `association_type` when calling `archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "product_id" in local_var_params:
            path_params["productId"] = local_var_params["product_id"]  # noqa: E501
        if "to_object_type" in local_var_params:
            path_params["toObjectType"] = local_var_params["to_object_type"]  # noqa: E501
        if "to_object_id" in local_var_params:
            path_params["toObjectId"] = local_var_params["to_object_id"]  # noqa: E501
        if "association_type" in local_var_params:
            path_params["associationType"] = local_var_params["association_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2_legacy"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/objects/products/{productId}/associations/{toObjectType}/{toObjectId}/{associationType}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create(self, product_id, to_object_type, to_object_id, association_type, **kwargs):  # noqa: E501
        """Associate a product with another object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(product_id, to_object_type, to_object_id, association_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str product_id: (required)
        :param str to_object_type: (required)
        :param str to_object_id: (required)
        :param str association_type: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SimplePublicObjectWithAssociations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_with_http_info(product_id, to_object_type, to_object_id, association_type, **kwargs)  # noqa: E501

    def create_with_http_info(self, product_id, to_object_type, to_object_id, association_type, **kwargs):  # noqa: E501
        """Associate a product with another object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(product_id, to_object_type, to_object_id, association_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str product_id: (required)
        :param str to_object_type: (required)
        :param str to_object_id: (required)
        :param str association_type: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SimplePublicObjectWithAssociations, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["product_id", "to_object_type", "to_object_id", "association_type"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method create" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ("product_id" not in local_var_params or local_var_params["product_id"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `product_id` when calling `create`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and ("to_object_type" not in local_var_params or local_var_params["to_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `create`")  # noqa: E501
        # verify the required parameter 'to_object_id' is set
        if self.api_client.client_side_validation and ("to_object_id" not in local_var_params or local_var_params["to_object_id"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_id` when calling `create`")  # noqa: E501
        # verify the required parameter 'association_type' is set
        if self.api_client.client_side_validation and ("association_type" not in local_var_params or local_var_params["association_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `association_type` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "product_id" in local_var_params:
            path_params["productId"] = local_var_params["product_id"]  # noqa: E501
        if "to_object_type" in local_var_params:
            path_params["toObjectType"] = local_var_params["to_object_type"]  # noqa: E501
        if "to_object_id" in local_var_params:
            path_params["toObjectId"] = local_var_params["to_object_id"]  # noqa: E501
        if "association_type" in local_var_params:
            path_params["associationType"] = local_var_params["association_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2_legacy"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/objects/products/{productId}/associations/{toObjectType}/{toObjectId}/{associationType}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SimplePublicObjectWithAssociations",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_all(self, product_id, to_object_type, **kwargs):  # noqa: E501
        """List associations of a product by type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all(product_id, to_object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str product_id: (required)
        :param str to_object_type: (required)
        :param str after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :param int limit: The maximum number of results to display per page.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CollectionResponseAssociatedIdForwardPaging
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_all_with_http_info(product_id, to_object_type, **kwargs)  # noqa: E501

    def get_all_with_http_info(self, product_id, to_object_type, **kwargs):  # noqa: E501
        """List associations of a product by type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_with_http_info(product_id, to_object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str product_id: (required)
        :param str to_object_type: (required)
        :param str after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :param int limit: The maximum number of results to display per page.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CollectionResponseAssociatedIdForwardPaging, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["product_id", "to_object_type", "after", "limit"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_all" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ("product_id" not in local_var_params or local_var_params["product_id"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `product_id` when calling `get_all`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and ("to_object_type" not in local_var_params or local_var_params["to_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `get_all`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "product_id" in local_var_params:
            path_params["productId"] = local_var_params["product_id"]  # noqa: E501
        if "to_object_type" in local_var_params:
            path_params["toObjectType"] = local_var_params["to_object_type"]  # noqa: E501

        query_params = []
        if "after" in local_var_params and local_var_params["after"] is not None:  # noqa: E501
            query_params.append(("after", local_var_params["after"]))  # noqa: E501
        if "limit" in local_var_params and local_var_params["limit"] is not None:  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2_legacy"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/objects/products/{productId}/associations/{toObjectType}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CollectionResponseAssociatedIdForwardPaging",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
