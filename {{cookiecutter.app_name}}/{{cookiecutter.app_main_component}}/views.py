"""Module controlling the 'View' of the application"""

import os
from os import path

from flask import Blueprint, flash, render_template, request
from flask.views import MethodView

from {{cookiecutter.app_name}}.{{cookiecutter.app_main_component}}.{{cookiecutter.cv_module}} import {{cookiecutter.cv_class}}
from {{cookiecutter.app_name}}.{{cookiecutter.app_main_component}}.forms import {{cookiecutter.input_form_name}}

CWD = os.getcwd()

{{cookiecutter.app_main_component_blueprint}} = Blueprint(__name__, '{{cookiecutter.app_main_component_blueprint}}')

class {{cookiecutter.blueprint_class_name}}}(MethodView):
    """Class handling the view of the form.

    There are two methods `get` and `set` which
    handle the respective request.
    """

    def get(self):
        """This method handles the GET request from the user
        which is when the main page is loaded.
        """
        # Enter code here
        pass

    def post(self):
        """Handles the POST request from the user
        """
        pass

{{cookiecutter.app_main_component_blueprint}}.add_url_rule(rule='/', view_func={{cookiecutter.blueprint_class_name}}}.as_view('home'))
