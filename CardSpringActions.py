
'''
Created on Jun 30, 2012

@author: bryanantigua
'''
import urllib2
import urllib
import httplib2


from web1 import settings
   
def authenticate():
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = "api.cardspring.com"
    password_mgr.add_password(None, top_level_url, settings.CARDSPRING_APP_ID, settings.CARDSPRING_APP_SECRET)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    opener.addheaders = [('Accept', 'application/json'),("Content-Type","application/x-www-form-urlencoded")]
    urllib2.install_opener(opener)
    
def authenticateWithHttplib2():
    h = httplib2.Http()
    h.add_credentials(settings.CARDSPRING_APP_ID, settings.CARDSPRING_APP_SECRET)
    header = {"Content-type": "application/x-www-form-urlencoded","Accept":"application/json"}
    auth = {'h': h, 'header' : header}
    return auth


######################################################################
#####                   USER ACTIONS                             #####
######################################################################

def createAUser(csID):
    authenticate()
    values = {'user_id':csID}
    url = 'https://api.cardspring.com/v1/users'
    data = urllib.urlencode(values)
    return urllib2.urlopen(url,data)
    
def getAUser(csID):
    authenticate()
    return urllib2.urlopen('https://api.cardspring.com/v1/users/'+ csID)

def getUsers():
    authenticate()
    return urllib2.urlopen('https://api.cardspring.com/v1/users')
def deleteAUser(csID):
    auth = authenticateWithHttplib2()
    response = auth['h'].request("https://api.cardspring.com/v1/users/"+csID, method = "DELETE", headers = auth['header'])
    return response


######################################################################
#####                   APP ACTIONS                              #####
######################################################################

def deleteAnApp(businessID, appID):
    auth = authenticateWithHttplib2()
    response = auth['h'].request("https://api.cardspring.com/v1/businesses/"+businessID+"/apps/"+appID, method = "DELETE", headers = auth['header'])
    return response

def modifyAnApp(businessID,appID, values):
    auth = authenticateWithHttplib2()
    data = urllib.urlencode(values)
    response = auth['h'].request('https://api.cardspring.com/v1/businesses/'+businessID+'/apps/'+appID, method = "PUT",body = data, headers = auth['header'])
    return response

def createAnApp(businessID,redemptionValues):
#   Example of values ... 
#   values = {'redemption[discount_summary]':'10 Off 50','redemption[discount_description]':'Save+%2410+your+next+purchase+of+%2450+or+more+at+The+Gap',
#              'redemption[type]':'terminal_discount','redemption[min_purchase]':'5000','redemption[amount]':'1000','notification[type]':'all_payment_events',
#              'notification[min_purchase]':'5000'}  
    authenticate()
    data = urllib.urlencode(redemptionValues)
    return urllib2.urlopen('https://api.cardspring.com/v1/businesses/'+businessID+'/apps',data) 

#def signUpForAllApps

def getAnApp(businessID,appID):
    authenticate()
    return urllib2.urlopen('https://api.cardspring.com/v1/businesses/'+businessID+'/apps/'+appID)
     
def listApps(businessID):
    authenticate()
    return urllib2.urlopen('https://api.cardspring.com/v1/businesses/'+businessID+'/apps')

#=================== SPECIFIC TO USER================================#

def getUserAppConnections(csID):
    authenticate()
    return urllib2.urlopen('https://api.cardspring.com/v1/users/'+csID+'/apps')

def createUserAppConnection(csID,appID):
    authenticate()
    values = {'app_id':appID}
    data  = urllib.urlencode(values)
    return urllib2.urlopen('https://api.cardspring.com/v1/users/'+csID+'/apps',data)

def getUserAppConnection(csID,appID):
    authenticate()
    return urllib2.urlopen('https://api.cardspring.com/v1/users/'+csID+'/apps'+appID)


def deleteAUserApp(csID,appID):
    auth = authenticateWithHttplib2()
    response = auth['h'].request('https://api.cardspring.com/v1/users/'+csID+'/apps/'+appID, method = "DELETE",headers = auth['header'])
    return response

######################################################################
#####                   CARD ACTIONS                             #####
######################################################################

def deleteACard(csID,token):
    auth = authenticateWithHttplib2()
    response = auth['h'].request("https://api.cardspring.com/v1/users/"+csID+'/cards/'+token, method = "DELETE", headers = auth['header'])
    return response

def createACard(csID,cardNumber,exp):
    authenticate()
    values = {'pan':cardNumber,'expiration':exp}
    data  = urllib.urlencode(values)
    return urllib2.urlopen('https://api.cardspring.com/v1/users/'+csID+'/cards',data)

def retrieveACard(csID,token):
    authenticate()
    return urllib2.urlopen('https://api.cardspring.com/v1/users/'+csID+'/cards/'+token)

def deleteABusinessConnection(businessID):
    auth = authenticateWithHttplib2()
    response = auth['h'].request("https://api.cardspring.com/v1/businesses/"+businessID+"/connection", method = "DELETE", headers = auth['header'])
    return response
    


######################################################################
#####                   BUSINESS ACTIONS                         #####
######################################################################

def getAllBusinesses(filters):
    authenticate()
    data = urllib.urlencode(filters)
    return urllib2.urlopen('https://api.cardspring.com/v1/businesses',data)

def getABusiness(businessID):
    authenticate()
    return urllib2.urlopen('https://api.cardspring.com/v1/businesses/'+businessID)

def getAllStores(businessID):
    authenticate()
    return urllib2.urlopen('https://api.cardspring.com/v1/businesses/'+businessID+'/stores')

def getAStore(businessID,storeID):
    authenticate()
    return urllib2.urlopen('https://api.cardspring.com/v1/businesses/'+businessID+'/stores/'+storeID)

def createBusinessConnection(businessID):
    authenticate()
    values = {'permissions' :'notification,purchase_data,redemption', 'authorization':'signature'}
    data = urllib.urlencode(values)
    return urllib2.urlopen('https://api.cardspring.com/v1/businesses/'+ businessID+'/connection', data)

def getBusinessConnections(activity):
    authenticate()
    values = {'connection':activity}
    data = urllib.urlencode(values)
    return urllib2.urlopen('https://api.cardspring.com/v1/businesses',data)

######################################################################
#####                   RANDO ACTIONS                            #####
######################################################################
  
def getPublisherInfo():
    authenticate()
    return urllib2.urlopen('https://api.cardspring.com/v1')

def getAllEvents():
    authenticate()
    return urllib2.urlopen('https://api.cardspring.com/v1/events')
 
# Only in Test Environment....
def testTransaction(values):
    authenticate()
    data = urllib.urlencode(values)
    return urllib2.urlopen('https://api.cardspring.com/v1/transactions',data)
