#!/usr/bin/python3
"""
Manipulate city.
"""
from db import storage
from db.models import City
from flask import abort, jsonify, make_response, request
from api.maps import blood_map


@blood_map.route('/cities', methods=['GET'], strict_slashes=False)
def list_city():
    """List Cities"""
    city_l = []
    all_objs = storage.all()
    for obj in all_objs:
        if isinstance(obj, City):
            city_l.append(obj.__dict__)

    return jsonify(city_l)
