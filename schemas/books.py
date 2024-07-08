from models.books import Book
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        include_fk = True

book_schema = BookSchema()
books_schema = BookSchema(many=True)