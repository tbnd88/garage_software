from flask import Blueprint, request, jsonify
from extensions import db
from models import Customer

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    customer = Customer(name=data['name'], phone=data.get('phone'), email=data.get('email'))
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_dict()), 201

@customers_bp.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([c.to_dict() for c in customers])
