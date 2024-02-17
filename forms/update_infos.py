#!/usr/bin/python3
""" Update Infos forms """
from app import bcrypt
from db.models.donor import Donor
from db.models.transfusion_center import TransfusionCenter as TC
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, ValidationError
from db import storage


# class TCUpdateForm(FlaskForm):
#     name = StringField('Name *', validators=[DataRequired()])
#     email = StringField('Email *', validators=[DataRequired(), Email()])
#     phone_number = StringField('Phone Number')
#     map_coordinates = StringField('Map Coordinates')
#     country = SelectField('Country *', coerce=int, validators=[DataRequired()])
#     city = SelectField('City *', coerce=int, validators=[DataRequired()])
#     submit = SubmitField('Update Informations')
#
#     def __init__(self, *args, **kwargs):
#         """Initialize choiced"""
#         super(TCRegistrationForm, self).__init__(*args, **kwargs)
#         self.country.choices = [(0, '---')] + [(country.id, country.name)
#                                                for country in storage.all('Country')]
#         self.city.choices = [(city.id, city.name)
#                              for city in storage.all('City')]
#
#     def validate_email(self, email):
#         """Check if the email is not already taken"""
#
#         tc = storage.session.query(TC).filter_by(email=email.data).first()
#
#         if tc:
#             raise ValidationError('This email is already used.')
#
#     def validate_phone_number(self, phone_number):
#         """Check if the phone number is not already taken"""
#         if not phone_number.data:
#             return
#
#         tc = storage.session.query(TC).filter_by(
#             phone_number=phone_number.data).first()
#
#         if tc:
#             raise ValidationError('This phone number is already used.')


class DonorUpdateInfos(FlaskForm):
    username = StringField('Username :', validators=[DataRequired()])
    email = StringField('Email :', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number :')
    full_name = StringField('Full Name :', validators=[DataRequired()])
    age = IntegerField('Age :', validators=[
                       DataRequired(), NumberRange(min=18)])
    gender = SelectField('Gender :', choices=[None, 'Male', 'Female'])
    blood_category = SelectField(
        'Blood Category :',
        choices=[
            None,
            'A+',
            'A-',
            'B+',
            'B-',
            'AB+',
            'AB-',
            'O+',
            'O-'])
    submit = SubmitField('Update Informations')

    def validate_email(self, email):
        """Check if the email is not already taken"""

        donor = storage.session.query(
            Donor).filter_by(email=email.data).first()

        if donor and donor != current_user:
            raise ValidationError('This email is already used.')

    def validate_username(self, username):
        """Check if the username is not already taken"""

        donor = storage.session.query(Donor).filter_by(
            username=username.data).first()

        if donor and donor != current_user:
            raise ValidationError('This username is already used.')

    def validate_phone_number(self, phone_number):
        """Check if the phone number is not already taken"""
        if not phone_number.data:
            return

        donor = storage.session.query(Donor).filter_by(
            phone_number=phone_number.data).first()

        if donor and donor != current_user:
            raise ValidationError('This phone number is already used.')


class ChangePassword(FlaskForm):
    """Fom for changing password"""
    actual_password = PasswordField(
        'Actual Password :', validators=[
            DataRequired(), Length(
                min=6)])

    new_password = PasswordField(
        'New Password :', validators=[
            DataRequired(), Length(
                min=6)])

    confirm_password = PasswordField(
        'Confirm Password :', validators=[
            DataRequired(), EqualTo('new_password')])

    submit = SubmitField('Change Password')

    def validate_actual_password(self, actual_password):
        """Check if the actual password is correct"""
        if not bcrypt.check_password_hash(
                current_user.password_hash, actual_password.data):
            raise ValidationError('Incorrect password.')
