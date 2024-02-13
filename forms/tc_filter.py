#!/usr/bin/python3
""" Filter forms """
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from db import storage


class TCFilter(FlaskForm):
    """Transfusion Center filter"""
    country = SelectField('Country', coerce=int, validators=[DataRequired()])
    city = SelectField('City', coerce=int, validators=[DataRequired()])
    center = SelectField('Center', coerce=int, validators=[DataRequired()])
    search = SubmitField('Show Center')

    def __init__(self, *args, **kwargs):
        """Initialize choices"""
        super(TCFilter, self).__init__(*args, **kwargs)
        self.country.choices = [(0, 'Select Country')] + [(country.id, country.name)
                                               for country in storage.all('Country')]
        self.city.choices = [(0, 'Select City')]
        self.center.choices = [(0, 'Select Center')]
