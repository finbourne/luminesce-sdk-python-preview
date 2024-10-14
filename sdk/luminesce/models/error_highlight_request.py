# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.699
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


class ErrorHighlightRequest(object):
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
        'lines': 'list[str]',
        'ensure_some_text_is_selected': 'bool'
    }

    attribute_map = {
        'lines': 'lines',
        'ensure_some_text_is_selected': 'ensureSomeTextIsSelected'
    }

    required_map = {
        'lines': 'required',
        'ensure_some_text_is_selected': 'optional'
    }

    def __init__(self, lines=None, ensure_some_text_is_selected=None, local_vars_configuration=None):  # noqa: E501
        """ErrorHighlightRequest - a model defined in OpenAPI"
        
        :param lines:  The lines of text the user currently has in the editor (required)
        :type lines: list[str]
        :param ensure_some_text_is_selected:  If an editor requires some selection of non-whitespace this can be set to true to force  at least one visible character to be selected.
        :type ensure_some_text_is_selected: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._lines = None
        self._ensure_some_text_is_selected = None
        self.discriminator = None

        self.lines = lines
        if ensure_some_text_is_selected is not None:
            self.ensure_some_text_is_selected = ensure_some_text_is_selected

    @property
    def lines(self):
        """Gets the lines of this ErrorHighlightRequest.  # noqa: E501

        The lines of text the user currently has in the editor  # noqa: E501

        :return: The lines of this ErrorHighlightRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this ErrorHighlightRequest.

        The lines of text the user currently has in the editor  # noqa: E501

        :param lines: The lines of this ErrorHighlightRequest.  # noqa: E501
        :type lines: list[str]
        """
        if self.local_vars_configuration.client_side_validation and lines is None:  # noqa: E501
            raise ValueError("Invalid value for `lines`, must not be `None`")  # noqa: E501

        self._lines = lines

    @property
    def ensure_some_text_is_selected(self):
        """Gets the ensure_some_text_is_selected of this ErrorHighlightRequest.  # noqa: E501

        If an editor requires some selection of non-whitespace this can be set to true to force  at least one visible character to be selected.  # noqa: E501

        :return: The ensure_some_text_is_selected of this ErrorHighlightRequest.  # noqa: E501
        :rtype: bool
        """
        return self._ensure_some_text_is_selected

    @ensure_some_text_is_selected.setter
    def ensure_some_text_is_selected(self, ensure_some_text_is_selected):
        """Sets the ensure_some_text_is_selected of this ErrorHighlightRequest.

        If an editor requires some selection of non-whitespace this can be set to true to force  at least one visible character to be selected.  # noqa: E501

        :param ensure_some_text_is_selected: The ensure_some_text_is_selected of this ErrorHighlightRequest.  # noqa: E501
        :type ensure_some_text_is_selected: bool
        """

        self._ensure_some_text_is_selected = ensure_some_text_is_selected

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
        if not isinstance(other, ErrorHighlightRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorHighlightRequest):
            return True

        return self.to_dict() != other.to_dict()
