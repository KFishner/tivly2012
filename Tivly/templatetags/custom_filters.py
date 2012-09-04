from django import template
from datetime import date
register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def externalurl(internalurl):
    try:
        external = "https://www.tivly.com" + str(internalurl) 
        return external
    except Exception as e:
        print str(e)
        return ""







