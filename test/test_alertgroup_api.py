# coding: utf-8

"""
    Alertmanager API

    API of the Prometheus Alertmanager (https://github.com/prometheus/alertmanager)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.alertgroup_api import AlertgroupApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAlertgroupApi(unittest.TestCase):
    """AlertgroupApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.alertgroup_api.AlertgroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_alert_groups(self):
        """Test case for get_alert_groups

        """
        pass


if __name__ == '__main__':
    unittest.main()