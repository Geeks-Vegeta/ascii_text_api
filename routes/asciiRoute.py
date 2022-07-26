from flask import request
from flask_restful import Resource
from controllers.ascii_controller import create_art

class AsciiRoute(Resource):
    def get(self):
        fonts = request.args.get('fonts')
        query = request.args.get('query')
        return create_art(query, fonts)
