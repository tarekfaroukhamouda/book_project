from models.author import Author
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        include_fk = True

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)