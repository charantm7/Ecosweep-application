from flask import Blueprint,render_template,request,flash

Auth = Blueprint('Auth',__name__)

@Auth.route('/signup',methods=['POST','GET',])
def signup():
    if request.method=='POST':
        email=request.form.get('email')
        name=request.form.get('first_name')
        pass1=request.form.get('password')
        pass2=request.form.get('confirmpassword')
        print(email,name,pass1,pass2)

        if pass1 != pass2:
            flash('Invalid password')
    return render_template('usersignup.html')

@Auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print("Email: ",email)
        print("password: ",password)
    return render_template('userlogin.html',boolean=True)

@Auth.route('/logout')
def logout():
    return render_template('hi.html')
