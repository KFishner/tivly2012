'''
Created on Jul 22, 2012

@author: bryanantigua
'''

from web1 import settings
from googlemaps import GoogleMaps
from Tivly.models import Businesses

    
def getMap(businessid):
    GOOGLEMAPS_API_KEY = settings.GOOGLEMAPS_API_KEY
    gmaps = GoogleMaps(GOOGLEMAPS_API_KEY)
    business = Businesses.objects.filter(businessID = businessid)[0]
    address = business.street + ' ' + business.city + ' ' + str(business.zipCode)
    lat, lng = gmaps.address_to_latlng(address)
    return lat,lng
        
        