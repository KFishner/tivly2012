'''
Created on Jul 22, 2012

@author: bryanantigua
'''
from Tivly.models import Cards
import json

def validateCard(request):
    errors = []
    number = request.POST.get('number')
    if not number:
        errors.append('Enter a correct credit card number')
    
    month = request.POST.get('month')
    if not month:
        errors.append('Enter a correct month')
    
    year = request.POST.get('year')
    if not year:
        errors.append('Enter a correct year')
    
    if not errors:
        result = json.load(request.POST.get())
        d = Cards(csID=request.COOKIES.get('csID'), token=result['token'], last4=result['last4'], expDate=result['expiration'], cardType=result['type'], typeString=result['type_string'])
        d.save()
    else:
        return errors 