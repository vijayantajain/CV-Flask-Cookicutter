"""Make the {{cookiecutter.app_name}} a flask app"""

import os
from os import path

from flask import Flask, render_template
from {{cookiecutter.app_name}}.{{cookiecutter.app_main_component}}.views import {{cookiecutter.app_main_component_blueprint}}

CWD = os.getcwd()
INSTANCE_PATH = path.join(CWD, 'instance')

app = Flask(__name__, instance_path=INSTANCE_PATH, instance_relative_config=True)
try:
    app.config.from_pyfile('config.py')
except FileNotFoundError:
    app.config['SECRET_KEY'] = 'Random Secret key'
app.register_blueprint({{cookiecutter.app_main_component_blueprint}})

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
