# routes.py
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.users import db, User
from models.books import db,Book,book_category
from models.author import Author
import json
from schemas.aurthor import author_schema,authors_schema

aurthor = Blueprint('aurthor', __name__)

@aurthor.route('/', methods=['POST','GET'])
@jwt_required()
def add_get_author():
    if request.method=='POST':
        current_user_id = get_jwt_identity()
        data = request.get_json()
        _author_first_name = data.get('first_name',None)
        _author_last_name = data.get('last_name',None)
        if _author_last_name is not None and _author_first_name is not None:    
            aurthor=Author(author_first_name=_author_first_name,author_last_name=_author_last_name,created_by=current_user_id)
            db.session.add(aurthor)
            db.session.commit()
            return author_schema.jsonify(aurthor), 201   
         
    aurthors = Author.query.filter_by(is_deleted=False)
    return authors_schema.jsonify(aurthors)
   

@aurthor.route('/<int:author_id>', methods=['PUT','GET'])
@jwt_required()
def get_update_aurthor(author_id):
    current_user_id = get_jwt_identity()
    aurthor=Author.query.filter_by(id=author_id,is_deleted=False).first()
    if aurthor is None:
        return  "No Aurthor Found match this id", 404
    if request.method=='PUT':
        data = request.get_json()
        aurthor.author_first_name=data.get("first_name",aurthor.author_first_name)
        aurthor.author_last_name=data.get("last_name",aurthor.author_last_name)
        aurthor.updated_by=current_user_id

        db.session.commit()
    try:
        
        author_data = author_schema.dump(aurthor)
        return author_data, 200
        
    except:
        return "No Aurthor", 400

@aurthor.route('/delete/<int:author_id>', methods=['DELETE'])
@jwt_required()
def get_cuurent_user(author_id):

    current_user_id = get_jwt_identity()
    aurthor=Author.query.get(author_id)
   
    if aurthor is None:
        return  "No Aurthor Found match this id", 404
    aurthor.is_deleted=True
    aurthor.updated_by=current_user_id
    db.session.commit()
    return "Deleted Succefully", 200