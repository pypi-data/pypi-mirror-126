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
from bapp_api_client.api.email_monitor_api import EmailMonitorApi  # noqa: E501
from bapp_api_client.rest import ApiException


class TestEmailMonitorApi(unittest.TestCase):
    """EmailMonitorApi unit test stubs"""

    def setUp(self):
        self.api = bapp_api_client.api.email_monitor_api.EmailMonitorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_email_monitor_account_create(self):
        """Test case for email_monitor_account_create

        """
        pass

    def test_email_monitor_account_delete(self):
        """Test case for email_monitor_account_delete

        """
        pass

    def test_email_monitor_account_list(self):
        """Test case for email_monitor_account_list

        """
        pass

    def test_email_monitor_account_partial_update(self):
        """Test case for email_monitor_account_partial_update

        """
        pass

    def test_email_monitor_account_read(self):
        """Test case for email_monitor_account_read

        """
        pass

    def test_email_monitor_account_update(self):
        """Test case for email_monitor_account_update

        """
        pass

    def test_email_monitor_actions_list(self):
        """Test case for email_monitor_actions_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
