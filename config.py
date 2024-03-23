# config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'moushtario'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/MyDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
