from bson.objectid import ObjectId


class Family:
    def __init__(self):
        pass

    @staticmethod
    def count(mongo_conn: object) -> int:
        return mongo_conn['family'].count({})

    @staticmethod
    def insert(name: str, mongo_conn: object) -> ObjectId:
        result = mongo_conn['family'].insert_one({
            'name': name
        })

        return result.inserted_id


class Members:
    def __init__(self):
        pass

    @staticmethod
    def insert(members: list, family_id: ObjectId, mongo_conn: object) -> list:
        inserted_ids = []

        for member in members:
            result = mongo_conn['family-members'].insert_one({
                'family-id': family_id,
                'birthday': member['birthday'],
                'email': member['email'],
                'fullname': member['fullname'],
                'gender': member['gender'],
                'relationship': member['relationship']
            })

            inserted_ids.append(result.inserted_id)

        return inserted_ids


class Pets:
    def __init__(self):
        pass

    @staticmethod
    def insert(pets: list, family_id: ObjectId, mongo_conn: object) -> list:
        inserted_ids = []

        for pet in pets:
            result = mongo_conn['family-pets'].insert_one({
                'family-id': family_id,
                'birthday': pet['birthday'],
                'type': pet['type'],
                'fullname': pet['fullname'],
                'gender': pet['gender']
            })

            inserted_ids.append(result.inserted_id)

        return inserted_ids
