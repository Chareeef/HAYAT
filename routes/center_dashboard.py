#!/ usr/bin/python3
"""
Our Flask Routes for Transfusion Center Dashboard
"""
from app import app, bcrypt
from db import storage
from flask import flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from forms.update_infos import TCUpdateInfos, ChangePasswordForm


@app.route('/center_dashboard', strict_slashes=False)
@login_required
def center_dashboard():
    """Render Transfusion Center dashboard"""
    center = current_user
    bags = current_user.blood_bags
    city = storage.get('City', center.city_id)
    country = storage.get('Country', city.country_id)

    return render_template('center_dashboard.html',
                           title='TC Dashboard',
                           center=center,
                           bags=bags,
                           city=city,
                           country=country,
                           nb_donors=len(center.donors))


@app.route('/update_blood_bags/', strict_slashes=False)
@app.route('/update_blood_bags/<int:bag_id>',
           methods=['GET', 'POST'], strict_slashes=False)
@login_required
def update_blood_bags(bag_id=None):
    """Update the Blood Bags statistics for the logged in TC"""
    center = current_user

    if request.method == 'POST':
        bag = storage.get('BloodBag', bag_id)
        bag.situation = dict(request.form).get('situation')
        bag.quantity = dict(request.form).get('quantity')
        bag.save()
        flash('Successfully updated !', 'success')
        return redirect(url_for('update_blood_bags'))

    bags = current_user.blood_bags

    return render_template('update_blood_bags.html',
                           title='Update Blood Bags',
                           center=center,
                           bags=bags)


@app.route('/update_center', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def update_center():
    """Render the form for updating transfusion center informations"""
    update_infos = TCUpdateInfos()
    change_pwd = ChangePasswordForm()

    center = current_user
    current_city = center.city
    current_country = current_city.country

    update_infos.country.choices = [(country.id, country.name)
                                    for country in storage.all('Country')]

    update_infos.city.choices = [(city.id, city.name)
                                 for city in storage.all('City')]

    if 'email' in dict(request.form) and update_infos.validate_on_submit():
        center.name = update_infos.name.data
        center.email = update_infos.email.data
        center.city_id = update_infos.city.data

        phone_number = update_infos.phone_number.data
        if phone_number == '':
            phone_number = None
        center.phone_number = phone_number

        location = update_infos.location.data
        if location == '':
            location = None
        center.location = location

        storage.commit()

        flash('Profile updated successfully !', 'success')
        return redirect(url_for('center_dashboard'))

    elif 'new_password' in dict(request.form) and change_pwd.validate_on_submit():
        new_hash = bcrypt.generate_password_hash(
            change_pwd.new_password.data).decode('utf-8')
        current_user.password_hash = new_hash

        storage.commit()

        flash('Password changed successfully !', 'success')
        return redirect(url_for('center_dashboard'))

    return render_template('update_center.html',
                           title='Update Infos',
                           update_infos=update_infos,
                           change_pwd=change_pwd,
                           current_country=current_country,
                           current_city=current_city,
                           center=center)
