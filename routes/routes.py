#!/usr/bin/python3
"""
Web Routes
"""
from flask import Flask, render_template, request
from flask_login import LoginManager, login_required
from api.maps.donor import *
from api.maps.transfusion_center import *
from api.maps.blood_bag import *
from api.maps.city import *
from api.maps.country import *
app = Flask(__name__)
login_manager = LoginManager(app)


@app.route('/home', strict_slashes=False)
def home_page():
    """provide Home page"""
    print("Home Page")


@app.route('/')
def home():
    """provide Home page"""
    home_page()


@app.route('/login', strict_slashes=False)
def longin():
    """Log in page"""
    pass # call to api for data exchange


@app.route('/register', methods=['POST'], strict_slashes=False)
def register():
    """ Register New Donor"""
    create_donor(request.get_json())


@app.route('/transfusion_center', strict_slashes=False)
@login_required
def center_dashboard():
    pass # call to api for data exchange.


@app.route('/dashboard', strict_slashes=False)
@login_required
def profile():
    """ User profile"""
    pass


@app.route('/logout', strict_slashes=False)
@login_required
def logout():
    """ Logout """
    pass
