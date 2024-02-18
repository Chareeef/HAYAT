#!/ usr/bin/python3
"""
Our Project Flask Getter Routes
"""
from app import app
from db import storage
from flask import flash, jsonify, redirect, url_for
from flask_login import current_user, login_required


@app.route('/get_cities/<int:country_id>', strict_slashes=False)
def get_cities(country_id):
    """Get the list of the country's cities"""
    country = storage.get('Country', country_id)

    cities = []
    if country:
        cities = [{'id': city.id, 'name': city.name}
                  for city in country.cities]
        cities.sort(key=lambda city: city['name'])

    return jsonify({'cities': cities})


@app.route('/get_centers/<int:city_id>', strict_slashes=False)
def get_centers(city_id):
    """Get the list of the city's transfusion centers"""
    city = storage.get('City', city_id)

    centers = []
    if city:
        centers = [{'id': center.id, 'name': center.name}
                   for center in city.centers]
        centers.sort(key=lambda center: center['name'])

    return jsonify({'centers': centers})


@app.route('/get_bags/<int:center_id>', strict_slashes=False)
def get_bags(center_id):
    """Get the list of the transfusion center's blood bags"""
    center = storage.get('TransfusionCenter', center_id)

    bags = []
    if center:
        bags = [bag.to_dict() for bag in center.blood_bags]
        bags.sort(key=lambda bag: bag['blood_category'])

    return jsonify({'bags': bags})


@app.route('/delete_account', methods=['POST'], strict_slashes=False)
@login_required
def delete_account():
    """Delete the current user's account"""
    current_user.delete()

    flash('Account deleted successfully', 'success')
    return redirect(url_for('home'))
