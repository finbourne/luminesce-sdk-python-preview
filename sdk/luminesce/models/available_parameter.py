# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.15.60
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


class AvailableParameter(object):
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
        'parameter_name': 'str',
        'fields': 'list[MappableField]'
    }

    attribute_map = {
        'provider_name': 'providerName',
        'parameter_name': 'parameterName',
        'fields': 'fields'
    }

    required_map = {
        'provider_name': 'required',
        'parameter_name': 'required',
        'fields': 'required'
    }

    def __init__(self, provider_name=None, parameter_name=None, fields=None, local_vars_configuration=None):  # noqa: E501
        """AvailableParameter - a model defined in OpenAPI"
        
        :param provider_name:  Name of the Provider with a TableParameter (required)
        :type provider_name: str
        :param parameter_name:  Name of the TableParameter on the Provider (required)
        :type parameter_name: str
        :param fields:  Fields that can be mapped to (required)
        :type fields: list[luminesce.MappableField]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._provider_name = None
        self._parameter_name = None
        self._fields = None
        self.discriminator = None

        self.provider_name = provider_name
        self.parameter_name = parameter_name
        self.fields = fields

    @property
    def provider_name(self):
        """Gets the provider_name of this AvailableParameter.  # noqa: E501

        Name of the Provider with a TableParameter  # noqa: E501

        :return: The provider_name of this AvailableParameter.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this AvailableParameter.

        Name of the Provider with a TableParameter  # noqa: E501

        :param provider_name: The provider_name of this AvailableParameter.  # noqa: E501
        :type provider_name: str
        """
        if self.local_vars_configuration.client_side_validation and provider_name is None:  # noqa: E501
            raise ValueError("Invalid value for `provider_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                provider_name is not None and len(provider_name) < 1):
            raise ValueError("Invalid value for `provider_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._provider_name = provider_name

    @property
    def parameter_name(self):
        """Gets the parameter_name of this AvailableParameter.  # noqa: E501

        Name of the TableParameter on the Provider  # noqa: E501

        :return: The parameter_name of this AvailableParameter.  # noqa: E501
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this AvailableParameter.

        Name of the TableParameter on the Provider  # noqa: E501

        :param parameter_name: The parameter_name of this AvailableParameter.  # noqa: E501
        :type parameter_name: str
        """
        if self.local_vars_configuration.client_side_validation and parameter_name is None:  # noqa: E501
            raise ValueError("Invalid value for `parameter_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                parameter_name is not None and len(parameter_name) < 1):
            raise ValueError("Invalid value for `parameter_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._parameter_name = parameter_name

    @property
    def fields(self):
        """Gets the fields of this AvailableParameter.  # noqa: E501

        Fields that can be mapped to  # noqa: E501

        :return: The fields of this AvailableParameter.  # noqa: E501
        :rtype: list[luminesce.MappableField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this AvailableParameter.

        Fields that can be mapped to  # noqa: E501

        :param fields: The fields of this AvailableParameter.  # noqa: E501
        :type fields: list[luminesce.MappableField]
        """
        if self.local_vars_configuration.client_side_validation and fields is None:  # noqa: E501
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

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
        if not isinstance(other, AvailableParameter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AvailableParameter):
            return True

        return self.to_dict() != other.to_dict()
