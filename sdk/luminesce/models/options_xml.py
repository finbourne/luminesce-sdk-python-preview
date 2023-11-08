# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.13.854
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


class OptionsXml(object):
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
        'column_types': 'str',
        'infer_type_row_count': 'int',
        'values_to_make_null': 'str',
        'column_names': 'str',
        'node_path': 'str',
        'namespaces': 'str'
    }

    attribute_map = {
        'column_types': 'columnTypes',
        'infer_type_row_count': 'inferTypeRowCount',
        'values_to_make_null': 'valuesToMakeNull',
        'column_names': 'columnNames',
        'node_path': 'nodePath',
        'namespaces': 'namespaces'
    }

    required_map = {
        'column_types': 'optional',
        'infer_type_row_count': 'optional',
        'values_to_make_null': 'optional',
        'column_names': 'optional',
        'node_path': 'optional',
        'namespaces': 'optional'
    }

    def __init__(self, column_types=None, infer_type_row_count=None, values_to_make_null=None, column_names=None, node_path=None, namespaces=None, local_vars_configuration=None):  # noqa: E501
        """OptionsXml - a model defined in OpenAPI"
        
        :param column_types:  Column types (comma delimited list of: '{types}', some columns may be left blank while others are specified)
        :type column_types: str
        :param infer_type_row_count:  If non-zero and 'types' is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified
        :type infer_type_row_count: int
        :param values_to_make_null:  Regex of values to map to 'null' in the returned data.
        :type values_to_make_null: str
        :param column_names:  Column Names either overrides the header row or steps in when there is no header row (comma delimited list)
        :type column_names: str
        :param node_path:  XPath query that selects the nodes to map to rows
        :type node_path: str
        :param namespaces:  Selected prefix(es) and namespace(s):prefix1=namespace1-uri1,prefix2=namespace2-uri2,...prefixN=namespaceN-uriN
        :type namespaces: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._column_types = None
        self._infer_type_row_count = None
        self._values_to_make_null = None
        self._column_names = None
        self._node_path = None
        self._namespaces = None
        self.discriminator = None

        self.column_types = column_types
        if infer_type_row_count is not None:
            self.infer_type_row_count = infer_type_row_count
        self.values_to_make_null = values_to_make_null
        self.column_names = column_names
        self.node_path = node_path
        self.namespaces = namespaces

    @property
    def column_types(self):
        """Gets the column_types of this OptionsXml.  # noqa: E501

        Column types (comma delimited list of: '{types}', some columns may be left blank while others are specified)  # noqa: E501

        :return: The column_types of this OptionsXml.  # noqa: E501
        :rtype: str
        """
        return self._column_types

    @column_types.setter
    def column_types(self, column_types):
        """Sets the column_types of this OptionsXml.

        Column types (comma delimited list of: '{types}', some columns may be left blank while others are specified)  # noqa: E501

        :param column_types: The column_types of this OptionsXml.  # noqa: E501
        :type column_types: str
        """

        self._column_types = column_types

    @property
    def infer_type_row_count(self):
        """Gets the infer_type_row_count of this OptionsXml.  # noqa: E501

        If non-zero and 'types' is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified  # noqa: E501

        :return: The infer_type_row_count of this OptionsXml.  # noqa: E501
        :rtype: int
        """
        return self._infer_type_row_count

    @infer_type_row_count.setter
    def infer_type_row_count(self, infer_type_row_count):
        """Sets the infer_type_row_count of this OptionsXml.

        If non-zero and 'types' is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified  # noqa: E501

        :param infer_type_row_count: The infer_type_row_count of this OptionsXml.  # noqa: E501
        :type infer_type_row_count: int
        """

        self._infer_type_row_count = infer_type_row_count

    @property
    def values_to_make_null(self):
        """Gets the values_to_make_null of this OptionsXml.  # noqa: E501

        Regex of values to map to 'null' in the returned data.  # noqa: E501

        :return: The values_to_make_null of this OptionsXml.  # noqa: E501
        :rtype: str
        """
        return self._values_to_make_null

    @values_to_make_null.setter
    def values_to_make_null(self, values_to_make_null):
        """Sets the values_to_make_null of this OptionsXml.

        Regex of values to map to 'null' in the returned data.  # noqa: E501

        :param values_to_make_null: The values_to_make_null of this OptionsXml.  # noqa: E501
        :type values_to_make_null: str
        """

        self._values_to_make_null = values_to_make_null

    @property
    def column_names(self):
        """Gets the column_names of this OptionsXml.  # noqa: E501

        Column Names either overrides the header row or steps in when there is no header row (comma delimited list)  # noqa: E501

        :return: The column_names of this OptionsXml.  # noqa: E501
        :rtype: str
        """
        return self._column_names

    @column_names.setter
    def column_names(self, column_names):
        """Sets the column_names of this OptionsXml.

        Column Names either overrides the header row or steps in when there is no header row (comma delimited list)  # noqa: E501

        :param column_names: The column_names of this OptionsXml.  # noqa: E501
        :type column_names: str
        """

        self._column_names = column_names

    @property
    def node_path(self):
        """Gets the node_path of this OptionsXml.  # noqa: E501

        XPath query that selects the nodes to map to rows  # noqa: E501

        :return: The node_path of this OptionsXml.  # noqa: E501
        :rtype: str
        """
        return self._node_path

    @node_path.setter
    def node_path(self, node_path):
        """Sets the node_path of this OptionsXml.

        XPath query that selects the nodes to map to rows  # noqa: E501

        :param node_path: The node_path of this OptionsXml.  # noqa: E501
        :type node_path: str
        """

        self._node_path = node_path

    @property
    def namespaces(self):
        """Gets the namespaces of this OptionsXml.  # noqa: E501

        Selected prefix(es) and namespace(s):prefix1=namespace1-uri1,prefix2=namespace2-uri2,...prefixN=namespaceN-uriN  # noqa: E501

        :return: The namespaces of this OptionsXml.  # noqa: E501
        :rtype: str
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this OptionsXml.

        Selected prefix(es) and namespace(s):prefix1=namespace1-uri1,prefix2=namespace2-uri2,...prefixN=namespaceN-uriN  # noqa: E501

        :param namespaces: The namespaces of this OptionsXml.  # noqa: E501
        :type namespaces: str
        """

        self._namespaces = namespaces

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
        if not isinstance(other, OptionsXml):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OptionsXml):
            return True

        return self.to_dict() != other.to_dict()