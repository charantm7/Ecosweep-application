import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max file size = 16MB
app.secret_key = 'your_secret_key'

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Initialize SQLite Database
def init_db():
    with sqlite3.connect("complaints.db") as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS complaints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location TEXT,
                description TEXT,
                image_path TEXT
            );
        """)

# Home route - displays the form
@app.route('/')
def index():
    return render_template('complaint.html')

# Route to handle the complaint submission
@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    # Get data from the form
    location = request.form.get('location')
    description = request.form.get('description')
    image = request.files.get('image')

    # Validate that location and description are provided
    if not location or not description:
        flash('Location and Description are required.')
        return redirect(url_for('index'))

    # Save the uploaded image (if any)
    image_path = None
    if image:
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)

    # Save the complaint data in the database
    with sqlite3.connect("complaints.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO complaints (location, description, image_path) VALUES (?, ?, ?)",
                    (location, description, image_path))
        con.commit()

    flash('Complaint submitted successfully!')
    return redirect(url_for('index'))

# API route to get all complaints (optional)
@app.route('/complaints', methods=['GET'])
def get_complaints():
    with sqlite3.connect("complaints.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM complaints")
        complaints = cur.fetchall()
    return jsonify(complaints)

@app.route('/view_complaints')
def view_complaints():
    with sqlite3.connect("complaints.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM complaints")
        complaints = cur.fetchall()
    return render_template('view_complaints.html', complaints=complaints)

if __name__ == '__main__':
    init_db()  # Initialize the database on startup
    app.run(debug=True)
