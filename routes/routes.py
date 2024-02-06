#!/usr/bin/python3
"""
Our Project Flask Routes
"""
from flask import render_template, redirect, request, url_for
from flask_login import current_user, LoginManager, login_required, login_user, logout
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
    """Render Home page"""
    return render_template('index.html')


@app.route('/login', strict_slashes=False)
def login_page():
    """Render Login page for both Donor and Transfusion Center"""
    return render_template('login.html')


@app.route('/login_donor', methods=['POST'], strict_slashes=False)
def login_donor():
    """Render login page"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    username = request.form.get('username')
    password = request.form.get('password')
    
    donors = storage.all('Donor')

    donor = None
    for d in donors:
        if d.username == username and bcrypt.check_password_hash(c.password_hash, # TODO
                                                                 password):
    
    if donor:
        login_user(donor, remember=True)
        return redirect(url_for('donor_dashboard'))
    else:
        # flash error
        return render_template('login.html')


@app.route('/login_center', methods=['POST'], strict_slashes=False)
def login_center():
    """Login as Transfusion Center"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    email = request.form.get('email')
    password = request.form.get('password')
    
    centers = storage.all('TransfusionCenter')

    center = None
    for c in centers:
        if c.email == email and bcrypt.check_password_hash(c.password_hash, # TODO
                                                           password):
            center = c
    
    if center:
        login_user(center, remember=True)
        return redirect(url_for('center_dashboard'))
    else:
        # flash error
        return render_template('login.html')


@app.route('/register_center', methods=['POST'], strict_slashes=False)
def register_center():
    """Register New Transfusion Center"""
    # Create via api
    pass


@app.route('/register_donor', methods=['POST'], strict_slashes=False)
def register_donor():
    """Register New Donor"""
    # Create via api
    pass


@app.route('/center_dashboard', strict_slashes=False)
@login_required
def center_dashboard():
    """Render Transfusion Center dashboard"""
    pass


@app.route('/donor_dashboard', strict_slashes=False)
@login_required
def donor_dashboard():
    """Render Donor dashboard"""
    pass


@app.route('/logout', strict_slashes=False)
@login_required
def logout():
    """ Logout """
    login_user()
    return redirect(url_for('home'))
