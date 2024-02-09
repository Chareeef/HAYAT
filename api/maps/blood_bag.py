#!/usr/bin/python3
"""
Manipulate blood Bags.
"""
from api.maps import blood_map
from db import storage
from db.models import BloodBag
from flask import jsonify, request, make_response, abort


@blood_map.route('/blood_bags', methods=['GET'], strict_slashes=False)
def list_blood_bags():
    """List Blood bags"""
    blood_bags = []
    all_objs = storage.all('BloodBag')
    for obj in all_objs:
        blood_bags.append(obj.to_dict())

    return jsonify(blood_bags)


@blood_map.route('/blood_bags/<id>', methods=['GET'], strict_slashes=False)
def get_blood_bag(id):
    """Get specific blood bags"""
    bags = storage.get('BloodBag', id)
    if not bags:
        abort(404)

    return jsonify(bags.to_dict())


@blood_map.route('/blood_bags', methods=['POST'], strict_slashes=False)
def new_blood_bag():
    """Register new blood bag"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'blood_category' not in request.get_json():
        abort(400, description="Blood Category")
    if 'center_id' not in request.get_json():
        abort(400, description="Center Id")

    data = request.get_json()
    bag = BloodBag(**data)
    storage.add(bag)
    storage.commit()

    return make_response(jsonify(bag.to_dict()), 201)


@blood_map.route('/blood_bags/<id>', methods=['PUT'], strict_slashes=False)
def update_blood_bag(id):
    """ Updates Blood Bags State. """
    bag = storage.get('BloodBag', id)

    if not bag:
        abort(404)

    if not request.get_json():
        abort(400, description='Not a JSON')

    ignore = [
        'id',
        'email',
        'create_at',
        'updated_at',
        'center_id',
        'blood_category']

    data = request.get_json()
    for key, val in data.items():
        if key not in ignore:
            setattr(bag, key, val)

    storage.commit()

    return make_response(jsonify(bag.to_dict()), 201)


@blood_map.route('/blood_bags/<id>', methods=['DELETE'], strict_slashes=False)
def delete_bags(id):
    """ Remove blood bags. """
    bag = storage.get('BloodBag', id)
    if not bag:
        abort(404)

    storage.delete(bag)
    storage.commit()

    return make_response(jsonify({'Deleted': 'Done'}), 200)
