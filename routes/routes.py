#!/ usr/bin/python3
"""
Our Project Flask Routes
"""
from api.maps.donor import *
from api.maps.transfusion_center import *
from api.maps.blood_bag import *
from api.maps.city import *
from api.maps.country import *
from app import app, bcrypt
from db import storage
from flask import flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from forms.registration import DonorRegistrationForm
import json
import requests


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home_page():
    """Render Home page"""
    return render_template('index.html')


@app.route('/login', strict_slashes=False)
def login():
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
        if d.username == username and bcrypt.check_password_hash(d.password_hash, # TODO
                                                                 password):
            donor = d

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


@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """Register page for both Donor and Transfusion Center"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    donor_form = DonorRegistrationForm()
    print(1)
    if donor_form.validate_on_submit():
        print(2)
        # If donor_form data is valid, process it
        username = donor_form.username.data
        full_name = donor_form.full_name.data
        email = donor_form.email.data
        phone_number = donor_form.phone_number.data
        password = donor_form.password.data
        age = donor_form.age.data
        gender = donor_form.gender.data
        blood_category = donor_form.blood_category.data

        # Hash the password
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a dictionary with donor data
        donor_dict = {
            'username': username,
            'full_name': full_name,
            'email': email,
            'phone_number': phone_number,
            'password_hash': hashed_pw,
            'age': age,
            'gender': gender,
            'blood_category': blood_category
        }

        json_data = json.dumps(donor_dict)

        url = "https://hayat-blood-donation.tech/api/donors"

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, data=json_data, headers=headers)
        print(donor_dict)
        print(response.__dict__)

        if response.status_code == 201:
            flash('Registration successful! Welcome, {}!'.donor_format(name), 'success')
            return redirect(url_for('login'))
    return render_template('register.html', donor_form=donor_form)


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
    logout_user()
    return redirect(url_for('home'))
