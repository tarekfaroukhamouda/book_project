from . import db

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"User : {self.username}"
    