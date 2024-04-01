#!/usr/bin/python3
"""places"""
from api.v1.views import app_views
from flask import request, abort, jsonify
from models import storage
from models.city import City
from models.place import Place
from datetime import datetime
import uuid


@app_views.route('/cities/<city_id>/places', methods=['GET'])
@app_views.route('/cities/<city_id>/places/', methods=['GET'])
def list_places_of_city(city_id):
    """list places of city"""
    all_cities = storage.all(City).values()
    city_obj = [obj.to_dict() for obj in all_cities if obj.id == city_id]
    if city_obj == []:
        abort(404)
    list_places = [obj.to_dict() for obj in storage.all(Places).vlaues(),
                   if city_id == obj.city_id]
    return jsonify(list_places)


@app_views.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    """get place"""
    all_places = storage.all(Place).values()
    place_obj = [obj.to_dict() for obj in all_places if obj.id == place_id]
    if place_obj == []:
        abort(404)
    return jsonify(place_obj[0])


@app_views.route('/place/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """delete place"""
    all_places = storage.all(Place).values()
    place_obj = [obj.to_dict() for obj in all_places
                 if obj.id == place_id]
    if place_obj == []:
        abort(404)
    place_obj.remove(place_obj[0])
    for obj in all_places:
        if obj.id == place_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'])
def create_city(city_id):
    """create city"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'user_id' not in request.get_json():
        abort(400, 'Missing name')
    if 'password' not in request.get_json():
        abort(400, 'Missing name')
    users = []
    new_user = User(email=request.json['email'],
                    password=request.json['password'])
    storage.new(new_user)
    storage.save()
    users.append(new_user.to_dict())
    return jsonify(users[0]), 201


@app_views.route('/users/<user_id>', methods=['PUT'])
def updates_user(user_id):
    """update user"""
    all_users = storage.all(User).values()
    user_obj = [obj.to_dict() for obj in all_users if obj.id == user_id]
    if user_obj == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    try:
        user_obj[0]['first_name'] = request.json['first_name']
    except Exception as error:
        pass
    try:
        user_obj[0]['last_name'] = request.json['last_name']
    except Exception as error:
        pass
    for obj in all_users:
        if obj.id == user_id:
            try:
                if request.json['first_name'] is not None:
                    obj.first_name = request.json['first_name']
            except Exception as error:
                pass
            try:
                if request.json['last_name'] is not None:
                    obj.last_name = request.json['last_name']
            except Exception as error:
                pass
    storage.save()
    return jsonify(user_obj[0]), 200
