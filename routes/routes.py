#!/usr/bin/python3
"""
Our Project Flask Routes
"""
from flask import Flask, render_template, request
from flask_login import LoginManager, login_required
from api.maps.donor import *
from api.maps.transfusion_center import *
from api.maps.blood_bag import *
from api.maps.city import *
from api.maps.country import *

app = Flask(__name__)
# Configure SECRET_KEY
login_manager = LoginManager(app)


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home_page():
    """provide Home page"""
    print("Home Page")


@app.route('/login', strict_slashes=False)
def login():
    """Render login page"""
    pass  # call to api for data exchange


@app.route('/login_center', methods=['POST'], strict_slashes=False)
def login_center():
    """Login as Transfusion Center"""
    login_center(request.get_json())


@app.route('/login_donor', methods=['POST'], strict_slashes=False)
def login_donor():
    """Login as Donor"""
    login_donor(request.get_json())


@app.route('/register', strict_slashes=False)
def register():
    """Render register page"""
    pass  # call to api for data exchange


@app.route('/register_center', methods=['POST'], strict_slashes=False)
def register_center():
    """Register New Transfusion Center"""
    create_center(request.get_json())


@app.route('/register_center', methods=['POST'], strict_slashes=False)
def register_center():
    """Register New Transfusion Center"""
    create_center(request.get_json())


@app.route('/register_donor', methods=['POST'], strict_slashes=False)
def register_donor():
    """Register New Donor"""
    create_donor(request.get_json())


@app.route('/center_dashboard', strict_slashes=False)
@login_required
def center_dashboard():
    """Render Transfusion Center dashboard"""
    pass  # call to api for data exchange.


@app.route('/donor_dashboard', strict_slashes=False)
@login_required
def donor_dashboard():
    """Render Donor dashboard"""
    pass


@app.route('/logout', strict_slashes=False)
@login_required
def logout():
    """ Logout """
    pass
