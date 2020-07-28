from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, session
from datetime import datetime
#import os


# -- Initialization section --
app = Flask(__name__)

app.config['PLACES_KEY'] = "AIzaSyB_VVeMFaOFWa9_AuOjHX-zy6N0Y9txPoE"


# -- Variables --
genres = [
    "amusement_park", "aquarium", "art_gallery", 
    "bakery" , "bar" , "book_store" , "bowling_alley", 
    "cafe", "campground", "casino", "clothing_store", "convenience_store", 
    "department_store", "drugstore", 
    "electronics_store", 
    "furniture_store", 
    "hair_care", "home_goods_store", 
    "jewelry_store", 
    "library", "liquor_store", 
    "movie_theater"
]


# -- Routes --
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html', genres = genres, time = datetime.now())


@app.route('/description', methods = ['POST', 'GET'])
def description():
    if request.method == 'POST':
        return render_template('description.html', time = datetime.now())