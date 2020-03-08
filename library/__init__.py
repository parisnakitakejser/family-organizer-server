from pymongo import MongoClient
import os


def init_mongo_conn(timeout: int = 30000):
    host_ip = os.getenv('DB_MONGO_HOST', 'localhost')
    host_port = os.getenv('DB_MONGO_PORT', '27017')
    database = os.getenv('DB_MONGO_DATABASE', 'project-family-organizer')
    username = os.getenv('DB_MONGO_USERNAME', None)
    password = os.getenv('DB_MONGO_PASSWORD', None)
    auth_source = os.getenv('DB_MONGO_AUTH_SOURCE', 'admin')
    auth_mechanism = os.getenv('DB_MONGO_AUTH_MECHANISM', 'SCRAM-SHA-256')

    try:
        auth_required = False
        if username is not None:
            auth_required = True

        kwargs = {
            'serverSelectionTimeoutMS': int(os.getenv('DB_MONGO_TIMEOUT', timeout))
        }

        if auth_required:
            kwargs.update({
                'username': username,
                'password': password,
                'authSource': auth_source,
                'authMechanism': auth_mechanism
            })

        client = MongoClient(f'{host_ip}:{host_port}', **kwargs)
        mongo_conn = client[database]

    except ValueError as e:
        print(f'MongoDB connection to {host_ip}:{host_port} refused')
        print(e)
        raise ValueError

    return mongo_conn, client
