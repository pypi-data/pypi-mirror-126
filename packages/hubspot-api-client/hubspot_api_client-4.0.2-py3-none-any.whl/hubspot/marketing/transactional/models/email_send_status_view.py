# coding: utf-8

"""
    Transactional Email

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.marketing.transactional.configuration import Configuration


class EmailSendStatusView(object):
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
    openapi_types = {"event_id": "EventIdView", "status_id": "str", "send_result": "str", "requested_at": "datetime", "started_at": "datetime", "completed_at": "datetime", "status": "str"}

    attribute_map = {
        "event_id": "eventId",
        "status_id": "statusId",
        "send_result": "sendResult",
        "requested_at": "requestedAt",
        "started_at": "startedAt",
        "completed_at": "completedAt",
        "status": "status",
    }

    def __init__(self, event_id=None, status_id=None, send_result=None, requested_at=None, started_at=None, completed_at=None, status=None, local_vars_configuration=None):  # noqa: E501
        """EmailSendStatusView - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event_id = None
        self._status_id = None
        self._send_result = None
        self._requested_at = None
        self._started_at = None
        self._completed_at = None
        self._status = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        self.status_id = status_id
        if send_result is not None:
            self.send_result = send_result
        if requested_at is not None:
            self.requested_at = requested_at
        if started_at is not None:
            self.started_at = started_at
        if completed_at is not None:
            self.completed_at = completed_at
        self.status = status

    @property
    def event_id(self):
        """Gets the event_id of this EmailSendStatusView.  # noqa: E501


        :return: The event_id of this EmailSendStatusView.  # noqa: E501
        :rtype: EventIdView
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this EmailSendStatusView.


        :param event_id: The event_id of this EmailSendStatusView.  # noqa: E501
        :type: EventIdView
        """

        self._event_id = event_id

    @property
    def status_id(self):
        """Gets the status_id of this EmailSendStatusView.  # noqa: E501

        Identifier used to query the status of the send.  # noqa: E501

        :return: The status_id of this EmailSendStatusView.  # noqa: E501
        :rtype: str
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this EmailSendStatusView.

        Identifier used to query the status of the send.  # noqa: E501

        :param status_id: The status_id of this EmailSendStatusView.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status_id is None:  # noqa: E501
            raise ValueError("Invalid value for `status_id`, must not be `None`")  # noqa: E501

        self._status_id = status_id

    @property
    def send_result(self):
        """Gets the send_result of this EmailSendStatusView.  # noqa: E501

        Result of the send.  # noqa: E501

        :return: The send_result of this EmailSendStatusView.  # noqa: E501
        :rtype: str
        """
        return self._send_result

    @send_result.setter
    def send_result(self, send_result):
        """Sets the send_result of this EmailSendStatusView.

        Result of the send.  # noqa: E501

        :param send_result: The send_result of this EmailSendStatusView.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "SENT",
            "IDEMPOTENT_IGNORE",
            "QUEUED",
            "IDEMPOTENT_FAIL",
            "THROTTLED",
            "EMAIL_DISABLED",
            "PORTAL_SUSPENDED",
            "INVALID_TO_ADDRESS",
            "BLOCKED_DOMAIN",
            "PREVIOUSLY_BOUNCED",
            "EMAIL_UNCONFIRMED",
            "PREVIOUS_SPAM",
            "PREVIOUSLY_UNSUBSCRIBED_MESSAGE",
            "PREVIOUSLY_UNSUBSCRIBED_PORTAL",
            "INVALID_FROM_ADDRESS",
            "CAMPAIGN_CANCELLED",
            "VALIDATION_FAILED",
            "MTA_IGNORE",
            "BLOCKED_ADDRESS",
            "PORTAL_OVER_LIMIT",
            "PORTAL_EXPIRED",
            "PORTAL_MISSING_MARKETING_SCOPE",
            "MISSING_TEMPLATE_PROPERTIES",
            "MISSING_REQUIRED_PARAMETER",
            "PORTAL_AUTHENTICATION_FAILURE",
            "MISSING_CONTENT",
            "CORRUPT_INPUT",
            "TEMPLATE_RENDER_EXCEPTION",
            "GRAYMAIL_SUPPRESSED",
            "UNCONFIGURED_SENDING_DOMAIN",
            "UNDELIVERABLE",
            "CANCELLED_ABUSE",
            "QUARANTINED_ADDRESS",
            "ADDRESS_ONLY_ACCEPTED_ON_PROD",
            "PORTAL_NOT_AUTHORIZED_FOR_APPLICATION",
            "ADDRESS_LIST_BOMBED",
            "ADDRESS_OPTED_OUT",
            "RECIPIENT_FATIGUE_SUPPRESSED",
            "TOO_MANY_RECIPIENTS",
            "PREVIOUSLY_UNSUBSCRIBED_BRAND",
            "NON_MARKETABLE_CONTACT",
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and send_result not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `send_result` ({0}), must be one of {1}".format(send_result, allowed_values))  # noqa: E501

        self._send_result = send_result

    @property
    def requested_at(self):
        """Gets the requested_at of this EmailSendStatusView.  # noqa: E501

        Time when the send was requested.  # noqa: E501

        :return: The requested_at of this EmailSendStatusView.  # noqa: E501
        :rtype: datetime
        """
        return self._requested_at

    @requested_at.setter
    def requested_at(self, requested_at):
        """Sets the requested_at of this EmailSendStatusView.

        Time when the send was requested.  # noqa: E501

        :param requested_at: The requested_at of this EmailSendStatusView.  # noqa: E501
        :type: datetime
        """

        self._requested_at = requested_at

    @property
    def started_at(self):
        """Gets the started_at of this EmailSendStatusView.  # noqa: E501

        Time when the send began processing.  # noqa: E501

        :return: The started_at of this EmailSendStatusView.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this EmailSendStatusView.

        Time when the send began processing.  # noqa: E501

        :param started_at: The started_at of this EmailSendStatusView.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def completed_at(self):
        """Gets the completed_at of this EmailSendStatusView.  # noqa: E501

        Time when the send was completed.  # noqa: E501

        :return: The completed_at of this EmailSendStatusView.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this EmailSendStatusView.

        Time when the send was completed.  # noqa: E501

        :param completed_at: The completed_at of this EmailSendStatusView.  # noqa: E501
        :type: datetime
        """

        self._completed_at = completed_at

    @property
    def status(self):
        """Gets the status of this EmailSendStatusView.  # noqa: E501

        Status of the send request.  # noqa: E501

        :return: The status of this EmailSendStatusView.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EmailSendStatusView.

        Status of the send request.  # noqa: E501

        :param status: The status of this EmailSendStatusView.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `status` ({0}), must be one of {1}".format(status, allowed_values))  # noqa: E501

        self._status = status

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
        if not isinstance(other, EmailSendStatusView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailSendStatusView):
            return True

        return self.to_dict() != other.to_dict()
