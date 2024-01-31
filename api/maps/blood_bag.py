#!/usr/bin/python3
"""
Manipulate blood Bags.
"""
from db import storage
from db.models import BloodBag
from flask import abort, jsonify, make_response, request
from api.maps import blood_map


@blood_map.route('/blood_bags', methods=['GET'], strict_slashes=False)
def list_blood_bags():
    """List Blood bags"""
    blood_bags = []
    all_objs = storage.all()
    for obj in all_objs:
        if isinstance(obj, BloodBag):
            blood_bags.append(obj.__dict__)

    return jsonify(blood_bags)
