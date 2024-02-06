#!/usr/bin/python3
"""
Manipulate country.
"""
from api.maps import blood_map
from db import storage
from db.models import Country
from flask import jsonify, abort, make_response, request


@blood_map.route('/countries', methods=['GET'], strict_slashes=False)
def list_country():
    """List Countries"""
    country_l = []
    all_objs = storage.all('Country')
    for obj in all_objs:
        country_l.append(obj.to_dict())

    return jsonify(country_l)


@blood_map.route('/countries/<id>', methods=['GET'], strict_slashes=False)
def get_country(id):
    """Get specific country"""
    country = storage.get('Country', id)
    if not country:
        abort(404)

    return jsonify(country.to_dict())


@blood_map.route('/countries', methods=['POST'], strict_slashes=False)
def register_country():
    """Register new country"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    country = Country(**data)
    storage.add(country)
    storage.commit()

    return make_response(jsonify(country.to_dict()), 201)


@blood_map.route('/countries/<id>', methods=['PUT'], strict_slashes=False)
def update_country(id):
    """ Updates country information. """
    country = storage.get('Country', id)
    
    if not country:
        abort(404)
        
    if not request.get_json():
        abort(400, description='Not a JSON')
        
    ignore = ['id', 'email', 'create_at', 'updated_at',]
    
    data = request.get_json()
    for key, val in data.items():
        if key not in ignore:
            setattr(country, key, val)
    
    storage.commit()

    return make_response(jsonify(country.to_dict()), 201)


@blood_map.route('/countries/<id>', methods=['DELETE'], strict_slashes=False)
def remove_country(id):
    """ remove country. """
    country = storage.get('Country', id)
    if not country:
        abort(404)
    
    storage.delete(country)
    storage.commit()

    return make_response(jsonify({'Deleted': 'Done'}), 200)
