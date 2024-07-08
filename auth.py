# routes.py
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.users import db, User
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    _email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=_email).first():
        return jsonify({"message": "User already exists"}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(email=_email, password=hashed_password,is_active=True)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    _email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=_email,is_active=True).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200
@jwt_required()

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def get_cuurent_user():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify(logged_in_as=user.email), 200