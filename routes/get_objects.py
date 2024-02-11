#!/ usr/bin/python3
"""
Our Project Flask Routes
"""
from app import app
from db import storage
from flask import jsonify


@app.route('/get_cities/<int:country_id>')
def get_cities(country_id):
    country = storage.get('Country', country_id)

    cities = []
    if country:
        cities = [{'id': city.id, 'name': city.name}
                  for city in country.cities]
        cities.sort(key=lambda city: city['name'])

    return jsonify({'cities': cities})


@app.route('/get_centers/<int:city_id>')
def get_centers(city_id):
    city = storage.get('City', city_id)

    centers = []
    if city:
        centers = [{'id': center.id, 'name': center.name}
                   for center in city.centers]
        centers.sort(key=lambda center: center['name'])

    return jsonify({'centers': centers})


@app.route('/get_bags/<int:center_id>')
def get_bags(center_id):
    center = storage.get('TransfusionCenter', center_id)

    bags = []
    if center:
        bags = [bag.to_dict() for bag in center.blood_bags]
        bags.sort(key=lambda bag: bag['blood_category'])

    return jsonify({'bags': bags})
