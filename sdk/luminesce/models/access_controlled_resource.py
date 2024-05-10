# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.15.162
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


class AccessControlledResource(object):
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
        'application': 'str',
        'name': 'str',
        'description': 'str',
        'actions': 'list[AccessControlledAction]',
        'identifier_parts': 'list[AccessControlledResourceIdentifierPartSchemaAttribute]'
    }

    attribute_map = {
        'application': 'application',
        'name': 'name',
        'description': 'description',
        'actions': 'actions',
        'identifier_parts': 'identifierParts'
    }

    required_map = {
        'application': 'optional',
        'name': 'optional',
        'description': 'optional',
        'actions': 'optional',
        'identifier_parts': 'optional'
    }

    def __init__(self, application=None, name=None, description=None, actions=None, identifier_parts=None, local_vars_configuration=None):  # noqa: E501
        """AccessControlledResource - a model defined in OpenAPI"
        
        :param application: 
        :type application: str
        :param name: 
        :type name: str
        :param description: 
        :type description: str
        :param actions: 
        :type actions: list[luminesce.AccessControlledAction]
        :param identifier_parts: 
        :type identifier_parts: list[luminesce.AccessControlledResourceIdentifierPartSchemaAttribute]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._application = None
        self._name = None
        self._description = None
        self._actions = None
        self._identifier_parts = None
        self.discriminator = None

        self.application = application
        self.name = name
        self.description = description
        self.actions = actions
        self.identifier_parts = identifier_parts

    @property
    def application(self):
        """Gets the application of this AccessControlledResource.  # noqa: E501


        :return: The application of this AccessControlledResource.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this AccessControlledResource.


        :param application: The application of this AccessControlledResource.  # noqa: E501
        :type application: str
        """

        self._application = application

    @property
    def name(self):
        """Gets the name of this AccessControlledResource.  # noqa: E501


        :return: The name of this AccessControlledResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessControlledResource.


        :param name: The name of this AccessControlledResource.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this AccessControlledResource.  # noqa: E501


        :return: The description of this AccessControlledResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccessControlledResource.


        :param description: The description of this AccessControlledResource.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def actions(self):
        """Gets the actions of this AccessControlledResource.  # noqa: E501


        :return: The actions of this AccessControlledResource.  # noqa: E501
        :rtype: list[luminesce.AccessControlledAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this AccessControlledResource.


        :param actions: The actions of this AccessControlledResource.  # noqa: E501
        :type actions: list[luminesce.AccessControlledAction]
        """

        self._actions = actions

    @property
    def identifier_parts(self):
        """Gets the identifier_parts of this AccessControlledResource.  # noqa: E501


        :return: The identifier_parts of this AccessControlledResource.  # noqa: E501
        :rtype: list[luminesce.AccessControlledResourceIdentifierPartSchemaAttribute]
        """
        return self._identifier_parts

    @identifier_parts.setter
    def identifier_parts(self, identifier_parts):
        """Sets the identifier_parts of this AccessControlledResource.


        :param identifier_parts: The identifier_parts of this AccessControlledResource.  # noqa: E501
        :type identifier_parts: list[luminesce.AccessControlledResourceIdentifierPartSchemaAttribute]
        """

        self._identifier_parts = identifier_parts

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
        if not isinstance(other, AccessControlledResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessControlledResource):
            return True

        return self.to_dict() != other.to_dict()
