# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.14.157
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


class CertificateState(object):
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
        'key': 'str',
        'version': 'int',
        'common_name': 'str',
        'type': 'CertificateType',
        'creation_status': 'CertificateStatus',
        'revocation_status': 'CertificateStatus',
        'validity_start': 'datetime',
        'validity_end': 'datetime',
        'revoked_at': 'datetime',
        'revoked_by': 'str',
        'created_at': 'datetime',
        'created_by': 'str',
        'serial_number': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'key': 'key',
        'version': 'version',
        'common_name': 'commonName',
        'type': 'type',
        'creation_status': 'creationStatus',
        'revocation_status': 'revocationStatus',
        'validity_start': 'validityStart',
        'validity_end': 'validityEnd',
        'revoked_at': 'revokedAt',
        'revoked_by': 'revokedBy',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'serial_number': 'serialNumber',
        'links': 'links'
    }

    required_map = {
        'key': 'optional',
        'version': 'optional',
        'common_name': 'optional',
        'type': 'optional',
        'creation_status': 'optional',
        'revocation_status': 'optional',
        'validity_start': 'optional',
        'validity_end': 'optional',
        'revoked_at': 'optional',
        'revoked_by': 'optional',
        'created_at': 'optional',
        'created_by': 'optional',
        'serial_number': 'optional',
        'links': 'optional'
    }

    def __init__(self, key=None, version=None, common_name=None, type=None, creation_status=None, revocation_status=None, validity_start=None, validity_end=None, revoked_at=None, revoked_by=None, created_at=None, created_by=None, serial_number=None, links=None, local_vars_configuration=None):  # noqa: E501
        """CertificateState - a model defined in OpenAPI"
        
        :param key:  The \"key\" to which this belongs in the dictionary,  basically the CN without any version information
        :type key: str
        :param version:  The version of this certificate
        :type version: int
        :param common_name:  The common Name of the Certificate
        :type common_name: str
        :param type: 
        :type type: luminesce.CertificateType
        :param creation_status: 
        :type creation_status: luminesce.CertificateStatus
        :param revocation_status: 
        :type revocation_status: luminesce.CertificateStatus
        :param validity_start:  The earliest point at which a certificate can be used
        :type validity_start: datetime
        :param validity_end:  The latest point at which a certificate can be used
        :type validity_end: datetime
        :param revoked_at:  The point at which this was revoked, if any
        :type revoked_at: datetime
        :param revoked_by:  The user which revoked this, if any
        :type revoked_by: str
        :param created_at:  The point at which this was created
        :type created_at: datetime
        :param created_by:  The user which created this
        :type created_by: str
        :param serial_number:  The Vault-issued serial number of the certificate, if any - used for revocation
        :type serial_number: str
        :param links:  The location within Configuration Store that this is saved to
        :type links: list[luminesce.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._version = None
        self._common_name = None
        self._type = None
        self._creation_status = None
        self._revocation_status = None
        self._validity_start = None
        self._validity_end = None
        self._revoked_at = None
        self._revoked_by = None
        self._created_at = None
        self._created_by = None
        self._serial_number = None
        self._links = None
        self.discriminator = None

        self.key = key
        if version is not None:
            self.version = version
        self.common_name = common_name
        if type is not None:
            self.type = type
        if creation_status is not None:
            self.creation_status = creation_status
        if revocation_status is not None:
            self.revocation_status = revocation_status
        self.validity_start = validity_start
        self.validity_end = validity_end
        self.revoked_at = revoked_at
        self.revoked_by = revoked_by
        self.created_at = created_at
        self.created_by = created_by
        self.serial_number = serial_number
        self.links = links

    @property
    def key(self):
        """Gets the key of this CertificateState.  # noqa: E501

        The \"key\" to which this belongs in the dictionary,  basically the CN without any version information  # noqa: E501

        :return: The key of this CertificateState.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CertificateState.

        The \"key\" to which this belongs in the dictionary,  basically the CN without any version information  # noqa: E501

        :param key: The key of this CertificateState.  # noqa: E501
        :type key: str
        """

        self._key = key

    @property
    def version(self):
        """Gets the version of this CertificateState.  # noqa: E501

        The version of this certificate  # noqa: E501

        :return: The version of this CertificateState.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CertificateState.

        The version of this certificate  # noqa: E501

        :param version: The version of this CertificateState.  # noqa: E501
        :type version: int
        """

        self._version = version

    @property
    def common_name(self):
        """Gets the common_name of this CertificateState.  # noqa: E501

        The common Name of the Certificate  # noqa: E501

        :return: The common_name of this CertificateState.  # noqa: E501
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this CertificateState.

        The common Name of the Certificate  # noqa: E501

        :param common_name: The common_name of this CertificateState.  # noqa: E501
        :type common_name: str
        """

        self._common_name = common_name

    @property
    def type(self):
        """Gets the type of this CertificateState.  # noqa: E501


        :return: The type of this CertificateState.  # noqa: E501
        :rtype: luminesce.CertificateType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CertificateState.


        :param type: The type of this CertificateState.  # noqa: E501
        :type type: luminesce.CertificateType
        """

        self._type = type

    @property
    def creation_status(self):
        """Gets the creation_status of this CertificateState.  # noqa: E501


        :return: The creation_status of this CertificateState.  # noqa: E501
        :rtype: luminesce.CertificateStatus
        """
        return self._creation_status

    @creation_status.setter
    def creation_status(self, creation_status):
        """Sets the creation_status of this CertificateState.


        :param creation_status: The creation_status of this CertificateState.  # noqa: E501
        :type creation_status: luminesce.CertificateStatus
        """

        self._creation_status = creation_status

    @property
    def revocation_status(self):
        """Gets the revocation_status of this CertificateState.  # noqa: E501


        :return: The revocation_status of this CertificateState.  # noqa: E501
        :rtype: luminesce.CertificateStatus
        """
        return self._revocation_status

    @revocation_status.setter
    def revocation_status(self, revocation_status):
        """Sets the revocation_status of this CertificateState.


        :param revocation_status: The revocation_status of this CertificateState.  # noqa: E501
        :type revocation_status: luminesce.CertificateStatus
        """

        self._revocation_status = revocation_status

    @property
    def validity_start(self):
        """Gets the validity_start of this CertificateState.  # noqa: E501

        The earliest point at which a certificate can be used  # noqa: E501

        :return: The validity_start of this CertificateState.  # noqa: E501
        :rtype: datetime
        """
        return self._validity_start

    @validity_start.setter
    def validity_start(self, validity_start):
        """Sets the validity_start of this CertificateState.

        The earliest point at which a certificate can be used  # noqa: E501

        :param validity_start: The validity_start of this CertificateState.  # noqa: E501
        :type validity_start: datetime
        """

        self._validity_start = validity_start

    @property
    def validity_end(self):
        """Gets the validity_end of this CertificateState.  # noqa: E501

        The latest point at which a certificate can be used  # noqa: E501

        :return: The validity_end of this CertificateState.  # noqa: E501
        :rtype: datetime
        """
        return self._validity_end

    @validity_end.setter
    def validity_end(self, validity_end):
        """Sets the validity_end of this CertificateState.

        The latest point at which a certificate can be used  # noqa: E501

        :param validity_end: The validity_end of this CertificateState.  # noqa: E501
        :type validity_end: datetime
        """

        self._validity_end = validity_end

    @property
    def revoked_at(self):
        """Gets the revoked_at of this CertificateState.  # noqa: E501

        The point at which this was revoked, if any  # noqa: E501

        :return: The revoked_at of this CertificateState.  # noqa: E501
        :rtype: datetime
        """
        return self._revoked_at

    @revoked_at.setter
    def revoked_at(self, revoked_at):
        """Sets the revoked_at of this CertificateState.

        The point at which this was revoked, if any  # noqa: E501

        :param revoked_at: The revoked_at of this CertificateState.  # noqa: E501
        :type revoked_at: datetime
        """

        self._revoked_at = revoked_at

    @property
    def revoked_by(self):
        """Gets the revoked_by of this CertificateState.  # noqa: E501

        The user which revoked this, if any  # noqa: E501

        :return: The revoked_by of this CertificateState.  # noqa: E501
        :rtype: str
        """
        return self._revoked_by

    @revoked_by.setter
    def revoked_by(self, revoked_by):
        """Sets the revoked_by of this CertificateState.

        The user which revoked this, if any  # noqa: E501

        :param revoked_by: The revoked_by of this CertificateState.  # noqa: E501
        :type revoked_by: str
        """

        self._revoked_by = revoked_by

    @property
    def created_at(self):
        """Gets the created_at of this CertificateState.  # noqa: E501

        The point at which this was created  # noqa: E501

        :return: The created_at of this CertificateState.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CertificateState.

        The point at which this was created  # noqa: E501

        :param created_at: The created_at of this CertificateState.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this CertificateState.  # noqa: E501

        The user which created this  # noqa: E501

        :return: The created_by of this CertificateState.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CertificateState.

        The user which created this  # noqa: E501

        :param created_by: The created_by of this CertificateState.  # noqa: E501
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def serial_number(self):
        """Gets the serial_number of this CertificateState.  # noqa: E501

        The Vault-issued serial number of the certificate, if any - used for revocation  # noqa: E501

        :return: The serial_number of this CertificateState.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this CertificateState.

        The Vault-issued serial number of the certificate, if any - used for revocation  # noqa: E501

        :param serial_number: The serial_number of this CertificateState.  # noqa: E501
        :type serial_number: str
        """

        self._serial_number = serial_number

    @property
    def links(self):
        """Gets the links of this CertificateState.  # noqa: E501

        The location within Configuration Store that this is saved to  # noqa: E501

        :return: The links of this CertificateState.  # noqa: E501
        :rtype: list[luminesce.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CertificateState.

        The location within Configuration Store that this is saved to  # noqa: E501

        :param links: The links of this CertificateState.  # noqa: E501
        :type links: list[luminesce.Link]
        """

        self._links = links

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
        if not isinstance(other, CertificateState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CertificateState):
            return True

        return self.to_dict() != other.to_dict()