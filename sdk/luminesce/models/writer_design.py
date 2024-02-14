# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.14.506
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


class WriterDesign(object):
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
        'sql': 'str',
        'available_to_map_from': 'list[ExpressionWithAlias]',
        'parameter': 'AvailableParameter',
        'available_parameters': 'list[AvailableParameter]'
    }

    attribute_map = {
        'sql': 'sql',
        'available_to_map_from': 'availableToMapFrom',
        'parameter': 'parameter',
        'available_parameters': 'availableParameters'
    }

    required_map = {
        'sql': 'required',
        'available_to_map_from': 'optional',
        'parameter': 'optional',
        'available_parameters': 'optional'
    }

    def __init__(self, sql=None, available_to_map_from=None, parameter=None, available_parameters=None, local_vars_configuration=None):  # noqa: E501
        """WriterDesign - a model defined in OpenAPI"
        
        :param sql:  Original SQL that started this off (required)
        :type sql: str
        :param available_to_map_from:  The data able to be mapped from as derived from the Sql
        :type available_to_map_from: list[luminesce.ExpressionWithAlias]
        :param parameter: 
        :type parameter: luminesce.AvailableParameter
        :param available_parameters:  All the parameter the user may wish to design
        :type available_parameters: list[luminesce.AvailableParameter]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._sql = None
        self._available_to_map_from = None
        self._parameter = None
        self._available_parameters = None
        self.discriminator = None

        self.sql = sql
        self.available_to_map_from = available_to_map_from
        if parameter is not None:
            self.parameter = parameter
        self.available_parameters = available_parameters

    @property
    def sql(self):
        """Gets the sql of this WriterDesign.  # noqa: E501

        Original SQL that started this off  # noqa: E501

        :return: The sql of this WriterDesign.  # noqa: E501
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this WriterDesign.

        Original SQL that started this off  # noqa: E501

        :param sql: The sql of this WriterDesign.  # noqa: E501
        :type sql: str
        """
        if self.local_vars_configuration.client_side_validation and sql is None:  # noqa: E501
            raise ValueError("Invalid value for `sql`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sql is not None and len(sql) < 1):
            raise ValueError("Invalid value for `sql`, length must be greater than or equal to `1`")  # noqa: E501

        self._sql = sql

    @property
    def available_to_map_from(self):
        """Gets the available_to_map_from of this WriterDesign.  # noqa: E501

        The data able to be mapped from as derived from the Sql  # noqa: E501

        :return: The available_to_map_from of this WriterDesign.  # noqa: E501
        :rtype: list[luminesce.ExpressionWithAlias]
        """
        return self._available_to_map_from

    @available_to_map_from.setter
    def available_to_map_from(self, available_to_map_from):
        """Sets the available_to_map_from of this WriterDesign.

        The data able to be mapped from as derived from the Sql  # noqa: E501

        :param available_to_map_from: The available_to_map_from of this WriterDesign.  # noqa: E501
        :type available_to_map_from: list[luminesce.ExpressionWithAlias]
        """

        self._available_to_map_from = available_to_map_from

    @property
    def parameter(self):
        """Gets the parameter of this WriterDesign.  # noqa: E501


        :return: The parameter of this WriterDesign.  # noqa: E501
        :rtype: luminesce.AvailableParameter
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this WriterDesign.


        :param parameter: The parameter of this WriterDesign.  # noqa: E501
        :type parameter: luminesce.AvailableParameter
        """

        self._parameter = parameter

    @property
    def available_parameters(self):
        """Gets the available_parameters of this WriterDesign.  # noqa: E501

        All the parameter the user may wish to design  # noqa: E501

        :return: The available_parameters of this WriterDesign.  # noqa: E501
        :rtype: list[luminesce.AvailableParameter]
        """
        return self._available_parameters

    @available_parameters.setter
    def available_parameters(self, available_parameters):
        """Sets the available_parameters of this WriterDesign.

        All the parameter the user may wish to design  # noqa: E501

        :param available_parameters: The available_parameters of this WriterDesign.  # noqa: E501
        :type available_parameters: list[luminesce.AvailableParameter]
        """

        self._available_parameters = available_parameters

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
        if not isinstance(other, WriterDesign):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WriterDesign):
            return True

        return self.to_dict() != other.to_dict()
