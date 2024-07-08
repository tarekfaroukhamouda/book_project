from . import db



class Author(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)
    author_first_name = db.Column(db.String(20), unique=False, nullable=False)
    author_last_name=db.Column(db.String(20), unique=False, nullable=False)
    image = db.Column(db.String(20))
    books = db.relationship('Book', backref='author', lazy=True)
    created_by=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    updated_by=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_deleted=db.Column(db.Boolean)


    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Name : {self.author_first_name} {self.author_last_name}"