# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.765
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


class ConvertToViewData(object):
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
        'query': 'str',
        'name': 'str',
        'description': 'str',
        'documentation_link': 'str',
        'view_parameters': 'list[ViewParameter]',
        'other_parameters': 'dict(str, str)',
        'starting_variable_name': 'str'
    }

    attribute_map = {
        'query': 'query',
        'name': 'name',
        'description': 'description',
        'documentation_link': 'documentationLink',
        'view_parameters': 'viewParameters',
        'other_parameters': 'otherParameters',
        'starting_variable_name': 'startingVariableName'
    }

    required_map = {
        'query': 'required',
        'name': 'required',
        'description': 'optional',
        'documentation_link': 'optional',
        'view_parameters': 'optional',
        'other_parameters': 'optional',
        'starting_variable_name': 'optional'
    }

    def __init__(self, query=None, name=None, description=None, documentation_link=None, view_parameters=None, other_parameters=None, starting_variable_name=None, local_vars_configuration=None):  # noqa: E501
        """ConvertToViewData - a model defined in OpenAPI"
        
        :param query:  view query (required)
        :type query: str
        :param name:  Name of view (required)
        :type name: str
        :param description:  Description of view
        :type description: str
        :param documentation_link:  Documentation link
        :type documentation_link: str
        :param view_parameters:  View parameters
        :type view_parameters: list[luminesce.ViewParameter]
        :param other_parameters:  Other parameters not explicitly handled by the ConvertToView generation.  These will be populated by the \"From SQL\" and should simply be returned by  the web GUI should the user edit / update / regenerate
        :type other_parameters: dict(str, str)
        :param starting_variable_name:  Which variable the this start with, null if not started from a full Create View Sql Statement.
        :type starting_variable_name: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._query = None
        self._name = None
        self._description = None
        self._documentation_link = None
        self._view_parameters = None
        self._other_parameters = None
        self._starting_variable_name = None
        self.discriminator = None

        self.query = query
        self.name = name
        self.description = description
        self.documentation_link = documentation_link
        self.view_parameters = view_parameters
        self.other_parameters = other_parameters
        self.starting_variable_name = starting_variable_name

    @property
    def query(self):
        """Gets the query of this ConvertToViewData.  # noqa: E501

        view query  # noqa: E501

        :return: The query of this ConvertToViewData.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this ConvertToViewData.

        view query  # noqa: E501

        :param query: The query of this ConvertToViewData.  # noqa: E501
        :type query: str
        """
        if self.local_vars_configuration.client_side_validation and query is None:  # noqa: E501
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                query is not None and len(query) < 1):
            raise ValueError("Invalid value for `query`, length must be greater than or equal to `1`")  # noqa: E501

        self._query = query

    @property
    def name(self):
        """Gets the name of this ConvertToViewData.  # noqa: E501

        Name of view  # noqa: E501

        :return: The name of this ConvertToViewData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConvertToViewData.

        Name of view  # noqa: E501

        :param name: The name of this ConvertToViewData.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 256):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ConvertToViewData.  # noqa: E501

        Description of view  # noqa: E501

        :return: The description of this ConvertToViewData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConvertToViewData.

        Description of view  # noqa: E501

        :param description: The description of this ConvertToViewData.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 256):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def documentation_link(self):
        """Gets the documentation_link of this ConvertToViewData.  # noqa: E501

        Documentation link  # noqa: E501

        :return: The documentation_link of this ConvertToViewData.  # noqa: E501
        :rtype: str
        """
        return self._documentation_link

    @documentation_link.setter
    def documentation_link(self, documentation_link):
        """Sets the documentation_link of this ConvertToViewData.

        Documentation link  # noqa: E501

        :param documentation_link: The documentation_link of this ConvertToViewData.  # noqa: E501
        :type documentation_link: str
        """
        if (self.local_vars_configuration.client_side_validation and
                documentation_link is not None and len(documentation_link) > 256):
            raise ValueError("Invalid value for `documentation_link`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                documentation_link is not None and len(documentation_link) < 0):
            raise ValueError("Invalid value for `documentation_link`, length must be greater than or equal to `0`")  # noqa: E501

        self._documentation_link = documentation_link

    @property
    def view_parameters(self):
        """Gets the view_parameters of this ConvertToViewData.  # noqa: E501

        View parameters  # noqa: E501

        :return: The view_parameters of this ConvertToViewData.  # noqa: E501
        :rtype: list[luminesce.ViewParameter]
        """
        return self._view_parameters

    @view_parameters.setter
    def view_parameters(self, view_parameters):
        """Sets the view_parameters of this ConvertToViewData.

        View parameters  # noqa: E501

        :param view_parameters: The view_parameters of this ConvertToViewData.  # noqa: E501
        :type view_parameters: list[luminesce.ViewParameter]
        """

        self._view_parameters = view_parameters

    @property
    def other_parameters(self):
        """Gets the other_parameters of this ConvertToViewData.  # noqa: E501

        Other parameters not explicitly handled by the ConvertToView generation.  These will be populated by the \"From SQL\" and should simply be returned by  the web GUI should the user edit / update / regenerate  # noqa: E501

        :return: The other_parameters of this ConvertToViewData.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._other_parameters

    @other_parameters.setter
    def other_parameters(self, other_parameters):
        """Sets the other_parameters of this ConvertToViewData.

        Other parameters not explicitly handled by the ConvertToView generation.  These will be populated by the \"From SQL\" and should simply be returned by  the web GUI should the user edit / update / regenerate  # noqa: E501

        :param other_parameters: The other_parameters of this ConvertToViewData.  # noqa: E501
        :type other_parameters: dict(str, str)
        """

        self._other_parameters = other_parameters

    @property
    def starting_variable_name(self):
        """Gets the starting_variable_name of this ConvertToViewData.  # noqa: E501

        Which variable the this start with, null if not started from a full Create View Sql Statement.  # noqa: E501

        :return: The starting_variable_name of this ConvertToViewData.  # noqa: E501
        :rtype: str
        """
        return self._starting_variable_name

    @starting_variable_name.setter
    def starting_variable_name(self, starting_variable_name):
        """Sets the starting_variable_name of this ConvertToViewData.

        Which variable the this start with, null if not started from a full Create View Sql Statement.  # noqa: E501

        :param starting_variable_name: The starting_variable_name of this ConvertToViewData.  # noqa: E501
        :type starting_variable_name: str
        """

        self._starting_variable_name = starting_variable_name

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
        if not isinstance(other, ConvertToViewData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConvertToViewData):
            return True

        return self.to_dict() != other.to_dict()
