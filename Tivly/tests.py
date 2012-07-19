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

print GetUsers().read()
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

##############################################################################################################################################################
#'''
#Created on Jul 6, 2012
#
#@author: bryanantigua
#'''
#from CardSpring import *
#from Tivly.models import *
#
#import urllib2
#import urllib
#import json
#import unicodedata
#import httplib
#
##########CallBACK TEST##############
#request = {}
#storeID ='cFHuUBk9qSCM'
#bID = 'l5sxg80QSa7O'
#appid = 'NLWgAaWVclvK'
#cardNumber='888685445668888'
#exp= '2015-10'
#ctoken = 'Im1CauI9sOT7'
#l4='8888'
#csid = 'J2ON89'   
#request = {}
#values = {'card_token':ctoken,'event_type':'settlement','amount':'2000','business_id':bID}
#response = TestTransaction(values)
#result = json.load(response)
#
#print result
##################################
#result['user_id'] = csid
#result['app_id'] = appid
#date_time = result['purchase_date_time'][:10]
#
#t = Transaction(appID = result['app_id'],csID = result['user_id'],date = date_time ,event_type = result['event_type'], businessID =result['business_id'],currency = result['currency'], amount = result['amount'],card_token = result['card_token'],transaction_id = result['id'], store_id =result['store_id'])
#t.save()
#
#reccomendedReward = MyRecommendations.objects.filter(reccsID = result['cs_id'], appID = result['app_id']).csID
#
#reccomendedBy = reccomendedReward.csID
#recommenderPoints = UserPoints.objects.filter(csID = reccomendedBy, businessID = result['business_id'])[0]
#
#recommenderPoints.points += 1
#recommenderPoints.save()
#
#
#if result['event_type'] == 'settlement' or result['event_type'] == 'authorization':
#    userPoints = UserPoints.objects.filter(csID = result['user_id'], businessID = result['business_id'])[0]      
#    userPoints.points = userPoints.points + 1
#    userPoints.visits = userPoints.visits + 1
#    userPoints.save()
#    
#
#if result['event_type'] == 'redemption':
#    reward = Rewards.objects.filter(appID = result['app_id'])[0]
#    userPoints.points = userPoints.points - reward.pointsNeeded
#    reccomendedReward.redeemed = True
#    reccomendedReward.save()
##############################################################################################
##business = json.load(GetABusiness({},bID))
##b= Businesses(businessID = business.get('id'), businessName = business.get('name'), Location = 'Palo Alto, CA', description = 'This place is awesome!!!', pictureLocation = '/static/redwoods/pampas.png', hours = '9-5 Errday')
##b.save()
####
##CreateUserAppConnection({},csid,appid)
##c = Apps(appID = appid, businessID = bID)
##c.save()
#####
##u = UserApps(appID =appid, businessID = bID, csID = csid)
##u.save()
##
##
##
##print CreateACard(request,csid,cardNumber,exp).read()
##
##print GetAUser(request,csid).read()
#
##
##d = Cards( csID = csid,token = ctoken,last4 = l4, expDate = exp,cardType = 'other', typeString = 'other')
##d.save()
#
##r = UserPoints(csID = csid, businessID = bID,points = 0)
##r.save()


