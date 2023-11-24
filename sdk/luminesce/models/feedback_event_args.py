# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.14.34
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


class FeedbackEventArgs(object):
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
        'when': 'datetime',
        'session_id': 'str',
        'execution_id': 'str',
        'level': 'FeedbackLevel',
        'sender': 'str',
        'state_id': 'int',
        'message_template': 'str',
        'property_values': 'list[object]',
        'message': 'str'
    }

    attribute_map = {
        'when': 'when',
        'session_id': 'sessionId',
        'execution_id': 'executionId',
        'level': 'level',
        'sender': 'sender',
        'state_id': 'stateId',
        'message_template': 'messageTemplate',
        'property_values': 'propertyValues',
        'message': 'message'
    }

    required_map = {
        'when': 'optional',
        'session_id': 'optional',
        'execution_id': 'optional',
        'level': 'optional',
        'sender': 'optional',
        'state_id': 'optional',
        'message_template': 'optional',
        'property_values': 'optional',
        'message': 'optional'
    }

    def __init__(self, when=None, session_id=None, execution_id=None, level=None, sender=None, state_id=None, message_template=None, property_values=None, message=None, local_vars_configuration=None):  # noqa: E501
        """FeedbackEventArgs - a model defined in OpenAPI"
        
        :param when: 
        :type when: datetime
        :param session_id: 
        :type session_id: str
        :param execution_id: 
        :type execution_id: str
        :param level: 
        :type level: luminesce.FeedbackLevel
        :param sender: 
        :type sender: str
        :param state_id: 
        :type state_id: int
        :param message_template: 
        :type message_template: str
        :param property_values: 
        :type property_values: list[object]
        :param message: 
        :type message: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._when = None
        self._session_id = None
        self._execution_id = None
        self._level = None
        self._sender = None
        self._state_id = None
        self._message_template = None
        self._property_values = None
        self._message = None
        self.discriminator = None

        if when is not None:
            self.when = when
        if session_id is not None:
            self.session_id = session_id
        if execution_id is not None:
            self.execution_id = execution_id
        if level is not None:
            self.level = level
        self.sender = sender
        self.state_id = state_id
        self.message_template = message_template
        self.property_values = property_values
        self.message = message

    @property
    def when(self):
        """Gets the when of this FeedbackEventArgs.  # noqa: E501


        :return: The when of this FeedbackEventArgs.  # noqa: E501
        :rtype: datetime
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this FeedbackEventArgs.


        :param when: The when of this FeedbackEventArgs.  # noqa: E501
        :type when: datetime
        """

        self._when = when

    @property
    def session_id(self):
        """Gets the session_id of this FeedbackEventArgs.  # noqa: E501


        :return: The session_id of this FeedbackEventArgs.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this FeedbackEventArgs.


        :param session_id: The session_id of this FeedbackEventArgs.  # noqa: E501
        :type session_id: str
        """

        self._session_id = session_id

    @property
    def execution_id(self):
        """Gets the execution_id of this FeedbackEventArgs.  # noqa: E501


        :return: The execution_id of this FeedbackEventArgs.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this FeedbackEventArgs.


        :param execution_id: The execution_id of this FeedbackEventArgs.  # noqa: E501
        :type execution_id: str
        """

        self._execution_id = execution_id

    @property
    def level(self):
        """Gets the level of this FeedbackEventArgs.  # noqa: E501


        :return: The level of this FeedbackEventArgs.  # noqa: E501
        :rtype: luminesce.FeedbackLevel
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this FeedbackEventArgs.


        :param level: The level of this FeedbackEventArgs.  # noqa: E501
        :type level: luminesce.FeedbackLevel
        """

        self._level = level

    @property
    def sender(self):
        """Gets the sender of this FeedbackEventArgs.  # noqa: E501


        :return: The sender of this FeedbackEventArgs.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this FeedbackEventArgs.


        :param sender: The sender of this FeedbackEventArgs.  # noqa: E501
        :type sender: str
        """

        self._sender = sender

    @property
    def state_id(self):
        """Gets the state_id of this FeedbackEventArgs.  # noqa: E501


        :return: The state_id of this FeedbackEventArgs.  # noqa: E501
        :rtype: int
        """
        return self._state_id

    @state_id.setter
    def state_id(self, state_id):
        """Sets the state_id of this FeedbackEventArgs.


        :param state_id: The state_id of this FeedbackEventArgs.  # noqa: E501
        :type state_id: int
        """

        self._state_id = state_id

    @property
    def message_template(self):
        """Gets the message_template of this FeedbackEventArgs.  # noqa: E501


        :return: The message_template of this FeedbackEventArgs.  # noqa: E501
        :rtype: str
        """
        return self._message_template

    @message_template.setter
    def message_template(self, message_template):
        """Sets the message_template of this FeedbackEventArgs.


        :param message_template: The message_template of this FeedbackEventArgs.  # noqa: E501
        :type message_template: str
        """

        self._message_template = message_template

    @property
    def property_values(self):
        """Gets the property_values of this FeedbackEventArgs.  # noqa: E501


        :return: The property_values of this FeedbackEventArgs.  # noqa: E501
        :rtype: list[object]
        """
        return self._property_values

    @property_values.setter
    def property_values(self, property_values):
        """Sets the property_values of this FeedbackEventArgs.


        :param property_values: The property_values of this FeedbackEventArgs.  # noqa: E501
        :type property_values: list[object]
        """

        self._property_values = property_values

    @property
    def message(self):
        """Gets the message of this FeedbackEventArgs.  # noqa: E501


        :return: The message of this FeedbackEventArgs.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this FeedbackEventArgs.


        :param message: The message of this FeedbackEventArgs.  # noqa: E501
        :type message: str
        """

        self._message = message

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
        if not isinstance(other, FeedbackEventArgs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeedbackEventArgs):
            return True

        return self.to_dict() != other.to_dict()
