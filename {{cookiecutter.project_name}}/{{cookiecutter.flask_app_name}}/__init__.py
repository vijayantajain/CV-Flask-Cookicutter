"""Make the {{cookiecutter.flask_app_name}} a flask app"""

import os
from os import path

from flask import Flask, render_template
from {{cookiecutter.flask_app_name}}.{{cookiecutter.flask_app_module}}.views import {{cookiecutter.flask_app_module_blueprint}}

CWD = os.getcwd()
INSTANCE_PATH = path.join(CWD, 'instance')

app = Flask(__name__, instance_path=INSTANCE_PATH, instance_relative_config=True)
try:
    app.config.from_pyfile('config.py')
except FileNotFoundError:
    app.config['SECRET_KEY'] = 'Random Secret key'
app.register_blueprint({{cookiecutter.flask_app_module_blueprint}})

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
