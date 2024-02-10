#!/usr/bin/python3
""" Login forms """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length


class TCLoginForm(FlaskForm):
    """Login form for Transfusion Center"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password', validators=[
            DataRequired(), Length(
                min=6)])
    submit = SubmitField('Login')


class DonorLoginForm(FlaskForm):
    """Login form for Donor"""
    username = StringField('Username', validators=[Length(max=120)])
    password = PasswordField(
        'Password', validators=[
            DataRequired(), Length(
                min=6)])
    submit = SubmitField('Login')
