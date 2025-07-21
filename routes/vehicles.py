from flask import Blueprint, request, jsonify, abort
from extensions import db
from models import vehicle, customer

vehicles_bp = Blueprint('vehicles', __name__, url_prefix='/vehicles')

@vehicles_bp.route('/add/<int:customer_id>', methods=['POST', 'GET'])
def add_vehicle(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        abort(404, description='Customer not found')

    data = request.get_json() if request.method == 'POST' else request.args

    vin = data.get('vin')
    make = data.get('make')
    model = data.get('model')
    year = data.get('year')
    color = data.get('color')
    license_plate = data.get('license_plate')

    if not vin or not make or not model or not year:
        return jsonify({'error': 'vin, make, model, and year are required'}), 400

    vehicle = Vehicle(
        vin=vin,
        make=make,
        model=model,
        year=int(year),
        color=color,
        license_plate=license_plate,
        customer=customer
    )

    db.session.add(vehicle)
    db.session.commit()

    return jsonify({
        'message': 'Vehicle added',
        'vehicle': {
            'id': vehicle.id,
            'vin': vehicle.vin,
            'make': vehicle.make,
            'model': vehicle.model,
            'year': vehicle.year,
            'color': vehicle.color,
            'license_plate': vehicle.license_plate,
            'customer_id': vehicle.customer_id
        }
    }), 201
