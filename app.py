import os
from flask import Flask
from flask_cors import CORS

from library.flask.users import FlaskUsers
from library.flask.system import FlaskSystem

prefix_path = os.getenv('FAMILY_ORGANIZER_PREFIX_URL', '/api/')

app = Flask(__name__)
CORS(app)
cros = CORS(app, resources={
    r"/api/*": {
        "origins": "*"
    }
})

app.add_url_rule(f'{prefix_path}users', view_func=FlaskUsers.users, methods=['GET', 'POST', 'PUT'])
app.add_url_rule(f'{prefix_path}system/status-verify', view_func=FlaskSystem.status_verify, methods=['GET'])
app.add_url_rule(f'{prefix_path}system/configuration/completed', view_func=FlaskSystem.configuration_completed, methods=['PUT'])

if __name__ == '__main__':
    app.run(debug=bool(os.getenv('FAMILY_ORGANIZER_DEBUG', False)), host=os.getenv('FAMILY_ORGANIZER_HOST', '0.0.0.0'))
