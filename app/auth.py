from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,logout_user,current_user,login_required

Auth = Blueprint('Auth',__name__)

@Auth.route('/signup',methods=['POST','GET',])
def signup():
    if request.method=='POST':
        email=request.form.get('email')
        name=request.form.get('first_name')
        pass1=request.form.get('password')
        pass2=request.form.get('confirmpassword')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist.', category='error')
        
        elif not email:
            flash('Please enter correct email address ex: @gmail.com',category='error')
        elif len(name) <=2:
            flash('Name should be greater than 2 characters!',category='error')
        elif len(pass1) <=6:
            flash('Password should be greater than 6 characters!',category='error')
        elif pass1 != pass2:
            flash('Password mismatch!', category='error')
        else:
            new_user = User(email=email,name=name,password=generate_password_hash(pass1,method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user()
            flash('Account created!', category='success')
            return redirect(url_for('user_interface.home'))
        
    return render_template('usersignup.html',user=current_user)

@Auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                login_user(user, remember=True)
                flash('Logged in successfully!', category='success')
                return redirect(url_for('user_interface.home'))
            else:
                flash('Incorrect password, try again!', category='error')
        else:
            flash('Email does not exist!', category='error')
        
    return render_template('userlogin.html',user=current_user)

@Auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('Auth.login'))
