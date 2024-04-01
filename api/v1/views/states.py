#!/usr/bin/python3
"""states"""
from api.v1.views import app_views
from flask import request, abort, jsonify
from models import storage
from models.state import State
from datetime import datetime
import uuid


app.url_map.strict_slashes = False


@app_views.route('/states/', methods=['GET'])
def list_states():
    """list states"""
    list_states = [obj.to_dict() for obj in storage.all(State).values()]
    return jsonify(list_states)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """get state"""
    all_states = storage.all(State).values()
    states_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if states_obj == []:
        abort(404)
    return jsonify(states_obj[0])


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """delete state"""
    all_states = storage.all(State).values()
    states_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if states_obj == []:
        abort(404)
    states_obj.remove(states_obj[0])
    for obj in all_states:
        if obj.id == state_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'])
def create_state():
    """create state"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    states = []
    new_state = State(name=request.json['name'])
    storage.new(new_state)
    storage.save()
    states.append(new_state.to_dict())
    return jsonify(states[0]), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """update state"""
    all_states = storage.all(State).values()
    states_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if states_obj == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    states_obj[0]['name'] = request.json['name']
    for obj in all_states:
        if obj.id == state_id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(state_obj[0]), 200
