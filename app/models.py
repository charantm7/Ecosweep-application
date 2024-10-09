from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Complaints(db.Model):
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    img1=db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    
    def __init__(self,location,description,user_id,img1):
        self.location = location
        self.description = description
        self.user_id = user_id
        self.img1=img1

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,  primary_key=True)
    email = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    Complaints= db.relationship('Complaints')

