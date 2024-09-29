from flask import Blueprint,render_template,request

Auth = Blueprint('Auth',__name__)

@Auth.route('/signup')
def signup():
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
    return render_template('logut.html')
