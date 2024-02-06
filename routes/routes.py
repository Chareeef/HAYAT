#!/usr/bin/python3
"""
Our Project Flask Routes
"""
from flask import render_template, request
from flask_login import LoginManager, login_required, login_user
import secrets
from db import storage
from api.maps.donor import *
from api.maps.transfusion_center import *
from api.maps.blood_bag import *
from api.maps.city import *
from api.maps.country import *
from api.app import app

app.config['SECRET_KEY'] = secrets.token_hex(24)
login_manager = LoginManager(app)


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home_page():
    """provide Home page"""
    return "Home Page"


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login_donor():
    """Render login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password_hash')
        
        donor = None # here query a donor with the above username
        
        if donor and donor.password_hash == password:
            login_user(donor, remember=True)
            return # redirect to dashboard


@app.route('/login_center', methods=['POST'], strict_slashes=False)
def login_center():
    """Login as Transfusion Center"""
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password_hash')
        
        center = None # here, query a center with the above username
        
        if center and center.password_hash == password:
            login_user(center, remember=True)
            return # redirect to dashboard


@app.route('/register_center', methods=['POST'], strict_slashes=False)
def register_center():
    """Register New Transfusion Center"""
    Register_transfusion_center(request.get_json())


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
    pass # redirect to home page.

