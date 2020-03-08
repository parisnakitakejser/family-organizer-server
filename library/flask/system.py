from flask import Response, request
from bson.json_util import dumps

from library import init_mongo_conn
from library.family import Family, Members, Pets

class FlaskSystem:
    @staticmethod
    def status_verify():
        return Response(dumps({
            'status': 'OK',
            'code': 200
        }), mimetype='text/json'), 200

    @staticmethod
    def configuration_completed():
        mongo_conn, client = init_mongo_conn()

        json_data = request.get_json()

        family_id = Family.insert(name=json_data['name'], mongo_conn=mongo_conn)
        member_ids = Members.insert(members=json_data['members'], family_id=family_id, mongo_conn=mongo_conn)
        pet_ids = Pets.insert(pets=json_data['pets'], family_id=family_id, mongo_conn=mongo_conn)

        return Response(dumps({
            'status': 'OK',
            'code': 200,
            'content': {
                'family-id': family_id,
                'member-ids': member_ids,
                'pet-ids': pet_ids
            }
        }), mimetype='text/json'), 200