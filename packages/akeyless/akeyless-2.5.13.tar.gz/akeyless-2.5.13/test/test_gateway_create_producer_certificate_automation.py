# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import akeyless
from akeyless.models.gateway_create_producer_certificate_automation import GatewayCreateProducerCertificateAutomation  # noqa: E501
from akeyless.rest import ApiException

class TestGatewayCreateProducerCertificateAutomation(unittest.TestCase):
    """GatewayCreateProducerCertificateAutomation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GatewayCreateProducerCertificateAutomation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.gateway_create_producer_certificate_automation.GatewayCreateProducerCertificateAutomation()  # noqa: E501
        if include_optional :
            return GatewayCreateProducerCertificateAutomation(
                admin_rotation_interval_days = 56, 
                allow_subdomains = True, 
                allowed_domains = [
                    '0'
                    ], 
                auto_generated_folder = '0', 
                enable_admin_rotation = True, 
                gateway_url = 'http://localhost:8000', 
                name = '0', 
                producer_encryption_key_name = '0', 
                root_first_in_chain = True, 
                sign_using_akeyless_pki = True, 
                signer_key_name = '0', 
                store_private_key = True, 
                token = '0', 
                uid_token = '0', 
                user_ttl = '0', 
                venafi_api_key = '0', 
                venafi_baseurl = '0', 
                venafi_password = '0', 
                venafi_use_tpp = True, 
                venafi_username = '0', 
                venafi_zone = '0'
            )
        else :
            return GatewayCreateProducerCertificateAutomation(
                name = '0',
                venafi_zone = '0',
        )

    def testGatewayCreateProducerCertificateAutomation(self):
        """Test GatewayCreateProducerCertificateAutomation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
