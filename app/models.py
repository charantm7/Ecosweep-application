from . import db
from flask_login import UserMixin
from sqlalchemy import func

class complaints(db.models):
    complaint_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.column(db.LargeBinary, nullable=False)
    description = db.column(db.Text, nullable=False)
    longitude = db.column(db.Float, nullable=False)
    latitude = db.column(db.Float, nullable=False)
    date = db.column(db.DateTime(timezone=True), default=func.now())
    
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255),nullable=True,unique=True)
    password = db.Column(db.String(255),nullable=True,unique=True)
    first_name = db.Column(db.String(255),nullable=True)
