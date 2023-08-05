# coding: utf-8

# flake8: noqa

"""
    CRM Objects

    CRM objects such as companies, contacts, deals, line items, products, tickets, and quotes are standard objects in HubSpot’s CRM. These core building blocks support custom properties, store critical information, and play a central role in the HubSpot application.  ## Supported Object Types  This API provides access to collections of CRM objects, which return a map of property names to values. Each object type has its own set of default properties, which can be found by exploring the [CRM Object Properties API](https://developers.hubspot.com/docs/methods/crm-properties/crm-properties-overview).  |Object Type |Properties returned by default | |--|--| | `companies` | `name`, `domain` | | `contacts` | `firstname`, `lastname`, `email` | | `deals` | `dealname`, `amount`, `closedate`, `pipeline`, `dealstage` | | `products` | `name`, `description`, `price` | | `tickets` | `content`, `hs_pipeline`, `hs_pipeline_stage`, `hs_ticket_category`, `hs_ticket_priority`, `subject` |  Find a list of all properties for an object type using the [CRM Object Properties](https://developers.hubspot.com/docs/methods/crm-properties/get-properties) API. e.g. `GET https://api.hubapi.com/properties/v2/companies/properties`. Change the properties returned in the response using the `properties` array in the request body.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from hubspot.crm.objects.api.associations_api import AssociationsApi
from hubspot.crm.objects.api.basic_api import BasicApi
from hubspot.crm.objects.api.batch_api import BatchApi
from hubspot.crm.objects.api.gdpr_api import GDPRApi
from hubspot.crm.objects.api.search_api import SearchApi

# import ApiClient
from hubspot.crm.objects.api_client import ApiClient
from hubspot.crm.objects.configuration import Configuration
from hubspot.crm.objects.exceptions import OpenApiException
from hubspot.crm.objects.exceptions import ApiTypeError
from hubspot.crm.objects.exceptions import ApiValueError
from hubspot.crm.objects.exceptions import ApiKeyError
from hubspot.crm.objects.exceptions import ApiException

# import models into sdk package
from hubspot.crm.objects.models.associated_id import AssociatedId
from hubspot.crm.objects.models.batch_input_simple_public_object_batch_input import BatchInputSimplePublicObjectBatchInput
from hubspot.crm.objects.models.batch_input_simple_public_object_id import BatchInputSimplePublicObjectId
from hubspot.crm.objects.models.batch_input_simple_public_object_input import BatchInputSimplePublicObjectInput
from hubspot.crm.objects.models.batch_read_input_simple_public_object_id import BatchReadInputSimplePublicObjectId
from hubspot.crm.objects.models.batch_response_simple_public_object import BatchResponseSimplePublicObject
from hubspot.crm.objects.models.batch_response_simple_public_object_with_errors import BatchResponseSimplePublicObjectWithErrors
from hubspot.crm.objects.models.collection_response_associated_id import CollectionResponseAssociatedId
from hubspot.crm.objects.models.collection_response_associated_id_forward_paging import CollectionResponseAssociatedIdForwardPaging
from hubspot.crm.objects.models.collection_response_simple_public_object_with_associations_forward_paging import CollectionResponseSimplePublicObjectWithAssociationsForwardPaging
from hubspot.crm.objects.models.collection_response_with_total_simple_public_object_forward_paging import CollectionResponseWithTotalSimplePublicObjectForwardPaging
from hubspot.crm.objects.models.error import Error
from hubspot.crm.objects.models.error_category import ErrorCategory
from hubspot.crm.objects.models.error_detail import ErrorDetail
from hubspot.crm.objects.models.filter import Filter
from hubspot.crm.objects.models.filter_group import FilterGroup
from hubspot.crm.objects.models.forward_paging import ForwardPaging
from hubspot.crm.objects.models.next_page import NextPage
from hubspot.crm.objects.models.paging import Paging
from hubspot.crm.objects.models.previous_page import PreviousPage
from hubspot.crm.objects.models.public_object_search_request import PublicObjectSearchRequest
from hubspot.crm.objects.models.simple_public_object import SimplePublicObject
from hubspot.crm.objects.models.simple_public_object_batch_input import SimplePublicObjectBatchInput
from hubspot.crm.objects.models.simple_public_object_id import SimplePublicObjectId
from hubspot.crm.objects.models.simple_public_object_input import SimplePublicObjectInput
from hubspot.crm.objects.models.simple_public_object_with_associations import SimplePublicObjectWithAssociations
from hubspot.crm.objects.models.standard_error import StandardError
