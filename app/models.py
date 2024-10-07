from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Complaints(db.Model):
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_data = db.Column(db.LargeBinary, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, location, description, image_data, user_id):
        self.location = location
        self.description = description
        self.image_data = image_data
        self.user_id = user_id
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,  primary_key=True)
    email = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    Complaints= db.relationship('Complaints')

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname}>'
