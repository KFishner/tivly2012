"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from CardSpring import RetrieveACard,Authenticate,CreateACard,GetUsers,GetAnApp,Authenticate,CreateAnApp,ListApps,TestTransaction,CreateUserAppConnection,GetAllEvents,GetPublisherInfo,GetUserAppConnection,CreateAUser,GetAppConnections,CreateBusinessConnection,GetAUser,GetAStore,GetAllStores, GetUsers,GetABusiness, GetAllBusinesses
from Tivly.models import *
#from DataBase import *
#TEST ENVIROMENT---------------
import urllib2
import urllib
import json
import httplib
import unicodedata
import httplib

request = {}
storeID ='cFHuUBk9qSCM'
bID = 'l5sxg80QSa7O'
appid = 'NLWgAaWVclvK'
cardNumber='8886854754588888'
exp= '2015-10'
ctoken = '4S83TJXk0Ky8'
l4='8888'
csid = 'J2ON89'   
request = {}
values = {'card_token':ctoken,'event_type':'settlement','amount':'2000','business_id':bID}

#r = Rewards.objects.filter(appID = appid)[0]
#mr = MyRewards(csID = csid, reward = r)
#mr.save()

#r = Rewards(description = "oi", businessID = bID, pointsNeeded =10)
##r.save()
#response = TestTransaction(values)
#result = json.load(response)
#print result




import httplib
import urllib


try:
    params = urllib.urlencode({'user_id':'PIQZAO'})
    headers = [("Content-type", "application/x-www-form-urlencoded"),("Accept", "application/json")]
    conn = httplib.HTTPConnection("api-test.cardspring.com/v1")
    conn.request("DELETE", "users/PIQZAO",headers)
    response = conn.getresponse()
    print response.read()

except urllib2.HTTPError, e:
        message = e.read()
        try:
            print json.loads(message)
        except Exception:
            try:
                print e.read()
            except Exception:
                print e.code, e.message


##print result
#t = Transaction(date = result['date_time'] ,event_type = result['event_type'], businessID =result['business_id'],currency = result['USD'], amount = result['2000'],card_token = result['card_token'],transaction_id = result['id'], store_id =result['store_id'])
##############################################################################################
#business = json.load(GetABusiness({},bID))
#b= Businesses(businessID = business.get('id'), businessName = business.get('name'), city = 'Palo Alto, CA',street = "541 Alma St",sundayHours = "11:30am-930pm",saturdayHours = "11:30am-930pm",fridayHours = "11:30am-930pm",thursdayHours = "11:30am-930pm",wednesdayHours = "11:30am-930pm", tuesdayHours = "11:30am-930pm",mondayHours = "11:30am-930pm",description = 'This place is awesome!!!', pictureLocation = '/static/redwoods/pampas.png', hours = '9-5 Errday')
#b.save()
###
##CreateUserAppConnection({},csid,appid)
#c = Apps(appID = appid, businessID = bID)
#c.save()
#####
#u = UserApps(appID =appid, businessID = bID, csID = csid)
#u.save()
#
#
##print GetAUser(request,csid).read()
#
#print CreateACard(csid,cardNumber,exp).read()
##
#d = Cards( csID = csid,token = ctoken,last4 = l4, expDate = exp,cardType = 'other', typeString = 'other')
#d.save()




