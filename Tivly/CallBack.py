'''
Created on Jul 6, 2012

@author: bryanantigua
'''
from Tivly.models import UserPoints,MyRewards,Rewards
from datetime import datetime

import urllib2
import urllib
import json
import unicodedata
import httplib
def callBack(request):    
    if request.method == "POST":
        csid = request.POST['user_id']
        userPoints = UserPoints.objects.filter(csID =csid, businessID = request.POST['business_id'])[0]
        
        rewardLookUp = Rewards.objects.filter(appID = request.POST['app_id'])[0]
        myReward = MyRewards.objects.filter(csID = csid, reward = rewardLookUp)
        myReward.used = True
        myReward.dateUsed = datetime.now()
        myReward.save()