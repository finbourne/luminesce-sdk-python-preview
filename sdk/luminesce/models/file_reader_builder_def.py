# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.14.332
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


class FileReaderBuilderDef(object):
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
        'auto_detect': 'AutoDetectType',
        'columns': 'list[ColumnInfo]',
        'limit': 'int',
        'source': 'Source',
        'available_sources': 'list[Source]',
        'variable_name': 'str',
        'file_path': 'str',
        'folder_filter': 'str',
        'zip_filter': 'str',
        'add_file_name': 'bool',
        'csv': 'OptionsCsv',
        'excel': 'OptionsExcel',
        'sq_lite': 'OptionsSqLite',
        'xml': 'OptionsXml',
        'parquet': 'OptionsParquet'
    }

    attribute_map = {
        'auto_detect': 'autoDetect',
        'columns': 'columns',
        'limit': 'limit',
        'source': 'source',
        'available_sources': 'availableSources',
        'variable_name': 'variableName',
        'file_path': 'filePath',
        'folder_filter': 'folderFilter',
        'zip_filter': 'zipFilter',
        'add_file_name': 'addFileName',
        'csv': 'csv',
        'excel': 'excel',
        'sq_lite': 'sqLite',
        'xml': 'xml',
        'parquet': 'parquet'
    }

    required_map = {
        'auto_detect': 'optional',
        'columns': 'optional',
        'limit': 'optional',
        'source': 'optional',
        'available_sources': 'optional',
        'variable_name': 'optional',
        'file_path': 'optional',
        'folder_filter': 'optional',
        'zip_filter': 'optional',
        'add_file_name': 'optional',
        'csv': 'optional',
        'excel': 'optional',
        'sq_lite': 'optional',
        'xml': 'optional',
        'parquet': 'optional'
    }

    def __init__(self, auto_detect=None, columns=None, limit=None, source=None, available_sources=None, variable_name=None, file_path=None, folder_filter=None, zip_filter=None, add_file_name=None, csv=None, excel=None, sq_lite=None, xml=None, parquet=None, local_vars_configuration=None):  # noqa: E501
        """FileReaderBuilderDef - a model defined in OpenAPI"
        
        :param auto_detect: 
        :type auto_detect: luminesce.AutoDetectType
        :param columns:  Column information for the results
        :type columns: list[luminesce.ColumnInfo]
        :param limit:  What limit be added to the load query?  Less than or equal to zero means none
        :type limit: int
        :param source: 
        :type source: luminesce.Source
        :param available_sources:  The source locations the user has access to.  The provider in essence.
        :type available_sources: list[luminesce.Source]
        :param variable_name:  The name of the variable for the `use` statement
        :type variable_name: str
        :param file_path:  The file (or folder) path
        :type file_path: str
        :param folder_filter:  The filter to apply to a folder (all matching files then being read) a RegExp
        :type folder_filter: str
        :param zip_filter:  The filter to apply to folder structures with zip archives (all matching files then being read) a RegExp
        :type zip_filter: str
        :param add_file_name:  Should a file name column be added to the output?
        :type add_file_name: bool
        :param csv: 
        :type csv: luminesce.OptionsCsv
        :param excel: 
        :type excel: luminesce.OptionsExcel
        :param sq_lite: 
        :type sq_lite: luminesce.OptionsSqLite
        :param xml: 
        :type xml: luminesce.OptionsXml
        :param parquet: 
        :type parquet: luminesce.OptionsParquet

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._auto_detect = None
        self._columns = None
        self._limit = None
        self._source = None
        self._available_sources = None
        self._variable_name = None
        self._file_path = None
        self._folder_filter = None
        self._zip_filter = None
        self._add_file_name = None
        self._csv = None
        self._excel = None
        self._sq_lite = None
        self._xml = None
        self._parquet = None
        self.discriminator = None

        if auto_detect is not None:
            self.auto_detect = auto_detect
        self.columns = columns
        if limit is not None:
            self.limit = limit
        if source is not None:
            self.source = source
        self.available_sources = available_sources
        self.variable_name = variable_name
        self.file_path = file_path
        self.folder_filter = folder_filter
        self.zip_filter = zip_filter
        if add_file_name is not None:
            self.add_file_name = add_file_name
        if csv is not None:
            self.csv = csv
        if excel is not None:
            self.excel = excel
        if sq_lite is not None:
            self.sq_lite = sq_lite
        if xml is not None:
            self.xml = xml
        if parquet is not None:
            self.parquet = parquet

    @property
    def auto_detect(self):
        """Gets the auto_detect of this FileReaderBuilderDef.  # noqa: E501


        :return: The auto_detect of this FileReaderBuilderDef.  # noqa: E501
        :rtype: luminesce.AutoDetectType
        """
        return self._auto_detect

    @auto_detect.setter
    def auto_detect(self, auto_detect):
        """Sets the auto_detect of this FileReaderBuilderDef.


        :param auto_detect: The auto_detect of this FileReaderBuilderDef.  # noqa: E501
        :type auto_detect: luminesce.AutoDetectType
        """

        self._auto_detect = auto_detect

    @property
    def columns(self):
        """Gets the columns of this FileReaderBuilderDef.  # noqa: E501

        Column information for the results  # noqa: E501

        :return: The columns of this FileReaderBuilderDef.  # noqa: E501
        :rtype: list[luminesce.ColumnInfo]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this FileReaderBuilderDef.

        Column information for the results  # noqa: E501

        :param columns: The columns of this FileReaderBuilderDef.  # noqa: E501
        :type columns: list[luminesce.ColumnInfo]
        """

        self._columns = columns

    @property
    def limit(self):
        """Gets the limit of this FileReaderBuilderDef.  # noqa: E501

        What limit be added to the load query?  Less than or equal to zero means none  # noqa: E501

        :return: The limit of this FileReaderBuilderDef.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this FileReaderBuilderDef.

        What limit be added to the load query?  Less than or equal to zero means none  # noqa: E501

        :param limit: The limit of this FileReaderBuilderDef.  # noqa: E501
        :type limit: int
        """

        self._limit = limit

    @property
    def source(self):
        """Gets the source of this FileReaderBuilderDef.  # noqa: E501


        :return: The source of this FileReaderBuilderDef.  # noqa: E501
        :rtype: luminesce.Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this FileReaderBuilderDef.


        :param source: The source of this FileReaderBuilderDef.  # noqa: E501
        :type source: luminesce.Source
        """

        self._source = source

    @property
    def available_sources(self):
        """Gets the available_sources of this FileReaderBuilderDef.  # noqa: E501

        The source locations the user has access to.  The provider in essence.  # noqa: E501

        :return: The available_sources of this FileReaderBuilderDef.  # noqa: E501
        :rtype: list[luminesce.Source]
        """
        return self._available_sources

    @available_sources.setter
    def available_sources(self, available_sources):
        """Sets the available_sources of this FileReaderBuilderDef.

        The source locations the user has access to.  The provider in essence.  # noqa: E501

        :param available_sources: The available_sources of this FileReaderBuilderDef.  # noqa: E501
        :type available_sources: list[luminesce.Source]
        """

        self._available_sources = available_sources

    @property
    def variable_name(self):
        """Gets the variable_name of this FileReaderBuilderDef.  # noqa: E501

        The name of the variable for the `use` statement  # noqa: E501

        :return: The variable_name of this FileReaderBuilderDef.  # noqa: E501
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this FileReaderBuilderDef.

        The name of the variable for the `use` statement  # noqa: E501

        :param variable_name: The variable_name of this FileReaderBuilderDef.  # noqa: E501
        :type variable_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                variable_name is not None and len(variable_name) > 256):
            raise ValueError("Invalid value for `variable_name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                variable_name is not None and len(variable_name) < 0):
            raise ValueError("Invalid value for `variable_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._variable_name = variable_name

    @property
    def file_path(self):
        """Gets the file_path of this FileReaderBuilderDef.  # noqa: E501

        The file (or folder) path  # noqa: E501

        :return: The file_path of this FileReaderBuilderDef.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this FileReaderBuilderDef.

        The file (or folder) path  # noqa: E501

        :param file_path: The file_path of this FileReaderBuilderDef.  # noqa: E501
        :type file_path: str
        """
        if (self.local_vars_configuration.client_side_validation and
                file_path is not None and len(file_path) > 256):
            raise ValueError("Invalid value for `file_path`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                file_path is not None and len(file_path) < 0):
            raise ValueError("Invalid value for `file_path`, length must be greater than or equal to `0`")  # noqa: E501

        self._file_path = file_path

    @property
    def folder_filter(self):
        """Gets the folder_filter of this FileReaderBuilderDef.  # noqa: E501

        The filter to apply to a folder (all matching files then being read) a RegExp  # noqa: E501

        :return: The folder_filter of this FileReaderBuilderDef.  # noqa: E501
        :rtype: str
        """
        return self._folder_filter

    @folder_filter.setter
    def folder_filter(self, folder_filter):
        """Sets the folder_filter of this FileReaderBuilderDef.

        The filter to apply to a folder (all matching files then being read) a RegExp  # noqa: E501

        :param folder_filter: The folder_filter of this FileReaderBuilderDef.  # noqa: E501
        :type folder_filter: str
        """
        if (self.local_vars_configuration.client_side_validation and
                folder_filter is not None and len(folder_filter) > 256):
            raise ValueError("Invalid value for `folder_filter`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                folder_filter is not None and len(folder_filter) < 0):
            raise ValueError("Invalid value for `folder_filter`, length must be greater than or equal to `0`")  # noqa: E501

        self._folder_filter = folder_filter

    @property
    def zip_filter(self):
        """Gets the zip_filter of this FileReaderBuilderDef.  # noqa: E501

        The filter to apply to folder structures with zip archives (all matching files then being read) a RegExp  # noqa: E501

        :return: The zip_filter of this FileReaderBuilderDef.  # noqa: E501
        :rtype: str
        """
        return self._zip_filter

    @zip_filter.setter
    def zip_filter(self, zip_filter):
        """Sets the zip_filter of this FileReaderBuilderDef.

        The filter to apply to folder structures with zip archives (all matching files then being read) a RegExp  # noqa: E501

        :param zip_filter: The zip_filter of this FileReaderBuilderDef.  # noqa: E501
        :type zip_filter: str
        """
        if (self.local_vars_configuration.client_side_validation and
                zip_filter is not None and len(zip_filter) > 256):
            raise ValueError("Invalid value for `zip_filter`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                zip_filter is not None and len(zip_filter) < 0):
            raise ValueError("Invalid value for `zip_filter`, length must be greater than or equal to `0`")  # noqa: E501

        self._zip_filter = zip_filter

    @property
    def add_file_name(self):
        """Gets the add_file_name of this FileReaderBuilderDef.  # noqa: E501

        Should a file name column be added to the output?  # noqa: E501

        :return: The add_file_name of this FileReaderBuilderDef.  # noqa: E501
        :rtype: bool
        """
        return self._add_file_name

    @add_file_name.setter
    def add_file_name(self, add_file_name):
        """Sets the add_file_name of this FileReaderBuilderDef.

        Should a file name column be added to the output?  # noqa: E501

        :param add_file_name: The add_file_name of this FileReaderBuilderDef.  # noqa: E501
        :type add_file_name: bool
        """

        self._add_file_name = add_file_name

    @property
    def csv(self):
        """Gets the csv of this FileReaderBuilderDef.  # noqa: E501


        :return: The csv of this FileReaderBuilderDef.  # noqa: E501
        :rtype: luminesce.OptionsCsv
        """
        return self._csv

    @csv.setter
    def csv(self, csv):
        """Sets the csv of this FileReaderBuilderDef.


        :param csv: The csv of this FileReaderBuilderDef.  # noqa: E501
        :type csv: luminesce.OptionsCsv
        """

        self._csv = csv

    @property
    def excel(self):
        """Gets the excel of this FileReaderBuilderDef.  # noqa: E501


        :return: The excel of this FileReaderBuilderDef.  # noqa: E501
        :rtype: luminesce.OptionsExcel
        """
        return self._excel

    @excel.setter
    def excel(self, excel):
        """Sets the excel of this FileReaderBuilderDef.


        :param excel: The excel of this FileReaderBuilderDef.  # noqa: E501
        :type excel: luminesce.OptionsExcel
        """

        self._excel = excel

    @property
    def sq_lite(self):
        """Gets the sq_lite of this FileReaderBuilderDef.  # noqa: E501


        :return: The sq_lite of this FileReaderBuilderDef.  # noqa: E501
        :rtype: luminesce.OptionsSqLite
        """
        return self._sq_lite

    @sq_lite.setter
    def sq_lite(self, sq_lite):
        """Sets the sq_lite of this FileReaderBuilderDef.


        :param sq_lite: The sq_lite of this FileReaderBuilderDef.  # noqa: E501
        :type sq_lite: luminesce.OptionsSqLite
        """

        self._sq_lite = sq_lite

    @property
    def xml(self):
        """Gets the xml of this FileReaderBuilderDef.  # noqa: E501


        :return: The xml of this FileReaderBuilderDef.  # noqa: E501
        :rtype: luminesce.OptionsXml
        """
        return self._xml

    @xml.setter
    def xml(self, xml):
        """Sets the xml of this FileReaderBuilderDef.


        :param xml: The xml of this FileReaderBuilderDef.  # noqa: E501
        :type xml: luminesce.OptionsXml
        """

        self._xml = xml

    @property
    def parquet(self):
        """Gets the parquet of this FileReaderBuilderDef.  # noqa: E501


        :return: The parquet of this FileReaderBuilderDef.  # noqa: E501
        :rtype: luminesce.OptionsParquet
        """
        return self._parquet

    @parquet.setter
    def parquet(self, parquet):
        """Sets the parquet of this FileReaderBuilderDef.


        :param parquet: The parquet of this FileReaderBuilderDef.  # noqa: E501
        :type parquet: luminesce.OptionsParquet
        """

        self._parquet = parquet

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
        if not isinstance(other, FileReaderBuilderDef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileReaderBuilderDef):
            return True

        return self.to_dict() != other.to_dict()
