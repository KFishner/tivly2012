'''
Created on Jul 6, 2012

@author: bryanantigua
'''
from Tivly.models import Transaction,UniqueBusinessHistory,MyRewards,Rewards, RewardHistory,UniqueRewardHistory
from datetime import datetime
from django.http import HttpResponse
from CardSpringActions import deleteAUserApp
from web1 import settings

def callBack(request):    
    result = request.POST
    
    #Find the user and the reward as mark it as used
    csid = result['user_id']
    rewardLookUp = Rewards.objects.filter(appID = request.POST['app_id'])[0]
    myReward = MyRewards.objects.filter(csID = csid, reward = rewardLookUp)[0]
    myReward.used = True
    myReward.dateUsed = datetime.now()
    myReward.save()
    
    #add to our general history...
    addToHistory = RewardHistory(csID = csid, reccomendedBy = myReward.reccomendedBy, reward = rewardLookUp,dateUsed = datetime.now())
    addToHistory.save()
    
    #add to our unique history...
    uniqueReward = RewardHistory.objects.filter(csID = csid, reward = rewardLookUp)
    
    
    if len(uniqueReward) == 1:
        addToUniqueHistory = UniqueRewardHistory(csID = csid, reccomendedBy = myReward.reccomendedBy, reward = rewardLookUp,dateUsed = datetime.now())
        addToUniqueHistory.save()
    
    Costumer = UniqueBusinessHistory.objects.filter(csID =csid, businessID = myReward.reward.businessID)
    if not Costumer.exists():
        newCustomer = UniqueBusinessHistory(csID = csid, businessID = myReward.reward.businessID, reward = myReward.reward, dateUsed = datetime.now())
        newCustomer.save()
        
    deleteAUserApp(csid,request.POST['app_id'])
    transaction = Transaction(csID = result['user_id'], appID = result['app_id'], date = datetime.now(), event_type = result['event_type'], businessID = myReward.reward.businessID,
                              currency= result['currency'], amount = result['amount'],card_token = result['card_token'], transaction_id = result['transaction_id'], store_id = result['store_id'],
                             )
    transaction.save()
    return HttpResponse()
