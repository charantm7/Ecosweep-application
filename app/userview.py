from flask import Blueprint,render_template

user_interface = Blueprint('user_interface',__name__)

@user_interface.route('/')
def home():
    return render_template('home.html')

@user_interface.route('/raisecomplaint')
def raisecomplaint():
    return render_template('raise_complaint.html')
