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


class StockValue(object):
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
        'stock': 'int',
        'product': 'int',
        'qty': 'str',
        'reserved': 'int'
    }

    attribute_map = {
        'id': 'id',
        'stock': 'stock',
        'product': 'product',
        'qty': 'qty',
        'reserved': 'reserved'
    }

    def __init__(self, id=None, stock=None, product=None, qty=None, reserved=None, _configuration=None):  # noqa: E501
        """StockValue - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._stock = None
        self._product = None
        self._qty = None
        self._reserved = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.stock = stock
        self.product = product
        if qty is not None:
            self.qty = qty
        if reserved is not None:
            self.reserved = reserved

    @property
    def id(self):
        """Gets the id of this StockValue.  # noqa: E501


        :return: The id of this StockValue.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StockValue.


        :param id: The id of this StockValue.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def stock(self):
        """Gets the stock of this StockValue.  # noqa: E501


        :return: The stock of this StockValue.  # noqa: E501
        :rtype: int
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this StockValue.


        :param stock: The stock of this StockValue.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and stock is None:
            raise ValueError("Invalid value for `stock`, must not be `None`")  # noqa: E501

        self._stock = stock

    @property
    def product(self):
        """Gets the product of this StockValue.  # noqa: E501


        :return: The product of this StockValue.  # noqa: E501
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this StockValue.


        :param product: The product of this StockValue.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and product is None:
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

    @property
    def qty(self):
        """Gets the qty of this StockValue.  # noqa: E501


        :return: The qty of this StockValue.  # noqa: E501
        :rtype: str
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this StockValue.


        :param qty: The qty of this StockValue.  # noqa: E501
        :type: str
        """

        self._qty = qty

    @property
    def reserved(self):
        """Gets the reserved of this StockValue.  # noqa: E501


        :return: The reserved of this StockValue.  # noqa: E501
        :rtype: int
        """
        return self._reserved

    @reserved.setter
    def reserved(self, reserved):
        """Sets the reserved of this StockValue.


        :param reserved: The reserved of this StockValue.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                reserved is not None and reserved > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `reserved`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                reserved is not None and reserved < 0):  # noqa: E501
            raise ValueError("Invalid value for `reserved`, must be a value greater than or equal to `0`")  # noqa: E501

        self._reserved = reserved

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
        if issubclass(StockValue, dict):
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
        if not isinstance(other, StockValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StockValue):
            return True

        return self.to_dict() != other.to_dict()
