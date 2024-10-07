from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Complaints(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_data = db.Column(db.LargeBinary, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,  primary_key=True)
    email = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    Complaints= db.relationship('Complaints')
