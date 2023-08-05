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
from akeyless.models.update_db_target_details import UpdateDBTargetDetails  # noqa: E501
from akeyless.rest import ApiException

class TestUpdateDBTargetDetails(unittest.TestCase):
    """UpdateDBTargetDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateDBTargetDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.update_db_target_details.UpdateDBTargetDetails()  # noqa: E501
        if include_optional :
            return UpdateDBTargetDetails(
                db_type = '0', 
                host_name = '0', 
                mongo_db_name = '0', 
                mongo_uri = '0', 
                name = '0', 
                port = '0', 
                protection_key = '0', 
                pwd = '0', 
                token = '0', 
                uid_token = '0', 
                user_name = '0'
            )
        else :
            return UpdateDBTargetDetails(
                name = '0',
        )

    def testUpdateDBTargetDetails(self):
        """Test UpdateDBTargetDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
