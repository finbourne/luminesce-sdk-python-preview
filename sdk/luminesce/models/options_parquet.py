# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.682
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


class OptionsParquet(object):
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
        'column_names_wanted': 'str'
    }

    attribute_map = {
        'column_names_wanted': 'columnNamesWanted'
    }

    required_map = {
        'column_names_wanted': 'optional'
    }

    def __init__(self, column_names_wanted=None, local_vars_configuration=None):  # noqa: E501
        """OptionsParquet - a model defined in OpenAPI"
        
        :param column_names_wanted:  Column (by Name) that should be returned (comma delimited list)
        :type column_names_wanted: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._column_names_wanted = None
        self.discriminator = None

        self.column_names_wanted = column_names_wanted

    @property
    def column_names_wanted(self):
        """Gets the column_names_wanted of this OptionsParquet.  # noqa: E501

        Column (by Name) that should be returned (comma delimited list)  # noqa: E501

        :return: The column_names_wanted of this OptionsParquet.  # noqa: E501
        :rtype: str
        """
        return self._column_names_wanted

    @column_names_wanted.setter
    def column_names_wanted(self, column_names_wanted):
        """Sets the column_names_wanted of this OptionsParquet.

        Column (by Name) that should be returned (comma delimited list)  # noqa: E501

        :param column_names_wanted: The column_names_wanted of this OptionsParquet.  # noqa: E501
        :type column_names_wanted: str
        """

        self._column_names_wanted = column_names_wanted

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
        if not isinstance(other, OptionsParquet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OptionsParquet):
            return True

        return self.to_dict() != other.to_dict()
