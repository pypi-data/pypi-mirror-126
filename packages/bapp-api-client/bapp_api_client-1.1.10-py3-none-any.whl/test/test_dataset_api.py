# coding: utf-8

"""
    BAPP API

    Test description  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@snippets.local
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import bapp_api_client
from bapp_api_client.api.dataset_api import DatasetApi  # noqa: E501
from bapp_api_client.rest import ApiException


class TestDatasetApi(unittest.TestCase):
    """DatasetApi unit test stubs"""

    def setUp(self):
        self.api = bapp_api_client.api.dataset_api.DatasetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dataset_city_list(self):
        """Test case for dataset_city_list

        """
        pass

    def test_dataset_company_info_read(self):
        """Test case for dataset_company_info_read

        """
        pass

    def test_dataset_country_list(self):
        """Test case for dataset_country_list

        """
        pass

    def test_dataset_currency_list(self):
        """Test case for dataset_currency_list

        """
        pass

    def test_dataset_device_create(self):
        """Test case for dataset_device_create

        """
        pass

    def test_dataset_exchange_rates_read(self):
        """Test case for dataset_exchange_rates_read

        """
        pass

    def test_dataset_generate_pdf_list(self):
        """Test case for dataset_generate_pdf_list

        """
        pass

    def test_dataset_generate_pdf_update(self):
        """Test case for dataset_generate_pdf_update

        """
        pass

    def test_dataset_language_list(self):
        """Test case for dataset_language_list

        """
        pass

    def test_dataset_measurement_unit_list(self):
        """Test case for dataset_measurement_unit_list

        """
        pass

    def test_dataset_notification_classes_list(self):
        """Test case for dataset_notification_classes_list

        """
        pass

    def test_dataset_notification_modules_list(self):
        """Test case for dataset_notification_modules_list

        """
        pass

    def test_dataset_region_list(self):
        """Test case for dataset_region_list

        """
        pass

    def test_dataset_template_list(self):
        """Test case for dataset_template_list

        """
        pass

    def test_dataset_vies_company_info_read(self):
        """Test case for dataset_vies_company_info_read

        """
        pass


if __name__ == '__main__':
    unittest.main()
