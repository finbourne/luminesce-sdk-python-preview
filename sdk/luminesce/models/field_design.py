# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.13.934
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


class FieldDesign(object):
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
        'alias': 'str',
        'data_type': 'DataType',
        'should_select': 'bool',
        'filters': 'list[FilterTermDesign]',
        'aggregations': 'list[Aggregation]'
    }

    attribute_map = {
        'name': 'name',
        'alias': 'alias',
        'data_type': 'dataType',
        'should_select': 'shouldSelect',
        'filters': 'filters',
        'aggregations': 'aggregations'
    }

    required_map = {
        'name': 'required',
        'alias': 'optional',
        'data_type': 'optional',
        'should_select': 'optional',
        'filters': 'optional',
        'aggregations': 'optional'
    }

    def __init__(self, name=None, alias=None, data_type=None, should_select=None, filters=None, aggregations=None, local_vars_configuration=None):  # noqa: E501
        """FieldDesign - a model defined in OpenAPI"
        
        :param name:  Name of the Field (required)
        :type name: str
        :param alias:  Alias if any (if none the Name is used)
        :type alias: str
        :param data_type: 
        :type data_type: luminesce.DataType
        :param should_select:  Should this be selected? False would imply it is only being filtered on.  Ignored when Aggregations are present
        :type should_select: bool
        :param filters:  Filter clauses to apply to this field (And'ed together)
        :type filters: list[luminesce.FilterTermDesign]
        :param aggregations:  Aggregations to apply (as opposed to simply selecting)
        :type aggregations: list[luminesce.Aggregation]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._alias = None
        self._data_type = None
        self._should_select = None
        self._filters = None
        self._aggregations = None
        self.discriminator = None

        self.name = name
        self.alias = alias
        if data_type is not None:
            self.data_type = data_type
        if should_select is not None:
            self.should_select = should_select
        self.filters = filters
        self.aggregations = aggregations

    @property
    def name(self):
        """Gets the name of this FieldDesign.  # noqa: E501

        Name of the Field  # noqa: E501

        :return: The name of this FieldDesign.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldDesign.

        Name of the Field  # noqa: E501

        :param name: The name of this FieldDesign.  # noqa: E501
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
    def alias(self):
        """Gets the alias of this FieldDesign.  # noqa: E501

        Alias if any (if none the Name is used)  # noqa: E501

        :return: The alias of this FieldDesign.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this FieldDesign.

        Alias if any (if none the Name is used)  # noqa: E501

        :param alias: The alias of this FieldDesign.  # noqa: E501
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
    def data_type(self):
        """Gets the data_type of this FieldDesign.  # noqa: E501


        :return: The data_type of this FieldDesign.  # noqa: E501
        :rtype: luminesce.DataType
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this FieldDesign.


        :param data_type: The data_type of this FieldDesign.  # noqa: E501
        :type data_type: luminesce.DataType
        """

        self._data_type = data_type

    @property
    def should_select(self):
        """Gets the should_select of this FieldDesign.  # noqa: E501

        Should this be selected? False would imply it is only being filtered on.  Ignored when Aggregations are present  # noqa: E501

        :return: The should_select of this FieldDesign.  # noqa: E501
        :rtype: bool
        """
        return self._should_select

    @should_select.setter
    def should_select(self, should_select):
        """Sets the should_select of this FieldDesign.

        Should this be selected? False would imply it is only being filtered on.  Ignored when Aggregations are present  # noqa: E501

        :param should_select: The should_select of this FieldDesign.  # noqa: E501
        :type should_select: bool
        """

        self._should_select = should_select

    @property
    def filters(self):
        """Gets the filters of this FieldDesign.  # noqa: E501

        Filter clauses to apply to this field (And'ed together)  # noqa: E501

        :return: The filters of this FieldDesign.  # noqa: E501
        :rtype: list[luminesce.FilterTermDesign]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this FieldDesign.

        Filter clauses to apply to this field (And'ed together)  # noqa: E501

        :param filters: The filters of this FieldDesign.  # noqa: E501
        :type filters: list[luminesce.FilterTermDesign]
        """

        self._filters = filters

    @property
    def aggregations(self):
        """Gets the aggregations of this FieldDesign.  # noqa: E501

        Aggregations to apply (as opposed to simply selecting)  # noqa: E501

        :return: The aggregations of this FieldDesign.  # noqa: E501
        :rtype: list[luminesce.Aggregation]
        """
        return self._aggregations

    @aggregations.setter
    def aggregations(self, aggregations):
        """Sets the aggregations of this FieldDesign.

        Aggregations to apply (as opposed to simply selecting)  # noqa: E501

        :param aggregations: The aggregations of this FieldDesign.  # noqa: E501
        :type aggregations: list[luminesce.Aggregation]
        """

        self._aggregations = aggregations

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
        if not isinstance(other, FieldDesign):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FieldDesign):
            return True

        return self.to_dict() != other.to_dict()
