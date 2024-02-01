#!/usr/bin/python3
"""
Manipulate country.
"""
from api.maps import blood_map
from db import storage
from flask import jsonify


@blood_map.route('/countries', methods=['GET'], strict_slashes=False)
def list_country():
    """List Countries"""
    country_l = []
    all_objs = storage.all('Country')
    for obj in all_objs:
        country_l.append(obj.to_dict())

    return jsonify(country_l)
