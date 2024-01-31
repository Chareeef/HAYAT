#!/usr/bin/python3
"""
Manipulate blood Bags.
"""
from api.maps import blood_map
from db import storage
from flask import jsonify


@blood_map.route('/blood_bags', methods=['GET'], strict_slashes=False)
def list_blood_bags():
    """List Blood bags"""
    blood_bags = []
    all_objs = storage.all('BloodBag')
    for obj in all_objs:
        blood_bags.append(obj.to_dict)

    return jsonify(blood_bags)
