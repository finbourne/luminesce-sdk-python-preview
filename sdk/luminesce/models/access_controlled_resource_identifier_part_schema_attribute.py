# coding: utf-8

"""
    FINBOURNE Honeycomb Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.10.56
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


class AccessControlledResourceIdentifierPartSchemaAttribute(object):
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
        'index': 'int',
        'name': 'str',
        'display_name': 'str',
        'description': 'str',
        'required': 'bool',
        'values_path': 'str',
        'type_id': 'object'
    }

    attribute_map = {
        'index': 'index',
        'name': 'name',
        'display_name': 'displayName',
        'description': 'description',
        'required': 'required',
        'values_path': 'valuesPath',
        'type_id': 'typeId'
    }

    required_map = {
        'index': 'optional',
        'name': 'optional',
        'display_name': 'optional',
        'description': 'optional',
        'required': 'optional',
        'values_path': 'optional',
        'type_id': 'optional'
    }

    def __init__(self, index=None, name=None, display_name=None, description=None, required=None, values_path=None, type_id=None, local_vars_configuration=None):  # noqa: E501
        """AccessControlledResourceIdentifierPartSchemaAttribute - a model defined in OpenAPI"
        
        :param index: 
        :type index: int
        :param name: 
        :type name: str
        :param display_name: 
        :type display_name: str
        :param description: 
        :type description: str
        :param required: 
        :type required: bool
        :param values_path: 
        :type values_path: str
        :param type_id: 
        :type type_id: object

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._index = None
        self._name = None
        self._display_name = None
        self._description = None
        self._required = None
        self._values_path = None
        self._type_id = None
        self.discriminator = None

        if index is not None:
            self.index = index
        self.name = name
        self.display_name = display_name
        self.description = description
        if required is not None:
            self.required = required
        self.values_path = values_path
        self.type_id = type_id

    @property
    def index(self):
        """Gets the index of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501


        :return: The index of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this AccessControlledResourceIdentifierPartSchemaAttribute.


        :param index: The index of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :type index: int
        """

        self._index = index

    @property
    def name(self):
        """Gets the name of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501


        :return: The name of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessControlledResourceIdentifierPartSchemaAttribute.


        :param name: The name of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501


        :return: The display_name of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AccessControlledResourceIdentifierPartSchemaAttribute.


        :param display_name: The display_name of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501


        :return: The description of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccessControlledResourceIdentifierPartSchemaAttribute.


        :param description: The description of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def required(self):
        """Gets the required of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501


        :return: The required of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this AccessControlledResourceIdentifierPartSchemaAttribute.


        :param required: The required of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :type required: bool
        """

        self._required = required

    @property
    def values_path(self):
        """Gets the values_path of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501


        :return: The values_path of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._values_path

    @values_path.setter
    def values_path(self, values_path):
        """Sets the values_path of this AccessControlledResourceIdentifierPartSchemaAttribute.


        :param values_path: The values_path of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :type values_path: str
        """

        self._values_path = values_path

    @property
    def type_id(self):
        """Gets the type_id of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501


        :return: The type_id of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :rtype: object
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this AccessControlledResourceIdentifierPartSchemaAttribute.


        :param type_id: The type_id of this AccessControlledResourceIdentifierPartSchemaAttribute.  # noqa: E501
        :type type_id: object
        """

        self._type_id = type_id

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
        if not isinstance(other, AccessControlledResourceIdentifierPartSchemaAttribute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessControlledResourceIdentifierPartSchemaAttribute):
            return True

        return self.to_dict() != other.to_dict()
