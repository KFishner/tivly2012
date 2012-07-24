'''
Created on Jul 6, 2012

@author: bryanantigua
'''
from Tivly.models import Transaction,UniqueBusinessHistory,MyRewards,Rewards, RewardHistory,UniqueRewardHistory
from datetime import datetime
from django.http import HttpResponse
from CardSpringActions import deleteAUserApp

def callBack(request):    
    result = request.POST
    csid = result['user_id']
    rewardLookUp = Rewards.objects.filter(appID = request.POST['app_id'])[0]
    myReward = MyRewards.objects.filter(csID = csid, reward = rewardLookUp)[0]
    myReward.used = True
    myReward.dateUsed = datetime.now()
    myReward.save()
    
    addToHistory = RewardHistory(csID = csid, reccomendedBy = myReward.reccomendedBy, reward = rewardLookUp,dateUsed = datetime.now())
    addToHistory.save()
    
    uniqueReward = RewardHistory.objects.filter(csID = csid, reward = rewardLookUp)
    
    if not uniqueReward.exists():
        addToUniqueHistory = UniqueRewardHistory(csID = csid, reccomendedBy = myReward.reccomendedBy, reward = rewardLookUp,dateUsed = datetime.now())
        addToUniqueHistory.save()
    
    Costumer = UniqueBusinessHistory.objects.filter(csID =csid, businessID = myReward.reward.businessID)
    if not Costumer.exists():
        newCustomer = UniqueBusinessHistory(csiD = csid, businessID = myReward.reward.businessID, reward = myReward.reward, dateUsed = datetime.now())
        newCustomer.save()
        
#    deleteAUserApp(csid,request.POST['app_id'])
    transaction = Transaction(csID = result['user_id'], appID = result['app_id'], date = datetime.now(), event_type = result['event_type'], businessID = result['business_ID'],
                              currency= result['currency'], amount = result['amount'],card_token = result['card_token'], transaction_id = result['transaction_id'], store_id = result['store_id'],
                             )
    transaction.save()
    return HttpResponse()
