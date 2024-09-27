from flask import Flask,blueprints

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='charantm@gmail.com'

    return app