"""
This file holds the tests for endpoints.py.
"""

from unittest import TestCase, skip 
from flask_restx import Resource, Api

import endpoints as ep

class EndpointTestCase(TestCase):

    def get_all_designs(self):
        designs = ep.AllDesigns(Resource)
        ret = designs.get() 
        self.assertIsInstance(ret,dict)

    def authorize_backblaze(self):
        designs = ep.GetAccess(Resource)
        ret = designs.get()
        assert ret.status_code == 200

    def get_upload_url(self):
        designs = ep.GetUpload_Url(Resource)
        ret = designs.get()
        assert ret.status_code == 200


    
    
