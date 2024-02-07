#!/ usr/bin/python3
"""
Our Project Flask Routes
"""
from app import app, bcrypt
from db import storage
from db.models.donor import Donor
from db.models.transfusion_center import TransfusionCenter
from flask import flash, render_template, jsonify, redirect, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from forms.registration import DonorRegistrationForm, TCRegistrationForm
from forms.login import DonorLoginForm, TCLoginForm


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    """Render Home page"""
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Login page for both Donor and Transfusion Center"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    tc_form = TCLoginForm()
    donor_form = DonorLoginForm()

    if tc_form.validate_on_submit():
        email = tc_form.email.data
        password = tc_form.password.data
        tc = storage.session.query(TransfusionCenter).filter_by(email=email).first()

        if tc and bcrypt.check_password_hash(tc.password_hash, password):
            login_user(tc)
            flash('Logged in successfully !', 'info')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    elif donor_form.validate_on_submit():
        username = donor_form.username.data
        donor = storage.session.query(Donor).filter_by(username=username).first()

        if donor and bcrypt.check_password_hash(donor.password_hash, donor_form.password.data):
            login_user(donor)
            flash('Logged in successfully !', 'info')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html', title='Login', tc_form=tc_form,
                           donor_form=donor_form)


@app.route('/get_cities/<int:country_id>')
def get_cities(country_id):
    country = storage.get('Country', country_id)
    cities = [{'id': city.id, 'name': city.name} for city in country.cities]
    cities.sort(key=lambda city: city['name'])
    return jsonify({'cities': cities})


@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """Register page for both Donor and Transfusion Center"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    tc_form = TCRegistrationForm()
    if tc_form.validate_on_submit():
        # If tc_form data is valid, process it
        name = tc_form.name.data
        email = tc_form.email.data
        phone_number = tc_form.phone_number.data
        password = tc_form.password.data
        country_id = tc_form.country.data 
        city_id = tc_form.city.data 

        # Hash the password
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

        if phone_number == '':
            phone_number = None

        # Create a dictionary with tc data
        tc_dict = {
            'name': name,
            'email': email,
            'phone_number': phone_number,
            'password_hash': hashed_pw,
            'city_id': city_id
        }

        tc = TransfusionCenter(**tc_dict)
        tc.save()
 
        flash('Registration successful! Welcome !', 'info')
        return redirect(url_for('login'))

    donor_form = DonorRegistrationForm()
    if donor_form.validate_on_submit():
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

        if phone_number == '':
            phone_number = None

        if gender == 'None':
            gender = None

        if blood_category == 'None':
            blood_category = None

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

        donor = Donor(**donor_dict)
        donor.save()
 
        flash(f'Registration successful! Welcome, {full_name}!', 'info')
        return redirect(url_for('login'))
 
    return render_template('register.html', title='Register', donor_form=donor_form,
                           tc_form=tc_form)


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
