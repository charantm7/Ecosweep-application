from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db_name = 'signup.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='charantm@gmail.com'
    app.config['SQLALCHEMY_DATABASE_URI']=  f'sqlite:///{db_name}' 
    db.init_app(app)

    from .userview import user_interface
    from .auth import Auth

    app.register_blueprint(user_interface, url_prefix="/")
    app.register_blueprint(Auth, url_prefix="/")

    return app