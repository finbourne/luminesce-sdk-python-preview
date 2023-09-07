# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.13.434
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


class OrderByTermDesign(object):
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
        'field': 'str',
        'direction': 'OrderByDirection'
    }

    attribute_map = {
        'field': 'field',
        'direction': 'direction'
    }

    required_map = {
        'field': 'required',
        'direction': 'optional'
    }

    def __init__(self, field=None, direction=None, local_vars_configuration=None):  # noqa: E501
        """OrderByTermDesign - a model defined in OpenAPI"
        
        :param field:  Name of the field to order by (required)
        :type field: str
        :param direction: 
        :type direction: luminesce.OrderByDirection

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._field = None
        self._direction = None
        self.discriminator = None

        self.field = field
        if direction is not None:
            self.direction = direction

    @property
    def field(self):
        """Gets the field of this OrderByTermDesign.  # noqa: E501

        Name of the field to order by  # noqa: E501

        :return: The field of this OrderByTermDesign.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this OrderByTermDesign.

        Name of the field to order by  # noqa: E501

        :param field: The field of this OrderByTermDesign.  # noqa: E501
        :type field: str
        """
        if self.local_vars_configuration.client_side_validation and field is None:  # noqa: E501
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                field is not None and len(field) > 256):
            raise ValueError("Invalid value for `field`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                field is not None and len(field) < 0):
            raise ValueError("Invalid value for `field`, length must be greater than or equal to `0`")  # noqa: E501

        self._field = field

    @property
    def direction(self):
        """Gets the direction of this OrderByTermDesign.  # noqa: E501


        :return: The direction of this OrderByTermDesign.  # noqa: E501
        :rtype: luminesce.OrderByDirection
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this OrderByTermDesign.


        :param direction: The direction of this OrderByTermDesign.  # noqa: E501
        :type direction: luminesce.OrderByDirection
        """

        self._direction = direction

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
        if not isinstance(other, OrderByTermDesign):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderByTermDesign):
            return True

        return self.to_dict() != other.to_dict()
