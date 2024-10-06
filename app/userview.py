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

@user_interface.route('/submit_complaint')
def submit_complaint():
    if request.method == 'POST':
        location = request.form['location']
        description = request.form['description']
        
        # Get the Base64 image data
        base64_image = request.form['image']
        
        # Extract the image data from the string
        header, encoded = base64_image.split(',', 1)
        image_data = base64.b64decode(encoded)
        
        # Save the image file (ensure you have appropriate file handling)
        filename = secure_filename('complaint_image.png')  # You can create unique filenames if needed
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        with open(filepath, 'wb') as f:
            f.write(image_data)
        
        # Store data in the database
        new_complaint = Complaints(location=location, description=description, image_url=filepath)
        db.session.add(new_complaint)
        db.session.commit()

        flash('Complaint submitted successfully!')
        return redirect(url_for('complaint_success'))  # Redirect to a success page

