"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from http import HTTPStatus
from flask import Flask
from flask import jsonify
from flask_restx import Resource, Api
import werkzeug.exceptions as wz

import db.db as db

app = Flask(__name__)
api = Api(app)

HELLO = 'Hola'
WORLD = 'mundo'


@api.route('/hello2')
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {HELLO: WORLD}


@api.route('/get_fonts')
class GetFonts(Resource):
    """
    This class serves tattoos fonts
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all font names.
        """
        fonts = db.get_fonts()
        if fonts is None:
            raise (wz.NotFound("Font db not found."))
        else:
            return jsonify(fonts)


@api.route('/get_artists')
class GetArtists(Resource):
    """
    This class serves tattoos fonts
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all font names.
        """
        fonts = db.get_artists()
        if fonts is None:
            raise (wz.NotFound("Font db not found."))
        else:
            return jsonify(fonts)


@api.route('/get_designs')
class GetDesigns(Resource):
    """
    This class serves tattoos fonts
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all font names.
        """
        fonts = db.get_designs()
        if fonts is None:
            raise (wz.NotFound("Font db not found."))
        else:
            return jsonify(fonts)


@api.route('/get_design/<genre>/<name>')
class GetDesign(Resource):
    """
    This class serves tatoos
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, genre, name):
        """
        The 'get(genre)' method returns the url for the url design associated
        with a genre
        """
        designs = db.get_designs()
        if designs is None:
            raise (wz.NotFound("Design db not found."))
        elif genre not in designs:
            raise (wz.NotFound("Genre not found."))
        else:
            return designs[genre][name]


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


@api.route('/search_design/<design>')
class CreateSearchDesign(Resource):
    """
    This class is for creating initial search query
    """
    @api.response(HTTPStatus.OK, 'Success')
    def post(self, design):
        return design
