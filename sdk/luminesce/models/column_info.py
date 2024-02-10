# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.14.486
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


class ColumnInfo(object):
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
        'select': 'bool',
        'type': 'DataType',
        'name': 'str',
        'x_path': 'str'
    }

    attribute_map = {
        'select': 'select',
        'type': 'type',
        'name': 'name',
        'x_path': 'xPath'
    }

    required_map = {
        'select': 'optional',
        'type': 'optional',
        'name': 'optional',
        'x_path': 'optional'
    }

    def __init__(self, select=None, type=None, name=None, x_path=None, local_vars_configuration=None):  # noqa: E501
        """ColumnInfo - a model defined in OpenAPI"
        
        :param select:  Should the column be used/selected?
        :type select: bool
        :param type: 
        :type type: luminesce.DataType
        :param name:  The name of the column
        :type name: str
        :param x_path:  Xpath for the column (only applicable to XML defined columns)
        :type x_path: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._select = None
        self._type = None
        self._name = None
        self._x_path = None
        self.discriminator = None

        if select is not None:
            self.select = select
        if type is not None:
            self.type = type
        self.name = name
        self.x_path = x_path

    @property
    def select(self):
        """Gets the select of this ColumnInfo.  # noqa: E501

        Should the column be used/selected?  # noqa: E501

        :return: The select of this ColumnInfo.  # noqa: E501
        :rtype: bool
        """
        return self._select

    @select.setter
    def select(self, select):
        """Sets the select of this ColumnInfo.

        Should the column be used/selected?  # noqa: E501

        :param select: The select of this ColumnInfo.  # noqa: E501
        :type select: bool
        """

        self._select = select

    @property
    def type(self):
        """Gets the type of this ColumnInfo.  # noqa: E501


        :return: The type of this ColumnInfo.  # noqa: E501
        :rtype: luminesce.DataType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ColumnInfo.


        :param type: The type of this ColumnInfo.  # noqa: E501
        :type type: luminesce.DataType
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this ColumnInfo.  # noqa: E501

        The name of the column  # noqa: E501

        :return: The name of this ColumnInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ColumnInfo.

        The name of the column  # noqa: E501

        :param name: The name of this ColumnInfo.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 256):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def x_path(self):
        """Gets the x_path of this ColumnInfo.  # noqa: E501

        Xpath for the column (only applicable to XML defined columns)  # noqa: E501

        :return: The x_path of this ColumnInfo.  # noqa: E501
        :rtype: str
        """
        return self._x_path

    @x_path.setter
    def x_path(self, x_path):
        """Sets the x_path of this ColumnInfo.

        Xpath for the column (only applicable to XML defined columns)  # noqa: E501

        :param x_path: The x_path of this ColumnInfo.  # noqa: E501
        :type x_path: str
        """
        if (self.local_vars_configuration.client_side_validation and
                x_path is not None and len(x_path) > 256):
            raise ValueError("Invalid value for `x_path`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                x_path is not None and len(x_path) < 0):
            raise ValueError("Invalid value for `x_path`, length must be greater than or equal to `0`")  # noqa: E501

        self._x_path = x_path

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
        if not isinstance(other, ColumnInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ColumnInfo):
            return True

        return self.to_dict() != other.to_dict()
