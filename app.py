#!/usr/bin/python3
"""Module containing our Flask app"""
from db import storage
from db.models.donor import Donor
from db.models.transfusion_center import TransfusionCenter as TC
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import secrets

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(24)
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
