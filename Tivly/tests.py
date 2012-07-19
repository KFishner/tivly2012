"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from CardSpring import * 
from Tivly.models import *
from Tivly.views import *
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

#print ListApps(bID).read()
#print DeleteAUserApp(csid,newappid)

#print GetAppConnections(csid).read()
print DeleteAUserApp(csid,newappid)

def Strip(csid,fn):
    rewardsList = MyRewards.objects.filter(csID =csid)
    for reward in rewardsList:
        reward.delete()
    
    csUser = CardSpringUser.objects.filter(csID = csid)
    csUser.delete()
    DeleteAUser(csid)
    
    fbUser = FBUser.objects.filter(first_name = fn)
    fbUser.delete()
    
    