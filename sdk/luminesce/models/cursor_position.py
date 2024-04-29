# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.15.104
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


class CursorPosition(object):
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
        'row': 'int',
        'column': 'int'
    }

    attribute_map = {
        'row': 'row',
        'column': 'column'
    }

    required_map = {
        'row': 'required',
        'column': 'required'
    }

    def __init__(self, row=None, column=None, local_vars_configuration=None):  # noqa: E501
        """CursorPosition - a model defined in OpenAPI"
        
        :param row:  Row (0 based) of the user's cursor position (required)
        :type row: int
        :param column:  Column (0 based) of the user's cursor position (required)
        :type column: int

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._row = None
        self._column = None
        self.discriminator = None

        self.row = row
        self.column = column

    @property
    def row(self):
        """Gets the row of this CursorPosition.  # noqa: E501

        Row (0 based) of the user's cursor position  # noqa: E501

        :return: The row of this CursorPosition.  # noqa: E501
        :rtype: int
        """
        return self._row

    @row.setter
    def row(self, row):
        """Sets the row of this CursorPosition.

        Row (0 based) of the user's cursor position  # noqa: E501

        :param row: The row of this CursorPosition.  # noqa: E501
        :type row: int
        """
        if self.local_vars_configuration.client_side_validation and row is None:  # noqa: E501
            raise ValueError("Invalid value for `row`, must not be `None`")  # noqa: E501

        self._row = row

    @property
    def column(self):
        """Gets the column of this CursorPosition.  # noqa: E501

        Column (0 based) of the user's cursor position  # noqa: E501

        :return: The column of this CursorPosition.  # noqa: E501
        :rtype: int
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this CursorPosition.

        Column (0 based) of the user's cursor position  # noqa: E501

        :param column: The column of this CursorPosition.  # noqa: E501
        :type column: int
        """
        if self.local_vars_configuration.client_side_validation and column is None:  # noqa: E501
            raise ValueError("Invalid value for `column`, must not be `None`")  # noqa: E501

        self._column = column

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
        if not isinstance(other, CursorPosition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CursorPosition):
            return True

        return self.to_dict() != other.to_dict()
