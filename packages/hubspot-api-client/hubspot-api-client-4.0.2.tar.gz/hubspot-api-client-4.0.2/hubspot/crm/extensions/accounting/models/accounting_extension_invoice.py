# coding: utf-8

"""
    Accounting Extension

    These APIs allow you to interact with HubSpot's Accounting Extension. It allows you to: * Specify the URLs that HubSpot will use when making webhook requests to your external accounting system. * Respond to webhook calls made to your external accounting system by HubSpot   # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.accounting.configuration import Configuration


class AccountingExtensionInvoice(object):
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
    openapi_types = {
        "amount_due": "float",
        "balance": "float",
        "due_date": "date",
        "invoice_number": "str",
        "customer_id": "str",
        "currency": "str",
        "invoice_link": "str",
        "customer_name": "str",
        "status": "str",
    }

    attribute_map = {
        "amount_due": "amountDue",
        "balance": "balance",
        "due_date": "dueDate",
        "invoice_number": "invoiceNumber",
        "customer_id": "customerId",
        "currency": "currency",
        "invoice_link": "invoiceLink",
        "customer_name": "customerName",
        "status": "status",
    }

    def __init__(
        self, amount_due=None, balance=None, due_date=None, invoice_number=None, customer_id=None, currency=None, invoice_link=None, customer_name=None, status=None, local_vars_configuration=None
    ):  # noqa: E501
        """AccountingExtensionInvoice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount_due = None
        self._balance = None
        self._due_date = None
        self._invoice_number = None
        self._customer_id = None
        self._currency = None
        self._invoice_link = None
        self._customer_name = None
        self._status = None
        self.discriminator = None

        self.amount_due = amount_due
        if balance is not None:
            self.balance = balance
        self.due_date = due_date
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if customer_id is not None:
            self.customer_id = customer_id
        self.currency = currency
        self.invoice_link = invoice_link
        self.customer_name = customer_name
        self.status = status

    @property
    def amount_due(self):
        """Gets the amount_due of this AccountingExtensionInvoice.  # noqa: E501

        The total amount due.  # noqa: E501

        :return: The amount_due of this AccountingExtensionInvoice.  # noqa: E501
        :rtype: float
        """
        return self._amount_due

    @amount_due.setter
    def amount_due(self, amount_due):
        """Sets the amount_due of this AccountingExtensionInvoice.

        The total amount due.  # noqa: E501

        :param amount_due: The amount_due of this AccountingExtensionInvoice.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and amount_due is None:  # noqa: E501
            raise ValueError("Invalid value for `amount_due`, must not be `None`")  # noqa: E501

        self._amount_due = amount_due

    @property
    def balance(self):
        """Gets the balance of this AccountingExtensionInvoice.  # noqa: E501

        The remaining outstanding balance due.  # noqa: E501

        :return: The balance of this AccountingExtensionInvoice.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this AccountingExtensionInvoice.

        The remaining outstanding balance due.  # noqa: E501

        :param balance: The balance of this AccountingExtensionInvoice.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def due_date(self):
        """Gets the due_date of this AccountingExtensionInvoice.  # noqa: E501

        The due date for payment of the invoice, in ISO-8601 date format (yyyy-MM-dd)  # noqa: E501

        :return: The due_date of this AccountingExtensionInvoice.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this AccountingExtensionInvoice.

        The due date for payment of the invoice, in ISO-8601 date format (yyyy-MM-dd)  # noqa: E501

        :param due_date: The due_date of this AccountingExtensionInvoice.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and due_date is None:  # noqa: E501
            raise ValueError("Invalid value for `due_date`, must not be `None`")  # noqa: E501

        self._due_date = due_date

    @property
    def invoice_number(self):
        """Gets the invoice_number of this AccountingExtensionInvoice.  # noqa: E501

        The invoice number  # noqa: E501

        :return: The invoice_number of this AccountingExtensionInvoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this AccountingExtensionInvoice.

        The invoice number  # noqa: E501

        :param invoice_number: The invoice_number of this AccountingExtensionInvoice.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def customer_id(self):
        """Gets the customer_id of this AccountingExtensionInvoice.  # noqa: E501

        The ID of the customer that this invoice is for.  # noqa: E501

        :return: The customer_id of this AccountingExtensionInvoice.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AccountingExtensionInvoice.

        The ID of the customer that this invoice is for.  # noqa: E501

        :param customer_id: The customer_id of this AccountingExtensionInvoice.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def currency(self):
        """Gets the currency of this AccountingExtensionInvoice.  # noqa: E501

        The ISO 4217 currency code that represents the currency of this invoice.  # noqa: E501

        :return: The currency of this AccountingExtensionInvoice.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AccountingExtensionInvoice.

        The ISO 4217 currency code that represents the currency of this invoice.  # noqa: E501

        :param currency: The currency of this AccountingExtensionInvoice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def invoice_link(self):
        """Gets the invoice_link of this AccountingExtensionInvoice.  # noqa: E501

        A link to the invoice in the external accounting system.  # noqa: E501

        :return: The invoice_link of this AccountingExtensionInvoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_link

    @invoice_link.setter
    def invoice_link(self, invoice_link):
        """Sets the invoice_link of this AccountingExtensionInvoice.

        A link to the invoice in the external accounting system.  # noqa: E501

        :param invoice_link: The invoice_link of this AccountingExtensionInvoice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and invoice_link is None:  # noqa: E501
            raise ValueError("Invalid value for `invoice_link`, must not be `None`")  # noqa: E501

        self._invoice_link = invoice_link

    @property
    def customer_name(self):
        """Gets the customer_name of this AccountingExtensionInvoice.  # noqa: E501

        The name of the customer that this invoice is for.  # noqa: E501

        :return: The customer_name of this AccountingExtensionInvoice.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this AccountingExtensionInvoice.

        The name of the customer that this invoice is for.  # noqa: E501

        :param customer_name: The customer_name of this AccountingExtensionInvoice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and customer_name is None:  # noqa: E501
            raise ValueError("Invalid value for `customer_name`, must not be `None`")  # noqa: E501

        self._customer_name = customer_name

    @property
    def status(self):
        """Gets the status of this AccountingExtensionInvoice.  # noqa: E501

        The currency status of the invoice.  # noqa: E501

        :return: The status of this AccountingExtensionInvoice.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountingExtensionInvoice.

        The currency status of the invoice.  # noqa: E501

        :param status: The status of this AccountingExtensionInvoice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["CREATED", "SENT", "PAID", "CLOSED", "OVERDUE", "VOIDED"]  # noqa: E501
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
        if not isinstance(other, AccountingExtensionInvoice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountingExtensionInvoice):
            return True

        return self.to_dict() != other.to_dict()
