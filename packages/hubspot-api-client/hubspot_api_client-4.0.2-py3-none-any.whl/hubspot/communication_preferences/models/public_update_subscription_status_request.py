# coding: utf-8

"""
    Subscriptions

    Subscriptions allow contacts to control what forms of communications they receive. Contacts can decide whether they want to receive communication pertaining to a specific topic, brand, or an entire HubSpot account.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.communication_preferences.configuration import Configuration


class PublicUpdateSubscriptionStatusRequest(object):
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
    openapi_types = {"email_address": "str", "subscription_id": "str", "legal_basis": "str", "legal_basis_explanation": "str"}

    attribute_map = {"email_address": "emailAddress", "subscription_id": "subscriptionId", "legal_basis": "legalBasis", "legal_basis_explanation": "legalBasisExplanation"}

    def __init__(self, email_address=None, subscription_id=None, legal_basis=None, legal_basis_explanation=None, local_vars_configuration=None):  # noqa: E501
        """PublicUpdateSubscriptionStatusRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email_address = None
        self._subscription_id = None
        self._legal_basis = None
        self._legal_basis_explanation = None
        self.discriminator = None

        self.email_address = email_address
        self.subscription_id = subscription_id
        if legal_basis is not None:
            self.legal_basis = legal_basis
        if legal_basis_explanation is not None:
            self.legal_basis_explanation = legal_basis_explanation

    @property
    def email_address(self):
        """Gets the email_address of this PublicUpdateSubscriptionStatusRequest.  # noqa: E501

        Contact's email address.  # noqa: E501

        :return: The email_address of this PublicUpdateSubscriptionStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this PublicUpdateSubscriptionStatusRequest.

        Contact's email address.  # noqa: E501

        :param email_address: The email_address of this PublicUpdateSubscriptionStatusRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def subscription_id(self):
        """Gets the subscription_id of this PublicUpdateSubscriptionStatusRequest.  # noqa: E501

        ID of the subscription the contact is being resubscribed to.  # noqa: E501

        :return: The subscription_id of this PublicUpdateSubscriptionStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this PublicUpdateSubscriptionStatusRequest.

        ID of the subscription the contact is being resubscribed to.  # noqa: E501

        :param subscription_id: The subscription_id of this PublicUpdateSubscriptionStatusRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subscription_id is None:  # noqa: E501
            raise ValueError("Invalid value for `subscription_id`, must not be `None`")  # noqa: E501

        self._subscription_id = subscription_id

    @property
    def legal_basis(self):
        """Gets the legal_basis of this PublicUpdateSubscriptionStatusRequest.  # noqa: E501

        Legal basis for resubscribing the contact (required for GDPR enabled portals).  # noqa: E501

        :return: The legal_basis of this PublicUpdateSubscriptionStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._legal_basis

    @legal_basis.setter
    def legal_basis(self, legal_basis):
        """Sets the legal_basis of this PublicUpdateSubscriptionStatusRequest.

        Legal basis for resubscribing the contact (required for GDPR enabled portals).  # noqa: E501

        :param legal_basis: The legal_basis of this PublicUpdateSubscriptionStatusRequest.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "LEGITIMATE_INTEREST_PQL",
            "LEGITIMATE_INTEREST_CLIENT",
            "PERFORMANCE_OF_CONTRACT",
            "CONSENT_WITH_NOTICE",
            "NON_GDPR",
            "PROCESS_AND_STORE",
            "LEGITIMATE_INTEREST_OTHER",
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and legal_basis not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `legal_basis` ({0}), must be one of {1}".format(legal_basis, allowed_values))  # noqa: E501

        self._legal_basis = legal_basis

    @property
    def legal_basis_explanation(self):
        """Gets the legal_basis_explanation of this PublicUpdateSubscriptionStatusRequest.  # noqa: E501

        A more detailed explanation to go with the legal basis (required for GDPR enabled portals).  # noqa: E501

        :return: The legal_basis_explanation of this PublicUpdateSubscriptionStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._legal_basis_explanation

    @legal_basis_explanation.setter
    def legal_basis_explanation(self, legal_basis_explanation):
        """Sets the legal_basis_explanation of this PublicUpdateSubscriptionStatusRequest.

        A more detailed explanation to go with the legal basis (required for GDPR enabled portals).  # noqa: E501

        :param legal_basis_explanation: The legal_basis_explanation of this PublicUpdateSubscriptionStatusRequest.  # noqa: E501
        :type: str
        """

        self._legal_basis_explanation = legal_basis_explanation

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
        if not isinstance(other, PublicUpdateSubscriptionStatusRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicUpdateSubscriptionStatusRequest):
            return True

        return self.to_dict() != other.to_dict()
