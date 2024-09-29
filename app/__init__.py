from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='charantm@gmail.com'

    from .userview import user_interface
    from .auth import Auth

    app.register_blueprint(user_interface, url_prefix="/")
    app.register_blueprint(Auth, url_prefix="/")

    return app