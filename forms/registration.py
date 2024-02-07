#!/usr/bin/python3
""" Registration forms """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange

class DonorRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    phone_number = StringField('Phone Number')
    full_name = StringField('Full Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18)])
    gender = SelectField('Gender', choices=['Male', 'Female', None])
    blood_category = SelectField('Blood Category', choices=[None, 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
    submit = SubmitField('Register')
