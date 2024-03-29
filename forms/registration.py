#!/usr/bin/python3
""" Registration forms """
from db.models.donor import Donor
from db.models.transfusion_center import TransfusionCenter as TC
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, ValidationError
from db import storage


class TCRegistrationForm(FlaskForm):
    """Transfusion Center Registration form"""
    name = StringField('Name *', validators=[DataRequired()])
    email = StringField('Email *', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password *', validators=[
            DataRequired(), Length(
                min=6)])
    confirm_password = PasswordField(
        'Confirm Password *', validators=[
            DataRequired(), EqualTo('password')])
    phone_number = StringField('Phone Number')
    location = StringField('Location')
    country = SelectField('Country *', coerce=int, validators=[DataRequired()])
    city = SelectField('City *', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Register')

    def __init__(self, *args, **kwargs):
        """Initialize choiced"""
        super(TCRegistrationForm, self).__init__(*args, **kwargs)
        self.country.choices = [(0, '---')] + [(country.id, country.name)
                                               for country in storage.all('Country')]
        self.city.choices = [(0, '---')] + [(city.id, city.name)
                                            for city in storage.all('City')]

    def validate_email(self, email):
        """Check if the email is not already taken"""

        tc = storage.session.query(TC).filter_by(email=email.data).first()

        if tc:
            raise ValidationError('This email is already used.')

    def validate_phone_number(self, phone_number):
        """Check if the phone number is not already taken"""

        tc = storage.session.query(TC).filter_by(
            phone_number=phone_number.data).first()

        if tc:
            raise ValidationError('This phone number is already used.')


class DonorRegistrationForm(FlaskForm):
    """Donor Registration form"""
    username = StringField('Username *', validators=[DataRequired()])
    email = StringField('Email *', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password *', validators=[
            DataRequired(), Length(
                min=6)])
    confirm_password = PasswordField(
        'Confirm Password *', validators=[
            DataRequired(), EqualTo('password')])
    phone_number = StringField('Phone Number')
    full_name = StringField('Full Name *', validators=[DataRequired()])
    age = IntegerField(
        'Age *', validators=[DataRequired(), NumberRange(min=18)])
    gender = SelectField('Gender',
                         choices=[
                             (None, 'None'), ('Male', 'Male'), ('Female', 'Female')],
                         default=None)
    blood_category = SelectField(
        'Blood Category',
        choices=[
            (None, 'None'),
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-')],
        default=None)
    submit = SubmitField('Register')

    def validate_email(self, email):
        """Check if the email is not already taken"""

        donor = storage.session.query(
            Donor).filter_by(email=email.data).first()

        if donor:
            raise ValidationError('This email is already used.')

    def validate_username(self, username):
        """Check if the username is not already taken"""

        donor = storage.session.query(Donor).filter_by(
            username=username.data).first()

        if donor:
            raise ValidationError('This username is already used.')

    def validate_phone_number(self, phone_number):
        """Check if the phone number is not already taken"""

        donor = storage.session.query(Donor).filter_by(
            phone_number=phone_number.data).first()

        if donor:
            raise ValidationError('This phone number is already used.')
