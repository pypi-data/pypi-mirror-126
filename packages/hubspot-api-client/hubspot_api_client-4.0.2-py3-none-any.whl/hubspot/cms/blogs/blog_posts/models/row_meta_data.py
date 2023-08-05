# coding: utf-8

"""
    Blog Post endpoints

    \"Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags\"  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.blogs.blog_posts.configuration import Configuration


class RowMetaData(object):
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
    openapi_types = {"styles": "Styles", "css_class": "str"}

    attribute_map = {"styles": "styles", "css_class": "cssClass"}

    def __init__(self, styles=None, css_class=None, local_vars_configuration=None):  # noqa: E501
        """RowMetaData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._styles = None
        self._css_class = None
        self.discriminator = None

        self.styles = styles
        self.css_class = css_class

    @property
    def styles(self):
        """Gets the styles of this RowMetaData.  # noqa: E501


        :return: The styles of this RowMetaData.  # noqa: E501
        :rtype: Styles
        """
        return self._styles

    @styles.setter
    def styles(self, styles):
        """Sets the styles of this RowMetaData.


        :param styles: The styles of this RowMetaData.  # noqa: E501
        :type: Styles
        """
        if self.local_vars_configuration.client_side_validation and styles is None:  # noqa: E501
            raise ValueError("Invalid value for `styles`, must not be `None`")  # noqa: E501

        self._styles = styles

    @property
    def css_class(self):
        """Gets the css_class of this RowMetaData.  # noqa: E501


        :return: The css_class of this RowMetaData.  # noqa: E501
        :rtype: str
        """
        return self._css_class

    @css_class.setter
    def css_class(self, css_class):
        """Sets the css_class of this RowMetaData.


        :param css_class: The css_class of this RowMetaData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and css_class is None:  # noqa: E501
            raise ValueError("Invalid value for `css_class`, must not be `None`")  # noqa: E501

        self._css_class = css_class

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
        if not isinstance(other, RowMetaData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RowMetaData):
            return True

        return self.to_dict() != other.to_dict()
