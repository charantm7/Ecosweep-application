from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os

db = SQLAlchemy()
db_name = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)

    from .userview import user_interface
    from .auth import Auth

    app.register_blueprint(user_interface, url_prefix="/")
    app.register_blueprint(Auth, url_prefix="/")

    from .models import User, Complaints


    with app.app_context():
        create_database()

    return app

def create_database():
    if not path.exists('Ecosweep-application/' + db_name):
        db.create_all()
        print('Database created')
