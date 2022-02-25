"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from http import HTTPStatus
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_restx import Resource, Api
from bson import json_util

import werkzeug.exceptions as wz

import db.db as db

app = Flask(__name__)
CORS(app)

api = Api(app)

HELLO = 'Hola'
WORLD = 'mundo'

OK = 0
NOT_FOUND = 1
DUPLICATE = 2


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


@api.route('/get_handle')
class GetHandle(Resource):
    """
    Get handle to backblaze bucket
    """
    def get(self):
        """
        Give to frontend -> front end will handle uploading
        and getting using the handle
        """
        return "s3.us-west-004.backblazeb2.com"


@api.route('/all_fonts')
class AllFonts(Resource):
    """
    This class lists tattoos fonts in json
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all fonts.
        """
        fonts = db.get_fonts().find()

        if fonts is None:
            raise (wz.NotFound("Fonts not found."))
        else:
            names = []
            for x in fonts:
                names.append(x['name'])

            return jsonify(names)


@api.route('/all_artists')
class AllArtists(Resource):
    """
    This class serves a list artists in json format
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all artsts names
        """
        artists = db.get_artists().find()

        if artists is None:
            raise (wz.NotFound("Artists not found."))
        else:
            names = []
            for x in artists:
                names.append(x['name'])
            return jsonify(names)


@api.route('/all_designs')
class AllDesigns(Resource):
    """
    This class lists designs in json
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all design names.
        """
        designs = db.get_designs().find()

        if designs is None:
            raise (wz.NotFound("Designs not found."))
        else:
            names = []
            for x in designs:
                names.append(x['name'])

            return jsonify(names)


@api.route('/design/<name>')
class Design(Resource):
    """
    This class tatoos info for a given name
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, name):
        """
        The 'get(name)' method returns all info associated with name
        """
        designs = db.get_designs()
        if designs is None:
            raise (wz.NotFound("Design db not found."))
        else:
            ret = designs.find({"name": name}).next()
            return json_util.dumps(ret)

    # def delete(self,name):
    #     """
    #     Deletes the design of a given name
    #     """
    #     designs = db.get_designs()
    #     if designs is None:
    #         raise (wz.NotFound("Design db not found."))
    #     else:
    #         return designs.find();

    #     return designs.delete_one({"name":name}).acknowledged

    # def put(self,name):
    #     """
    #     Adds or Update new design of a given name
    #     """
    #     parser = reqparse.RequestParser()
    #     parser.add_argument("")

    #     args = parser_args()


@api.route('/font/<name>')
class Font(Resource):
    """
    This class tatoos info for a given name
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, name):
        """
        The 'get(name)' method returns all info associated with name
        """
        fonts = db.get_fonts()
        if fonts is None:
            raise (wz.NotFound("Font db not found."))
        else:
            ret = fonts.find({"name": name}).next()
            return json_util.dumps(ret)

    def delete(self, name):
        """
        Deletes the font of a given name
        """
        fonts = db.get_fonts()
        if fonts is None:
            raise (wz.NotFound("Font db not found."))
        else:
            fonts.delete_one({"name": name})
            return OK

    def put(self, name):
        """
        Adds or Update new font of a given name
        """
        # adds entry to mongodb
        fonts = db.get_fonts()
        if fonts is None:
            raise (wz.NotFound("Font db not found."))
        else:
            fonts.replace_one({"name": name}, {"name": name}, True)
            return OK
        # add file to backblaze bucket


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
