
from . import db


book_category = db.Table('book_category',
    db.Column('ISPN', db.Integer, db.ForeignKey('book.ISPN'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)
class Book(db.Model):
   
    ISPN = db.Column(db.String, primary_key=True)
    book_title = db.Column(db.String(20), unique=False, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    book_page_numbers = db.Column(db.String(20), unique=False, nullable=False)
    categories = db.relationship('Category', secondary=book_category, backref=db.backref('books', lazy='dynamic'))
    created_by=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    updated_by=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_deleted=db.Column(db.Boolean)

    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Book : {self.book_title}, Author: {self.author}"