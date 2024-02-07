#!/usr/bin/python3
"""
Manipulate donors.
"""
from api.maps import blood_map
from db import storage
from db.models import Donor
from flask import abort, jsonify, make_response, request


@blood_map.route('/donors', methods=['GET'], strict_slashes=False)
def list_donors():
    """List Donors"""
    donor_l = []
    all_objs = storage.all('Donor')
    for obj in all_objs:
        donor_l.append(obj.to_dict())

    return jsonify(donor_l)


@blood_map.route('/donors/<id>', methods=['GET'], strict_slashes=False)
def get_donor(id):
    """Get specific Donor"""
    donor = storage.get('Donor', id)
    if not donor:
        abort(404)

    return jsonify(donor.to_dict())


@blood_map.route('/donors', methods=['POST'], strict_slashes=False)
def create_donor(route_data=None):
    """Register new donor"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password_hash' not in request.get_json():
        abort(400, description="Missing password")
    data = request.get_json()

    donor = Donor(**data)
    storage.add(donor)
    storage.commit()

    return make_response(jsonify(donor.to_dict()), 201)


@blood_map.route('/donors/<id>', methods=['PUT'], strict_slashes=False)
def update_donor(id):
    """ Updates Donor information. """
    donor = storage.get('Donor', id)
    
    if not donor:
        abort(404)
        
    if not request.get_json():
        abort(400, description='Not a JSON')
        
    ignore = ['id', 'email', 'create_at', 'updated_at']
    
    data = request.get_json()
    for key, val in data.items():
        if key not in ignore:
            setattr(donor, key, val)
    
    storage.commit()

    return make_response(jsonify(donor.to_dict()), 201)


@blood_map.route('/donors/<id>', methods=['DELETE'], strict_slashes=False)
def delete_donor(id):
    """ Delete donor account. """
    donor = storage.get('Donor', id)
    if not donor:
        abort(404)
    
    storage.delete(donor)
    storage.commit()

    return make_response(jsonify({'Deleted': 'Done'}), 200)
