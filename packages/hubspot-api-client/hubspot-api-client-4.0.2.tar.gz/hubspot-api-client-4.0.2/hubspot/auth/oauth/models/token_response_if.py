# coding: utf-8

"""
    OAuthService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.auth.oauth.configuration import Configuration


class TokenResponseIF(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"refresh_token": "str", "expires_in": "int", "access_token": "str", "id_token": "str", "token_type": "str"}

    attribute_map = {"refresh_token": "refresh_token", "expires_in": "expires_in", "access_token": "access_token", "id_token": "id_token", "token_type": "token_type"}

    def __init__(self, refresh_token=None, expires_in=None, access_token=None, id_token=None, token_type=None, local_vars_configuration=None):  # noqa: E501
        """TokenResponseIF - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._refresh_token = None
        self._expires_in = None
        self._access_token = None
        self._id_token = None
        self._token_type = None
        self.discriminator = None

        self.refresh_token = refresh_token
        self.expires_in = expires_in
        self.access_token = access_token
        if id_token is not None:
            self.id_token = id_token
        self.token_type = token_type

    @property
    def refresh_token(self):
        """Gets the refresh_token of this TokenResponseIF.  # noqa: E501


        :return: The refresh_token of this TokenResponseIF.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this TokenResponseIF.


        :param refresh_token: The refresh_token of this TokenResponseIF.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and refresh_token is None:  # noqa: E501
            raise ValueError("Invalid value for `refresh_token`, must not be `None`")  # noqa: E501

        self._refresh_token = refresh_token

    @property
    def expires_in(self):
        """Gets the expires_in of this TokenResponseIF.  # noqa: E501


        :return: The expires_in of this TokenResponseIF.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this TokenResponseIF.


        :param expires_in: The expires_in of this TokenResponseIF.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and expires_in is None:  # noqa: E501
            raise ValueError("Invalid value for `expires_in`, must not be `None`")  # noqa: E501

        self._expires_in = expires_in

    @property
    def access_token(self):
        """Gets the access_token of this TokenResponseIF.  # noqa: E501


        :return: The access_token of this TokenResponseIF.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this TokenResponseIF.


        :param access_token: The access_token of this TokenResponseIF.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and access_token is None:  # noqa: E501
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def id_token(self):
        """Gets the id_token of this TokenResponseIF.  # noqa: E501


        :return: The id_token of this TokenResponseIF.  # noqa: E501
        :rtype: str
        """
        return self._id_token

    @id_token.setter
    def id_token(self, id_token):
        """Sets the id_token of this TokenResponseIF.


        :param id_token: The id_token of this TokenResponseIF.  # noqa: E501
        :type: str
        """

        self._id_token = id_token

    @property
    def token_type(self):
        """Gets the token_type of this TokenResponseIF.  # noqa: E501


        :return: The token_type of this TokenResponseIF.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this TokenResponseIF.


        :param token_type: The token_type of this TokenResponseIF.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and token_type is None:  # noqa: E501
            raise ValueError("Invalid value for `token_type`, must not be `None`")  # noqa: E501

        self._token_type = token_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TokenResponseIF):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenResponseIF):
            return True

        return self.to_dict() != other.to_dict()
