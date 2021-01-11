"""
Routes and views for the flask application.
"""
from FlaskWebProject1.service.cosmosdbservice  import cosmosdbservice
from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
from flask import jsonify
from flask import request

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/api/v1.0/processing/telemetry', methods=['POST'])
def create_newEntry():
    serialId = request.form['serialId']
    location = request.form['location']
    timestamp = request.form['timestamp']
    service = cosmosdbservice()
    service.updateLocation(serialId,location,timestamp)
    resp = jsonify(success=True)
    return resp

    
    
    