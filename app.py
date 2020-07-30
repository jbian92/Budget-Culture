from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, session
from datetime import datetime
from model import getPlaces, getPhotos
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
places = getPlaces(types, app.config['PLACES_KEY'])
photos = getPhotos(places, app.config['PLACES_KEY'])

# -- Routes --
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', time = datetime.now())

@app.route('/homepage')
def homepage():
    set_genre_vars()
    
    return render_template('homepage.html', genres = genres, types = types, places = places, photos = photos, time = datetime.now())

def set_genre_vars():
    for genre in genres:
        genres[genre]["carid"] = "carouselExampleControls" + str(types.index(genre))
        genres[genre]["carhref"] = "#carouselExampleControls" + str(types.index(genre))


@app.route('/searchdescription', methods = ['POST', 'GET'])
def description():
    if request.method == 'POST':
        name = request.form["place_name"]
        for place_type in places:
            for place in places[place_type]:
                if place["name"] == name:
                    return render_template('description.html', place_type = place_type, time = datetime.now())
    else:
        return "error"