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


class Partner(object):
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
        'name': 'str',
        'vat_id': 'str',
        'reg_com': 'str',
        'sale_discount': 'str',
        'purchase_discount': 'str',
        'sale_due_days': 'int',
        'purchase_due_days': 'int',
        'is_company': 'bool',
        'country': 'str',
        'region': 'int',
        'city': 'int',
        'address': 'str',
        'supplier': 'bool',
        'email': 'str',
        'phone': 'str',
        'data_access': 'list[str]',
        'connected_company': 'str',
        'agent': 'str',
        'bank': 'str',
        'iban': 'str',
        'former_partner_id': 'int',
        'balance_data': 'str',
        'markup': 'str',
        'category': 'int',
        'pays_vat': 'bool',
        'bapp_company_id': 'str',
        'related_partner': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vat_id': 'vat_id',
        'reg_com': 'reg_com',
        'sale_discount': 'sale_discount',
        'purchase_discount': 'purchase_discount',
        'sale_due_days': 'sale_due_days',
        'purchase_due_days': 'purchase_due_days',
        'is_company': 'is_company',
        'country': 'country',
        'region': 'region',
        'city': 'city',
        'address': 'address',
        'supplier': 'supplier',
        'email': 'email',
        'phone': 'phone',
        'data_access': 'data_access',
        'connected_company': 'connected_company',
        'agent': 'agent',
        'bank': 'bank',
        'iban': 'iban',
        'former_partner_id': 'former_partner_id',
        'balance_data': 'balance_data',
        'markup': 'markup',
        'category': 'category',
        'pays_vat': 'pays_vat',
        'bapp_company_id': 'bapp_company_id',
        'related_partner': 'related_partner'
    }

    def __init__(self, id=None, name=None, vat_id=None, reg_com=None, sale_discount=None, purchase_discount=None, sale_due_days=None, purchase_due_days=None, is_company=None, country=None, region=None, city=None, address=None, supplier=None, email=None, phone=None, data_access=None, connected_company=None, agent=None, bank=None, iban=None, former_partner_id=None, balance_data=None, markup=None, category=None, pays_vat=None, bapp_company_id=None, related_partner=None, _configuration=None):  # noqa: E501
        """Partner - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._vat_id = None
        self._reg_com = None
        self._sale_discount = None
        self._purchase_discount = None
        self._sale_due_days = None
        self._purchase_due_days = None
        self._is_company = None
        self._country = None
        self._region = None
        self._city = None
        self._address = None
        self._supplier = None
        self._email = None
        self._phone = None
        self._data_access = None
        self._connected_company = None
        self._agent = None
        self._bank = None
        self._iban = None
        self._former_partner_id = None
        self._balance_data = None
        self._markup = None
        self._category = None
        self._pays_vat = None
        self._bapp_company_id = None
        self._related_partner = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if vat_id is not None:
            self.vat_id = vat_id
        if reg_com is not None:
            self.reg_com = reg_com
        if sale_discount is not None:
            self.sale_discount = sale_discount
        if purchase_discount is not None:
            self.purchase_discount = purchase_discount
        if sale_due_days is not None:
            self.sale_due_days = sale_due_days
        if purchase_due_days is not None:
            self.purchase_due_days = purchase_due_days
        if is_company is not None:
            self.is_company = is_company
        self.country = country
        if region is not None:
            self.region = region
        if city is not None:
            self.city = city
        self.address = address
        if supplier is not None:
            self.supplier = supplier
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if data_access is not None:
            self.data_access = data_access
        if connected_company is not None:
            self.connected_company = connected_company
        if agent is not None:
            self.agent = agent
        if bank is not None:
            self.bank = bank
        if iban is not None:
            self.iban = iban
        if former_partner_id is not None:
            self.former_partner_id = former_partner_id
        if balance_data is not None:
            self.balance_data = balance_data
        if markup is not None:
            self.markup = markup
        if category is not None:
            self.category = category
        if pays_vat is not None:
            self.pays_vat = pays_vat
        if bapp_company_id is not None:
            self.bapp_company_id = bapp_company_id
        if related_partner is not None:
            self.related_partner = related_partner

    @property
    def id(self):
        """Gets the id of this Partner.  # noqa: E501


        :return: The id of this Partner.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Partner.


        :param id: The id of this Partner.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Partner.  # noqa: E501


        :return: The name of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Partner.


        :param name: The name of this Partner.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 200):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def vat_id(self):
        """Gets the vat_id of this Partner.  # noqa: E501


        :return: The vat_id of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._vat_id

    @vat_id.setter
    def vat_id(self, vat_id):
        """Sets the vat_id of this Partner.


        :param vat_id: The vat_id of this Partner.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                vat_id is not None and len(vat_id) > 60):
            raise ValueError("Invalid value for `vat_id`, length must be less than or equal to `60`")  # noqa: E501

        self._vat_id = vat_id

    @property
    def reg_com(self):
        """Gets the reg_com of this Partner.  # noqa: E501


        :return: The reg_com of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._reg_com

    @reg_com.setter
    def reg_com(self, reg_com):
        """Sets the reg_com of this Partner.


        :param reg_com: The reg_com of this Partner.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                reg_com is not None and len(reg_com) > 60):
            raise ValueError("Invalid value for `reg_com`, length must be less than or equal to `60`")  # noqa: E501

        self._reg_com = reg_com

    @property
    def sale_discount(self):
        """Gets the sale_discount of this Partner.  # noqa: E501

        Reducere oferită acestui partener la cumpărarea de la dvs.  # noqa: E501

        :return: The sale_discount of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._sale_discount

    @sale_discount.setter
    def sale_discount(self, sale_discount):
        """Sets the sale_discount of this Partner.

        Reducere oferită acestui partener la cumpărarea de la dvs.  # noqa: E501

        :param sale_discount: The sale_discount of this Partner.  # noqa: E501
        :type: str
        """

        self._sale_discount = sale_discount

    @property
    def purchase_discount(self):
        """Gets the purchase_discount of this Partner.  # noqa: E501

        Reducere oferită de acest partener atunci când cumpărați de la el.  # noqa: E501

        :return: The purchase_discount of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._purchase_discount

    @purchase_discount.setter
    def purchase_discount(self, purchase_discount):
        """Sets the purchase_discount of this Partner.

        Reducere oferită de acest partener atunci când cumpărați de la el.  # noqa: E501

        :param purchase_discount: The purchase_discount of this Partner.  # noqa: E501
        :type: str
        """

        self._purchase_discount = purchase_discount

    @property
    def sale_due_days(self):
        """Gets the sale_due_days of this Partner.  # noqa: E501

        Termenul limită pentru plățile oferite de dvs. către acest partener.  # noqa: E501

        :return: The sale_due_days of this Partner.  # noqa: E501
        :rtype: int
        """
        return self._sale_due_days

    @sale_due_days.setter
    def sale_due_days(self, sale_due_days):
        """Sets the sale_due_days of this Partner.

        Termenul limită pentru plățile oferite de dvs. către acest partener.  # noqa: E501

        :param sale_due_days: The sale_due_days of this Partner.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                sale_due_days is not None and sale_due_days > 32767):  # noqa: E501
            raise ValueError("Invalid value for `sale_due_days`, must be a value less than or equal to `32767`")  # noqa: E501
        if (self._configuration.client_side_validation and
                sale_due_days is not None and sale_due_days < 0):  # noqa: E501
            raise ValueError("Invalid value for `sale_due_days`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sale_due_days = sale_due_days

    @property
    def purchase_due_days(self):
        """Gets the purchase_due_days of this Partner.  # noqa: E501

        Termenul limită pentru plățile oferite de acest partener.  # noqa: E501

        :return: The purchase_due_days of this Partner.  # noqa: E501
        :rtype: int
        """
        return self._purchase_due_days

    @purchase_due_days.setter
    def purchase_due_days(self, purchase_due_days):
        """Sets the purchase_due_days of this Partner.

        Termenul limită pentru plățile oferite de acest partener.  # noqa: E501

        :param purchase_due_days: The purchase_due_days of this Partner.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                purchase_due_days is not None and purchase_due_days > 32767):  # noqa: E501
            raise ValueError("Invalid value for `purchase_due_days`, must be a value less than or equal to `32767`")  # noqa: E501
        if (self._configuration.client_side_validation and
                purchase_due_days is not None and purchase_due_days < 0):  # noqa: E501
            raise ValueError("Invalid value for `purchase_due_days`, must be a value greater than or equal to `0`")  # noqa: E501

        self._purchase_due_days = purchase_due_days

    @property
    def is_company(self):
        """Gets the is_company of this Partner.  # noqa: E501


        :return: The is_company of this Partner.  # noqa: E501
        :rtype: bool
        """
        return self._is_company

    @is_company.setter
    def is_company(self, is_company):
        """Sets the is_company of this Partner.


        :param is_company: The is_company of this Partner.  # noqa: E501
        :type: bool
        """

        self._is_company = is_company

    @property
    def country(self):
        """Gets the country of this Partner.  # noqa: E501


        :return: The country of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Partner.


        :param country: The country of this Partner.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def region(self):
        """Gets the region of this Partner.  # noqa: E501


        :return: The region of this Partner.  # noqa: E501
        :rtype: int
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Partner.


        :param region: The region of this Partner.  # noqa: E501
        :type: int
        """

        self._region = region

    @property
    def city(self):
        """Gets the city of this Partner.  # noqa: E501


        :return: The city of this Partner.  # noqa: E501
        :rtype: int
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Partner.


        :param city: The city of this Partner.  # noqa: E501
        :type: int
        """

        self._city = city

    @property
    def address(self):
        """Gets the address of this Partner.  # noqa: E501


        :return: The address of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Partner.


        :param address: The address of this Partner.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                address is not None and len(address) > 200):
            raise ValueError("Invalid value for `address`, length must be less than or equal to `200`")  # noqa: E501
        if (self._configuration.client_side_validation and
                address is not None and len(address) < 1):
            raise ValueError("Invalid value for `address`, length must be greater than or equal to `1`")  # noqa: E501

        self._address = address

    @property
    def supplier(self):
        """Gets the supplier of this Partner.  # noqa: E501


        :return: The supplier of this Partner.  # noqa: E501
        :rtype: bool
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this Partner.


        :param supplier: The supplier of this Partner.  # noqa: E501
        :type: bool
        """

        self._supplier = supplier

    @property
    def email(self):
        """Gets the email of this Partner.  # noqa: E501


        :return: The email of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Partner.


        :param email: The email of this Partner.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                email is not None and len(email) > 254):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this Partner.  # noqa: E501


        :return: The phone of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Partner.


        :param phone: The phone of this Partner.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                phone is not None and len(phone) > 200):
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `200`")  # noqa: E501

        self._phone = phone

    @property
    def data_access(self):
        """Gets the data_access of this Partner.  # noqa: E501


        :return: The data_access of this Partner.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_access

    @data_access.setter
    def data_access(self, data_access):
        """Sets the data_access of this Partner.


        :param data_access: The data_access of this Partner.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["0", "1", "2", "3"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(data_access).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `data_access` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(data_access) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._data_access = data_access

    @property
    def connected_company(self):
        """Gets the connected_company of this Partner.  # noqa: E501


        :return: The connected_company of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._connected_company

    @connected_company.setter
    def connected_company(self, connected_company):
        """Sets the connected_company of this Partner.


        :param connected_company: The connected_company of this Partner.  # noqa: E501
        :type: str
        """

        self._connected_company = connected_company

    @property
    def agent(self):
        """Gets the agent of this Partner.  # noqa: E501


        :return: The agent of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this Partner.


        :param agent: The agent of this Partner.  # noqa: E501
        :type: str
        """

        self._agent = agent

    @property
    def bank(self):
        """Gets the bank of this Partner.  # noqa: E501


        :return: The bank of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """Sets the bank of this Partner.


        :param bank: The bank of this Partner.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                bank is not None and len(bank) > 100):
            raise ValueError("Invalid value for `bank`, length must be less than or equal to `100`")  # noqa: E501

        self._bank = bank

    @property
    def iban(self):
        """Gets the iban of this Partner.  # noqa: E501


        :return: The iban of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this Partner.


        :param iban: The iban of this Partner.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                iban is not None and len(iban) > 29):
            raise ValueError("Invalid value for `iban`, length must be less than or equal to `29`")  # noqa: E501

        self._iban = iban

    @property
    def former_partner_id(self):
        """Gets the former_partner_id of this Partner.  # noqa: E501


        :return: The former_partner_id of this Partner.  # noqa: E501
        :rtype: int
        """
        return self._former_partner_id

    @former_partner_id.setter
    def former_partner_id(self, former_partner_id):
        """Sets the former_partner_id of this Partner.


        :param former_partner_id: The former_partner_id of this Partner.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                former_partner_id is not None and former_partner_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `former_partner_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                former_partner_id is not None and former_partner_id < 0):  # noqa: E501
            raise ValueError("Invalid value for `former_partner_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._former_partner_id = former_partner_id

    @property
    def balance_data(self):
        """Gets the balance_data of this Partner.  # noqa: E501


        :return: The balance_data of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._balance_data

    @balance_data.setter
    def balance_data(self, balance_data):
        """Sets the balance_data of this Partner.


        :param balance_data: The balance_data of this Partner.  # noqa: E501
        :type: str
        """

        self._balance_data = balance_data

    @property
    def markup(self):
        """Gets the markup of this Partner.  # noqa: E501

        Adaos la pretul de baza al produsului impus acestui partener.  # noqa: E501

        :return: The markup of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._markup

    @markup.setter
    def markup(self, markup):
        """Sets the markup of this Partner.

        Adaos la pretul de baza al produsului impus acestui partener.  # noqa: E501

        :param markup: The markup of this Partner.  # noqa: E501
        :type: str
        """

        self._markup = markup

    @property
    def category(self):
        """Gets the category of this Partner.  # noqa: E501


        :return: The category of this Partner.  # noqa: E501
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Partner.


        :param category: The category of this Partner.  # noqa: E501
        :type: int
        """

        self._category = category

    @property
    def pays_vat(self):
        """Gets the pays_vat of this Partner.  # noqa: E501


        :return: The pays_vat of this Partner.  # noqa: E501
        :rtype: bool
        """
        return self._pays_vat

    @pays_vat.setter
    def pays_vat(self, pays_vat):
        """Sets the pays_vat of this Partner.


        :param pays_vat: The pays_vat of this Partner.  # noqa: E501
        :type: bool
        """

        self._pays_vat = pays_vat

    @property
    def bapp_company_id(self):
        """Gets the bapp_company_id of this Partner.  # noqa: E501


        :return: The bapp_company_id of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._bapp_company_id

    @bapp_company_id.setter
    def bapp_company_id(self, bapp_company_id):
        """Sets the bapp_company_id of this Partner.


        :param bapp_company_id: The bapp_company_id of this Partner.  # noqa: E501
        :type: str
        """

        self._bapp_company_id = bapp_company_id

    @property
    def related_partner(self):
        """Gets the related_partner of this Partner.  # noqa: E501


        :return: The related_partner of this Partner.  # noqa: E501
        :rtype: int
        """
        return self._related_partner

    @related_partner.setter
    def related_partner(self, related_partner):
        """Sets the related_partner of this Partner.


        :param related_partner: The related_partner of this Partner.  # noqa: E501
        :type: int
        """

        self._related_partner = related_partner

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
        if issubclass(Partner, dict):
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
        if not isinstance(other, Partner):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Partner):
            return True

        return self.to_dict() != other.to_dict()
