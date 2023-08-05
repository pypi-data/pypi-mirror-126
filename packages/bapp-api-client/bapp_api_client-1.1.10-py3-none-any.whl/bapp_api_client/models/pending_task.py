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


class PendingTask(object):
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
        'name': 'str',
        'file': 'str',
        'expires': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'file': 'file',
        'expires': 'expires'
    }

    def __init__(self, name=None, file=None, expires=None, _configuration=None):  # noqa: E501
        """PendingTask - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._file = None
        self._expires = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if file is not None:
            self.file = file
        self.expires = expires

    @property
    def name(self):
        """Gets the name of this PendingTask.  # noqa: E501


        :return: The name of this PendingTask.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PendingTask.


        :param name: The name of this PendingTask.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 200):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501

        self._name = name

    @property
    def file(self):
        """Gets the file of this PendingTask.  # noqa: E501


        :return: The file of this PendingTask.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this PendingTask.


        :param file: The file of this PendingTask.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def expires(self):
        """Gets the expires of this PendingTask.  # noqa: E501


        :return: The expires of this PendingTask.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this PendingTask.


        :param expires: The expires of this PendingTask.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and expires is None:
            raise ValueError("Invalid value for `expires`, must not be `None`")  # noqa: E501

        self._expires = expires

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
        if issubclass(PendingTask, dict):
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
        if not isinstance(other, PendingTask):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PendingTask):
            return True

        return self.to_dict() != other.to_dict()
