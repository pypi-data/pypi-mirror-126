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


class PartnerContact(object):
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
        'partner': 'int',
        'bapp_user': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'position': 'str',
        'phone': 'str',
        'primary': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'partner': 'partner',
        'bapp_user': 'bapp_user',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'position': 'position',
        'phone': 'phone',
        'primary': 'primary'
    }

    def __init__(self, id=None, partner=None, bapp_user=None, first_name=None, last_name=None, email=None, position=None, phone=None, primary=None, _configuration=None):  # noqa: E501
        """PartnerContact - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._partner = None
        self._bapp_user = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._position = None
        self._phone = None
        self._primary = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.partner = partner
        if bapp_user is not None:
            self.bapp_user = bapp_user
        self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        self.email = email
        self.position = position
        if phone is not None:
            self.phone = phone
        if primary is not None:
            self.primary = primary

    @property
    def id(self):
        """Gets the id of this PartnerContact.  # noqa: E501


        :return: The id of this PartnerContact.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PartnerContact.


        :param id: The id of this PartnerContact.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def partner(self):
        """Gets the partner of this PartnerContact.  # noqa: E501


        :return: The partner of this PartnerContact.  # noqa: E501
        :rtype: int
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this PartnerContact.


        :param partner: The partner of this PartnerContact.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and partner is None:
            raise ValueError("Invalid value for `partner`, must not be `None`")  # noqa: E501

        self._partner = partner

    @property
    def bapp_user(self):
        """Gets the bapp_user of this PartnerContact.  # noqa: E501

        Utilizatorul Bapp conectat la acest partener  # noqa: E501

        :return: The bapp_user of this PartnerContact.  # noqa: E501
        :rtype: str
        """
        return self._bapp_user

    @bapp_user.setter
    def bapp_user(self, bapp_user):
        """Sets the bapp_user of this PartnerContact.

        Utilizatorul Bapp conectat la acest partener  # noqa: E501

        :param bapp_user: The bapp_user of this PartnerContact.  # noqa: E501
        :type: str
        """

        self._bapp_user = bapp_user

    @property
    def first_name(self):
        """Gets the first_name of this PartnerContact.  # noqa: E501


        :return: The first_name of this PartnerContact.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PartnerContact.


        :param first_name: The first_name of this PartnerContact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                first_name is not None and len(first_name) > 100):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                first_name is not None and len(first_name) < 1):
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this PartnerContact.  # noqa: E501


        :return: The last_name of this PartnerContact.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PartnerContact.


        :param last_name: The last_name of this PartnerContact.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                last_name is not None and len(last_name) > 100):
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                last_name is not None and len(last_name) < 1):
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this PartnerContact.  # noqa: E501


        :return: The email of this PartnerContact.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PartnerContact.


        :param email: The email of this PartnerContact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                email is not None and len(email) > 254):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501
        if (self._configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def position(self):
        """Gets the position of this PartnerContact.  # noqa: E501


        :return: The position of this PartnerContact.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PartnerContact.


        :param position: The position of this PartnerContact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                position is not None and len(position) > 200):
            raise ValueError("Invalid value for `position`, length must be less than or equal to `200`")  # noqa: E501
        if (self._configuration.client_side_validation and
                position is not None and len(position) < 1):
            raise ValueError("Invalid value for `position`, length must be greater than or equal to `1`")  # noqa: E501

        self._position = position

    @property
    def phone(self):
        """Gets the phone of this PartnerContact.  # noqa: E501


        :return: The phone of this PartnerContact.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PartnerContact.


        :param phone: The phone of this PartnerContact.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                phone is not None and len(phone) > 200):
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `200`")  # noqa: E501

        self._phone = phone

    @property
    def primary(self):
        """Gets the primary of this PartnerContact.  # noqa: E501


        :return: The primary of this PartnerContact.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this PartnerContact.


        :param primary: The primary of this PartnerContact.  # noqa: E501
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
        if issubclass(PartnerContact, dict):
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
        if not isinstance(other, PartnerContact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartnerContact):
            return True

        return self.to_dict() != other.to_dict()
