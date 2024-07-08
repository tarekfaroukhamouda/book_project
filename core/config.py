import os
from pathlib import Path
from dotenv import load_dotenv

path_env=Path('.')/".env"
load_dotenv(dotenv_path=path_env)
class Settings:
    PROJECT_NAME="Book Mangment"
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///book.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'myjwtsecretkey')  # Change this!

settings=Settings()