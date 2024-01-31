#!/usr/bin/python3
"""
Manipulate country.
"""
from db import storage
from db.models import Country
from flask import abort, jsonify, make_response, request
from api.maps import blood_map


@blood_map.route('/countries', methods=['GET'], strict_slashes=False)
def list_country():
    """List Countries"""
    country_l = []
    all_objs = storage.all()
    for obj in all_objs:
        if isinstance(obj, Country):
            country_l.append(obj.__dict__)

    return jsonify(country_l)
