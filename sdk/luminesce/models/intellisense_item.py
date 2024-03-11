# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.14.688
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


class IntellisenseItem(object):
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
        'caption': 'str',
        'value': 'str',
        'meta': 'str',
        'score': 'int',
        'doc_html': 'str',
        'type': 'IntellisenseType'
    }

    attribute_map = {
        'caption': 'caption',
        'value': 'value',
        'meta': 'meta',
        'score': 'score',
        'doc_html': 'docHtml',
        'type': 'type'
    }

    required_map = {
        'caption': 'required',
        'value': 'required',
        'meta': 'optional',
        'score': 'optional',
        'doc_html': 'optional',
        'type': 'optional'
    }

    def __init__(self, caption=None, value=None, meta=None, score=None, doc_html=None, type=None, local_vars_configuration=None):  # noqa: E501
        """IntellisenseItem - a model defined in OpenAPI"
        
        :param caption:  The value to show the user in the popup (required)
        :type caption: str
        :param value:  The value to substitute in (required)
        :type value: str
        :param meta:  The light-grey text shown to the right of the Caption in the popup
        :type meta: str
        :param score:  How important is this.  Bigger is more important.
        :type score: int
        :param doc_html:  Popup further info (as in a whole documentation article!)
        :type doc_html: str
        :param type: 
        :type type: luminesce.IntellisenseType

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._caption = None
        self._value = None
        self._meta = None
        self._score = None
        self._doc_html = None
        self._type = None
        self.discriminator = None

        self.caption = caption
        self.value = value
        self.meta = meta
        if score is not None:
            self.score = score
        self.doc_html = doc_html
        if type is not None:
            self.type = type

    @property
    def caption(self):
        """Gets the caption of this IntellisenseItem.  # noqa: E501

        The value to show the user in the popup  # noqa: E501

        :return: The caption of this IntellisenseItem.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this IntellisenseItem.

        The value to show the user in the popup  # noqa: E501

        :param caption: The caption of this IntellisenseItem.  # noqa: E501
        :type caption: str
        """
        if self.local_vars_configuration.client_side_validation and caption is None:  # noqa: E501
            raise ValueError("Invalid value for `caption`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                caption is not None and len(caption) < 1):
            raise ValueError("Invalid value for `caption`, length must be greater than or equal to `1`")  # noqa: E501

        self._caption = caption

    @property
    def value(self):
        """Gets the value of this IntellisenseItem.  # noqa: E501

        The value to substitute in  # noqa: E501

        :return: The value of this IntellisenseItem.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IntellisenseItem.

        The value to substitute in  # noqa: E501

        :param value: The value of this IntellisenseItem.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) < 1):
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self._value = value

    @property
    def meta(self):
        """Gets the meta of this IntellisenseItem.  # noqa: E501

        The light-grey text shown to the right of the Caption in the popup  # noqa: E501

        :return: The meta of this IntellisenseItem.  # noqa: E501
        :rtype: str
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this IntellisenseItem.

        The light-grey text shown to the right of the Caption in the popup  # noqa: E501

        :param meta: The meta of this IntellisenseItem.  # noqa: E501
        :type meta: str
        """

        self._meta = meta

    @property
    def score(self):
        """Gets the score of this IntellisenseItem.  # noqa: E501

        How important is this.  Bigger is more important.  # noqa: E501

        :return: The score of this IntellisenseItem.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this IntellisenseItem.

        How important is this.  Bigger is more important.  # noqa: E501

        :param score: The score of this IntellisenseItem.  # noqa: E501
        :type score: int
        """

        self._score = score

    @property
    def doc_html(self):
        """Gets the doc_html of this IntellisenseItem.  # noqa: E501

        Popup further info (as in a whole documentation article!)  # noqa: E501

        :return: The doc_html of this IntellisenseItem.  # noqa: E501
        :rtype: str
        """
        return self._doc_html

    @doc_html.setter
    def doc_html(self, doc_html):
        """Sets the doc_html of this IntellisenseItem.

        Popup further info (as in a whole documentation article!)  # noqa: E501

        :param doc_html: The doc_html of this IntellisenseItem.  # noqa: E501
        :type doc_html: str
        """

        self._doc_html = doc_html

    @property
    def type(self):
        """Gets the type of this IntellisenseItem.  # noqa: E501


        :return: The type of this IntellisenseItem.  # noqa: E501
        :rtype: luminesce.IntellisenseType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IntellisenseItem.


        :param type: The type of this IntellisenseItem.  # noqa: E501
        :type type: luminesce.IntellisenseType
        """

        self._type = type

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
        if not isinstance(other, IntellisenseItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntellisenseItem):
            return True

        return self.to_dict() != other.to_dict()