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

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

class User:
    
    def __init__(self, request):
        self.csUser = self.getCardSpringUser(request)
        self.fbUser = FBUser.objects.get(fb_id = self.csUser.fbID)
        self.cards = Cards.objects.filter(csID = self.csUser.csID)
        self.myRewards = MyRewards.objects.filter(csID = self.csUser.csID)
        email = self.fbUser.email
        firstname = self.fbUser.first_name
        print "self.csuser.emailed = " + str(self.csUser.emailed)
        if not self.csUser.emailed:
            print "sending email"
            from_email = 'team@tivly.com'
            to = email
            subject = "Welcome to Tivly!" 
            try:
                plaintext = get_template('welcome_to.txt')
                htmly = get_template('welcome_to.html')
                d = Context({ 'firstname': firstname })
                text_content = plaintext.render(d)
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                self.csUser.emailed = True
                self.csUser.save()
                print "message sent to %s" % email
            except Exception as e:
                print "email failed"
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

        print "sending new rewardemail"
        email = str(self.fbUser.email)
        name = str(self.fbUser.first_name)
        busname = str(business.businessName)
        description = rewardToAdd.description
        try:
            plaintext = get_template('newreward.txt')
            htmly = get_template('newreward.html')
            d = Context({ 'firstname': name, 'busname':busname, 'description':description, 'rew1':myLevel1Reward, 'rew2':myLevel2Reward, 'business':business, 'csID':self.csUser.csID, 'rID':rid })
            subject = "Congratulations! A New Reward" 
            fromAddr = "team@tivly.com"
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, fromAddr, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            print "message sent to %s" % email
        except Exception as e:
            print str(e)
#        recommendation.delete() 4

        
        
