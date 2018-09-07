"""Module for defining the form as well check-functions for form-input"""

from os import path

from flask_wtf import FlaskForm
# from wtforms import

class {{cookiecutter.input_form_name}}}(FlaskForm):
    """A WTForm used by Jinja to generate HTML

    Parameters
    ----------
    FlaskForm : Class FlaskForm
        InputForm inherits `FlaskForm`
    """
    # Add fields here
