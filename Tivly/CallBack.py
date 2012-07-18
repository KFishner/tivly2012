'''
Created on Jul 6, 2012

@author: bryanantigua
'''
from CardSpring import *
from Tivly.models import *

import urllib2
import urllib
import json
import unicodedata
import httplib
def callBack(request):    
    if request.method == "POST":
        csid = request.POST['user_id']
        userPoints = UserPoints.objects.filter(csID =csid, businessID = request.POST['business_id'])[0]
             
        if request.POST['event_type'] == 'settlement' or request.POST['event_type'] == 'authorization':
#            userPoints.points = userPoints.points + 1
#            userPoints.visits = userPoints.visits + 1
#            userPoints.save()
            continue
        
        if request.POST['event_type'] == 'redemption':
            rewardLookUp = Rewards.objects.filter(appID = request.POST['app_id'])[0]
            myReward = MyRewards.objects.filter(csID = csid, reward = rewardLookUp)
            myReward.used = True
            myReward.save()
            
#            userPoints.points = userPoints.points - reward.pointsNeeded
#            userPoints.save()