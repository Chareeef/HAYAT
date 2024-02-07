#!/usr/bin/python3
""" Login forms """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length


class TCLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')


class DonorLoginForm(FlaskForm):
    login_option = SelectField('Login Option', choices=[('email', 'Email'), ('username', 'Username')], validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), Length(max=120)])
    username = StringField('Username', validators=[Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')
