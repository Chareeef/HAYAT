#!/ usr/bin/python3
"""
Flask Routes for the Donor dashboard
"""
from app import app, bcrypt
from db import storage
from flask import flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from forms.update_infos import DonorUpdateInfos, ChangePasswordForm


@app.route('/donor_dashboard', strict_slashes=False)
@login_required
def donor_dashboard():
    """Render Donor Profile page"""
    return render_template('donor_dashboard.html',
                           title='Profile',
                           donor=current_user)


@app.route('/update_donor', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def update_donor():
    """Render the form for updating Donor informations"""
    update_infos = DonorUpdateInfos()
    change_pwd = ChangePasswordForm()

    donor = current_user
    blood_categories = ['None', 'A+', 'A-', 'B+', 'B-',
                        'AB+', 'AB-', 'O+', 'O-']
    genders = ['None', 'Male', 'Female']

    if 'email' in dict(request.form) and update_infos.validate_on_submit():
        donor.username = update_infos.username.data
        donor.email = update_infos.email.data
        donor.full_name = update_infos.full_name.data
        donor.age = update_infos.age.data

        phone_number = update_infos.phone_number.data
        if phone_number == '':
            phone_number = None
        donor.phone_number = phone_number

        gender = update_infos.gender.data
        if gender in ['', 'None']:
            gender = None
        donor.gender = gender

        blood_category = update_infos.blood_category.data
        if blood_category in ['', 'None']:
            blood_category = None
        donor.blood_category = blood_category

        storage.commit()

        flash('Profile updated successfully !', 'success')
        return redirect(url_for('donor_dashboard'))

    elif 'new_password' in dict(request.form) and change_pwd.validate_on_submit():
        new_hash = bcrypt.generate_password_hash(
            change_pwd.new_password.data).decode('utf-8')
        current_user.password_hash = new_hash

        storage.commit()

        flash('Password changed successfully !', 'success')
        return redirect(url_for('donor_dashboard'))

    return render_template('update_donor.html',
                           title='Update Infos',
                           update_infos=update_infos,
                           change_pwd=change_pwd,
                           blood_categories=blood_categories,
                           genders=genders,
                           donor=donor)
