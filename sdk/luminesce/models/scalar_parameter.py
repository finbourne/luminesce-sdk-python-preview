# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.385
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


class ScalarParameter(object):
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
        'name': 'str',
        'type': 'DataType',
        'value': 'object'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'value': 'value'
    }

    required_map = {
        'name': 'required',
        'type': 'required',
        'value': 'optional'
    }

    def __init__(self, name=None, type=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ScalarParameter - a model defined in OpenAPI"
        
        :param name:  Name of the scalar parameter (required)
        :type name: str
        :param type:  (required)
        :type type: luminesce.DataType
        :param value:  the default value of the parameter
        :type value: object

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._type = None
        self._value = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.value = value

    @property
    def name(self):
        """Gets the name of this ScalarParameter.  # noqa: E501

        Name of the scalar parameter  # noqa: E501

        :return: The name of this ScalarParameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScalarParameter.

        Name of the scalar parameter  # noqa: E501

        :param name: The name of this ScalarParameter.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 256):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this ScalarParameter.  # noqa: E501


        :return: The type of this ScalarParameter.  # noqa: E501
        :rtype: luminesce.DataType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScalarParameter.


        :param type: The type of this ScalarParameter.  # noqa: E501
        :type type: luminesce.DataType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def value(self):
        """Gets the value of this ScalarParameter.  # noqa: E501

        the default value of the parameter  # noqa: E501

        :return: The value of this ScalarParameter.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ScalarParameter.

        the default value of the parameter  # noqa: E501

        :param value: The value of this ScalarParameter.  # noqa: E501
        :type value: object
        """

        self._value = value

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
        if not isinstance(other, ScalarParameter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScalarParameter):
            return True

        return self.to_dict() != other.to_dict()
