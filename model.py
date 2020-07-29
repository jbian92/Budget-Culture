import requests

def getPlaces(genres, key):
    location = "40.7489,-73.9680" # united nations
    radius = 16100 # about 10 miles
    places = {}

    for genre in genres:
        request_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={genre}&key={key}"
        response = requests.get(request_url).json()
        results = response["results"]
        places.update({genre: results})
    
    return places


    # https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.7489,-73.9680&radius=50000&type=movie_theater&key=AIzaSyB_VVeMFaOFWa9_AuOjHX-zy6N0Y9txPoE

    # https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=1500&type=restaurant&keyword=cruise&key=AIzaSyB_VVeMFaOFWa9_AuOjHX-zy6N0Y9txPoE