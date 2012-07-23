'''
Created on Jul 6, 2012

@author: bryanantigua
'''
from Tivly.models import Transaction,MyRewards,Rewards
from datetime import datetime
from CardSpringActions import deleteAUserApp

def callBack(request):    
        csid = request.POST['user_id']
        result = request.Post.get()
#        userPoints = UserPoints.objects.filter(csID =csid, businessID = request.POST['business_id'])[0]
        rewardLookUp = Rewards.objects.filter(appID = request.POST['app_id'])[0]
        myReward = MyRewards.objects.filter(csID = csid, reward = rewardLookUp)
        myReward.used = True
        myReward.dateUsed = datetime.now()
        myReward.save()
        deleteAUserApp(csid,request.POST['app_id'])
        transaction = Transaction(csID = result['user_id'], appID = result['app_id'], date = datetime.now(), event_type = result['event_type'], businessID = result['business_ID'],
                                  currency= result['currency'], amount = result['amount'],card_token = result['card_token'], transaction_id = result['transaction_id'], store_id = result['store_id'],
                                  date = datetime.now())
        transaction.save()
