#!/usr/bin/python3
"""Module containing our Flask app"""
from db import storage
from db.models.donor import Donor
from db.models.transfusion_center import TransfusionCenter as TC
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = '9c714e2657ea33a5d8fed340b5f10e5cbb5d0393e2'
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def user_loader(user_id):
    """Load the current user"""
    user = storage.session.query(Donor).get(int(user_id))

    if not user:
        user = storage.session.query(TC).get(int(user_id))

    return user


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()

from routes.routes import *


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
