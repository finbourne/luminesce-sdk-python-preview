# coding: utf-8

"""
    FINBOURNE Honeycomb Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.6.25
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


class BackgroundMultiQueryResponse(object):
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
        'fetch_json': 'list[Link]',
        'fetch_json_proper': 'list[Link]',
        'fetch_csv': 'list[Link]',
        'fetch_pipe': 'list[Link]',
        'fetch_excel': 'list[Link]',
        'fetch_sqlite': 'list[Link]'
    }

    attribute_map = {
        'execution_id': 'executionId',
        'progress': 'progress',
        'cancel': 'cancel',
        'fetch_json': 'fetchJson',
        'fetch_json_proper': 'fetchJsonProper',
        'fetch_csv': 'fetchCsv',
        'fetch_pipe': 'fetchPipe',
        'fetch_excel': 'fetchExcel',
        'fetch_sqlite': 'fetchSqlite'
    }

    required_map = {
        'execution_id': 'optional',
        'progress': 'optional',
        'cancel': 'optional',
        'fetch_json': 'optional',
        'fetch_json_proper': 'optional',
        'fetch_csv': 'optional',
        'fetch_pipe': 'optional',
        'fetch_excel': 'optional',
        'fetch_sqlite': 'optional'
    }

    def __init__(self, execution_id=None, progress=None, cancel=None, fetch_json=None, fetch_json_proper=None, fetch_csv=None, fetch_pipe=None, fetch_excel=None, fetch_sqlite=None, local_vars_configuration=None):  # noqa: E501
        """BackgroundMultiQueryResponse - a model defined in OpenAPI"
        
        :param execution_id: 
        :type execution_id: str
        :param progress: 
        :type progress: luminesce.Link
        :param cancel: 
        :type cancel: luminesce.Link
        :param fetch_json: 
        :type fetch_json: list[luminesce.Link]
        :param fetch_json_proper: 
        :type fetch_json_proper: list[luminesce.Link]
        :param fetch_csv: 
        :type fetch_csv: list[luminesce.Link]
        :param fetch_pipe: 
        :type fetch_pipe: list[luminesce.Link]
        :param fetch_excel: 
        :type fetch_excel: list[luminesce.Link]
        :param fetch_sqlite: 
        :type fetch_sqlite: list[luminesce.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._execution_id = None
        self._progress = None
        self._cancel = None
        self._fetch_json = None
        self._fetch_json_proper = None
        self._fetch_csv = None
        self._fetch_pipe = None
        self._fetch_excel = None
        self._fetch_sqlite = None
        self.discriminator = None

        if execution_id is not None:
            self.execution_id = execution_id
        if progress is not None:
            self.progress = progress
        if cancel is not None:
            self.cancel = cancel
        self.fetch_json = fetch_json
        self.fetch_json_proper = fetch_json_proper
        self.fetch_csv = fetch_csv
        self.fetch_pipe = fetch_pipe
        self.fetch_excel = fetch_excel
        self.fetch_sqlite = fetch_sqlite

    @property
    def execution_id(self):
        """Gets the execution_id of this BackgroundMultiQueryResponse.  # noqa: E501


        :return: The execution_id of this BackgroundMultiQueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this BackgroundMultiQueryResponse.


        :param execution_id: The execution_id of this BackgroundMultiQueryResponse.  # noqa: E501
        :type execution_id: str
        """

        self._execution_id = execution_id

    @property
    def progress(self):
        """Gets the progress of this BackgroundMultiQueryResponse.  # noqa: E501


        :return: The progress of this BackgroundMultiQueryResponse.  # noqa: E501
        :rtype: luminesce.Link
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this BackgroundMultiQueryResponse.


        :param progress: The progress of this BackgroundMultiQueryResponse.  # noqa: E501
        :type progress: luminesce.Link
        """

        self._progress = progress

    @property
    def cancel(self):
        """Gets the cancel of this BackgroundMultiQueryResponse.  # noqa: E501


        :return: The cancel of this BackgroundMultiQueryResponse.  # noqa: E501
        :rtype: luminesce.Link
        """
        return self._cancel

    @cancel.setter
    def cancel(self, cancel):
        """Sets the cancel of this BackgroundMultiQueryResponse.


        :param cancel: The cancel of this BackgroundMultiQueryResponse.  # noqa: E501
        :type cancel: luminesce.Link
        """

        self._cancel = cancel

    @property
    def fetch_json(self):
        """Gets the fetch_json of this BackgroundMultiQueryResponse.  # noqa: E501


        :return: The fetch_json of this BackgroundMultiQueryResponse.  # noqa: E501
        :rtype: list[luminesce.Link]
        """
        return self._fetch_json

    @fetch_json.setter
    def fetch_json(self, fetch_json):
        """Sets the fetch_json of this BackgroundMultiQueryResponse.


        :param fetch_json: The fetch_json of this BackgroundMultiQueryResponse.  # noqa: E501
        :type fetch_json: list[luminesce.Link]
        """

        self._fetch_json = fetch_json

    @property
    def fetch_json_proper(self):
        """Gets the fetch_json_proper of this BackgroundMultiQueryResponse.  # noqa: E501


        :return: The fetch_json_proper of this BackgroundMultiQueryResponse.  # noqa: E501
        :rtype: list[luminesce.Link]
        """
        return self._fetch_json_proper

    @fetch_json_proper.setter
    def fetch_json_proper(self, fetch_json_proper):
        """Sets the fetch_json_proper of this BackgroundMultiQueryResponse.


        :param fetch_json_proper: The fetch_json_proper of this BackgroundMultiQueryResponse.  # noqa: E501
        :type fetch_json_proper: list[luminesce.Link]
        """

        self._fetch_json_proper = fetch_json_proper

    @property
    def fetch_csv(self):
        """Gets the fetch_csv of this BackgroundMultiQueryResponse.  # noqa: E501


        :return: The fetch_csv of this BackgroundMultiQueryResponse.  # noqa: E501
        :rtype: list[luminesce.Link]
        """
        return self._fetch_csv

    @fetch_csv.setter
    def fetch_csv(self, fetch_csv):
        """Sets the fetch_csv of this BackgroundMultiQueryResponse.


        :param fetch_csv: The fetch_csv of this BackgroundMultiQueryResponse.  # noqa: E501
        :type fetch_csv: list[luminesce.Link]
        """

        self._fetch_csv = fetch_csv

    @property
    def fetch_pipe(self):
        """Gets the fetch_pipe of this BackgroundMultiQueryResponse.  # noqa: E501


        :return: The fetch_pipe of this BackgroundMultiQueryResponse.  # noqa: E501
        :rtype: list[luminesce.Link]
        """
        return self._fetch_pipe

    @fetch_pipe.setter
    def fetch_pipe(self, fetch_pipe):
        """Sets the fetch_pipe of this BackgroundMultiQueryResponse.


        :param fetch_pipe: The fetch_pipe of this BackgroundMultiQueryResponse.  # noqa: E501
        :type fetch_pipe: list[luminesce.Link]
        """

        self._fetch_pipe = fetch_pipe

    @property
    def fetch_excel(self):
        """Gets the fetch_excel of this BackgroundMultiQueryResponse.  # noqa: E501


        :return: The fetch_excel of this BackgroundMultiQueryResponse.  # noqa: E501
        :rtype: list[luminesce.Link]
        """
        return self._fetch_excel

    @fetch_excel.setter
    def fetch_excel(self, fetch_excel):
        """Sets the fetch_excel of this BackgroundMultiQueryResponse.


        :param fetch_excel: The fetch_excel of this BackgroundMultiQueryResponse.  # noqa: E501
        :type fetch_excel: list[luminesce.Link]
        """

        self._fetch_excel = fetch_excel

    @property
    def fetch_sqlite(self):
        """Gets the fetch_sqlite of this BackgroundMultiQueryResponse.  # noqa: E501


        :return: The fetch_sqlite of this BackgroundMultiQueryResponse.  # noqa: E501
        :rtype: list[luminesce.Link]
        """
        return self._fetch_sqlite

    @fetch_sqlite.setter
    def fetch_sqlite(self, fetch_sqlite):
        """Sets the fetch_sqlite of this BackgroundMultiQueryResponse.


        :param fetch_sqlite: The fetch_sqlite of this BackgroundMultiQueryResponse.  # noqa: E501
        :type fetch_sqlite: list[luminesce.Link]
        """

        self._fetch_sqlite = fetch_sqlite

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
        if not isinstance(other, BackgroundMultiQueryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackgroundMultiQueryResponse):
            return True

        return self.to_dict() != other.to_dict()
