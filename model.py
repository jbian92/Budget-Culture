import requests

def getPlaces(placeTypes, key):
    location = "40.7489,-73.9680" # united nations
    radius = 16100 # about 10 miles
    places = {}

    for placeType in placeTypes:
        request_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={placeType}&key={key}"
        response = requests.get(request_url).json()
        results = response["results"]
        places.update({placeType: results})
    
    return places

def getPhotos(places, key):
    maxwidth = 300 # based on card width in homepage.html
    photos = {}

    for placeType in places:
        type_urls = []
        for place in places[placeType]:
            image_url = "https://via.placeholder.com/150" # default image
            if "photos" in place.keys():
                photoreference = place["photos"][0]["photo_reference"]
                image_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={maxwidth}&photoreference={photoreference}&key={key}"
            type_urls.append(image_url)
        photos.update({placeType: type_urls})
    
    return photos