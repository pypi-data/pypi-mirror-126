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


class Order(object):
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
        'currency': 'str',
        'language': 'str',
        'source': 'int',
        'source_text': 'str',
        'delivery_type': 'int',
        'delivered_by': 'str',
        'delivery_identifier': 'str',
        'delivery_date': 'datetime',
        'delivery_country': 'str',
        'delivery_region': 'int',
        'delivery_city': 'int',
        'delivery_address': 'str',
        'specific_date_time_requested': 'datetime',
        '_date': 'date',
        'exchange_rate': 'str',
        'payment_type': 'int',
        'discount': 'str',
        'uuid': 'str',
        'number': 'str',
        'status': 'int',
        'subtotal': 'str',
        'tax_value': 'str',
        'total': 'str',
        'discounted_total': 'str',
        'subtotal_currency': 'str',
        'tax_value_currency': 'str',
        'total_currency': 'str',
        'discounted_total_currency': 'str',
        'extra': 'object',
        'items': 'list[OrderItemModel]',
        'created_by': 'str',
        'modified_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'partner': 'partner',
        'currency': 'currency',
        'language': 'language',
        'source': 'source',
        'source_text': 'source_text',
        'delivery_type': 'delivery_type',
        'delivered_by': 'delivered_by',
        'delivery_identifier': 'delivery_identifier',
        'delivery_date': 'delivery_date',
        'delivery_country': 'delivery_country',
        'delivery_region': 'delivery_region',
        'delivery_city': 'delivery_city',
        'delivery_address': 'delivery_address',
        'specific_date_time_requested': 'specific_date_time_requested',
        '_date': 'date',
        'exchange_rate': 'exchange_rate',
        'payment_type': 'payment_type',
        'discount': 'discount',
        'uuid': 'uuid',
        'number': 'number',
        'status': 'status',
        'subtotal': 'subtotal',
        'tax_value': 'tax_value',
        'total': 'total',
        'discounted_total': 'discounted_total',
        'subtotal_currency': 'subtotal_currency',
        'tax_value_currency': 'tax_value_currency',
        'total_currency': 'total_currency',
        'discounted_total_currency': 'discounted_total_currency',
        'extra': 'extra',
        'items': 'items',
        'created_by': 'created_by',
        'modified_by': 'modified_by'
    }

    def __init__(self, id=None, partner=None, currency=None, language=None, source=None, source_text=None, delivery_type=None, delivered_by=None, delivery_identifier=None, delivery_date=None, delivery_country=None, delivery_region=None, delivery_city=None, delivery_address=None, specific_date_time_requested=None, _date=None, exchange_rate=None, payment_type=None, discount=None, uuid=None, number=None, status=None, subtotal=None, tax_value=None, total=None, discounted_total=None, subtotal_currency=None, tax_value_currency=None, total_currency=None, discounted_total_currency=None, extra=None, items=None, created_by=None, modified_by=None, _configuration=None):  # noqa: E501
        """Order - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._partner = None
        self._currency = None
        self._language = None
        self._source = None
        self._source_text = None
        self._delivery_type = None
        self._delivered_by = None
        self._delivery_identifier = None
        self._delivery_date = None
        self._delivery_country = None
        self._delivery_region = None
        self._delivery_city = None
        self._delivery_address = None
        self._specific_date_time_requested = None
        self.__date = None
        self._exchange_rate = None
        self._payment_type = None
        self._discount = None
        self._uuid = None
        self._number = None
        self._status = None
        self._subtotal = None
        self._tax_value = None
        self._total = None
        self._discounted_total = None
        self._subtotal_currency = None
        self._tax_value_currency = None
        self._total_currency = None
        self._discounted_total_currency = None
        self._extra = None
        self._items = None
        self._created_by = None
        self._modified_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.partner = partner
        self.currency = currency
        self.language = language
        if source is not None:
            self.source = source
        if source_text is not None:
            self.source_text = source_text
        if delivery_type is not None:
            self.delivery_type = delivery_type
        if delivered_by is not None:
            self.delivered_by = delivered_by
        if delivery_identifier is not None:
            self.delivery_identifier = delivery_identifier
        if delivery_date is not None:
            self.delivery_date = delivery_date
        if delivery_country is not None:
            self.delivery_country = delivery_country
        if delivery_region is not None:
            self.delivery_region = delivery_region
        if delivery_city is not None:
            self.delivery_city = delivery_city
        if delivery_address is not None:
            self.delivery_address = delivery_address
        if specific_date_time_requested is not None:
            self.specific_date_time_requested = specific_date_time_requested
        self._date = _date
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if payment_type is not None:
            self.payment_type = payment_type
        if discount is not None:
            self.discount = discount
        if uuid is not None:
            self.uuid = uuid
        if number is not None:
            self.number = number
        if status is not None:
            self.status = status
        if subtotal is not None:
            self.subtotal = subtotal
        if tax_value is not None:
            self.tax_value = tax_value
        if total is not None:
            self.total = total
        if discounted_total is not None:
            self.discounted_total = discounted_total
        if subtotal_currency is not None:
            self.subtotal_currency = subtotal_currency
        if tax_value_currency is not None:
            self.tax_value_currency = tax_value_currency
        if total_currency is not None:
            self.total_currency = total_currency
        if discounted_total_currency is not None:
            self.discounted_total_currency = discounted_total_currency
        if extra is not None:
            self.extra = extra
        self.items = items
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by

    @property
    def id(self):
        """Gets the id of this Order.  # noqa: E501


        :return: The id of this Order.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.


        :param id: The id of this Order.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def partner(self):
        """Gets the partner of this Order.  # noqa: E501


        :return: The partner of this Order.  # noqa: E501
        :rtype: int
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this Order.


        :param partner: The partner of this Order.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and partner is None:
            raise ValueError("Invalid value for `partner`, must not be `None`")  # noqa: E501

        self._partner = partner

    @property
    def currency(self):
        """Gets the currency of this Order.  # noqa: E501


        :return: The currency of this Order.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Order.


        :param currency: The currency of this Order.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def language(self):
        """Gets the language of this Order.  # noqa: E501


        :return: The language of this Order.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Order.


        :param language: The language of this Order.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def source(self):
        """Gets the source of this Order.  # noqa: E501


        :return: The source of this Order.  # noqa: E501
        :rtype: int
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Order.


        :param source: The source of this Order.  # noqa: E501
        :type: int
        """

        self._source = source

    @property
    def source_text(self):
        """Gets the source_text of this Order.  # noqa: E501

        Descrierea sursei  # noqa: E501

        :return: The source_text of this Order.  # noqa: E501
        :rtype: str
        """
        return self._source_text

    @source_text.setter
    def source_text(self, source_text):
        """Sets the source_text of this Order.

        Descrierea sursei  # noqa: E501

        :param source_text: The source_text of this Order.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                source_text is not None and len(source_text) > 100):
            raise ValueError("Invalid value for `source_text`, length must be less than or equal to `100`")  # noqa: E501

        self._source_text = source_text

    @property
    def delivery_type(self):
        """Gets the delivery_type of this Order.  # noqa: E501


        :return: The delivery_type of this Order.  # noqa: E501
        :rtype: int
        """
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, delivery_type):
        """Sets the delivery_type of this Order.


        :param delivery_type: The delivery_type of this Order.  # noqa: E501
        :type: int
        """

        self._delivery_type = delivery_type

    @property
    def delivered_by(self):
        """Gets the delivered_by of this Order.  # noqa: E501


        :return: The delivered_by of this Order.  # noqa: E501
        :rtype: str
        """
        return self._delivered_by

    @delivered_by.setter
    def delivered_by(self, delivered_by):
        """Sets the delivered_by of this Order.


        :param delivered_by: The delivered_by of this Order.  # noqa: E501
        :type: str
        """

        self._delivered_by = delivered_by

    @property
    def delivery_identifier(self):
        """Gets the delivery_identifier of this Order.  # noqa: E501


        :return: The delivery_identifier of this Order.  # noqa: E501
        :rtype: str
        """
        return self._delivery_identifier

    @delivery_identifier.setter
    def delivery_identifier(self, delivery_identifier):
        """Sets the delivery_identifier of this Order.


        :param delivery_identifier: The delivery_identifier of this Order.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                delivery_identifier is not None and len(delivery_identifier) > 100):
            raise ValueError("Invalid value for `delivery_identifier`, length must be less than or equal to `100`")  # noqa: E501

        self._delivery_identifier = delivery_identifier

    @property
    def delivery_date(self):
        """Gets the delivery_date of this Order.  # noqa: E501


        :return: The delivery_date of this Order.  # noqa: E501
        :rtype: datetime
        """
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, delivery_date):
        """Sets the delivery_date of this Order.


        :param delivery_date: The delivery_date of this Order.  # noqa: E501
        :type: datetime
        """

        self._delivery_date = delivery_date

    @property
    def delivery_country(self):
        """Gets the delivery_country of this Order.  # noqa: E501


        :return: The delivery_country of this Order.  # noqa: E501
        :rtype: str
        """
        return self._delivery_country

    @delivery_country.setter
    def delivery_country(self, delivery_country):
        """Sets the delivery_country of this Order.


        :param delivery_country: The delivery_country of this Order.  # noqa: E501
        :type: str
        """

        self._delivery_country = delivery_country

    @property
    def delivery_region(self):
        """Gets the delivery_region of this Order.  # noqa: E501


        :return: The delivery_region of this Order.  # noqa: E501
        :rtype: int
        """
        return self._delivery_region

    @delivery_region.setter
    def delivery_region(self, delivery_region):
        """Sets the delivery_region of this Order.


        :param delivery_region: The delivery_region of this Order.  # noqa: E501
        :type: int
        """

        self._delivery_region = delivery_region

    @property
    def delivery_city(self):
        """Gets the delivery_city of this Order.  # noqa: E501


        :return: The delivery_city of this Order.  # noqa: E501
        :rtype: int
        """
        return self._delivery_city

    @delivery_city.setter
    def delivery_city(self, delivery_city):
        """Sets the delivery_city of this Order.


        :param delivery_city: The delivery_city of this Order.  # noqa: E501
        :type: int
        """

        self._delivery_city = delivery_city

    @property
    def delivery_address(self):
        """Gets the delivery_address of this Order.  # noqa: E501


        :return: The delivery_address of this Order.  # noqa: E501
        :rtype: str
        """
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        """Sets the delivery_address of this Order.


        :param delivery_address: The delivery_address of this Order.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                delivery_address is not None and len(delivery_address) > 200):
            raise ValueError("Invalid value for `delivery_address`, length must be less than or equal to `200`")  # noqa: E501

        self._delivery_address = delivery_address

    @property
    def specific_date_time_requested(self):
        """Gets the specific_date_time_requested of this Order.  # noqa: E501


        :return: The specific_date_time_requested of this Order.  # noqa: E501
        :rtype: datetime
        """
        return self._specific_date_time_requested

    @specific_date_time_requested.setter
    def specific_date_time_requested(self, specific_date_time_requested):
        """Sets the specific_date_time_requested of this Order.


        :param specific_date_time_requested: The specific_date_time_requested of this Order.  # noqa: E501
        :type: datetime
        """

        self._specific_date_time_requested = specific_date_time_requested

    @property
    def _date(self):
        """Gets the _date of this Order.  # noqa: E501


        :return: The _date of this Order.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Order.


        :param _date: The _date of this Order.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this Order.  # noqa: E501


        :return: The exchange_rate of this Order.  # noqa: E501
        :rtype: str
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this Order.


        :param exchange_rate: The exchange_rate of this Order.  # noqa: E501
        :type: str
        """

        self._exchange_rate = exchange_rate

    @property
    def payment_type(self):
        """Gets the payment_type of this Order.  # noqa: E501


        :return: The payment_type of this Order.  # noqa: E501
        :rtype: int
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this Order.


        :param payment_type: The payment_type of this Order.  # noqa: E501
        :type: int
        """

        self._payment_type = payment_type

    @property
    def discount(self):
        """Gets the discount of this Order.  # noqa: E501

        Procentaj default, daca este completat rescrie discountul articolelor  # noqa: E501

        :return: The discount of this Order.  # noqa: E501
        :rtype: str
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this Order.

        Procentaj default, daca este completat rescrie discountul articolelor  # noqa: E501

        :param discount: The discount of this Order.  # noqa: E501
        :type: str
        """

        self._discount = discount

    @property
    def uuid(self):
        """Gets the uuid of this Order.  # noqa: E501


        :return: The uuid of this Order.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Order.


        :param uuid: The uuid of this Order.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def number(self):
        """Gets the number of this Order.  # noqa: E501


        :return: The number of this Order.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Order.


        :param number: The number of this Order.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                number is not None and len(number) < 1):
            raise ValueError("Invalid value for `number`, length must be greater than or equal to `1`")  # noqa: E501

        self._number = number

    @property
    def status(self):
        """Gets the status of this Order.  # noqa: E501


        :return: The status of this Order.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.


        :param status: The status of this Order.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def subtotal(self):
        """Gets the subtotal of this Order.  # noqa: E501

        Subtotal RON redus/întreg  # noqa: E501

        :return: The subtotal of this Order.  # noqa: E501
        :rtype: str
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """Sets the subtotal of this Order.

        Subtotal RON redus/întreg  # noqa: E501

        :param subtotal: The subtotal of this Order.  # noqa: E501
        :type: str
        """

        self._subtotal = subtotal

    @property
    def tax_value(self):
        """Gets the tax_value of this Order.  # noqa: E501

        TVA RON redus/întreg  # noqa: E501

        :return: The tax_value of this Order.  # noqa: E501
        :rtype: str
        """
        return self._tax_value

    @tax_value.setter
    def tax_value(self, tax_value):
        """Sets the tax_value of this Order.

        TVA RON redus/întreg  # noqa: E501

        :param tax_value: The tax_value of this Order.  # noqa: E501
        :type: str
        """

        self._tax_value = tax_value

    @property
    def total(self):
        """Gets the total of this Order.  # noqa: E501

        Total RON redus/întreg  # noqa: E501

        :return: The total of this Order.  # noqa: E501
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Order.

        Total RON redus/întreg  # noqa: E501

        :param total: The total of this Order.  # noqa: E501
        :type: str
        """

        self._total = total

    @property
    def discounted_total(self):
        """Gets the discounted_total of this Order.  # noqa: E501

        Suma valorilor reduse din articole  # noqa: E501

        :return: The discounted_total of this Order.  # noqa: E501
        :rtype: str
        """
        return self._discounted_total

    @discounted_total.setter
    def discounted_total(self, discounted_total):
        """Sets the discounted_total of this Order.

        Suma valorilor reduse din articole  # noqa: E501

        :param discounted_total: The discounted_total of this Order.  # noqa: E501
        :type: str
        """

        self._discounted_total = discounted_total

    @property
    def subtotal_currency(self):
        """Gets the subtotal_currency of this Order.  # noqa: E501

        Subtotal valută redus/întreg  # noqa: E501

        :return: The subtotal_currency of this Order.  # noqa: E501
        :rtype: str
        """
        return self._subtotal_currency

    @subtotal_currency.setter
    def subtotal_currency(self, subtotal_currency):
        """Sets the subtotal_currency of this Order.

        Subtotal valută redus/întreg  # noqa: E501

        :param subtotal_currency: The subtotal_currency of this Order.  # noqa: E501
        :type: str
        """

        self._subtotal_currency = subtotal_currency

    @property
    def tax_value_currency(self):
        """Gets the tax_value_currency of this Order.  # noqa: E501

        TVA valută redus/întreg  # noqa: E501

        :return: The tax_value_currency of this Order.  # noqa: E501
        :rtype: str
        """
        return self._tax_value_currency

    @tax_value_currency.setter
    def tax_value_currency(self, tax_value_currency):
        """Sets the tax_value_currency of this Order.

        TVA valută redus/întreg  # noqa: E501

        :param tax_value_currency: The tax_value_currency of this Order.  # noqa: E501
        :type: str
        """

        self._tax_value_currency = tax_value_currency

    @property
    def total_currency(self):
        """Gets the total_currency of this Order.  # noqa: E501

        Total valută redus/întreg  # noqa: E501

        :return: The total_currency of this Order.  # noqa: E501
        :rtype: str
        """
        return self._total_currency

    @total_currency.setter
    def total_currency(self, total_currency):
        """Sets the total_currency of this Order.

        Total valută redus/întreg  # noqa: E501

        :param total_currency: The total_currency of this Order.  # noqa: E501
        :type: str
        """

        self._total_currency = total_currency

    @property
    def discounted_total_currency(self):
        """Gets the discounted_total_currency of this Order.  # noqa: E501

        Suma valorilor reduse din articole  # noqa: E501

        :return: The discounted_total_currency of this Order.  # noqa: E501
        :rtype: str
        """
        return self._discounted_total_currency

    @discounted_total_currency.setter
    def discounted_total_currency(self, discounted_total_currency):
        """Sets the discounted_total_currency of this Order.

        Suma valorilor reduse din articole  # noqa: E501

        :param discounted_total_currency: The discounted_total_currency of this Order.  # noqa: E501
        :type: str
        """

        self._discounted_total_currency = discounted_total_currency

    @property
    def extra(self):
        """Gets the extra of this Order.  # noqa: E501

        Acest field este pentru a se stoca idul și tipul facturii.  # noqa: E501

        :return: The extra of this Order.  # noqa: E501
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this Order.

        Acest field este pentru a se stoca idul și tipul facturii.  # noqa: E501

        :param extra: The extra of this Order.  # noqa: E501
        :type: object
        """

        self._extra = extra

    @property
    def items(self):
        """Gets the items of this Order.  # noqa: E501

          # noqa: E501

        :return: The items of this Order.  # noqa: E501
        :rtype: list[OrderItemModel]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Order.

          # noqa: E501

        :param items: The items of this Order.  # noqa: E501
        :type: list[OrderItemModel]
        """
        if self._configuration.client_side_validation and items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def created_by(self):
        """Gets the created_by of this Order.  # noqa: E501

        User id that created this record  # noqa: E501

        :return: The created_by of this Order.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Order.

        User id that created this record  # noqa: E501

        :param created_by: The created_by of this Order.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this Order.  # noqa: E501

        Last user id that modified this record  # noqa: E501

        :return: The modified_by of this Order.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Order.

        Last user id that modified this record  # noqa: E501

        :param modified_by: The modified_by of this Order.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Order):
            return True

        return self.to_dict() != other.to_dict()
