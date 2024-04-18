# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.15.42
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


class QueryDesign(object):
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
        'table_name': 'str',
        'alias': 'str',
        'fields': 'list[FieldDesign]',
        'order_by': 'list[OrderByTermDesign]',
        'limit': 'int',
        'warnings': 'list[str]',
        'available_fields': 'list[AvailableField]'
    }

    attribute_map = {
        'table_name': 'tableName',
        'alias': 'alias',
        'fields': 'fields',
        'order_by': 'orderBy',
        'limit': 'limit',
        'warnings': 'warnings',
        'available_fields': 'availableFields'
    }

    required_map = {
        'table_name': 'required',
        'alias': 'optional',
        'fields': 'required',
        'order_by': 'optional',
        'limit': 'optional',
        'warnings': 'optional',
        'available_fields': 'optional'
    }

    def __init__(self, table_name=None, alias=None, fields=None, order_by=None, limit=None, warnings=None, available_fields=None, local_vars_configuration=None):  # noqa: E501
        """QueryDesign - a model defined in OpenAPI"
        
        :param table_name:  Name of the table being designed (required)
        :type table_name: str
        :param alias:  Alias for the table in the generated SQL, if any
        :type alias: str
        :param fields:  Fields to be selected, aggregated over and/or filtered on (required)
        :type fields: list[luminesce.FieldDesign]
        :param order_by:  Order By clauses to apply
        :type order_by: list[luminesce.OrderByTermDesign]
        :param limit:  Row limit to apply, if any
        :type limit: int
        :param warnings:  Any warnings to show the user when converting from SQL to this representation
        :type warnings: list[str]
        :param available_fields:  Fields that are known to be available for design when parsing SQL
        :type available_fields: list[luminesce.AvailableField]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._table_name = None
        self._alias = None
        self._fields = None
        self._order_by = None
        self._limit = None
        self._warnings = None
        self._available_fields = None
        self.discriminator = None

        self.table_name = table_name
        self.alias = alias
        self.fields = fields
        self.order_by = order_by
        self.limit = limit
        self.warnings = warnings
        self.available_fields = available_fields

    @property
    def table_name(self):
        """Gets the table_name of this QueryDesign.  # noqa: E501

        Name of the table being designed  # noqa: E501

        :return: The table_name of this QueryDesign.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this QueryDesign.

        Name of the table being designed  # noqa: E501

        :param table_name: The table_name of this QueryDesign.  # noqa: E501
        :type table_name: str
        """
        if self.local_vars_configuration.client_side_validation and table_name is None:  # noqa: E501
            raise ValueError("Invalid value for `table_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                table_name is not None and len(table_name) > 256):
            raise ValueError("Invalid value for `table_name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                table_name is not None and len(table_name) < 0):
            raise ValueError("Invalid value for `table_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._table_name = table_name

    @property
    def alias(self):
        """Gets the alias of this QueryDesign.  # noqa: E501

        Alias for the table in the generated SQL, if any  # noqa: E501

        :return: The alias of this QueryDesign.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this QueryDesign.

        Alias for the table in the generated SQL, if any  # noqa: E501

        :param alias: The alias of this QueryDesign.  # noqa: E501
        :type alias: str
        """
        if (self.local_vars_configuration.client_side_validation and
                alias is not None and len(alias) > 256):
            raise ValueError("Invalid value for `alias`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                alias is not None and len(alias) < 0):
            raise ValueError("Invalid value for `alias`, length must be greater than or equal to `0`")  # noqa: E501

        self._alias = alias

    @property
    def fields(self):
        """Gets the fields of this QueryDesign.  # noqa: E501

        Fields to be selected, aggregated over and/or filtered on  # noqa: E501

        :return: The fields of this QueryDesign.  # noqa: E501
        :rtype: list[luminesce.FieldDesign]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this QueryDesign.

        Fields to be selected, aggregated over and/or filtered on  # noqa: E501

        :param fields: The fields of this QueryDesign.  # noqa: E501
        :type fields: list[luminesce.FieldDesign]
        """
        if self.local_vars_configuration.client_side_validation and fields is None:  # noqa: E501
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def order_by(self):
        """Gets the order_by of this QueryDesign.  # noqa: E501

        Order By clauses to apply  # noqa: E501

        :return: The order_by of this QueryDesign.  # noqa: E501
        :rtype: list[luminesce.OrderByTermDesign]
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this QueryDesign.

        Order By clauses to apply  # noqa: E501

        :param order_by: The order_by of this QueryDesign.  # noqa: E501
        :type order_by: list[luminesce.OrderByTermDesign]
        """

        self._order_by = order_by

    @property
    def limit(self):
        """Gets the limit of this QueryDesign.  # noqa: E501

        Row limit to apply, if any  # noqa: E501

        :return: The limit of this QueryDesign.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueryDesign.

        Row limit to apply, if any  # noqa: E501

        :param limit: The limit of this QueryDesign.  # noqa: E501
        :type limit: int
        """

        self._limit = limit

    @property
    def warnings(self):
        """Gets the warnings of this QueryDesign.  # noqa: E501

        Any warnings to show the user when converting from SQL to this representation  # noqa: E501

        :return: The warnings of this QueryDesign.  # noqa: E501
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this QueryDesign.

        Any warnings to show the user when converting from SQL to this representation  # noqa: E501

        :param warnings: The warnings of this QueryDesign.  # noqa: E501
        :type warnings: list[str]
        """

        self._warnings = warnings

    @property
    def available_fields(self):
        """Gets the available_fields of this QueryDesign.  # noqa: E501

        Fields that are known to be available for design when parsing SQL  # noqa: E501

        :return: The available_fields of this QueryDesign.  # noqa: E501
        :rtype: list[luminesce.AvailableField]
        """
        return self._available_fields

    @available_fields.setter
    def available_fields(self, available_fields):
        """Sets the available_fields of this QueryDesign.

        Fields that are known to be available for design when parsing SQL  # noqa: E501

        :param available_fields: The available_fields of this QueryDesign.  # noqa: E501
        :type available_fields: list[luminesce.AvailableField]
        """

        self._available_fields = available_fields

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
        if not isinstance(other, QueryDesign):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryDesign):
            return True

        return self.to_dict() != other.to_dict()
