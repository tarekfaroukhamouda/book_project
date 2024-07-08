# routes.py
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.users import db, User
from models.books import db,Book,book_category
from schemas.books import book_schema,books_schema
from models.category import Category
books = Blueprint('books', __name__)


@books.route('/', methods=['POST','GET'])
@jwt_required()
def add_get_book():
    if request.method=='POST':
        current_user_id = get_jwt_identity()
        data = request.get_json()
        _book_ispn=data.get('book_ispn')
        _book_title=data.get("book_title")
        _author_id=data.get('author_id')
        _category_ids=data.get('category',[])
        _book_page_numbers=data.get('book_page_numbers')

        if _book_ispn is not None and _book_title is not None and _author_id and _category_ids is not None:   
            _categories = Category.query.filter(Category.id.in_(_category_ids)).all()
        
            if len(_categories) != len(_category_ids):
                return jsonify({'error': 'One or more categories not found'}), 404
 
            book=Book(ISPN=_book_ispn[:20],book_title=_book_title,author_id=_author_id,book_page_numbers=_book_page_numbers,categories=_categories,created_by=current_user_id,updated_by=current_user_id,is_deleted=False)
            db.session.add(book)
            db.session.commit()
            return book_schema.jsonify(book), 201   
         
    books = Book.query.filter_by()
    return books_schema.jsonify(books)
   

@books.route('/<int:book_ispn>', methods=['PUT','GET'])
@jwt_required()
def get_update_book(book_ispn):
    current_user_id = get_jwt_identity()
    book=Book.query.filter_by(ISPN=book_ispn).first()
    if book is None:
        return  "No Book Found match this id", 404
    if request.method=='PUT':
        data = request.get_json()
        book.book_title=data.get("book_title",book.book_title)
        book.author_id=data.get("author_id",book.author_id)
        book.book_page_numbers=data.get("book_page_numbers",book.book_page_numbers)
        book.updated_by=current_user_id

        db.session.commit()
    try:
        
        book_data = book_schema.dump(book)
        return book_data, 200
        
    except:
        return "No Aurthor", 400


@books.route('category/<int:category_id>', methods=['GET'])
@jwt_required()
def get_book_by_catgory(category_id):
    books = Book.query \
                .join(book_category, Book.ISPN == book_category.c.ISPN) \
                .filter(book_category.c.category_id == category_id) \
                .all()
    if not books:
        return 'No books found for the given category ID', 404
    try:
        book_data = books_schema.dump(books)
        return book_data, 200
    except:
        return "No Aurthor", 400


@books.route('/delete/<int:book_ispn>', methods=['DELETE'])
@jwt_required()
def get_cuurent_user(book_ispn):

    current_user_id = get_jwt_identity()
    aurthor=Book.query.get(book_ispn)
   
    if aurthor is None:
        return  "No Book Found match this id", 404
    aurthor.is_deleted=True
    aurthor.updated_by=current_user_id
    db.session.commit()
    return "Deleted Succefully", 200