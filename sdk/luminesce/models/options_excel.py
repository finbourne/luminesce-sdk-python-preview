# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.14.681
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


class OptionsExcel(object):
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
        'column_types': 'str',
        'infer_type_row_count': 'int',
        'no_header': 'bool',
        'calculate': 'bool',
        'password': 'str',
        'worksheet': 'str',
        'range_or_table': 'str',
        'ignore_invalid_cells': 'bool',
        'ignore_blank_rows': 'bool'
    }

    attribute_map = {
        'column_names': 'columnNames',
        'column_types': 'columnTypes',
        'infer_type_row_count': 'inferTypeRowCount',
        'no_header': 'noHeader',
        'calculate': 'calculate',
        'password': 'password',
        'worksheet': 'worksheet',
        'range_or_table': 'rangeOrTable',
        'ignore_invalid_cells': 'ignoreInvalidCells',
        'ignore_blank_rows': 'ignoreBlankRows'
    }

    required_map = {
        'column_names': 'optional',
        'column_types': 'optional',
        'infer_type_row_count': 'optional',
        'no_header': 'optional',
        'calculate': 'optional',
        'password': 'optional',
        'worksheet': 'optional',
        'range_or_table': 'optional',
        'ignore_invalid_cells': 'optional',
        'ignore_blank_rows': 'optional'
    }

    def __init__(self, column_names=None, column_types=None, infer_type_row_count=None, no_header=None, calculate=None, password=None, worksheet=None, range_or_table=None, ignore_invalid_cells=None, ignore_blank_rows=None, local_vars_configuration=None):  # noqa: E501
        """OptionsExcel - a model defined in OpenAPI"
        
        :param column_names:  Column Names either overrides the header row or steps in when there is no header row (comma delimited list)
        :type column_names: str
        :param column_types:  Column types (comma delimited list of: '{types}', some columns may be left blank while others are specified)
        :type column_types: str
        :param infer_type_row_count:  If non-zero and 'types' is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified
        :type infer_type_row_count: int
        :param no_header:  Set this if there is no header row
        :type no_header: bool
        :param calculate:  Whether to attempt a calculation of the imported cell range prior to import
        :type calculate: bool
        :param password:  If specified will be used as the password used for password protected workbooks
        :type password: str
        :param worksheet:  The worksheet containing the cell range to import (name or index, will default to first)
        :type worksheet: str
        :param range_or_table:  The cell range to import as either a specified range or a table name
        :type range_or_table: str
        :param ignore_invalid_cells:  If specified cells which can not be successfully converted to the target type will be ignored
        :type ignore_invalid_cells: bool
        :param ignore_blank_rows:  If the entire rows has only blank cells it will be ignored will be ignored
        :type ignore_blank_rows: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._column_names = None
        self._column_types = None
        self._infer_type_row_count = None
        self._no_header = None
        self._calculate = None
        self._password = None
        self._worksheet = None
        self._range_or_table = None
        self._ignore_invalid_cells = None
        self._ignore_blank_rows = None
        self.discriminator = None

        self.column_names = column_names
        self.column_types = column_types
        if infer_type_row_count is not None:
            self.infer_type_row_count = infer_type_row_count
        if no_header is not None:
            self.no_header = no_header
        if calculate is not None:
            self.calculate = calculate
        self.password = password
        self.worksheet = worksheet
        self.range_or_table = range_or_table
        if ignore_invalid_cells is not None:
            self.ignore_invalid_cells = ignore_invalid_cells
        if ignore_blank_rows is not None:
            self.ignore_blank_rows = ignore_blank_rows

    @property
    def column_names(self):
        """Gets the column_names of this OptionsExcel.  # noqa: E501

        Column Names either overrides the header row or steps in when there is no header row (comma delimited list)  # noqa: E501

        :return: The column_names of this OptionsExcel.  # noqa: E501
        :rtype: str
        """
        return self._column_names

    @column_names.setter
    def column_names(self, column_names):
        """Sets the column_names of this OptionsExcel.

        Column Names either overrides the header row or steps in when there is no header row (comma delimited list)  # noqa: E501

        :param column_names: The column_names of this OptionsExcel.  # noqa: E501
        :type column_names: str
        """

        self._column_names = column_names

    @property
    def column_types(self):
        """Gets the column_types of this OptionsExcel.  # noqa: E501

        Column types (comma delimited list of: '{types}', some columns may be left blank while others are specified)  # noqa: E501

        :return: The column_types of this OptionsExcel.  # noqa: E501
        :rtype: str
        """
        return self._column_types

    @column_types.setter
    def column_types(self, column_types):
        """Sets the column_types of this OptionsExcel.

        Column types (comma delimited list of: '{types}', some columns may be left blank while others are specified)  # noqa: E501

        :param column_types: The column_types of this OptionsExcel.  # noqa: E501
        :type column_types: str
        """

        self._column_types = column_types

    @property
    def infer_type_row_count(self):
        """Gets the infer_type_row_count of this OptionsExcel.  # noqa: E501

        If non-zero and 'types' is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified  # noqa: E501

        :return: The infer_type_row_count of this OptionsExcel.  # noqa: E501
        :rtype: int
        """
        return self._infer_type_row_count

    @infer_type_row_count.setter
    def infer_type_row_count(self, infer_type_row_count):
        """Sets the infer_type_row_count of this OptionsExcel.

        If non-zero and 'types' is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified  # noqa: E501

        :param infer_type_row_count: The infer_type_row_count of this OptionsExcel.  # noqa: E501
        :type infer_type_row_count: int
        """

        self._infer_type_row_count = infer_type_row_count

    @property
    def no_header(self):
        """Gets the no_header of this OptionsExcel.  # noqa: E501

        Set this if there is no header row  # noqa: E501

        :return: The no_header of this OptionsExcel.  # noqa: E501
        :rtype: bool
        """
        return self._no_header

    @no_header.setter
    def no_header(self, no_header):
        """Sets the no_header of this OptionsExcel.

        Set this if there is no header row  # noqa: E501

        :param no_header: The no_header of this OptionsExcel.  # noqa: E501
        :type no_header: bool
        """

        self._no_header = no_header

    @property
    def calculate(self):
        """Gets the calculate of this OptionsExcel.  # noqa: E501

        Whether to attempt a calculation of the imported cell range prior to import  # noqa: E501

        :return: The calculate of this OptionsExcel.  # noqa: E501
        :rtype: bool
        """
        return self._calculate

    @calculate.setter
    def calculate(self, calculate):
        """Sets the calculate of this OptionsExcel.

        Whether to attempt a calculation of the imported cell range prior to import  # noqa: E501

        :param calculate: The calculate of this OptionsExcel.  # noqa: E501
        :type calculate: bool
        """

        self._calculate = calculate

    @property
    def password(self):
        """Gets the password of this OptionsExcel.  # noqa: E501

        If specified will be used as the password used for password protected workbooks  # noqa: E501

        :return: The password of this OptionsExcel.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this OptionsExcel.

        If specified will be used as the password used for password protected workbooks  # noqa: E501

        :param password: The password of this OptionsExcel.  # noqa: E501
        :type password: str
        """

        self._password = password

    @property
    def worksheet(self):
        """Gets the worksheet of this OptionsExcel.  # noqa: E501

        The worksheet containing the cell range to import (name or index, will default to first)  # noqa: E501

        :return: The worksheet of this OptionsExcel.  # noqa: E501
        :rtype: str
        """
        return self._worksheet

    @worksheet.setter
    def worksheet(self, worksheet):
        """Sets the worksheet of this OptionsExcel.

        The worksheet containing the cell range to import (name or index, will default to first)  # noqa: E501

        :param worksheet: The worksheet of this OptionsExcel.  # noqa: E501
        :type worksheet: str
        """

        self._worksheet = worksheet

    @property
    def range_or_table(self):
        """Gets the range_or_table of this OptionsExcel.  # noqa: E501

        The cell range to import as either a specified range or a table name  # noqa: E501

        :return: The range_or_table of this OptionsExcel.  # noqa: E501
        :rtype: str
        """
        return self._range_or_table

    @range_or_table.setter
    def range_or_table(self, range_or_table):
        """Sets the range_or_table of this OptionsExcel.

        The cell range to import as either a specified range or a table name  # noqa: E501

        :param range_or_table: The range_or_table of this OptionsExcel.  # noqa: E501
        :type range_or_table: str
        """

        self._range_or_table = range_or_table

    @property
    def ignore_invalid_cells(self):
        """Gets the ignore_invalid_cells of this OptionsExcel.  # noqa: E501

        If specified cells which can not be successfully converted to the target type will be ignored  # noqa: E501

        :return: The ignore_invalid_cells of this OptionsExcel.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_invalid_cells

    @ignore_invalid_cells.setter
    def ignore_invalid_cells(self, ignore_invalid_cells):
        """Sets the ignore_invalid_cells of this OptionsExcel.

        If specified cells which can not be successfully converted to the target type will be ignored  # noqa: E501

        :param ignore_invalid_cells: The ignore_invalid_cells of this OptionsExcel.  # noqa: E501
        :type ignore_invalid_cells: bool
        """

        self._ignore_invalid_cells = ignore_invalid_cells

    @property
    def ignore_blank_rows(self):
        """Gets the ignore_blank_rows of this OptionsExcel.  # noqa: E501

        If the entire rows has only blank cells it will be ignored will be ignored  # noqa: E501

        :return: The ignore_blank_rows of this OptionsExcel.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_blank_rows

    @ignore_blank_rows.setter
    def ignore_blank_rows(self, ignore_blank_rows):
        """Sets the ignore_blank_rows of this OptionsExcel.

        If the entire rows has only blank cells it will be ignored will be ignored  # noqa: E501

        :param ignore_blank_rows: The ignore_blank_rows of this OptionsExcel.  # noqa: E501
        :type ignore_blank_rows: bool
        """

        self._ignore_blank_rows = ignore_blank_rows

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
        if not isinstance(other, OptionsExcel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OptionsExcel):
            return True

        return self.to_dict() != other.to_dict()
