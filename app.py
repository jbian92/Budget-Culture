from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, session
from datetime import datetime
from model import getPlaces
#import os


# -- Initialization section --
app = Flask(__name__)

app.config['PLACES_KEY'] = "AIzaSyB_VVeMFaOFWa9_AuOjHX-zy6N0Y9txPoE"


# -- Variables --
genres = {
     "amusement_park": {"title": "Amusement Parks", "carid": "", "carhref": ""},
     "aquarium": {"title": "Aquariums", "carid": "", "carhref": ""},
     "art_gallery": {"title": "Art Galleries", "carid": "", "carhref": ""},
     "bakery": {"title": "Bakeries", "carid": "", "carhref": ""},
     "bar": {"title": "Bars", "carid": "", "carhref": ""},
     "book_store": {"title": "Book Stores", "carid": "", "carhref": ""},
     "bowling_alley": {"title": "Bowling Allies", "carid": "", "carhref": ""},
     "cafe": {"title": "Cafes", "carid": "", "carhref": ""},
     "campground": {"title": "Campgrounds", "carid": "", "carhref": ""},
     "casino": {"title": "Casinos", "carid": "", "carhref": ""},
     "clothing_store": {"title": "Clothing Stores", "carid": "", "carhref": ""},
     "department_store": {"title": "Department Stores", "carid": "", "carhref": ""},
     "library": {"title": "Libraries", "carid": "", "carhref": ""},
     "movie_theater": {"title": "Movie Theaters", "carid": "", "carhref": ""},
     "night_club": {"title": "Night Clubs", "carid": "", "carhref": ""},
     "park": {"title": "Parks", "carid": "", "carhref": ""},
     "restaurant": {"title": "Restaurants", "carid": "", "carhref": ""},
     "shopping_mall": {"title": "Shopping Malls", "carid": "", "carhref": ""},
     "spa": {"title": "Spas", "carid": "", "carhref": ""},
     "store": {"title": "Stores", "carid": "", "carhref": ""},
     "tourist_attraction": {"title": "Tourist Attractions", "carid": "", "carhref": ""},
     "zoo": {"title": "Zoos", "carid": "", "carhref": ""}
}

types = list(genres.keys())

# -- Routes --
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', time = datetime.now())

@app.route('/homepage')
def homepage():
    set_carvars()
    places = getPlaces(types, app.config['PLACES_KEY'])
    print(places)

    return render_template('homepage.html', genres = genres, types = types, places = places, time = datetime.now())

def set_carvars():
    for genre in genres:
        genres[genre]["carid"] = "carouselExampleControls" + str(types.index(genre))
        genres[genre]["carhref"] = "#carouselExampleControls" + str(types.index(genre))


@app.route('/description', methods = ['POST', 'GET'])
def description():
    if request.method == 'POST':
        return render_template('description.html', time = datetime.now())
    else:
        return "error"