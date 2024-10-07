from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager

db = SQLAlchemy()
db_name = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    from .userview import user_interface
    from .auth import Auth

    app.register_blueprint(user_interface, url_prefix="/")
    app.register_blueprint(Auth, url_prefix="/")

    from .models import User


    with app.app_context():
        create_database()

    login_manager = LoginManager()
    login_manager.login_view = 'Auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(int(id))

    return app

def create_database():
    if not path.exists('Ecosweep-application/' + db_name):
        db.create_all()
        print('Database created')
