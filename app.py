#!/usr/bin/python3
"""Module containing our Flask app"""
from db.models.donor import Donor
from db.models.transfusion_center import TransfusionCenter
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import secrets

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(24)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

@login_manager.user_loader
def user_loader(user_id):
    """Load the current user"""
    user = Donor.query.get(int(user_id))

    if not user:
        user = TransfusionCenter.query.get(int(user_id))

    return user

from routes.routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
