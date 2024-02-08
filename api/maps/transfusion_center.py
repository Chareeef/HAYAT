#!/usr/bin/python3
"""
Manipulate Transfusion center..
"""
from api.maps import blood_map
from db import storage
from db.models import TransfusionCenter
from flask import jsonify, make_response, request, abort


@blood_map.route('/transfusion_centers', methods=['GET'], strict_slashes=False)
def list_centers():
    """List Transfusion centers"""
    centers_l = []
    all_objs = storage.all('TransfusionCenter')
    for obj in all_objs:
        centers_l.append(obj.to_dict())

    return jsonify(centers_l)


@blood_map.route(
    '/transfusion_centers/<id>',
    methods=['GET'],
    strict_slashes=False)
def get_transfusion_center(id):
    """Get specific transfusion_center"""
    transfusion_center = storage.get('TransfusionCenter', id)
    if not transfusion_center:
        abort(404)

    return jsonify(transfusion_center.to_dict())


@blood_map.route(
    '/transfusion_centers',
    methods=['POST'],
    strict_slashes=False)
def create_transfusion_center(route_data=None):
    """Register new transfusion center"""
    if not route_data:
        if not request.get_json():
            abort(400, description="Not a JSON")

        if 'email' not in request.get_json():
            abort(400, description="Missing email")
        if 'password_hash' not in request.get_json():
            abort(400, description="Missing password")
        if 'coordinates' not in request.get_json():
            abort(400, description="Missing coordinates")
        data = request.get_json()
    else:
        data = route_data

    transfusion_center = TransfusionCenter(**data)
    storage.add(transfusion_center)
    storage.commit()

    return make_response(jsonify(transfusion_center.to_dict()), 201)


@blood_map.route(
    '/transfusion_centers/<id>',
    methods=['PUT'],
    strict_slashes=False)
def update_transfusion_center(id):
    """ Updates transfusion center information. """
    transfusion_center = storage.get('TransfusionCenter', id)

    if not transfusion_center:
        abort(404)

    if not request.get_json():
        abort(400, description='Not a JSON')

    ignore = ['id', 'create_at', 'updated_at']

    data = request.get_json()
    for key, val in data.items():
        if key not in ignore:
            setattr(transfusion_center, key, val)

    storage.commit()

    return make_response(jsonify(transfusion_center.to_dict()), 201)


@blood_map.route(
    '/transfusion_centers/<id>',
    methods=['DELETE'],
    strict_slashes=False)
def delete_transfusion_center(id):
    """ remove transfusion center. """
    transfusion_center = storage.get('TransfusionCenter', id)
    if not transfusion_center:
        abort(404)

    storage.delete(transfusion_center)
    storage.commit()

    return make_response(jsonify({'Deleted': 'Done'}), 200)
