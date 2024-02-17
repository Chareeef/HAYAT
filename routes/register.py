#!/ usr/bin/python3
"""
Our Project Flask Routes
"""
from app import app, bcrypt
from db.models.blood_bag import BloodBag
from db.models.donor import Donor
from db.models.transfusion_center import TransfusionCenter
from flask import flash, render_template, redirect, url_for
from flask_login import current_user
from forms.registration import DonorRegistrationForm, TCRegistrationForm


@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """Register page for both Donor and Transfusion Center"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    tc_form = TCRegistrationForm()
    if tc_form.validate_on_submit():
        # If tc_form data is valid, process it
        name = tc_form.name.data.strip()
        email = tc_form.email.data.strip()
        phone_number = tc_form.phone_number.data.strip()
        location = tc_form.location.data.strip()
        password = tc_form.password.data.strip()
        country_id = tc_form.country.data
        city_id = tc_form.city.data

        # Hash the password
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

        if phone_number == '':
            phone_number = None

        if location == '':
            location = None

        # Create a dictionary with tc data
        tc_dict = {
            'name': name,
            'email': email,
            'phone_number': phone_number,
            'location': location,
            'password_hash': hashed_pw,
            'city_id': city_id
        }

        tc = TransfusionCenter(**tc_dict)
        tc.save()

        # Assign blood bags
        categories = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

        for blood_category in categories:
            bag = BloodBag(blood_category=blood_category,
                           quantity=30,
                           situation='Stable',
                           center_id=tc.id)
            bag.save()

        flash('Successfully registered ! Welcome !', 'success')
        return redirect(url_for('login'))

    donor_form = DonorRegistrationForm()
    if donor_form.validate_on_submit():
        # If donor_form data is valid, process it
        username = donor_form.username.data.strip()
        full_name = donor_form.full_name.data.strip()
        email = donor_form.email.data.strip()
        phone_number = donor_form.phone_number.data.strip()
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

        flash(f'Registration successful ! Welcome, {full_name}!', 'success')
        return redirect(url_for('login'))

    return render_template(
        'register.html',
        title='Register',
        donor_form=donor_form,
        tc_form=tc_form)
