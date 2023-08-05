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


class EmailAlias(object):
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
        'employee_email': 'str'
    }

    attribute_map = {
        'employee_email': 'employee_email'
    }

    def __init__(self, employee_email=None, _configuration=None):  # noqa: E501
        """EmailAlias - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._employee_email = None
        self.discriminator = None

        if employee_email is not None:
            self.employee_email = employee_email

    @property
    def employee_email(self):
        """Gets the employee_email of this EmailAlias.  # noqa: E501


        :return: The employee_email of this EmailAlias.  # noqa: E501
        :rtype: str
        """
        return self._employee_email

    @employee_email.setter
    def employee_email(self, employee_email):
        """Sets the employee_email of this EmailAlias.


        :param employee_email: The employee_email of this EmailAlias.  # noqa: E501
        :type: str
        """

        self._employee_email = employee_email

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
        if issubclass(EmailAlias, dict):
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
        if not isinstance(other, EmailAlias):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailAlias):
            return True

        return self.to_dict() != other.to_dict()
