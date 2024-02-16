#!/ usr/bin/python3
"""
Our Project Flask Routes
"""
from app import app
from db import storage
from flask import flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required


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
