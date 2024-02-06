#!/usr/bin/python3
"""
Manipulate city.
"""
from api.maps import blood_map
from db import storage
from db.models import City
from flask import jsonify, request, abort, make_response


@blood_map.route('/cities', methods=['GET'], strict_slashes=False)
def list_city():
    """List Cities"""
    city_l = []
    all_objs = storage.all('City')
    for obj in all_objs:
        city_l.append(obj.to_dict())

    return jsonify(city_l)


@blood_map.route('/cities/<id>', methods=['GET'], strict_slashes=False)
def get_city(id):
    """Get specific City"""
    city = storage.get('City', id)
    if not city:
        abort(404)

    return jsonify(city.to_dict())


@blood_map.route('/cities', methods=['POST'], strict_slashes=False)
def register_city():
    """Register new city"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    if 'country_id' not in request.get_json():
        abort(400, description="Missing country Id")

    data = request.get_json()
    city = City(**data)
    storage.add(city)
    storage.commit()

    return make_response(jsonify(city.to_dict()), 201)


@blood_map.route('/cities/<id>', methods=['PUT'], strict_slashes=False)
def update_city(id):
    """ Updates City information. """
    city = storage.get('City', id)
    
    if not city:
        abort(404)
        
    if not request.get_json():
        abort(400, description='Not a JSON')
        
    ignore = ['id', 'email', 'create_at', 'updated_at', 'name', 'country_id']
    
    data = request.get_json()
    for key, val in data.items():
        if key not in ignore:
            setattr(city, key, val)
    
    storage.commit()

    return make_response(jsonify(city.to_dict()), 201)


@blood_map.route('/cities/<id>', methods=['DELETE'], strict_slashes=False)
def remove_city(id):
    """ Remove City """
    city = storage.get('City', id)
    if not city:
        abort(404)
    
    storage.delete(city)
    storage.commit()

    return make_response(jsonify({'Deleted': 'Done'}), 200)
