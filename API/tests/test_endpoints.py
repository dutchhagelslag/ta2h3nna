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


    # def test_get_fonts(self):
    #     fonts = ep.GetFonts(Resource)
    #     ret = fonts.get()
    #     self.assertIsInstance(ret, dict)


    # def test_get_artists(self):
    #     artists = ep.GetArtists(Resource)
    #     ret = artists.get()
    #     self.assertIsInstance(ret, dict)


    # def test_get_designs(self):
    #     designs = ep.GetDesigns(Resource)
    #     ret = designs.get()
    #     self.assertIsInstance(ret, dict)



