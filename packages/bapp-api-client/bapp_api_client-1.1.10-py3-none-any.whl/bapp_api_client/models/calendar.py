# coding: utf-8

"""
    BAPP API

    Test description  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@snippets.local
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from bapp_api_client.configuration import Configuration


class Calendar(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'created_at': 'datetime',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'description': 'str',
        'status': 'int',
        'extra': 'object',
        'created_by': 'str',
        'resource': 'int',
        'partner': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'description': 'description',
        'status': 'status',
        'extra': 'extra',
        'created_by': 'created_by',
        'resource': 'resource',
        'partner': 'partner'
    }

    def __init__(self, id=None, created_at=None, start_date=None, end_date=None, description=None, status=None, extra=None, created_by=None, resource=None, partner=None, _configuration=None):  # noqa: E501
        """Calendar - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._created_at = None
        self._start_date = None
        self._end_date = None
        self._description = None
        self._status = None
        self._extra = None
        self._created_by = None
        self._resource = None
        self._partner = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if extra is not None:
            self.extra = extra
        if created_by is not None:
            self.created_by = created_by
        self.resource = resource
        if partner is not None:
            self.partner = partner

    @property
    def id(self):
        """Gets the id of this Calendar.  # noqa: E501


        :return: The id of this Calendar.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Calendar.


        :param id: The id of this Calendar.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this Calendar.  # noqa: E501


        :return: The created_at of this Calendar.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Calendar.


        :param created_at: The created_at of this Calendar.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def start_date(self):
        """Gets the start_date of this Calendar.  # noqa: E501


        :return: The start_date of this Calendar.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Calendar.


        :param start_date: The start_date of this Calendar.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Calendar.  # noqa: E501


        :return: The end_date of this Calendar.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Calendar.


        :param end_date: The end_date of this Calendar.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def description(self):
        """Gets the description of this Calendar.  # noqa: E501


        :return: The description of this Calendar.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Calendar.


        :param description: The description of this Calendar.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this Calendar.  # noqa: E501


        :return: The status of this Calendar.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Calendar.


        :param status: The status of this Calendar.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def extra(self):
        """Gets the extra of this Calendar.  # noqa: E501


        :return: The extra of this Calendar.  # noqa: E501
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this Calendar.


        :param extra: The extra of this Calendar.  # noqa: E501
        :type: object
        """

        self._extra = extra

    @property
    def created_by(self):
        """Gets the created_by of this Calendar.  # noqa: E501


        :return: The created_by of this Calendar.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Calendar.


        :param created_by: The created_by of this Calendar.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def resource(self):
        """Gets the resource of this Calendar.  # noqa: E501


        :return: The resource of this Calendar.  # noqa: E501
        :rtype: int
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Calendar.


        :param resource: The resource of this Calendar.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and resource is None:
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

    @property
    def partner(self):
        """Gets the partner of this Calendar.  # noqa: E501


        :return: The partner of this Calendar.  # noqa: E501
        :rtype: int
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this Calendar.


        :param partner: The partner of this Calendar.  # noqa: E501
        :type: int
        """

        self._partner = partner

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Calendar, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Calendar):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Calendar):
            return True

        return self.to_dict() != other.to_dict()
