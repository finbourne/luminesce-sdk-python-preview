# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.14.810
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


class OptionsCsv(object):
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
        'column_names': 'str',
        'column_names_wanted': 'str',
        'column_types': 'str',
        'infer_type_row_count': 'int',
        'no_header': 'bool',
        'delimiter': 'str',
        'escape': 'str',
        'quote': 'str',
        'values_to_make_null': 'str',
        'skip_pre_header': 'int',
        'skip_post_header': 'int',
        'skip_invalid_rows': 'bool'
    }

    attribute_map = {
        'column_names': 'columnNames',
        'column_names_wanted': 'columnNamesWanted',
        'column_types': 'columnTypes',
        'infer_type_row_count': 'inferTypeRowCount',
        'no_header': 'noHeader',
        'delimiter': 'delimiter',
        'escape': 'escape',
        'quote': 'quote',
        'values_to_make_null': 'valuesToMakeNull',
        'skip_pre_header': 'skipPreHeader',
        'skip_post_header': 'skipPostHeader',
        'skip_invalid_rows': 'skipInvalidRows'
    }

    required_map = {
        'column_names': 'optional',
        'column_names_wanted': 'optional',
        'column_types': 'optional',
        'infer_type_row_count': 'optional',
        'no_header': 'optional',
        'delimiter': 'optional',
        'escape': 'optional',
        'quote': 'optional',
        'values_to_make_null': 'optional',
        'skip_pre_header': 'optional',
        'skip_post_header': 'optional',
        'skip_invalid_rows': 'optional'
    }

    def __init__(self, column_names=None, column_names_wanted=None, column_types=None, infer_type_row_count=None, no_header=None, delimiter=None, escape=None, quote=None, values_to_make_null=None, skip_pre_header=None, skip_post_header=None, skip_invalid_rows=None, local_vars_configuration=None):  # noqa: E501
        """OptionsCsv - a model defined in OpenAPI"
        
        :param column_names:  Column Names either overrides the header row or steps in when there is no header row (comma delimited list)
        :type column_names: str
        :param column_names_wanted:  Column (by Name) that should be returned (comma delimited list)
        :type column_names_wanted: str
        :param column_types:  Column types (comma delimited list of: '{types}', some columns may be left blank while others are specified)
        :type column_types: str
        :param infer_type_row_count:  If non-zero and 'types' is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified
        :type infer_type_row_count: int
        :param no_header:  Set this if there is no header row
        :type no_header: bool
        :param delimiter:  The delimiter between values (\\t for tab)
        :type delimiter: str
        :param escape:  Character used to escape the 'Quote' character when within a value
        :type escape: str
        :param quote:  Character used around any field containing the 'delimiter' or a line break.
        :type quote: str
        :param values_to_make_null:  Regex of values to map to 'null' in the returned data.
        :type values_to_make_null: str
        :param skip_pre_header:  Number of rows to ignore before the header row
        :type skip_pre_header: int
        :param skip_post_header:  Number of rows to ignore after the header row
        :type skip_post_header: int
        :param skip_invalid_rows:  Skip invalid data rows (totally invalid ones),   This also allows for potentially wrong data if it can be handled somewhat e.g. embedded quotes misused (and still returns such rows).  In either case a warning will show in the progress feedback.
        :type skip_invalid_rows: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._column_names = None
        self._column_names_wanted = None
        self._column_types = None
        self._infer_type_row_count = None
        self._no_header = None
        self._delimiter = None
        self._escape = None
        self._quote = None
        self._values_to_make_null = None
        self._skip_pre_header = None
        self._skip_post_header = None
        self._skip_invalid_rows = None
        self.discriminator = None

        self.column_names = column_names
        self.column_names_wanted = column_names_wanted
        self.column_types = column_types
        if infer_type_row_count is not None:
            self.infer_type_row_count = infer_type_row_count
        if no_header is not None:
            self.no_header = no_header
        self.delimiter = delimiter
        self.escape = escape
        self.quote = quote
        self.values_to_make_null = values_to_make_null
        if skip_pre_header is not None:
            self.skip_pre_header = skip_pre_header
        if skip_post_header is not None:
            self.skip_post_header = skip_post_header
        if skip_invalid_rows is not None:
            self.skip_invalid_rows = skip_invalid_rows

    @property
    def column_names(self):
        """Gets the column_names of this OptionsCsv.  # noqa: E501

        Column Names either overrides the header row or steps in when there is no header row (comma delimited list)  # noqa: E501

        :return: The column_names of this OptionsCsv.  # noqa: E501
        :rtype: str
        """
        return self._column_names

    @column_names.setter
    def column_names(self, column_names):
        """Sets the column_names of this OptionsCsv.

        Column Names either overrides the header row or steps in when there is no header row (comma delimited list)  # noqa: E501

        :param column_names: The column_names of this OptionsCsv.  # noqa: E501
        :type column_names: str
        """

        self._column_names = column_names

    @property
    def column_names_wanted(self):
        """Gets the column_names_wanted of this OptionsCsv.  # noqa: E501

        Column (by Name) that should be returned (comma delimited list)  # noqa: E501

        :return: The column_names_wanted of this OptionsCsv.  # noqa: E501
        :rtype: str
        """
        return self._column_names_wanted

    @column_names_wanted.setter
    def column_names_wanted(self, column_names_wanted):
        """Sets the column_names_wanted of this OptionsCsv.

        Column (by Name) that should be returned (comma delimited list)  # noqa: E501

        :param column_names_wanted: The column_names_wanted of this OptionsCsv.  # noqa: E501
        :type column_names_wanted: str
        """

        self._column_names_wanted = column_names_wanted

    @property
    def column_types(self):
        """Gets the column_types of this OptionsCsv.  # noqa: E501

        Column types (comma delimited list of: '{types}', some columns may be left blank while others are specified)  # noqa: E501

        :return: The column_types of this OptionsCsv.  # noqa: E501
        :rtype: str
        """
        return self._column_types

    @column_types.setter
    def column_types(self, column_types):
        """Sets the column_types of this OptionsCsv.

        Column types (comma delimited list of: '{types}', some columns may be left blank while others are specified)  # noqa: E501

        :param column_types: The column_types of this OptionsCsv.  # noqa: E501
        :type column_types: str
        """

        self._column_types = column_types

    @property
    def infer_type_row_count(self):
        """Gets the infer_type_row_count of this OptionsCsv.  # noqa: E501

        If non-zero and 'types' is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified  # noqa: E501

        :return: The infer_type_row_count of this OptionsCsv.  # noqa: E501
        :rtype: int
        """
        return self._infer_type_row_count

    @infer_type_row_count.setter
    def infer_type_row_count(self, infer_type_row_count):
        """Sets the infer_type_row_count of this OptionsCsv.

        If non-zero and 'types' is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified  # noqa: E501

        :param infer_type_row_count: The infer_type_row_count of this OptionsCsv.  # noqa: E501
        :type infer_type_row_count: int
        """

        self._infer_type_row_count = infer_type_row_count

    @property
    def no_header(self):
        """Gets the no_header of this OptionsCsv.  # noqa: E501

        Set this if there is no header row  # noqa: E501

        :return: The no_header of this OptionsCsv.  # noqa: E501
        :rtype: bool
        """
        return self._no_header

    @no_header.setter
    def no_header(self, no_header):
        """Sets the no_header of this OptionsCsv.

        Set this if there is no header row  # noqa: E501

        :param no_header: The no_header of this OptionsCsv.  # noqa: E501
        :type no_header: bool
        """

        self._no_header = no_header

    @property
    def delimiter(self):
        """Gets the delimiter of this OptionsCsv.  # noqa: E501

        The delimiter between values (\\t for tab)  # noqa: E501

        :return: The delimiter of this OptionsCsv.  # noqa: E501
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this OptionsCsv.

        The delimiter between values (\\t for tab)  # noqa: E501

        :param delimiter: The delimiter of this OptionsCsv.  # noqa: E501
        :type delimiter: str
        """

        self._delimiter = delimiter

    @property
    def escape(self):
        """Gets the escape of this OptionsCsv.  # noqa: E501

        Character used to escape the 'Quote' character when within a value  # noqa: E501

        :return: The escape of this OptionsCsv.  # noqa: E501
        :rtype: str
        """
        return self._escape

    @escape.setter
    def escape(self, escape):
        """Sets the escape of this OptionsCsv.

        Character used to escape the 'Quote' character when within a value  # noqa: E501

        :param escape: The escape of this OptionsCsv.  # noqa: E501
        :type escape: str
        """

        self._escape = escape

    @property
    def quote(self):
        """Gets the quote of this OptionsCsv.  # noqa: E501

        Character used around any field containing the 'delimiter' or a line break.  # noqa: E501

        :return: The quote of this OptionsCsv.  # noqa: E501
        :rtype: str
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this OptionsCsv.

        Character used around any field containing the 'delimiter' or a line break.  # noqa: E501

        :param quote: The quote of this OptionsCsv.  # noqa: E501
        :type quote: str
        """

        self._quote = quote

    @property
    def values_to_make_null(self):
        """Gets the values_to_make_null of this OptionsCsv.  # noqa: E501

        Regex of values to map to 'null' in the returned data.  # noqa: E501

        :return: The values_to_make_null of this OptionsCsv.  # noqa: E501
        :rtype: str
        """
        return self._values_to_make_null

    @values_to_make_null.setter
    def values_to_make_null(self, values_to_make_null):
        """Sets the values_to_make_null of this OptionsCsv.

        Regex of values to map to 'null' in the returned data.  # noqa: E501

        :param values_to_make_null: The values_to_make_null of this OptionsCsv.  # noqa: E501
        :type values_to_make_null: str
        """

        self._values_to_make_null = values_to_make_null

    @property
    def skip_pre_header(self):
        """Gets the skip_pre_header of this OptionsCsv.  # noqa: E501

        Number of rows to ignore before the header row  # noqa: E501

        :return: The skip_pre_header of this OptionsCsv.  # noqa: E501
        :rtype: int
        """
        return self._skip_pre_header

    @skip_pre_header.setter
    def skip_pre_header(self, skip_pre_header):
        """Sets the skip_pre_header of this OptionsCsv.

        Number of rows to ignore before the header row  # noqa: E501

        :param skip_pre_header: The skip_pre_header of this OptionsCsv.  # noqa: E501
        :type skip_pre_header: int
        """

        self._skip_pre_header = skip_pre_header

    @property
    def skip_post_header(self):
        """Gets the skip_post_header of this OptionsCsv.  # noqa: E501

        Number of rows to ignore after the header row  # noqa: E501

        :return: The skip_post_header of this OptionsCsv.  # noqa: E501
        :rtype: int
        """
        return self._skip_post_header

    @skip_post_header.setter
    def skip_post_header(self, skip_post_header):
        """Sets the skip_post_header of this OptionsCsv.

        Number of rows to ignore after the header row  # noqa: E501

        :param skip_post_header: The skip_post_header of this OptionsCsv.  # noqa: E501
        :type skip_post_header: int
        """

        self._skip_post_header = skip_post_header

    @property
    def skip_invalid_rows(self):
        """Gets the skip_invalid_rows of this OptionsCsv.  # noqa: E501

        Skip invalid data rows (totally invalid ones),   This also allows for potentially wrong data if it can be handled somewhat e.g. embedded quotes misused (and still returns such rows).  In either case a warning will show in the progress feedback.  # noqa: E501

        :return: The skip_invalid_rows of this OptionsCsv.  # noqa: E501
        :rtype: bool
        """
        return self._skip_invalid_rows

    @skip_invalid_rows.setter
    def skip_invalid_rows(self, skip_invalid_rows):
        """Sets the skip_invalid_rows of this OptionsCsv.

        Skip invalid data rows (totally invalid ones),   This also allows for potentially wrong data if it can be handled somewhat e.g. embedded quotes misused (and still returns such rows).  In either case a warning will show in the progress feedback.  # noqa: E501

        :param skip_invalid_rows: The skip_invalid_rows of this OptionsCsv.  # noqa: E501
        :type skip_invalid_rows: bool
        """

        self._skip_invalid_rows = skip_invalid_rows

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
        if not isinstance(other, OptionsCsv):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OptionsCsv):
            return True

        return self.to_dict() != other.to_dict()
