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


class PublicDataPhoto(object):
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
        'owner': 'int',
        'photo': 'str',
        'primary': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'owner': 'owner',
        'photo': 'photo',
        'primary': 'primary'
    }

    def __init__(self, id=None, owner=None, photo=None, primary=None, _configuration=None):  # noqa: E501
        """PublicDataPhoto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._owner = None
        self._photo = None
        self._primary = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if owner is not None:
            self.owner = owner
        if photo is not None:
            self.photo = photo
        if primary is not None:
            self.primary = primary

    @property
    def id(self):
        """Gets the id of this PublicDataPhoto.  # noqa: E501


        :return: The id of this PublicDataPhoto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicDataPhoto.


        :param id: The id of this PublicDataPhoto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def owner(self):
        """Gets the owner of this PublicDataPhoto.  # noqa: E501


        :return: The owner of this PublicDataPhoto.  # noqa: E501
        :rtype: int
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this PublicDataPhoto.


        :param owner: The owner of this PublicDataPhoto.  # noqa: E501
        :type: int
        """

        self._owner = owner

    @property
    def photo(self):
        """Gets the photo of this PublicDataPhoto.  # noqa: E501


        :return: The photo of this PublicDataPhoto.  # noqa: E501
        :rtype: str
        """
        return self._photo

    @photo.setter
    def photo(self, photo):
        """Sets the photo of this PublicDataPhoto.


        :param photo: The photo of this PublicDataPhoto.  # noqa: E501
        :type: str
        """

        self._photo = photo

    @property
    def primary(self):
        """Gets the primary of this PublicDataPhoto.  # noqa: E501


        :return: The primary of this PublicDataPhoto.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this PublicDataPhoto.


        :param primary: The primary of this PublicDataPhoto.  # noqa: E501
        :type: bool
        """

        self._primary = primary

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
        if issubclass(PublicDataPhoto, dict):
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
        if not isinstance(other, PublicDataPhoto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicDataPhoto):
            return True

        return self.to_dict() != other.to_dict()
