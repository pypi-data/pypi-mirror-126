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


class SpecificPartnerPackagePrice(object):
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
        'price': 'str',
        'partner': 'int',
        'package': 'int',
        'currency': 'str'
    }

    attribute_map = {
        'id': 'id',
        'price': 'price',
        'partner': 'partner',
        'package': 'package',
        'currency': 'currency'
    }

    def __init__(self, id=None, price=None, partner=None, package=None, currency=None, _configuration=None):  # noqa: E501
        """SpecificPartnerPackagePrice - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._price = None
        self._partner = None
        self._package = None
        self._currency = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.price = price
        self.partner = partner
        self.package = package
        self.currency = currency

    @property
    def id(self):
        """Gets the id of this SpecificPartnerPackagePrice.  # noqa: E501


        :return: The id of this SpecificPartnerPackagePrice.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SpecificPartnerPackagePrice.


        :param id: The id of this SpecificPartnerPackagePrice.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def price(self):
        """Gets the price of this SpecificPartnerPackagePrice.  # noqa: E501


        :return: The price of this SpecificPartnerPackagePrice.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SpecificPartnerPackagePrice.


        :param price: The price of this SpecificPartnerPackagePrice.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def partner(self):
        """Gets the partner of this SpecificPartnerPackagePrice.  # noqa: E501


        :return: The partner of this SpecificPartnerPackagePrice.  # noqa: E501
        :rtype: int
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this SpecificPartnerPackagePrice.


        :param partner: The partner of this SpecificPartnerPackagePrice.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and partner is None:
            raise ValueError("Invalid value for `partner`, must not be `None`")  # noqa: E501

        self._partner = partner

    @property
    def package(self):
        """Gets the package of this SpecificPartnerPackagePrice.  # noqa: E501


        :return: The package of this SpecificPartnerPackagePrice.  # noqa: E501
        :rtype: int
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this SpecificPartnerPackagePrice.


        :param package: The package of this SpecificPartnerPackagePrice.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and package is None:
            raise ValueError("Invalid value for `package`, must not be `None`")  # noqa: E501

        self._package = package

    @property
    def currency(self):
        """Gets the currency of this SpecificPartnerPackagePrice.  # noqa: E501


        :return: The currency of this SpecificPartnerPackagePrice.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SpecificPartnerPackagePrice.


        :param currency: The currency of this SpecificPartnerPackagePrice.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

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
        if issubclass(SpecificPartnerPackagePrice, dict):
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
        if not isinstance(other, SpecificPartnerPackagePrice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpecificPartnerPackagePrice):
            return True

        return self.to_dict() != other.to_dict()
