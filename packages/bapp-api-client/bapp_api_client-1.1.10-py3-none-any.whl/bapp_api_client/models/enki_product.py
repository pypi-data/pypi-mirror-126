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


class EnkiProduct(object):
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
        'partner_product': 'int',
        'partner': 'int',
        'category': 'int'
    }

    attribute_map = {
        'id': 'id',
        'partner_product': 'partner_product',
        'partner': 'partner',
        'category': 'category'
    }

    def __init__(self, id=None, partner_product=None, partner=None, category=None, _configuration=None):  # noqa: E501
        """EnkiProduct - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._partner_product = None
        self._partner = None
        self._category = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.partner_product = partner_product
        self.partner = partner
        self.category = category

    @property
    def id(self):
        """Gets the id of this EnkiProduct.  # noqa: E501


        :return: The id of this EnkiProduct.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnkiProduct.


        :param id: The id of this EnkiProduct.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def partner_product(self):
        """Gets the partner_product of this EnkiProduct.  # noqa: E501


        :return: The partner_product of this EnkiProduct.  # noqa: E501
        :rtype: int
        """
        return self._partner_product

    @partner_product.setter
    def partner_product(self, partner_product):
        """Sets the partner_product of this EnkiProduct.


        :param partner_product: The partner_product of this EnkiProduct.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and partner_product is None:
            raise ValueError("Invalid value for `partner_product`, must not be `None`")  # noqa: E501

        self._partner_product = partner_product

    @property
    def partner(self):
        """Gets the partner of this EnkiProduct.  # noqa: E501


        :return: The partner of this EnkiProduct.  # noqa: E501
        :rtype: int
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this EnkiProduct.


        :param partner: The partner of this EnkiProduct.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and partner is None:
            raise ValueError("Invalid value for `partner`, must not be `None`")  # noqa: E501

        self._partner = partner

    @property
    def category(self):
        """Gets the category of this EnkiProduct.  # noqa: E501


        :return: The category of this EnkiProduct.  # noqa: E501
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this EnkiProduct.


        :param category: The category of this EnkiProduct.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

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
        if issubclass(EnkiProduct, dict):
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
        if not isinstance(other, EnkiProduct):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnkiProduct):
            return True

        return self.to_dict() != other.to_dict()
