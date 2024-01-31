#!/usr/bin/python3
"""
Manipulate donors.
"""
from db import storage
from db.models import Donor
from flask import abort, jsonify, make_response, request
from api.maps import blood_map


@blood_map.route('/donors', methods=['GET'], strict_slashes=False)
def list_donors():
    """List Users."""
    donor_l = []
    all_objs = storage.all()
    for obj in all_objs:
        if isinstance(obj, Donor):
            donor_l.append(obj.__dict__)

    return jsonify(donor_l)
