from flask import Blueprint, request, jsonify
from autos_data import autos_data

automobiles_bp = Blueprint('automobile', __name__)


@automobiles_bp.route('/')
def index():
    return { 'all_autos': autos_data }



@automobiles_bp.route('/<int:idx>/')
def show(idx):
    return { 'auto': autos_data[idx] }



@automobiles_bp.route('/', methods=['POST'])
def create():

    # Access JSON data
    make = request.json['make']
    model = request.json['model']

    # Access form data
    # make = request.form['make']
    # model = request.form['model']

    autos_data.append({
        'make': make,
        'model': model
    })

    return { 'message': 'created automobile' }



@automobiles_bp.route('/<int:idx>/', methods=['PUT'])
def update(idx):
    update_dict = {}
    if 'make' in request.json:
        update_dict['make'] = request.json['make']
    
    if 'model' in request.json:
        update_dict['model'] = request.json['model']

    autos_data[idx].update(update_dict)

    return autos_data[idx]



@automobiles_bp.route('/<int:idx>/', methods=['DELETE'])
def delete(idx):
    autos_data.pop(idx)

    return jsonify(autos_data)
