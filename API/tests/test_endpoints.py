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

    def put_fonts(self):
        fonts = ep.Font(Resource)

        assert fonts.put("italian") == 0
        print("created font: italian")

        assert fonts.put("comic_sans") == 0
        print("created font: comic_sans")

        assert fonts.put("mono2") == 0
        print("created font: mono2")

    def get_all_artists(self):
        artists = ep.AllArtists(Resource)

        ret = artists.get() 
        self.assertIsInstance(ret,dict)

    def get_all_designs(self):
        designs = ep.AllDesigns(Resource)

        ret = designs.get() 
        self.assertIsInstance(ret,dict)

    def get_all_fonts(self):
        fonts = ep.AllFonts(Resource)

        ret = fonts.get() 
        self.assertIsInstance(ret,dict)

    def get_fonts(self):
        fonts = ep.Font(Resource)
        assert fonts.get("italian") == 0 
        assert fonts.get("comic_sans") == 0 
        assert fonts.get("mono2") == 0 

    def delete_fonts(self):
        fonts = ep.Font(Resource)

        assert fonts.delete("italian") == 0
        print("deleted font: italian")

        assert fonts.delete("comic_sans") == 0
        print("deleted font: comic_sans")

        assert fonts.delete("mono2") == 0
        print("deleted font: mono2")

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
