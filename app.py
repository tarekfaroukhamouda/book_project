from flask import Flask
from flask_jwt_extended import JWTManager
from models import db 
from core.config import Settings
from auth import auth_bp
from books import books
from aurthor import aurthor
def create_app():
    app = Flask(__name__)
    app.config.from_object(Settings)
    db.init_app(app)
    JWTManager(app)  
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(books, url_prefix='/books')
    app.register_blueprint(aurthor, url_prefix='/aurthor')

    @app.route('/')
    def hello():
        return "Hello, Flask!"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)