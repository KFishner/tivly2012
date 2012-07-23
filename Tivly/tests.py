"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from CardSpringActions import * 
from Tivly.models import *
from Tivly.views import *
import urllib2
import urllib
import json
import httplib
import unicodedata
import httplib2
from web1 import settings
from urlparse import parse_qsl
request = {}
#storeID ='cFHuUBk9qSCM'
#bID = 'l5sxg80QSa7O'
#appid = 'NLWgAaWVclvK'
#newappid = 'kpj90OAR8sg9'
#cardNumber='8886854754588888'
#exp= '2015-10'
#ctoken = '4S83TJXk0Ky8'
#l4='8888'
#csid = 'J2ON89'   
#request = {}
#values = {'card_token':ctoken,'event_type':'settlement','amount':'2000','business_id':bID}
#############################################
#csid = 'PLZBS0'
#DeleteAUser(csid)
#csu = CardSpringUser.objects.get(csID = csid)
#csu.delete()
#print 'csu deleted'
#fbu = FBUser.objects.get(first_name = 'Bryan')
#token = FBAccessTokens.objects.get(user = fbu)
#token.delete()
#print 'token deleted'
#Fbf = FBFriends.objects.filter(user = fbu)
#for f in Fbf:
#    f.delete()
#print 'friends deleted!'    
#myr = MyRewards.objects.filter(csID = csid)
#
#for r in myr:
#    r.delete()
#    print 'reward deleted'
#
#fbu.delete()
#print 'fb deleted'
#
#print 'you\'re wiped !'
#

#response = createACard('5RVRHK','1129384599856','2020-03')
CSUser = CardSpringUser(request)
print CSUser.myRewards





    