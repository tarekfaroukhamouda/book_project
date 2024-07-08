from . import db


class Category(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20), unique=True, nullable=False)
    def __repr__(self):
        return f"Name : {self.author_first_name} {self.author_last_name}"