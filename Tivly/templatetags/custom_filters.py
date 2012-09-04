from django import template
from datetime import date
register = template.Library()

"""given a birthday, return the age of the swimmer"""
def externalurl(internalurl):
    external = "https://www.tivly.com" + str(internalurl) 
    return external
register.filter('externalurl', externalurl)







