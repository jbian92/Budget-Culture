from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, session
from datetime import datetime
import os

# -- Initialization section --
app = Flask(__name__)

app.config['PLACES_KEY'] = "AIzaSyB_VVeMFaOFWa9_AuOjHX-zy6N0Y9txPoE"

# -- Routes --
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html', time = datetime.now())


@app.route('/description', methods = ['POST', 'GET'])
def description():
    if request.method == 'POST':
        return render_template('description.html', time = datetime.now())