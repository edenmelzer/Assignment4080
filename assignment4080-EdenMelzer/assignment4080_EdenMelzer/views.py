"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from assignment4080_EdenMelzer import app

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
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='About',
        year=datetime.now().year,
        message='Your about page - the top rated players in FIFA 19.'
    )

@app.route('/gallery')
def gallery():
    """Renders the about page."""
    return render_template(
        'gallery.html',
        title='Gallery',
        year=datetime.now().year,
        message='These are the top rated players from my favorite team FC Barcelona.'
    )
