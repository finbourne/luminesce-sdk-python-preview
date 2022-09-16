# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.11.222
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


class Column(object):
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
        'is_primary_key': 'bool',
        'is_main': 'bool',
        'is_required_by_provider': 'bool',
        'client_ids': 'list[str]',
        'name': 'str',
        'type': 'DataType',
        'description': 'str',
        'display_name': 'str',
        'condition_usage': 'ConditionAttributes',
        'sample_values': 'str',
        'allowed_values': 'str'
    }

    attribute_map = {
        'is_primary_key': 'isPrimaryKey',
        'is_main': 'isMain',
        'is_required_by_provider': 'isRequiredByProvider',
        'client_ids': 'clientIds',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'display_name': 'displayName',
        'condition_usage': 'conditionUsage',
        'sample_values': 'sampleValues',
        'allowed_values': 'allowedValues'
    }

    required_map = {
        'is_primary_key': 'optional',
        'is_main': 'optional',
        'is_required_by_provider': 'optional',
        'client_ids': 'optional',
        'name': 'optional',
        'type': 'optional',
        'description': 'optional',
        'display_name': 'optional',
        'condition_usage': 'optional',
        'sample_values': 'optional',
        'allowed_values': 'optional'
    }

    def __init__(self, is_primary_key=None, is_main=None, is_required_by_provider=None, client_ids=None, name=None, type=None, description=None, display_name=None, condition_usage=None, sample_values=None, allowed_values=None, local_vars_configuration=None):  # noqa: E501
        """Column - a model defined in OpenAPI"
        
        :param is_primary_key: 
        :type is_primary_key: bool
        :param is_main: 
        :type is_main: bool
        :param is_required_by_provider: 
        :type is_required_by_provider: bool
        :param client_ids: 
        :type client_ids: list[str]
        :param name: 
        :type name: str
        :param type: 
        :type type: luminesce.DataType
        :param description: 
        :type description: str
        :param display_name: 
        :type display_name: str
        :param condition_usage: 
        :type condition_usage: luminesce.ConditionAttributes
        :param sample_values: 
        :type sample_values: str
        :param allowed_values: 
        :type allowed_values: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._is_primary_key = None
        self._is_main = None
        self._is_required_by_provider = None
        self._client_ids = None
        self._name = None
        self._type = None
        self._description = None
        self._display_name = None
        self._condition_usage = None
        self._sample_values = None
        self._allowed_values = None
        self.discriminator = None

        if is_primary_key is not None:
            self.is_primary_key = is_primary_key
        if is_main is not None:
            self.is_main = is_main
        if is_required_by_provider is not None:
            self.is_required_by_provider = is_required_by_provider
        self.client_ids = client_ids
        self.name = name
        if type is not None:
            self.type = type
        self.description = description
        self.display_name = display_name
        if condition_usage is not None:
            self.condition_usage = condition_usage
        self.sample_values = sample_values
        self.allowed_values = allowed_values

    @property
    def is_primary_key(self):
        """Gets the is_primary_key of this Column.  # noqa: E501


        :return: The is_primary_key of this Column.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary_key

    @is_primary_key.setter
    def is_primary_key(self, is_primary_key):
        """Sets the is_primary_key of this Column.


        :param is_primary_key: The is_primary_key of this Column.  # noqa: E501
        :type is_primary_key: bool
        """

        self._is_primary_key = is_primary_key

    @property
    def is_main(self):
        """Gets the is_main of this Column.  # noqa: E501


        :return: The is_main of this Column.  # noqa: E501
        :rtype: bool
        """
        return self._is_main

    @is_main.setter
    def is_main(self, is_main):
        """Sets the is_main of this Column.


        :param is_main: The is_main of this Column.  # noqa: E501
        :type is_main: bool
        """

        self._is_main = is_main

    @property
    def is_required_by_provider(self):
        """Gets the is_required_by_provider of this Column.  # noqa: E501


        :return: The is_required_by_provider of this Column.  # noqa: E501
        :rtype: bool
        """
        return self._is_required_by_provider

    @is_required_by_provider.setter
    def is_required_by_provider(self, is_required_by_provider):
        """Sets the is_required_by_provider of this Column.


        :param is_required_by_provider: The is_required_by_provider of this Column.  # noqa: E501
        :type is_required_by_provider: bool
        """

        self._is_required_by_provider = is_required_by_provider

    @property
    def client_ids(self):
        """Gets the client_ids of this Column.  # noqa: E501


        :return: The client_ids of this Column.  # noqa: E501
        :rtype: list[str]
        """
        return self._client_ids

    @client_ids.setter
    def client_ids(self, client_ids):
        """Sets the client_ids of this Column.


        :param client_ids: The client_ids of this Column.  # noqa: E501
        :type client_ids: list[str]
        """

        self._client_ids = client_ids

    @property
    def name(self):
        """Gets the name of this Column.  # noqa: E501


        :return: The name of this Column.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Column.


        :param name: The name of this Column.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Column.  # noqa: E501


        :return: The type of this Column.  # noqa: E501
        :rtype: luminesce.DataType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Column.


        :param type: The type of this Column.  # noqa: E501
        :type type: luminesce.DataType
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this Column.  # noqa: E501


        :return: The description of this Column.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Column.


        :param description: The description of this Column.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this Column.  # noqa: E501


        :return: The display_name of this Column.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Column.


        :param display_name: The display_name of this Column.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def condition_usage(self):
        """Gets the condition_usage of this Column.  # noqa: E501


        :return: The condition_usage of this Column.  # noqa: E501
        :rtype: luminesce.ConditionAttributes
        """
        return self._condition_usage

    @condition_usage.setter
    def condition_usage(self, condition_usage):
        """Sets the condition_usage of this Column.


        :param condition_usage: The condition_usage of this Column.  # noqa: E501
        :type condition_usage: luminesce.ConditionAttributes
        """

        self._condition_usage = condition_usage

    @property
    def sample_values(self):
        """Gets the sample_values of this Column.  # noqa: E501


        :return: The sample_values of this Column.  # noqa: E501
        :rtype: str
        """
        return self._sample_values

    @sample_values.setter
    def sample_values(self, sample_values):
        """Sets the sample_values of this Column.


        :param sample_values: The sample_values of this Column.  # noqa: E501
        :type sample_values: str
        """

        self._sample_values = sample_values

    @property
    def allowed_values(self):
        """Gets the allowed_values of this Column.  # noqa: E501


        :return: The allowed_values of this Column.  # noqa: E501
        :rtype: str
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """Sets the allowed_values of this Column.


        :param allowed_values: The allowed_values of this Column.  # noqa: E501
        :type allowed_values: str
        """

        self._allowed_values = allowed_values

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
        if not isinstance(other, Column):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Column):
            return True

        return self.to_dict() != other.to_dict()
