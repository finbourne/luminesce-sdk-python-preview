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


class CaseStatementDesign(object):
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
        'selected_field': 'str',
        'case_statement_items': 'list[CaseStatementItem]'
    }

    attribute_map = {
        'selected_field': 'selectedField',
        'case_statement_items': 'caseStatementItems'
    }

    required_map = {
        'selected_field': 'optional',
        'case_statement_items': 'optional'
    }

    def __init__(self, selected_field=None, case_statement_items=None, local_vars_configuration=None):  # noqa: E501
        """CaseStatementDesign - a model defined in OpenAPI"
        
        :param selected_field:  Selected field in the SQL query.
        :type selected_field: str
        :param case_statement_items:  A list containing the filter, source, and target.
        :type case_statement_items: list[luminesce.CaseStatementItem]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._selected_field = None
        self._case_statement_items = None
        self.discriminator = None

        self.selected_field = selected_field
        self.case_statement_items = case_statement_items

    @property
    def selected_field(self):
        """Gets the selected_field of this CaseStatementDesign.  # noqa: E501

        Selected field in the SQL query.  # noqa: E501

        :return: The selected_field of this CaseStatementDesign.  # noqa: E501
        :rtype: str
        """
        return self._selected_field

    @selected_field.setter
    def selected_field(self, selected_field):
        """Sets the selected_field of this CaseStatementDesign.

        Selected field in the SQL query.  # noqa: E501

        :param selected_field: The selected_field of this CaseStatementDesign.  # noqa: E501
        :type selected_field: str
        """

        self._selected_field = selected_field

    @property
    def case_statement_items(self):
        """Gets the case_statement_items of this CaseStatementDesign.  # noqa: E501

        A list containing the filter, source, and target.  # noqa: E501

        :return: The case_statement_items of this CaseStatementDesign.  # noqa: E501
        :rtype: list[luminesce.CaseStatementItem]
        """
        return self._case_statement_items

    @case_statement_items.setter
    def case_statement_items(self, case_statement_items):
        """Sets the case_statement_items of this CaseStatementDesign.

        A list containing the filter, source, and target.  # noqa: E501

        :param case_statement_items: The case_statement_items of this CaseStatementDesign.  # noqa: E501
        :type case_statement_items: list[luminesce.CaseStatementItem]
        """

        self._case_statement_items = case_statement_items

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
        if not isinstance(other, CaseStatementDesign):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CaseStatementDesign):
            return True

        return self.to_dict() != other.to_dict()
