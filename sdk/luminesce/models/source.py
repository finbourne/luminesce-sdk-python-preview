# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.599
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


class Source(object):
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
        'location': 'str',
        'type': 'SourceType'
    }

    attribute_map = {
        'location': 'location',
        'type': 'type'
    }

    required_map = {
        'location': 'optional',
        'type': 'optional'
    }

    def __init__(self, location=None, type=None, local_vars_configuration=None):  # noqa: E501
        """Source - a model defined in OpenAPI"
        
        :param location:  The source location.  Start of a provider name, `Drive`, `LocalFs`, `AwsS3` etc.
        :type location: str
        :param type: 
        :type type: luminesce.SourceType

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._location = None
        self._type = None
        self.discriminator = None

        self.location = location
        if type is not None:
            self.type = type

    @property
    def location(self):
        """Gets the location of this Source.  # noqa: E501

        The source location.  Start of a provider name, `Drive`, `LocalFs`, `AwsS3` etc.  # noqa: E501

        :return: The location of this Source.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Source.

        The source location.  Start of a provider name, `Drive`, `LocalFs`, `AwsS3` etc.  # noqa: E501

        :param location: The location of this Source.  # noqa: E501
        :type location: str
        """
        if (self.local_vars_configuration.client_side_validation and
                location is not None and len(location) > 256):
            raise ValueError("Invalid value for `location`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                location is not None and len(location) < 0):
            raise ValueError("Invalid value for `location`, length must be greater than or equal to `0`")  # noqa: E501

        self._location = location

    @property
    def type(self):
        """Gets the type of this Source.  # noqa: E501


        :return: The type of this Source.  # noqa: E501
        :rtype: luminesce.SourceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Source.


        :param type: The type of this Source.  # noqa: E501
        :type type: luminesce.SourceType
        """

        self._type = type

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
        if not isinstance(other, Source):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Source):
            return True

        return self.to_dict() != other.to_dict()
