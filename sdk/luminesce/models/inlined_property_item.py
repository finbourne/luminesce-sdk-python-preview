# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.249
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


class InlinedPropertyItem(object):
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
        'key': 'str',
        'name': 'str',
        'is_main': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'is_main': 'isMain',
        'description': 'description'
    }

    required_map = {
        'key': 'required',
        'name': 'optional',
        'is_main': 'optional',
        'description': 'optional'
    }

    def __init__(self, key=None, name=None, is_main=None, description=None, local_vars_configuration=None):  # noqa: E501
        """InlinedPropertyItem - a model defined in OpenAPI"
        
        :param key:  Key of the property (required)
        :type key: str
        :param name:  Name of the property
        :type name: str
        :param is_main:  Is Main indicator for the property
        :type is_main: bool
        :param description:  Description of the property
        :type description: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._name = None
        self._is_main = None
        self._description = None
        self.discriminator = None

        self.key = key
        self.name = name
        if is_main is not None:
            self.is_main = is_main
        self.description = description

    @property
    def key(self):
        """Gets the key of this InlinedPropertyItem.  # noqa: E501

        Key of the property  # noqa: E501

        :return: The key of this InlinedPropertyItem.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this InlinedPropertyItem.

        Key of the property  # noqa: E501

        :param key: The key of this InlinedPropertyItem.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key is not None and len(key) < 1):
            raise ValueError("Invalid value for `key`, length must be greater than or equal to `1`")  # noqa: E501

        self._key = key

    @property
    def name(self):
        """Gets the name of this InlinedPropertyItem.  # noqa: E501

        Name of the property  # noqa: E501

        :return: The name of this InlinedPropertyItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlinedPropertyItem.

        Name of the property  # noqa: E501

        :param name: The name of this InlinedPropertyItem.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def is_main(self):
        """Gets the is_main of this InlinedPropertyItem.  # noqa: E501

        Is Main indicator for the property  # noqa: E501

        :return: The is_main of this InlinedPropertyItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_main

    @is_main.setter
    def is_main(self, is_main):
        """Sets the is_main of this InlinedPropertyItem.

        Is Main indicator for the property  # noqa: E501

        :param is_main: The is_main of this InlinedPropertyItem.  # noqa: E501
        :type is_main: bool
        """

        self._is_main = is_main

    @property
    def description(self):
        """Gets the description of this InlinedPropertyItem.  # noqa: E501

        Description of the property  # noqa: E501

        :return: The description of this InlinedPropertyItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlinedPropertyItem.

        Description of the property  # noqa: E501

        :param description: The description of this InlinedPropertyItem.  # noqa: E501
        :type description: str
        """

        self._description = description

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
        if not isinstance(other, InlinedPropertyItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlinedPropertyItem):
            return True

        return self.to_dict() != other.to_dict()
