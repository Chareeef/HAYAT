#!/usr/bin/python3
"""
Manipulate Transfusion center..
"""
from db import storage
from db.models import TransfusionCenter
from flask import abort, jsonify, make_response, request
from api.maps import blood_map


@blood_map.route('/transfusion_centers', methods=['GET'], strict_slashes=False)
def list_centers():
    """List Transfusion centers"""
    centers_l = []
    all_objs = storage.all()
    for obj in all_objs:
        if isinstance(obj, TransfusionCenter):
            centers_l.append(obj.__dict__)

    return jsonify(centers_l)
