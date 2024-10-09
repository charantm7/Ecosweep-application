from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User, Complaints
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,logout_user,current_user,login_required
import base64
import os
from io import BytesIO


Auth = Blueprint('Auth',__name__)



@Auth.route('/signup',methods=['POST','GET'])
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
        elif len(pass1) <=4:
            flash('Password should be greater than 6 characters!',category='error')
        elif pass1 != pass2:
            flash('Password mismatch!', category='error')
        else:
            new_user = User(email=email,name=name,password=generate_password_hash(pass1,method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
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

@Auth.route('/profile/<int:id>')
@login_required
def profile(id):
    user = User.query.get(id)
    return render_template('profile.html',user=user)

@Auth.route('/submit_complaint', methods=['POST', 'GET'])
@login_required
def submit_complaint():
    if request.method == 'POST':
        location = request.form.get('location')
        description = request.form.get('description')

        image_data = None
        if 'cameraOutput' in request.form and request.form['cameraOutput']:
            image_base64 = request.form['cameraOutput'].split(',')[1] 
            image_data = base64.b64decode(image_base64) 

        new_complaint = Complaints(
            location=location, 
            description=description, 
            user_id=current_user.id, 
            image_data=image_data
        )

        db.session.add(new_complaint)
        db.session.commit()

        flash('Complaint submitted successfully!', category='success')
        return redirect(url_for('user_interface.home'))

    return redirect(url_for('user_interface.home'))


@Auth.route('/admin_panel')
@login_required
def admin_panel():
    if current_user.id == 1:
        complaints = Complaints.query.all()

        for complaint in complaints:
            if complaint.image_data:
                complaint.image_data = base64.b64encode(complaint.image_data).decode('utf-8')

        return render_template('admin.html', complaints=complaints)
    
    return render_template('404.html')



    




