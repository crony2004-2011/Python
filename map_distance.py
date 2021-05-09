from pygeocoder import Geocoder
from geopy.geocoders import Nominatim

def distance(zipcode1,zipcode2):
    from geopy import distance
    zipcode1 = "Los Angeles"
    zipcode2 = "San Diego"
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(zipcode1)
    location2 = geolocator.geocode(zipcode2)
    x = location.latitude,location.longitude
    y = location2.latitude,location2.longitude
    net_distance = distance.distance(x,y).km
    print(round(net_distance,0))
#WE HAVE CREATED A FUNCTION TO MEASURE DISTANCE BETWEEN ANY TWO PLACES
distance('New Delhi','Rohtak')