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


class AccountingDocument(object):
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
        'preview_image': 'str',
        'created_at': 'datetime',
        'modified_at': 'datetime',
        'source': 'int',
        'hash': 'str',
        'original': 'str',
        'original_mime_type': 'str',
        'image': 'str',
        'preview': 'str',
        'status': 'int',
        'document_type': 'int',
        'document_number': 'str',
        'document_date': 'date',
        'document_due_date': 'date',
        'value': 'str',
        'extra_data': 'object',
        'tag': 'int',
        'company': 'int',
        'created_by': 'str',
        'modified_by': 'str',
        'partner': 'int',
        'currency': 'str'
    }

    attribute_map = {
        'id': 'id',
        'preview_image': 'preview_image',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'source': 'source',
        'hash': 'hash',
        'original': 'original',
        'original_mime_type': 'original_mime_type',
        'image': 'image',
        'preview': 'preview',
        'status': 'status',
        'document_type': 'document_type',
        'document_number': 'document_number',
        'document_date': 'document_date',
        'document_due_date': 'document_due_date',
        'value': 'value',
        'extra_data': 'extra_data',
        'tag': 'tag',
        'company': 'company',
        'created_by': 'created_by',
        'modified_by': 'modified_by',
        'partner': 'partner',
        'currency': 'currency'
    }

    def __init__(self, id=None, preview_image=None, created_at=None, modified_at=None, source=None, hash=None, original=None, original_mime_type=None, image=None, preview=None, status=None, document_type=None, document_number=None, document_date=None, document_due_date=None, value=None, extra_data=None, tag=None, company=None, created_by=None, modified_by=None, partner=None, currency=None, _configuration=None):  # noqa: E501
        """AccountingDocument - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._preview_image = None
        self._created_at = None
        self._modified_at = None
        self._source = None
        self._hash = None
        self._original = None
        self._original_mime_type = None
        self._image = None
        self._preview = None
        self._status = None
        self._document_type = None
        self._document_number = None
        self._document_date = None
        self._document_due_date = None
        self._value = None
        self._extra_data = None
        self._tag = None
        self._company = None
        self._created_by = None
        self._modified_by = None
        self._partner = None
        self._currency = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if preview_image is not None:
            self.preview_image = preview_image
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if source is not None:
            self.source = source
        if hash is not None:
            self.hash = hash
        if original is not None:
            self.original = original
        if original_mime_type is not None:
            self.original_mime_type = original_mime_type
        if image is not None:
            self.image = image
        if preview is not None:
            self.preview = preview
        if status is not None:
            self.status = status
        if document_type is not None:
            self.document_type = document_type
        if document_number is not None:
            self.document_number = document_number
        if document_date is not None:
            self.document_date = document_date
        if document_due_date is not None:
            self.document_due_date = document_due_date
        if value is not None:
            self.value = value
        if extra_data is not None:
            self.extra_data = extra_data
        if tag is not None:
            self.tag = tag
        if company is not None:
            self.company = company
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if partner is not None:
            self.partner = partner
        if currency is not None:
            self.currency = currency

    @property
    def id(self):
        """Gets the id of this AccountingDocument.  # noqa: E501


        :return: The id of this AccountingDocument.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountingDocument.


        :param id: The id of this AccountingDocument.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def preview_image(self):
        """Gets the preview_image of this AccountingDocument.  # noqa: E501


        :return: The preview_image of this AccountingDocument.  # noqa: E501
        :rtype: str
        """
        return self._preview_image

    @preview_image.setter
    def preview_image(self, preview_image):
        """Sets the preview_image of this AccountingDocument.


        :param preview_image: The preview_image of this AccountingDocument.  # noqa: E501
        :type: str
        """

        self._preview_image = preview_image

    @property
    def created_at(self):
        """Gets the created_at of this AccountingDocument.  # noqa: E501

        Date and time at which this record was added  # noqa: E501

        :return: The created_at of this AccountingDocument.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AccountingDocument.

        Date and time at which this record was added  # noqa: E501

        :param created_at: The created_at of this AccountingDocument.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this AccountingDocument.  # noqa: E501

        Date and time at which this record was modified  # noqa: E501

        :return: The modified_at of this AccountingDocument.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this AccountingDocument.

        Date and time at which this record was modified  # noqa: E501

        :param modified_at: The modified_at of this AccountingDocument.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def source(self):
        """Gets the source of this AccountingDocument.  # noqa: E501


        :return: The source of this AccountingDocument.  # noqa: E501
        :rtype: int
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this AccountingDocument.


        :param source: The source of this AccountingDocument.  # noqa: E501
        :type: int
        """

        self._source = source

    @property
    def hash(self):
        """Gets the hash of this AccountingDocument.  # noqa: E501


        :return: The hash of this AccountingDocument.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this AccountingDocument.


        :param hash: The hash of this AccountingDocument.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                hash is not None and len(hash) < 1):
            raise ValueError("Invalid value for `hash`, length must be greater than or equal to `1`")  # noqa: E501

        self._hash = hash

    @property
    def original(self):
        """Gets the original of this AccountingDocument.  # noqa: E501


        :return: The original of this AccountingDocument.  # noqa: E501
        :rtype: str
        """
        return self._original

    @original.setter
    def original(self, original):
        """Sets the original of this AccountingDocument.


        :param original: The original of this AccountingDocument.  # noqa: E501
        :type: str
        """

        self._original = original

    @property
    def original_mime_type(self):
        """Gets the original_mime_type of this AccountingDocument.  # noqa: E501


        :return: The original_mime_type of this AccountingDocument.  # noqa: E501
        :rtype: str
        """
        return self._original_mime_type

    @original_mime_type.setter
    def original_mime_type(self, original_mime_type):
        """Sets the original_mime_type of this AccountingDocument.


        :param original_mime_type: The original_mime_type of this AccountingDocument.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                original_mime_type is not None and len(original_mime_type) < 1):
            raise ValueError("Invalid value for `original_mime_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._original_mime_type = original_mime_type

    @property
    def image(self):
        """Gets the image of this AccountingDocument.  # noqa: E501


        :return: The image of this AccountingDocument.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this AccountingDocument.


        :param image: The image of this AccountingDocument.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def preview(self):
        """Gets the preview of this AccountingDocument.  # noqa: E501


        :return: The preview of this AccountingDocument.  # noqa: E501
        :rtype: str
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """Sets the preview of this AccountingDocument.


        :param preview: The preview of this AccountingDocument.  # noqa: E501
        :type: str
        """

        self._preview = preview

    @property
    def status(self):
        """Gets the status of this AccountingDocument.  # noqa: E501


        :return: The status of this AccountingDocument.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountingDocument.


        :param status: The status of this AccountingDocument.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def document_type(self):
        """Gets the document_type of this AccountingDocument.  # noqa: E501


        :return: The document_type of this AccountingDocument.  # noqa: E501
        :rtype: int
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this AccountingDocument.


        :param document_type: The document_type of this AccountingDocument.  # noqa: E501
        :type: int
        """

        self._document_type = document_type

    @property
    def document_number(self):
        """Gets the document_number of this AccountingDocument.  # noqa: E501


        :return: The document_number of this AccountingDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_number

    @document_number.setter
    def document_number(self, document_number):
        """Sets the document_number of this AccountingDocument.


        :param document_number: The document_number of this AccountingDocument.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                document_number is not None and len(document_number) > 100):
            raise ValueError("Invalid value for `document_number`, length must be less than or equal to `100`")  # noqa: E501

        self._document_number = document_number

    @property
    def document_date(self):
        """Gets the document_date of this AccountingDocument.  # noqa: E501


        :return: The document_date of this AccountingDocument.  # noqa: E501
        :rtype: date
        """
        return self._document_date

    @document_date.setter
    def document_date(self, document_date):
        """Sets the document_date of this AccountingDocument.


        :param document_date: The document_date of this AccountingDocument.  # noqa: E501
        :type: date
        """

        self._document_date = document_date

    @property
    def document_due_date(self):
        """Gets the document_due_date of this AccountingDocument.  # noqa: E501


        :return: The document_due_date of this AccountingDocument.  # noqa: E501
        :rtype: date
        """
        return self._document_due_date

    @document_due_date.setter
    def document_due_date(self, document_due_date):
        """Sets the document_due_date of this AccountingDocument.


        :param document_due_date: The document_due_date of this AccountingDocument.  # noqa: E501
        :type: date
        """

        self._document_due_date = document_due_date

    @property
    def value(self):
        """Gets the value of this AccountingDocument.  # noqa: E501


        :return: The value of this AccountingDocument.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AccountingDocument.


        :param value: The value of this AccountingDocument.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def extra_data(self):
        """Gets the extra_data of this AccountingDocument.  # noqa: E501


        :return: The extra_data of this AccountingDocument.  # noqa: E501
        :rtype: object
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data):
        """Sets the extra_data of this AccountingDocument.


        :param extra_data: The extra_data of this AccountingDocument.  # noqa: E501
        :type: object
        """

        self._extra_data = extra_data

    @property
    def tag(self):
        """Gets the tag of this AccountingDocument.  # noqa: E501


        :return: The tag of this AccountingDocument.  # noqa: E501
        :rtype: int
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this AccountingDocument.


        :param tag: The tag of this AccountingDocument.  # noqa: E501
        :type: int
        """

        self._tag = tag

    @property
    def company(self):
        """Gets the company of this AccountingDocument.  # noqa: E501

        Firma care deține această înregistrare.  # noqa: E501

        :return: The company of this AccountingDocument.  # noqa: E501
        :rtype: int
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this AccountingDocument.

        Firma care deține această înregistrare.  # noqa: E501

        :param company: The company of this AccountingDocument.  # noqa: E501
        :type: int
        """

        self._company = company

    @property
    def created_by(self):
        """Gets the created_by of this AccountingDocument.  # noqa: E501

        User id that created this record  # noqa: E501

        :return: The created_by of this AccountingDocument.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AccountingDocument.

        User id that created this record  # noqa: E501

        :param created_by: The created_by of this AccountingDocument.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this AccountingDocument.  # noqa: E501

        Last user id that modified this record  # noqa: E501

        :return: The modified_by of this AccountingDocument.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this AccountingDocument.

        Last user id that modified this record  # noqa: E501

        :param modified_by: The modified_by of this AccountingDocument.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def partner(self):
        """Gets the partner of this AccountingDocument.  # noqa: E501


        :return: The partner of this AccountingDocument.  # noqa: E501
        :rtype: int
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this AccountingDocument.


        :param partner: The partner of this AccountingDocument.  # noqa: E501
        :type: int
        """

        self._partner = partner

    @property
    def currency(self):
        """Gets the currency of this AccountingDocument.  # noqa: E501


        :return: The currency of this AccountingDocument.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AccountingDocument.


        :param currency: The currency of this AccountingDocument.  # noqa: E501
        :type: str
        """

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
        if issubclass(AccountingDocument, dict):
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
        if not isinstance(other, AccountingDocument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountingDocument):
            return True

        return self.to_dict() != other.to_dict()
