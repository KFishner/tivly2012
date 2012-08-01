'''
Created on Jul 22, 2012

@author: bryanantigua
'''
from Facebook import facebookLogin
from Management import IDGenerator
from CardSpringActions import createAUser,createUserAppConnection
from datetime import datetime
from Tivly.models import FBUser,MyRecommendations,Cards, UserPoints, MyRewards,Rewards, CardSpringUser

class CSUser:
    
    def __init__(self, request):
        self.csUser = self.getCardSpringUser(request)
        self.fbUser = FBUser.objects.get(fb_id = self.csUser.fbID)
        self.myCurrentRecommendations = MyRecommendations.objects.filter(csID = self.csUser.csID)
        self.cards = Cards.objects.filter(csID = self.csUser.csID)
        self.userPoints = UserPoints.objects.filter(csID = self.csUser.csID)
        self.myRewards = MyRewards.objects.filter(csID = self.csUser.csID)
        
    
    def getCardSpringUser(self,request):
        code = request.GET.get('code', None)
#        code = None    
        cardspringID = request.COOKIES.get('csID',None)
#        cardspringID = '2YIKLB'
        
        if code is not None:
            fbUser = facebookLogin(request)
            CSUser = CardSpringUser.objects.filter(fbID = fbUser.fb_id)
            if not CSUser.exists():
                cardspringID = IDGenerator()
                CSUser = CardSpringUser(csID = cardspringID, points = 0, fbID = fbUser.fb_id, dateJoined = datetime.now())
                CSUser.save()                
                createAUser(cardspringID)
                CSUser = CardSpringUser.objects.filter(csID = cardspringID)
        
        elif cardspringID is not None:
            CSUser = CardSpringUser.objects.filter(csID = cardspringID)
        
        else:
            cardspringID = IDGenerator()
            CSUser = CardSpringUser(csID = cardspringID, points = 0, fbID = fbUser.fb_id, dateJoined = datetime.now())
            CSUser.save()                
            createAUser(cardspringID)
            CSUser = CardSpringUser.objects.filter(csID = cardspringID)
        
        CSUser = CSUser[0]
        return CSUser
    
    def  getRewardStatistics(self,business):
        used = 0
        left = 0
        redeemed = 0
        
        for reward in self.myRewards:
            if reward.reward.businessID == business.businessID:
                if reward.used is False:
                    left += 1
                else:
                    used += 1
                
        recRewards = MyRewards.objects.filter(reccomendedBy = self.csUser.csID)
        recommended = len(recRewards)
        for reward in recRewards:
            if reward.used is True:
                redeemed += 1
            
        return used,left,redeemed,recommended
    
    

    def addRecommendationToRewards(self,recid):
        rec = MyRecommendations.objects.filter(recID = recid)  
        if rec.exists():
            rec = rec[0]
            userPoints = UserPoints.objects.filter(csID = self.csUser.csID, businessID = rec.businessID)
                
            if not userPoints.exists():
                userPoints = UserPoints(csID = self.csUser.csID, businessID = rec.businessID, points = 0, visits = 0)
                userPoints.save()
            
            self.setReward(recid)
        return
    
    def setReward(self, recid):
        recommendation = MyRecommendations.objects.filter(recID = recid)[0]
        isUsed = True
        if recommendation.businessID != "tivly":
            createUserAppConnection(self.csUser.csID,recommendation.appID)
            isUsed = False
        recReward = Rewards.objects.filter(appID = recommendation.appID)[0]
        myReward = MyRewards(csID = self.csUser.csID, reward = recReward, reccomendedBy = recommendation.csID, used = isUsed)
        myReward.save()
#        recommendation.delete()

        
        