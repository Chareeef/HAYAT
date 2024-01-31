#!/usr/bin/python3
"""
Manipulate city.
"""
from api.maps import blood_map
from db import storage
from flask import jsonify


@blood_map.route('/cities', methods=['GET'], strict_slashes=False)
def list_city():
    """List Cities"""
    city_l = []
    all_objs = storage.all('City')
    for obj in all_objs:
        city_l.append(obj.to_dict())

    return jsonify(city_l)
