from . import db
from flask_login import UserMixin

class complaints(db.models):
    id = db.Column(db.Integer, primary_key=True)
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255),nullable=True,unique=True)
    password = db.Column(db.String(255),nullable=True,unique=True)
    first_name = db.Column(db.String(255),nullable=True)
