#!/usr/bin/python3
"""
Manipulate Transfusion center..
"""
from api.maps import blood_map
from db import storage
from flask import jsonify


@blood_map.route('/transfusion_centers', methods=['GET'], strict_slashes=False)
def list_transfusion_centers():
    """List Transfusion centers"""
    centers_l = []
    all_objs = storage.all('TransfusionCenter')
    for obj in all_objs:
        centers_l.append(obj.to_dict())

    return jsonify(centers_l)
