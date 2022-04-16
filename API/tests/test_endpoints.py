"""
This file holds the tests for endpoints.py.
"""

from unittest import TestCase, skip 
from flask_restx import Resource, Api

import endpoints as ep

class EndpointTestCase(TestCase):

    def get_all_artists(self):
        artists = ep.AllArtists(Resource)

        ret = artists.get() 
        self.assertIsInstance(ret,dict)

    def get_all_designs(self):
        designs = ep.AllDesigns(Resource)

        ret = designs.get() 
        self.assertIsInstance(ret,dict)

    def get_design(self):
        design = ep.Design(Resource)
        ret = design.get()
        self.assertIsInstance(ret,str)

