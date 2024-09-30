# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.660
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from luminesce.configuration import Configuration


class InlinedPropertyDesign(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'provider_name': 'str',
        'inlined_property_items': 'list[InlinedPropertyItem]'
    }

    attribute_map = {
        'provider_name': 'providerName',
        'inlined_property_items': 'inlinedPropertyItems'
    }

    required_map = {
        'provider_name': 'optional',
        'inlined_property_items': 'optional'
    }

    def __init__(self, provider_name=None, inlined_property_items=None, local_vars_configuration=None):  # noqa: E501
        """InlinedPropertyDesign - a model defined in OpenAPI"
        
        :param provider_name:  The provider name for which these properties are to be inlined
        :type provider_name: str
        :param inlined_property_items:  Collection of Inlined properties
        :type inlined_property_items: list[luminesce.InlinedPropertyItem]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._provider_name = None
        self._inlined_property_items = None
        self.discriminator = None

        self.provider_name = provider_name
        self.inlined_property_items = inlined_property_items

    @property
    def provider_name(self):
        """Gets the provider_name of this InlinedPropertyDesign.  # noqa: E501

        The provider name for which these properties are to be inlined  # noqa: E501

        :return: The provider_name of this InlinedPropertyDesign.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this InlinedPropertyDesign.

        The provider name for which these properties are to be inlined  # noqa: E501

        :param provider_name: The provider_name of this InlinedPropertyDesign.  # noqa: E501
        :type provider_name: str
        """

        self._provider_name = provider_name

    @property
    def inlined_property_items(self):
        """Gets the inlined_property_items of this InlinedPropertyDesign.  # noqa: E501

        Collection of Inlined properties  # noqa: E501

        :return: The inlined_property_items of this InlinedPropertyDesign.  # noqa: E501
        :rtype: list[luminesce.InlinedPropertyItem]
        """
        return self._inlined_property_items

    @inlined_property_items.setter
    def inlined_property_items(self, inlined_property_items):
        """Sets the inlined_property_items of this InlinedPropertyDesign.

        Collection of Inlined properties  # noqa: E501

        :param inlined_property_items: The inlined_property_items of this InlinedPropertyDesign.  # noqa: E501
        :type inlined_property_items: list[luminesce.InlinedPropertyItem]
        """

        self._inlined_property_items = inlined_property_items

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlinedPropertyDesign):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlinedPropertyDesign):
            return True

        return self.to_dict() != other.to_dict()
