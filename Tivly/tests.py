"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from CardSpring import * 
from Tivly.models import *
#from DataBase import *
#TEST ENVIROMENT---------------
import urllib2
import urllib
import json
import httplib
import unicodedata
import httplib2
from web1 import settings



request = {}
storeID ='cFHuUBk9qSCM'
bID = 'l5sxg80QSa7O'
appid = 'NLWgAaWVclvK'
newappid = 'kpj90OAR8sg9'
cardNumber='8886854754588888'
exp= '2015-10'
ctoken = '4S83TJXk0Ky8'
l4='8888'
csid = 'J2ON89'   
request = {}
values = {'card_token':ctoken,'event_type':'settlement','amount':'2000','business_id':bID}

print DeleteAUserApp(csid,newappid)





###########################################################################################
#try:
#    
#except urllib2.HTTPError, e:
#        message = e.read()
#        try:
#            print json.loads(message)
#        except Exception:
#            try:
#                print e.read()
#            except Exception:
#                print e.code, e.message

#t = Transaction(date = result['date_time'] ,event_type = result['event_type'], businessID =result['business_id'],currency = result['USD'], amount = result['2000'],card_token = result['card_token'],transaction_id = result['id'], store_id =result['store_id'])

#r = Rewards.objects.filter(appID = appid)[0]
#mr = MyRewards(csID = csid, reward = r)
#mr.save()

#r = Rewards(description = "oi", businessID = bID, pointsNeeded =10)
##r.save()
#response = TestTransaction(values)
#result = json.load(response)
#print result


