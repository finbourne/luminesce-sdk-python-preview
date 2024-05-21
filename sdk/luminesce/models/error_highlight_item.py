# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.15.231
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


class ErrorHighlightItem(object):
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
        'start': 'CursorPosition',
        'stop': 'CursorPosition',
        'no_viable_alternative_start': 'CursorPosition',
        'length': 'int',
        'message': 'str'
    }

    attribute_map = {
        'start': 'start',
        'stop': 'stop',
        'no_viable_alternative_start': 'noViableAlternativeStart',
        'length': 'length',
        'message': 'message'
    }

    required_map = {
        'start': 'required',
        'stop': 'required',
        'no_viable_alternative_start': 'optional',
        'length': 'required',
        'message': 'required'
    }

    def __init__(self, start=None, stop=None, no_viable_alternative_start=None, length=None, message=None, local_vars_configuration=None):  # noqa: E501
        """ErrorHighlightItem - a model defined in OpenAPI"
        
        :param start:  (required)
        :type start: luminesce.CursorPosition
        :param stop:  (required)
        :type stop: luminesce.CursorPosition
        :param no_viable_alternative_start: 
        :type no_viable_alternative_start: luminesce.CursorPosition
        :param length:  The length of the error token counting line breaks if any (required)
        :type length: int
        :param message:  The error message (required)
        :type message: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start = None
        self._stop = None
        self._no_viable_alternative_start = None
        self._length = None
        self._message = None
        self.discriminator = None

        self.start = start
        self.stop = stop
        if no_viable_alternative_start is not None:
            self.no_viable_alternative_start = no_viable_alternative_start
        self.length = length
        self.message = message

    @property
    def start(self):
        """Gets the start of this ErrorHighlightItem.  # noqa: E501


        :return: The start of this ErrorHighlightItem.  # noqa: E501
        :rtype: luminesce.CursorPosition
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ErrorHighlightItem.


        :param start: The start of this ErrorHighlightItem.  # noqa: E501
        :type start: luminesce.CursorPosition
        """
        if self.local_vars_configuration.client_side_validation and start is None:  # noqa: E501
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def stop(self):
        """Gets the stop of this ErrorHighlightItem.  # noqa: E501


        :return: The stop of this ErrorHighlightItem.  # noqa: E501
        :rtype: luminesce.CursorPosition
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this ErrorHighlightItem.


        :param stop: The stop of this ErrorHighlightItem.  # noqa: E501
        :type stop: luminesce.CursorPosition
        """
        if self.local_vars_configuration.client_side_validation and stop is None:  # noqa: E501
            raise ValueError("Invalid value for `stop`, must not be `None`")  # noqa: E501

        self._stop = stop

    @property
    def no_viable_alternative_start(self):
        """Gets the no_viable_alternative_start of this ErrorHighlightItem.  # noqa: E501


        :return: The no_viable_alternative_start of this ErrorHighlightItem.  # noqa: E501
        :rtype: luminesce.CursorPosition
        """
        return self._no_viable_alternative_start

    @no_viable_alternative_start.setter
    def no_viable_alternative_start(self, no_viable_alternative_start):
        """Sets the no_viable_alternative_start of this ErrorHighlightItem.


        :param no_viable_alternative_start: The no_viable_alternative_start of this ErrorHighlightItem.  # noqa: E501
        :type no_viable_alternative_start: luminesce.CursorPosition
        """

        self._no_viable_alternative_start = no_viable_alternative_start

    @property
    def length(self):
        """Gets the length of this ErrorHighlightItem.  # noqa: E501

        The length of the error token counting line breaks if any  # noqa: E501

        :return: The length of this ErrorHighlightItem.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this ErrorHighlightItem.

        The length of the error token counting line breaks if any  # noqa: E501

        :param length: The length of this ErrorHighlightItem.  # noqa: E501
        :type length: int
        """
        if self.local_vars_configuration.client_side_validation and length is None:  # noqa: E501
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def message(self):
        """Gets the message of this ErrorHighlightItem.  # noqa: E501

        The error message  # noqa: E501

        :return: The message of this ErrorHighlightItem.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorHighlightItem.

        The error message  # noqa: E501

        :param message: The message of this ErrorHighlightItem.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                message is not None and len(message) < 1):
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `1`")  # noqa: E501

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
        if not isinstance(other, ErrorHighlightItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorHighlightItem):
            return True

        return self.to_dict() != other.to_dict()
