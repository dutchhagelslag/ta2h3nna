"""
This file holds the tests for endpoints.py.
"""

from unittest import TestCase, skip 
from flask_restx import Resource, Api
import endpoints as ep
import os
import json

class EndpointTestCase(TestCase):

    def test_env_vars(self):
        self.assertIsInstance(os.environ.get('BB_APPKEY'), str)
        self.assertIsInstance(os.environ.get('BB_KEYID'), str)

    def test_all_designs(self):
        designs = ep.AllDesigns(Resource)
        ret = designs.get() 
        self.assertIsInstance(ret,str)

    def test_authorize_backblaze(self):
        designs = ep.GetAccess(Resource)
        ret = designs.get()
        self.assertIsInstance(ret,dict)

    def test_get_upload_url(self):
        designs = ep.GetUpload_Url(Resource)
        ret = designs.get()
        self.assertIsInstance(ret,dict)

    def test_get_endpoints(self):
        designs = ep.Endpoints(Resource)
        ret = designs.get()
        self.assertIsInstance(ret,dict)

    
    
        
