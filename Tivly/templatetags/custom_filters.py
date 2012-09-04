from django import template
from datetime import date
register = template.Library()



def externalurl(internalurl):
    try:
        external = "https://www.tivly.com" + str(internalurl) 
        return external
    except Exception as e:
        print str(e)
        return ""
register.filter('externalurl', externalurl)






