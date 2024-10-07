from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import login_required,current_user
from.models import Complaints
from . import db
import os

user_interface = Blueprint('user_interface',__name__)

@user_interface.route('/')
def home():
    return render_template('home.html', user=current_user)

@user_interface.route('/raisecomplaint')
@login_required
def raisecomplaint():
    return render_template('raise_complaint.html')



