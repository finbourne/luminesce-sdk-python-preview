# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.765
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


class MappableField(object):
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
        'type': 'DataType',
        'description': 'str',
        'display_name': 'str',
        'sample_values': 'str',
        'allowed_values': 'str',
        'mandatory_for_actions': 'str',
        'mapping': 'ExpressionWithAlias'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'display_name': 'displayName',
        'sample_values': 'sampleValues',
        'allowed_values': 'allowedValues',
        'mandatory_for_actions': 'mandatoryForActions',
        'mapping': 'mapping'
    }

    required_map = {
        'name': 'optional',
        'type': 'optional',
        'description': 'optional',
        'display_name': 'optional',
        'sample_values': 'optional',
        'allowed_values': 'optional',
        'mandatory_for_actions': 'optional',
        'mapping': 'optional'
    }

    def __init__(self, name=None, type=None, description=None, display_name=None, sample_values=None, allowed_values=None, mandatory_for_actions=None, mapping=None, local_vars_configuration=None):  # noqa: E501
        """MappableField - a model defined in OpenAPI"
        
        :param name:  Name of the field in need of mapping (The field name from within the Table Parameter itself)
        :type name: str
        :param type: 
        :type type: luminesce.DataType
        :param description:  Description of the field (just for rendering to the user)
        :type description: str
        :param display_name:  Display Name of the field (just for rendering to the user)
        :type display_name: str
        :param sample_values:  Example values for the field (just for rendering to the user)
        :type sample_values: str
        :param allowed_values:  Any set of exactly allowed values for the field (perhaps just for rendering to the user, if nothing else)
        :type allowed_values: str
        :param mandatory_for_actions:  Which `Actions` is this mandatory for? If any (and potentially when), perhaps just for rendering to the user, if nothing else
        :type mandatory_for_actions: str
        :param mapping: 
        :type mapping: luminesce.ExpressionWithAlias

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._type = None
        self._description = None
        self._display_name = None
        self._sample_values = None
        self._allowed_values = None
        self._mandatory_for_actions = None
        self._mapping = None
        self.discriminator = None

        self.name = name
        if type is not None:
            self.type = type
        self.description = description
        self.display_name = display_name
        self.sample_values = sample_values
        self.allowed_values = allowed_values
        self.mandatory_for_actions = mandatory_for_actions
        if mapping is not None:
            self.mapping = mapping

    @property
    def name(self):
        """Gets the name of this MappableField.  # noqa: E501

        Name of the field in need of mapping (The field name from within the Table Parameter itself)  # noqa: E501

        :return: The name of this MappableField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MappableField.

        Name of the field in need of mapping (The field name from within the Table Parameter itself)  # noqa: E501

        :param name: The name of this MappableField.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this MappableField.  # noqa: E501


        :return: The type of this MappableField.  # noqa: E501
        :rtype: luminesce.DataType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MappableField.


        :param type: The type of this MappableField.  # noqa: E501
        :type type: luminesce.DataType
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this MappableField.  # noqa: E501

        Description of the field (just for rendering to the user)  # noqa: E501

        :return: The description of this MappableField.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MappableField.

        Description of the field (just for rendering to the user)  # noqa: E501

        :param description: The description of this MappableField.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this MappableField.  # noqa: E501

        Display Name of the field (just for rendering to the user)  # noqa: E501

        :return: The display_name of this MappableField.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this MappableField.

        Display Name of the field (just for rendering to the user)  # noqa: E501

        :param display_name: The display_name of this MappableField.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def sample_values(self):
        """Gets the sample_values of this MappableField.  # noqa: E501

        Example values for the field (just for rendering to the user)  # noqa: E501

        :return: The sample_values of this MappableField.  # noqa: E501
        :rtype: str
        """
        return self._sample_values

    @sample_values.setter
    def sample_values(self, sample_values):
        """Sets the sample_values of this MappableField.

        Example values for the field (just for rendering to the user)  # noqa: E501

        :param sample_values: The sample_values of this MappableField.  # noqa: E501
        :type sample_values: str
        """

        self._sample_values = sample_values

    @property
    def allowed_values(self):
        """Gets the allowed_values of this MappableField.  # noqa: E501

        Any set of exactly allowed values for the field (perhaps just for rendering to the user, if nothing else)  # noqa: E501

        :return: The allowed_values of this MappableField.  # noqa: E501
        :rtype: str
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """Sets the allowed_values of this MappableField.

        Any set of exactly allowed values for the field (perhaps just for rendering to the user, if nothing else)  # noqa: E501

        :param allowed_values: The allowed_values of this MappableField.  # noqa: E501
        :type allowed_values: str
        """

        self._allowed_values = allowed_values

    @property
    def mandatory_for_actions(self):
        """Gets the mandatory_for_actions of this MappableField.  # noqa: E501

        Which `Actions` is this mandatory for? If any (and potentially when), perhaps just for rendering to the user, if nothing else  # noqa: E501

        :return: The mandatory_for_actions of this MappableField.  # noqa: E501
        :rtype: str
        """
        return self._mandatory_for_actions

    @mandatory_for_actions.setter
    def mandatory_for_actions(self, mandatory_for_actions):
        """Sets the mandatory_for_actions of this MappableField.

        Which `Actions` is this mandatory for? If any (and potentially when), perhaps just for rendering to the user, if nothing else  # noqa: E501

        :param mandatory_for_actions: The mandatory_for_actions of this MappableField.  # noqa: E501
        :type mandatory_for_actions: str
        """

        self._mandatory_for_actions = mandatory_for_actions

    @property
    def mapping(self):
        """Gets the mapping of this MappableField.  # noqa: E501


        :return: The mapping of this MappableField.  # noqa: E501
        :rtype: luminesce.ExpressionWithAlias
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        """Sets the mapping of this MappableField.


        :param mapping: The mapping of this MappableField.  # noqa: E501
        :type mapping: luminesce.ExpressionWithAlias
        """

        self._mapping = mapping

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
        if not isinstance(other, MappableField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MappableField):
            return True

        return self.to_dict() != other.to_dict()
