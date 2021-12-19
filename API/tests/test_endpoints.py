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


    def test_get_design_genre(self):
        """
        Check if get_design return a dict for genre
        """
        lr = ep.TattooDesigns(Resource)
        ret = lr.get("Classic_Americana", "Boxer")
        self.assertIsInstance(ret,str)


