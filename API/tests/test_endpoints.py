"""
This file holds the tests for endpoints.py.
"""

from unittest import TestCase, skip 
from flask_restx import Resource, Api

import endpoints as ep

class EndpointTestCase(TestCase):


    def test_hello(self):
        hello = ep.HelloWorld(Resource)
        ret = hello.get()
        self.assertIsInstance(ret, dict)
        self.assertIn(ep.HELLO, ret)


    def test_get_fonts(self):
        fonts = ep.TattooFonts(Resource)
        ret = fonts.get()
        self.assertIsInstance(ret, dict)


    def test_test(self):
        """
        Post-condition 2: keys to the dict are strings
        """
        lr = ep.Tattoo(Resource)
        ret = lr.get(str)
        self.assertIsInstance(ret,str)


