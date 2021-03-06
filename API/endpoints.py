"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
import os
from http import HTTPStatus
from flask import Flask
from flask_cors import CORS
from flask_restx import Resource, Api
from bson.json_util import dumps

import db.db as db
import requests
from requests.auth import HTTPBasicAuth


app = Flask(__name__)
CORS(app)

api = Api(app)

OK = 0
NOT_FOUND = 1
DUPLICATE = 2


@api.route('/authorize_backblaze_access')
class GetAccess(Resource):
    """
    Get json with authorized token to access backblaze api for upload/delete
    """
    def get(self):
        """
        Give auth token and bb api
        """
        # Auth information from Backblaze
        key_id = os.environ["BB_KEYID"]
        application_key = os.environ["BB_APPKEY"]

        # Authenticate
        path = 'https://api.backblazeb2.com/b2api/v1/b2_authorize_account'
        result = requests.get(path,
                              auth=HTTPBasicAuth(key_id, application_key))
        # Read response
        return result.json()


@api.route('/get_upload_url')
class GetUpload_Url(Resource):
    """
    Get json with url to upload
    """
    def get(self):
        """
        Get json with url to upload
        """
        # Auth information from Backblaze
        key_id = os.environ["BB_KEYID"]
        application_key = os.environ["BB_APPKEY"]

        # Authenticate
        path = 'https://api.backblazeb2.com/b2api/v1/b2_authorize_account'
        result = requests.get(path,
                              auth=HTTPBasicAuth(key_id, application_key))

        # Read response
        auth = result.json()

        api_url = auth['apiUrl'] + '/b2api/v2/b2_get_upload_url'

        print(api_url)
        account_authorization_token = auth['authorizationToken']
        bucket_id = "8d5894f45da9ef2674e90913"

        url_res = requests.post(api_url,
                                json={'bucketId': bucket_id},
                                headers={'Authorization':
                                         account_authorization_token})

        return url_res.json()


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

        list_designs = list(designs)
        json_data = dumps(list_designs, sort_keys=True, indent=4)
        return json_data


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
