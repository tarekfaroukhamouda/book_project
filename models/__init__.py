from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .users import User
from .category import Category
from .author import Author
from .books import Book