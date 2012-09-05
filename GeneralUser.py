'''
Created on Jul 22, 2012

@author: bryanantigua
'''
from django.core.mail import *
from Facebook import facebookLogin
from Management import IDGenerator
from CardSpringActions import createAUser,createUserAppConnection
from datetime import datetime
from Tivly.models import FBUser,Cards, MyRewards,Rewards, Businesses, CardSpringUser

class User:
    
    def __init__(self, request):
        self.csUser = self.getCardSpringUser(request)
        self.fbUser = FBUser.objects.get(fb_id = self.csUser.fbID)
        self.cards = Cards.objects.filter(csID = self.csUser.csID)
        self.myRewards = MyRewards.objects.filter(csID = self.csUser.csID)
        email = self.fbUser.email
        name = self.fbUser.first_name
        print "self.csuser.emailed = " + str(self.csUser.emailed)
        if not self.csUser.emailed:
            print "sending email"
            subject = "Welcome to Tivly!" 
            fromAddr = "info@tivly.com"
            bodyTemplate = "Hi %s,\n\nWelcome to Tivly!\n\nGetting started:\n\t1 -- Signin to your account at www.tivly.com\n\t2 -- Share the places you love with friends\n\t3 -- Start earning points towards awesome rewards\n\t4 -- Swipe your payment card at your favorite places to redeem rewards - that's it!\n\nReply to this email with any questions\nYou can check it out at http://www.tivly.com/splash/.\n\nBest Regards,\nThe Tivly Team\n\n\n\nCopyright 2012 Tivly, All rights reserved.\nYou are receiving this email because you redeemed a discount at one of our partner stores or signed up at www.tivly.com\n\nOur mailing address is:\n\nTivly\n151 Lytton Ave\nPalo Alto, CA 94031"
            messages = []
            try:
                body = bodyTemplate % (name)
                messages.append((subject, body, fromAddr, [email.encode('ascii')]))
                messages = tuple(messages)
                send_mass_mail(messages)
                self.csUser.emailed = True
                self.csUser.save()
                print "message sent to %s" % email
            except Exception as e:
                print str(e)
        
    
    def getCardSpringUser(self,request):
        code = request.GET.get('code', None)
        cardspringID = request.COOKIES.get('csID',None)
        
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
                
        recRewards = MyRewards.objects.filter(businessID = business.businessID, reccomendedBy = self.csUser.csID)
        recommended = len(recRewards)
        for reward in recRewards:
            if reward.used is True:
                redeemed += 1
            
        return used,left,redeemed,recommended
    
    

    def addRecommendationToRewards(self,recommendedBy,rid):
        rewardToAdd = Rewards.objects.filter(rID = rid)  
        if rewardToAdd.exists():
            rewardToAdd = rewardToAdd[0]      
            self.setReward(recommendedBy,rid)
        return
    
    def setReward(self, recommendedby,rid):
        rewardToAdd = Rewards.objects.get(rID = rid)
        business = Businesses.objects.get(businessID = rewardToAdd.businessID)
        myLevel1Reward = Rewards.objects.get(businessID = rewardToAdd.businessID, level = 1)
        myLevel2Reward = Rewards.objects.get(businessID = rewardToAdd.businessID, level = 2)
        isUsed = True
        if str(rewardToAdd.businessID) != "tivly" and str(rewardToAdd.appID) != "racecourse" and rewardToAdd.businessID != "l5sxg80QSa7O":
            createUserAppConnection(self.csUser.csID,rewardToAdd.appID)
            createUserAppConnection(self.csUser.csID,myLevel1Reward.appID)
            createUserAppConnection(self.csUser.csID,myLevel2Reward.appID)
            isUsed = False
            
#        recReward = Rewards.objects.filter(appID = recommendation.appID)[0]
        myIntroReward = MyRewards(businessID = rewardToAdd.businessID, csID = self.csUser.csID, reward = rewardToAdd, reccomendedBy = recommendedby, used = isUsed)
        ml1r = MyRewards(businessID = myLevel1Reward.businessID,csID = self.csUser.csID, reward = myLevel1Reward, reccomendedBy = recommendedby, used = False)
        ml2r = MyRewards(businessID = myLevel1Reward.businessID, csID = self.csUser.csID, reward = myLevel2Reward, reccomendedBy = recommendedby, used = False)

        myIntroReward.save()
        ml1r.save()
        ml2r.save()
        print "\n\n********REWARDS SAVED, SENDING EMAIL******\n\n"

        if True:
            print "sending new rewardemail"
            subject = "Congratulations! A New Reward" 
            fromAddr = "info@tivly.com"
            bodyTemplate = "Congratulations %s!\n\n%s is now in your favorites on Tivly!\n\nShare %s with your friends!\n\t1 -- Sign in to your account at www.tivly.com\n\t2 -- Select %s\n\t3 -- Share via Facebook, Twitter, or email\n\t4 -- Earn points when your friends redeem their rewards\n\t5 -- Swipe your payment card at %s to redeem your own rewards - that's it!\n\nReply to this email with any questions\n\nBest Regards,\nThe Tivly Team\n\n\nCopyright 2012 Tivly, All rights reserved.\nYou are receiving this email because you redeemed a discount at one of our partner stores or signed up at www.tivly.com\n\nOur mailing address is:\n\nTivly\n151 Lytton Ave\nPalo Alto, CA 94031"
            messages = []
            email = str(self.fbUser.email)
            name = str(self.fbUser.first_name)
            
            print email
            print name
            busname = str(business.businessName)
            try:
                body = bodyTemplate % (name, busname, busname, busname,busname )
                messages.append((subject, body, fromAddr, [email.encode('ascii')]))
                messages = tuple(messages)
                send_mass_mail(messages)
                print "message sent to %s" % email
            except Exception as e:
                print str(e)
#        recommendation.delete() 4

        
        
