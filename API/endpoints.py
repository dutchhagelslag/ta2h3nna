"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
import os
from http import HTTPStatus
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_restx import Resource, Api
from bson.json_util import dumps

import werkzeug.exceptions as wz

import db.db as db
import requests
from requests.auth import HTTPBasicAuth


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


@api.route('/authorize_backblaze_access')
class GetAccess(Resource):
    """
    Get json with authorized token to access backblaze api for upload/delete
    """
    def get(self):
        """
        Give to frontend -> front end will handle uploading
        and getting using the handle
        """
        # Auth information from Backblaze
        key_id = os.environ["BB_KEYID"]
        application_key = os.environ["BB_APPKEY"]

        # Authenticate
        path = 'https://api.backblazeb2.com/b2api/v1/b2_authorize_account'
        result = requests.get(path,
                              auth=HTTPBasicAuth(key_id, application_key))
        if result.status_code != 200:
            print('Error - Could not connect to BackBlaze B2')
            exit()

        # Read response
        result_json = result.json()
        return result_json
        # account_id = result_json['accountId']
        # auth_token = result_json['authorizationToken']
        # api_url    = result_json['apiUrl'] + '/b2api/v1'
        # download_url = result_json['downloadUrl'] + '/file/'
        # api_session = requests.Session()
        # api_session.headers.update({ 'Authorization': auth_token })


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
        Returns a json of all designs and their metadata
        """
        designs = db.get_designs().find()

        if designs is None:
            raise (wz.NotFound("Designs not found."))
        else:
            list_designs = list(designs)
            json_data = dumps(list_designs, sort_keys=True, indent=4)
            return json_data


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
            return jsonify(dumps(ret))

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
            return dumps(ret)

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
