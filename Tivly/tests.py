"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from CardSpringActions import * 
from CSUserObject import *
from Tivly.models import *
from Tivly.views import *
from Management import *
import urllib2
import urllib
import json
import httplib
import unicodedata
from web1 import settings
from urlparse import parse_qsl
from django.http import HttpResponse
from googlemaps import GoogleMaps
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
csid = '2YIKLB'
#deleteAUser(csid)
#response = HttpResponse()
#response.set_cookie('csID', csid)
#csUser = CSUser(response)
#business = Businesses.objects.filter(businessID = 'tivly')[0]
#used,left,redeemed,recommended = csUser.getRewardStatistics(business)
#
#print 'used: ' + str(used),'left: ' + str(left),'redeemed: ' + str(redeemed),'reccommended ' + str(recommended)
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
##

#response = createACard('5RVRHK','1129384599856','2020-03')

#authenticate()
#print urllib2.urlopen('https://api.cardspring.com/v1').read()
#print getAUser('5RVRHK').read()

#try:
#    values = {'event_type':'settlement','transaction_id':'yN0LiDG5YOwt','purchase_date_time':'2012-01-01 12:34:56','amount':2000,'currency':'USD','app_id':'kpj90OAR8sg9',
#              'business_id':'l5sxg80QSa7O','store_id':'qmGITK2sHg5G','user_id':'5RVRHK','card_token':'K9o694RkK34r'}
#    url = 'http://mygoods.co/callback'
#    data = urllib.urlencode(values)
#    urllib2.urlopen(url,data)
#    print 'success!'
#    
#except urllib2.HTTPError, error:
#    print error.read()
# 
#
#
#print len(MyRewards.objects.filter(reccomendedBy = 'XE6AN1', used = True))
#
#myRewards = MyRewards.objects.filter(csID = 'XE6AN1')
#
#points = 0
#redeemable = {}
#firstTime = True
#for targetReward in myRewards:
#    pointValue = len(MyRewards.objects.filter(reccomendedBy = 'XE6AN1', used = True))
#    print 'reward: '+targetReward.reward.description  
#    print 'points needed: '+str(targetReward.reward.pointsNeeded)
#    print 'point value: '+str(pointValue)
#    print 'used?: '+ str(targetReward.used)
#    if targetReward.reward.pointsNeeded <= pointValue and targetReward.used == False:
#        print 'here!'
#        business = Businesses.objects.filter(businessID = targetReward.reward.businessID)[0]
#        redeemable[targetReward.reward] = business
#
##for reward in myRewards:
##    if reward.reward.level == 0:
##        reward.used = True
##    else:
##        reward.used = False
##    reward.save()
#            
#print redeemable
#
#values = {'businessID':'racecourse','businessName':'The Fleming Race Course','city':'Long Valley','street':'1 Fleming Ct.','zipcode': '07853',
#          'mondayHours':'7:30am - 9:00pm','tuesdayHours':'7:30am - 9:00pm','wednesdayHours':'7:30am - 9:00pm', 'thursdayHours':'7:30am - 9:00pm',
#          'fridayHours':'7:30am - 9:00pm','saturdayHours':'7:30am - 9:00pm','sundayHours':'7:30am - 9:00pm', 'description':'Oldest race course in New Jersey, home to the classics',
#          'pictureLocation':'somewhere','website':'https://www.facebook.com/pages/Fleming-Racecourse/507330119294163'}
#
#AddBusiness(values)

URL = settings.URL
csid = 'blah'
FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
redirect = 'https://www.tivly.com/home'
CARDSPRING_APP_ID = settings.CARDSPRING_APP_ID

securityToken = IDGenerator(32)
timestamp = datetime.now()
key = settings.CARDSPRING_APP_ID
raw = '{'+securityToken+'}:{'+str(datetime.now())+'}:{XE6AN1}'
hashed = hmac.new(key, raw, sha1)
print '0x'+hashed.hexdigest()



    