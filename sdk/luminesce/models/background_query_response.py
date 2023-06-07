# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.12.895
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


class BackgroundQueryResponse(object):
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
        'execution_id': 'str',
        'progress': 'Link',
        'cancel': 'Link',
        'fetch_json': 'Link',
        'fetch_json_proper': 'Link',
        'fetch_xml': 'Link',
        'fetch_parquet': 'Link',
        'fetch_csv': 'Link',
        'fetch_pipe': 'Link',
        'fetch_excel': 'Link',
        'fetch_sqlite': 'Link',
        'histogram': 'Link'
    }

    attribute_map = {
        'execution_id': 'executionId',
        'progress': 'progress',
        'cancel': 'cancel',
        'fetch_json': 'fetchJson',
        'fetch_json_proper': 'fetchJsonProper',
        'fetch_xml': 'fetchXml',
        'fetch_parquet': 'fetchParquet',
        'fetch_csv': 'fetchCsv',
        'fetch_pipe': 'fetchPipe',
        'fetch_excel': 'fetchExcel',
        'fetch_sqlite': 'fetchSqlite',
        'histogram': 'histogram'
    }

    required_map = {
        'execution_id': 'optional',
        'progress': 'optional',
        'cancel': 'optional',
        'fetch_json': 'optional',
        'fetch_json_proper': 'optional',
        'fetch_xml': 'optional',
        'fetch_parquet': 'optional',
        'fetch_csv': 'optional',
        'fetch_pipe': 'optional',
        'fetch_excel': 'optional',
        'fetch_sqlite': 'optional',
        'histogram': 'optional'
    }

    def __init__(self, execution_id=None, progress=None, cancel=None, fetch_json=None, fetch_json_proper=None, fetch_xml=None, fetch_parquet=None, fetch_csv=None, fetch_pipe=None, fetch_excel=None, fetch_sqlite=None, histogram=None, local_vars_configuration=None):  # noqa: E501
        """BackgroundQueryResponse - a model defined in OpenAPI"
        
        :param execution_id:  ExecutionId of the started-query
        :type execution_id: str
        :param progress: 
        :type progress: luminesce.Link
        :param cancel: 
        :type cancel: luminesce.Link
        :param fetch_json: 
        :type fetch_json: luminesce.Link
        :param fetch_json_proper: 
        :type fetch_json_proper: luminesce.Link
        :param fetch_xml: 
        :type fetch_xml: luminesce.Link
        :param fetch_parquet: 
        :type fetch_parquet: luminesce.Link
        :param fetch_csv: 
        :type fetch_csv: luminesce.Link
        :param fetch_pipe: 
        :type fetch_pipe: luminesce.Link
        :param fetch_excel: 
        :type fetch_excel: luminesce.Link
        :param fetch_sqlite: 
        :type fetch_sqlite: luminesce.Link
        :param histogram: 
        :type histogram: luminesce.Link

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._execution_id = None
        self._progress = None
        self._cancel = None
        self._fetch_json = None
        self._fetch_json_proper = None
        self._fetch_xml = None
        self._fetch_parquet = None
        self._fetch_csv = None
        self._fetch_pipe = None
        self._fetch_excel = None
        self._fetch_sqlite = None
        self._histogram = None
        self.discriminator = None

        self.execution_id = execution_id
        if progress is not None:
            self.progress = progress
        if cancel is not None:
            self.cancel = cancel
        if fetch_json is not None:
            self.fetch_json = fetch_json
        if fetch_json_proper is not None:
            self.fetch_json_proper = fetch_json_proper
        if fetch_xml is not None:
            self.fetch_xml = fetch_xml
        if fetch_parquet is not None:
            self.fetch_parquet = fetch_parquet
        if fetch_csv is not None:
            self.fetch_csv = fetch_csv
        if fetch_pipe is not None:
            self.fetch_pipe = fetch_pipe
        if fetch_excel is not None:
            self.fetch_excel = fetch_excel
        if fetch_sqlite is not None:
            self.fetch_sqlite = fetch_sqlite
        if histogram is not None:
            self.histogram = histogram

    @property
    def execution_id(self):
        """Gets the execution_id of this BackgroundQueryResponse.  # noqa: E501

        ExecutionId of the started-query  # noqa: E501

        :return: The execution_id of this BackgroundQueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this BackgroundQueryResponse.

        ExecutionId of the started-query  # noqa: E501

        :param execution_id: The execution_id of this BackgroundQueryResponse.  # noqa: E501
        :type execution_id: str
        """

        self._execution_id = execution_id

    @property
    def progress(self):
        """Gets the progress of this BackgroundQueryResponse.  # noqa: E501


        :return: The progress of this BackgroundQueryResponse.  # noqa: E501
        :rtype: luminesce.Link
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this BackgroundQueryResponse.


        :param progress: The progress of this BackgroundQueryResponse.  # noqa: E501
        :type progress: luminesce.Link
        """

        self._progress = progress

    @property
    def cancel(self):
        """Gets the cancel of this BackgroundQueryResponse.  # noqa: E501


        :return: The cancel of this BackgroundQueryResponse.  # noqa: E501
        :rtype: luminesce.Link
        """
        return self._cancel

    @cancel.setter
    def cancel(self, cancel):
        """Sets the cancel of this BackgroundQueryResponse.


        :param cancel: The cancel of this BackgroundQueryResponse.  # noqa: E501
        :type cancel: luminesce.Link
        """

        self._cancel = cancel

    @property
    def fetch_json(self):
        """Gets the fetch_json of this BackgroundQueryResponse.  # noqa: E501


        :return: The fetch_json of this BackgroundQueryResponse.  # noqa: E501
        :rtype: luminesce.Link
        """
        return self._fetch_json

    @fetch_json.setter
    def fetch_json(self, fetch_json):
        """Sets the fetch_json of this BackgroundQueryResponse.


        :param fetch_json: The fetch_json of this BackgroundQueryResponse.  # noqa: E501
        :type fetch_json: luminesce.Link
        """

        self._fetch_json = fetch_json

    @property
    def fetch_json_proper(self):
        """Gets the fetch_json_proper of this BackgroundQueryResponse.  # noqa: E501


        :return: The fetch_json_proper of this BackgroundQueryResponse.  # noqa: E501
        :rtype: luminesce.Link
        """
        return self._fetch_json_proper

    @fetch_json_proper.setter
    def fetch_json_proper(self, fetch_json_proper):
        """Sets the fetch_json_proper of this BackgroundQueryResponse.


        :param fetch_json_proper: The fetch_json_proper of this BackgroundQueryResponse.  # noqa: E501
        :type fetch_json_proper: luminesce.Link
        """

        self._fetch_json_proper = fetch_json_proper

    @property
    def fetch_xml(self):
        """Gets the fetch_xml of this BackgroundQueryResponse.  # noqa: E501


        :return: The fetch_xml of this BackgroundQueryResponse.  # noqa: E501
        :rtype: luminesce.Link
        """
        return self._fetch_xml

    @fetch_xml.setter
    def fetch_xml(self, fetch_xml):
        """Sets the fetch_xml of this BackgroundQueryResponse.


        :param fetch_xml: The fetch_xml of this BackgroundQueryResponse.  # noqa: E501
        :type fetch_xml: luminesce.Link
        """

        self._fetch_xml = fetch_xml

    @property
    def fetch_parquet(self):
        """Gets the fetch_parquet of this BackgroundQueryResponse.  # noqa: E501


        :return: The fetch_parquet of this BackgroundQueryResponse.  # noqa: E501
        :rtype: luminesce.Link
        """
        return self._fetch_parquet

    @fetch_parquet.setter
    def fetch_parquet(self, fetch_parquet):
        """Sets the fetch_parquet of this BackgroundQueryResponse.


        :param fetch_parquet: The fetch_parquet of this BackgroundQueryResponse.  # noqa: E501
        :type fetch_parquet: luminesce.Link
        """

        self._fetch_parquet = fetch_parquet

    @property
    def fetch_csv(self):
        """Gets the fetch_csv of this BackgroundQueryResponse.  # noqa: E501


        :return: The fetch_csv of this BackgroundQueryResponse.  # noqa: E501
        :rtype: luminesce.Link
        """
        return self._fetch_csv

    @fetch_csv.setter
    def fetch_csv(self, fetch_csv):
        """Sets the fetch_csv of this BackgroundQueryResponse.


        :param fetch_csv: The fetch_csv of this BackgroundQueryResponse.  # noqa: E501
        :type fetch_csv: luminesce.Link
        """

        self._fetch_csv = fetch_csv

    @property
    def fetch_pipe(self):
        """Gets the fetch_pipe of this BackgroundQueryResponse.  # noqa: E501


        :return: The fetch_pipe of this BackgroundQueryResponse.  # noqa: E501
        :rtype: luminesce.Link
        """
        return self._fetch_pipe

    @fetch_pipe.setter
    def fetch_pipe(self, fetch_pipe):
        """Sets the fetch_pipe of this BackgroundQueryResponse.


        :param fetch_pipe: The fetch_pipe of this BackgroundQueryResponse.  # noqa: E501
        :type fetch_pipe: luminesce.Link
        """

        self._fetch_pipe = fetch_pipe

    @property
    def fetch_excel(self):
        """Gets the fetch_excel of this BackgroundQueryResponse.  # noqa: E501


        :return: The fetch_excel of this BackgroundQueryResponse.  # noqa: E501
        :rtype: luminesce.Link
        """
        return self._fetch_excel

    @fetch_excel.setter
    def fetch_excel(self, fetch_excel):
        """Sets the fetch_excel of this BackgroundQueryResponse.


        :param fetch_excel: The fetch_excel of this BackgroundQueryResponse.  # noqa: E501
        :type fetch_excel: luminesce.Link
        """

        self._fetch_excel = fetch_excel

    @property
    def fetch_sqlite(self):
        """Gets the fetch_sqlite of this BackgroundQueryResponse.  # noqa: E501


        :return: The fetch_sqlite of this BackgroundQueryResponse.  # noqa: E501
        :rtype: luminesce.Link
        """
        return self._fetch_sqlite

    @fetch_sqlite.setter
    def fetch_sqlite(self, fetch_sqlite):
        """Sets the fetch_sqlite of this BackgroundQueryResponse.


        :param fetch_sqlite: The fetch_sqlite of this BackgroundQueryResponse.  # noqa: E501
        :type fetch_sqlite: luminesce.Link
        """

        self._fetch_sqlite = fetch_sqlite

    @property
    def histogram(self):
        """Gets the histogram of this BackgroundQueryResponse.  # noqa: E501


        :return: The histogram of this BackgroundQueryResponse.  # noqa: E501
        :rtype: luminesce.Link
        """
        return self._histogram

    @histogram.setter
    def histogram(self, histogram):
        """Sets the histogram of this BackgroundQueryResponse.


        :param histogram: The histogram of this BackgroundQueryResponse.  # noqa: E501
        :type histogram: luminesce.Link
        """

        self._histogram = histogram

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
        if not isinstance(other, BackgroundQueryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackgroundQueryResponse):
            return True

        return self.to_dict() != other.to_dict()
