
'''
Created on Jun 30, 2012

@author: bryanantigua
'''
import urllib2
import urllib


from web1 import settings
   
def Authenticate():
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = "api-test.cardspring.com"
    password_mgr.add_password(None, top_level_url, settings.CARDSPRING_APP_ID, settings.CARDSPRING_APP_SECRET)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    opener.addheaders = [('Accept', 'application/json'),("Content-Type","application/x-www-form-urlencoded")]
    urllib2.install_opener(opener)

def GetPublisherInfo():
    Authenticate()
    return urllib2.urlopen('https://api-test.cardspring.com/v1')

def CreateAUser(csID):
    Authenticate()
    values = {'user_id':csID}
    url = 'https://api-test.cardspring.com/v1/users'
    data = urllib.urlencode(values)
    return urllib2.urlopen(url,data)
    
def GetAUser(csID):
    Authenticate()
    return urllib2.urlopen('https://api-test.cardspring.com/v1/users/'+ csID)

def GetUsers():
    Authenticate()
    return urllib2.urlopen('https://api-test.cardspring.com/v1/users')

def RetrieveACard(csID,token):
    Authenticate()
    return urllib2.urlopen('https://api-test.cardspring.com/v1/users/'+csID+'/cards/'+token)

def GetAllBusinesses(filters):
    Authenticate()
    data = urllib.urlencode(filters)
    return urllib2.urlopen('https://api-test.cardspring.com/v1/businesses',data)

def GetABusiness(businessID):
    Authenticate()
    return urllib2.urlopen('https://api-test.cardspring.com/v1/businesses/'+businessID)

def GetAllStores(businessID):
    Authenticate()
    return urllib2.urlopen('https://api-test.cardspring.com/v1/businesses/'+businessID+'/stores')

def GetAStore(businessID,storeID):
    Authenticate()
    return urllib2.urlopen('https://api-test.cardspring.com/v1/businesses/'+businessID+'/stores/'+storeID)

def CreateBusinessConnection(businessID):
    Authenticate()
    values = {'permissions' :'notification,purchase_data,redemption', 'authorization':'signature'}
    data = urllib.urlencode(values)
    return urllib2.urlopen('https://api-test.cardspring.com/v1/businesses/'+ businessID+'/connection', data)

def GetBusinessConnections(activity):
    Authenticate()
    values = {'connection':activity}
    data = urllib.urlencode(values)
    return urllib2.urlopen('https://api-test.cardspring.com/v1/businesses',data)

def CreateAnApp(businessID,redemptionValues):
    Authenticate()
#    values = {'redemption[discount_summary]':'10 Off 50','redemption[discount_description]':'Save+%2410+your+next+purchase+of+%2450+or+more+at+The+Gap',
#              'redemption[type]':'terminal_discount','redemption[min_purchase]':'5000','redemption[amount]':'1000','notification[type]':'all_payment_events',
#              'notification[min_purchase]':'5000'}  
    data = urllib.urlencode(redemptionValues)
    return urllib2.urlopen('https://api-test.cardspring.com/v1/businesses/'+businessID+'/apps',data) 

def GetAnApp(businessID,appID):
    Authenticate()
    return urllib2.urlopen('https://api-test.cardspring.com/v1/businesses/'+businessID+'/apps/'+appID)
     
def ListApps(businessID):
    Authenticate()
    return urllib2.urlopen('https://api-test.cardspring.com/v1/businesses/'+businessID+'/apps')

def GetAllEvents():
    Authenticate()
    return urllib2.urlopen('https://api-test.cardspring.com/v1/events')

def GetAppConnections(csID):
    Authenticate()
    return urllib2.urlopen('https://api-test.cardspring.com/v1/users/'+csID+'/apps')

def CreateUserAppConnection(csID,appID):
    Authenticate()
    values = {'app_id':appID}
    data  = urllib.urlencode(values)
    return urllib2.urlopen('https://api-test.cardspring.com/v1/users/'+csID+'/apps',data)

def GetUserAppConnection(csID,appID):
    Authenticate()
    return urllib2.urlopen('https://api-test.cardspring.com/v1/users/'+csID+'/apps'+appID)

def CreateACard(csID,cardNumber,exp):
    Authenticate()
    values = {'pan':cardNumber,'expiration':exp}
    data  = urllib.urlencode(values)
    return urllib2.urlopen('https://api-test.cardspring.com/v1/users/'+csID+'/cards',data)
 
# Only in Test Environment....

def TestTransaction(values):
    Authenticate()
    data = urllib.urlencode(values)
    return urllib2.urlopen('https://api-test.cardspring.com/v1/transactions',data)

