'''
Created on Jul 3, 2012

@author: bryanantigua
'''
from Tivly.models import Businesses, Rewards
from CardSpringActions import createBusinessConnection,createAnApp
import string
import random

########################################################
#####             BACKEND TOOLS                    #####
########################################################


    
def IDGenerator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
    

def AddBusiness(values):
    b = Businesses(businessID = values['businessID'], businessName= values['businessName'],city = values['city'], 
                   street = values['street'], zipCode = values['zipcode'], mondayHours = values['mondayHours'], 
                   tuesdayHours = values['tuesdayHours'], wednesdayHours = values['wednesdayHours'],thursdayHours = values['thursdayHours'],
                   fridayHours = values['fridayHours'], saturdayHours = values['saturdayHours'], sundayHours = values['sundayHours'], 
                   description = values['description'], pictureLocation = values['pictureLocation'],website = values['website'])
    createBusinessConnection(values['businessID'])
    b.save()
    
def AddReward(values, redemptionValues):
    r = Rewards(rID = values['rID'],appID = values['appID'],businessID = values['businessID'], description = values['description'],
                 pointsNeeded = values['pointsNeeded'] )
    createAnApp(values['businessID'], redemptionValues)
    r.save()
        