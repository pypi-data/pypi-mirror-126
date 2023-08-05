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


class UserTicketMessage(object):
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
        'title': 'str',
        'message': 'str',
        'employee': 'int',
        'created_at': 'datetime',
        'modified_at': 'datetime',
        'created_by': 'str',
        'files': 'list[str]',
        'attachments': 'str',
        'close_ticket': 'bool',
        'can_edit': 'str',
        'can_delete_before': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'message': 'message',
        'employee': 'employee',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'created_by': 'created_by',
        'files': 'files',
        'attachments': 'attachments',
        'close_ticket': 'close_ticket',
        'can_edit': 'can_edit',
        'can_delete_before': 'can_delete_before'
    }

    def __init__(self, id=None, title=None, message=None, employee=None, created_at=None, modified_at=None, created_by=None, files=None, attachments=None, close_ticket=None, can_edit=None, can_delete_before=None, _configuration=None):  # noqa: E501
        """UserTicketMessage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._title = None
        self._message = None
        self._employee = None
        self._created_at = None
        self._modified_at = None
        self._created_by = None
        self._files = None
        self._attachments = None
        self._close_ticket = None
        self._can_edit = None
        self._can_delete_before = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        self.message = message
        if employee is not None:
            self.employee = employee
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if created_by is not None:
            self.created_by = created_by
        if files is not None:
            self.files = files
        if attachments is not None:
            self.attachments = attachments
        if close_ticket is not None:
            self.close_ticket = close_ticket
        if can_edit is not None:
            self.can_edit = can_edit
        if can_delete_before is not None:
            self.can_delete_before = can_delete_before

    @property
    def id(self):
        """Gets the id of this UserTicketMessage.  # noqa: E501


        :return: The id of this UserTicketMessage.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserTicketMessage.


        :param id: The id of this UserTicketMessage.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this UserTicketMessage.  # noqa: E501


        :return: The title of this UserTicketMessage.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserTicketMessage.


        :param title: The title of this UserTicketMessage.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                title is not None and len(title) > 200):
            raise ValueError("Invalid value for `title`, length must be less than or equal to `200`")  # noqa: E501

        self._title = title

    @property
    def message(self):
        """Gets the message of this UserTicketMessage.  # noqa: E501


        :return: The message of this UserTicketMessage.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this UserTicketMessage.


        :param message: The message of this UserTicketMessage.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                message is not None and len(message) < 1):
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `1`")  # noqa: E501

        self._message = message

    @property
    def employee(self):
        """Gets the employee of this UserTicketMessage.  # noqa: E501


        :return: The employee of this UserTicketMessage.  # noqa: E501
        :rtype: int
        """
        return self._employee

    @employee.setter
    def employee(self, employee):
        """Sets the employee of this UserTicketMessage.


        :param employee: The employee of this UserTicketMessage.  # noqa: E501
        :type: int
        """

        self._employee = employee

    @property
    def created_at(self):
        """Gets the created_at of this UserTicketMessage.  # noqa: E501

        Date and time at which this record was added  # noqa: E501

        :return: The created_at of this UserTicketMessage.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserTicketMessage.

        Date and time at which this record was added  # noqa: E501

        :param created_at: The created_at of this UserTicketMessage.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this UserTicketMessage.  # noqa: E501

        Date and time at which this record was modified  # noqa: E501

        :return: The modified_at of this UserTicketMessage.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this UserTicketMessage.

        Date and time at which this record was modified  # noqa: E501

        :param modified_at: The modified_at of this UserTicketMessage.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def created_by(self):
        """Gets the created_by of this UserTicketMessage.  # noqa: E501


        :return: The created_by of this UserTicketMessage.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this UserTicketMessage.


        :param created_by: The created_by of this UserTicketMessage.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def files(self):
        """Gets the files of this UserTicketMessage.  # noqa: E501

          # noqa: E501

        :return: The files of this UserTicketMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this UserTicketMessage.

          # noqa: E501

        :param files: The files of this UserTicketMessage.  # noqa: E501
        :type: list[str]
        """

        self._files = files

    @property
    def attachments(self):
        """Gets the attachments of this UserTicketMessage.  # noqa: E501


        :return: The attachments of this UserTicketMessage.  # noqa: E501
        :rtype: str
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this UserTicketMessage.


        :param attachments: The attachments of this UserTicketMessage.  # noqa: E501
        :type: str
        """

        self._attachments = attachments

    @property
    def close_ticket(self):
        """Gets the close_ticket of this UserTicketMessage.  # noqa: E501


        :return: The close_ticket of this UserTicketMessage.  # noqa: E501
        :rtype: bool
        """
        return self._close_ticket

    @close_ticket.setter
    def close_ticket(self, close_ticket):
        """Sets the close_ticket of this UserTicketMessage.


        :param close_ticket: The close_ticket of this UserTicketMessage.  # noqa: E501
        :type: bool
        """

        self._close_ticket = close_ticket

    @property
    def can_edit(self):
        """Gets the can_edit of this UserTicketMessage.  # noqa: E501


        :return: The can_edit of this UserTicketMessage.  # noqa: E501
        :rtype: str
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        """Sets the can_edit of this UserTicketMessage.


        :param can_edit: The can_edit of this UserTicketMessage.  # noqa: E501
        :type: str
        """

        self._can_edit = can_edit

    @property
    def can_delete_before(self):
        """Gets the can_delete_before of this UserTicketMessage.  # noqa: E501


        :return: The can_delete_before of this UserTicketMessage.  # noqa: E501
        :rtype: str
        """
        return self._can_delete_before

    @can_delete_before.setter
    def can_delete_before(self, can_delete_before):
        """Sets the can_delete_before of this UserTicketMessage.


        :param can_delete_before: The can_delete_before of this UserTicketMessage.  # noqa: E501
        :type: str
        """

        self._can_delete_before = can_delete_before

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
        if issubclass(UserTicketMessage, dict):
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
        if not isinstance(other, UserTicketMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserTicketMessage):
            return True

        return self.to_dict() != other.to_dict()
