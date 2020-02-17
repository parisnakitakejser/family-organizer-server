from flask import Response
from bson.json_util import dumps


class FlaskSystem:
    @staticmethod
    def status_verify():
        return Response(dumps({
            'status': 'OK',
            'code': 200
        }), mimetype='text/json'), 200
