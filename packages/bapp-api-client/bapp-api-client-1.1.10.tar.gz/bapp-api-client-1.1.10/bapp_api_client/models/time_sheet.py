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


class TimeSheet(object):
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
        'type': 'str',
        'start_period': 'datetime',
        'end_period': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'start_period': 'start_period',
        'end_period': 'end_period'
    }

    def __init__(self, id=None, type=None, start_period=None, end_period=None, _configuration=None):  # noqa: E501
        """TimeSheet - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._type = None
        self._start_period = None
        self._end_period = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        self.start_period = start_period
        self.end_period = end_period

    @property
    def id(self):
        """Gets the id of this TimeSheet.  # noqa: E501


        :return: The id of this TimeSheet.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimeSheet.


        :param id: The id of this TimeSheet.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this TimeSheet.  # noqa: E501


        :return: The type of this TimeSheet.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TimeSheet.


        :param type: The type of this TimeSheet.  # noqa: E501
        :type: str
        """
        allowed_values = ["P", "Pz", "N", "AM", "CM", "CO", "CFP", "I", "M", "O", "PRB", "PRM", "EV", "DT", "DS"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def start_period(self):
        """Gets the start_period of this TimeSheet.  # noqa: E501


        :return: The start_period of this TimeSheet.  # noqa: E501
        :rtype: datetime
        """
        return self._start_period

    @start_period.setter
    def start_period(self, start_period):
        """Sets the start_period of this TimeSheet.


        :param start_period: The start_period of this TimeSheet.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and start_period is None:
            raise ValueError("Invalid value for `start_period`, must not be `None`")  # noqa: E501

        self._start_period = start_period

    @property
    def end_period(self):
        """Gets the end_period of this TimeSheet.  # noqa: E501


        :return: The end_period of this TimeSheet.  # noqa: E501
        :rtype: datetime
        """
        return self._end_period

    @end_period.setter
    def end_period(self, end_period):
        """Sets the end_period of this TimeSheet.


        :param end_period: The end_period of this TimeSheet.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and end_period is None:
            raise ValueError("Invalid value for `end_period`, must not be `None`")  # noqa: E501

        self._end_period = end_period

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
        if issubclass(TimeSheet, dict):
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
        if not isinstance(other, TimeSheet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeSheet):
            return True

        return self.to_dict() != other.to_dict()
