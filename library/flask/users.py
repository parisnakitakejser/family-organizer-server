from flask import Response
from bson.json_util import dumps


class FlaskUsers:
    @staticmethod
    def users():
        return Response(dumps({
            'status': 'OK',
            'code': 200
        }), mimetype='text/json'), 200
