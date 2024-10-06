from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Complaints(db.Model):
    complaint_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.LargeBinary)
    description = db.Column(db.Text(1000))
    longitude = db.Column(db.Float(200))
    latitude = db.Column(db.Float(200))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,  primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    Complaints= db.relationship('Complaints')
