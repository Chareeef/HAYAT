#!/usr/bin/python3
""" Registration forms """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange
from db import storage

class TCRegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    phone_number = StringField('Phone Number')
    map_coordinates = StringField('Map Coordinates')
    country = SelectField('Country', coerce=int, validators=[DataRequired()])
    city = SelectField('City', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Register')

    def __init__(self, *args, **kwargs):
        super(TCRegistrationForm, self).__init__(*args, **kwargs)
        self.country.choices = [(0, '---')] + [(country.id, country.name) for country in storage.all('Country')]
        self.city.choices = [(city.id, city.name) for city in storage.all('City')]


class DonorRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    phone_number = StringField('Phone Number')
    full_name = StringField('Full Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18)])
    gender = SelectField('Gender', choices=[None, 'Male', 'Female'])
    blood_category = SelectField('Blood Category', choices=[None, 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
    submit = SubmitField('Register')
