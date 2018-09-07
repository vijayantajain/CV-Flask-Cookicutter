"""Module to run the app"""

import os

from {{cookiecutter.app_name}} import app

PORT = int(os.environ.get('PORT', "{{cookiecutter.port_address}}"))
app.run(host='{{cookiecutter.host_address}}', port=PORT)
