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


class InlineResponse20012(object):
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
        'task_id': 'str',
        'progress_type': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'progress_type': 'progress_type'
    }

    def __init__(self, task_id=None, progress_type=None, _configuration=None):  # noqa: E501
        """InlineResponse20012 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._task_id = None
        self._progress_type = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if progress_type is not None:
            self.progress_type = progress_type

    @property
    def task_id(self):
        """Gets the task_id of this InlineResponse20012.  # noqa: E501


        :return: The task_id of this InlineResponse20012.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this InlineResponse20012.


        :param task_id: The task_id of this InlineResponse20012.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def progress_type(self):
        """Gets the progress_type of this InlineResponse20012.  # noqa: E501


        :return: The progress_type of this InlineResponse20012.  # noqa: E501
        :rtype: str
        """
        return self._progress_type

    @progress_type.setter
    def progress_type(self, progress_type):
        """Sets the progress_type of this InlineResponse20012.


        :param progress_type: The progress_type of this InlineResponse20012.  # noqa: E501
        :type: str
        """
        allowed_values = ["percentage", "start_finish"]  # noqa: E501
        if (self._configuration.client_side_validation and
                progress_type not in allowed_values):
            raise ValueError(
                "Invalid value for `progress_type` ({0}), must be one of {1}"  # noqa: E501
                .format(progress_type, allowed_values)
            )

        self._progress_type = progress_type

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
        if issubclass(InlineResponse20012, dict):
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
        if not isinstance(other, InlineResponse20012):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20012):
            return True

        return self.to_dict() != other.to_dict()
