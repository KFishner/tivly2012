from web1 import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from Management import IDGenerator
from CardSpringActions import deleteAUser
from django.shortcuts import redirect
from datetime import datetime
from CallBack import callBack
from Tivly.models import CardSpringUser, MyRecommendations, Businesses, MyRewards, Rewards, ContactUsForm, Cards, FBUser,FBFriends, FBAccessTokens
from CreditCard import validateCard
from GMaps import getMap
from CSUserObject import CSUser
from django.views.decorators.csrf import csrf_exempt
from hashlib import sha1
import hmac


def login (request):
    #template variables... 
    pictureAvailable = False      
    FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
    facebookRedirect = 'https://www.tivly.com/home'
    redirectURL = 'https://www.tivly.com/splash'

    csid = request.COOKIES.get('csID',None)
    if csid is None:
        return redirect(redirectURL)
    else:
        FACEBOOK_API_ID = settings.FACEBOOK_APP_ID
        return render_to_response('signin.html', locals(),context_instance= RequestContext(request)) 

def loginWithRec(request,recommendedBy,rid):
    #template variables...
    pictureAvailable = True
    pictureLocation = Businesses.objects.filter(businessID = Rewards.objects.filter(rID = rid)[0].businessID)[0].pictureLocation
    businessName = Businesses.objects.filter(businessID = Rewards.objects.filter(rID = rid)[0].businessID)[0].businessName
    FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
    facebookRedirect = 'https://www.tivly.com/home'
    response = render_to_response('signin.html', locals(),context_instance= RequestContext(request))
    response.set_cookie('rID',rid)
    response.set_cookie('recommendedBy',recommendedBy)
    return response
                     
def home(request):
    #template variables...
    URL = settings.URL  
    user = CSUser(request)
    
    cc = Cards.objects.filter(csID = user.csUser.csID)
    
    if cc:
        hasCard = True  
    
    else:
        hasCard = False
        
    rid = request.COOKIES.get('rID', None)
    recommendedBy = request.COOKIES.get('recommendedBy', None)
    if rid is not None:
        rewardToAdd = Rewards.objects.filter(rID = rid)
        rewardCheck = MyRewards.objects.filter(csID = user.csUser.csID, reward = rewardToAdd)
        if not rewardCheck.exists():
            user.addRecommendationToRewards(recommendedBy,rid)

    businessList= []
    
    for reward in user.myRewards:
        business = Businesses.objects.filter(businessID = reward.reward.businessID)[0]
        if business in businessList:
            continue
        else:
            businessList.append(business)
    
    response = render_to_response('myfavorites.html', locals(),context_instance= RequestContext(request))
    response.set_cookie('csID',user.csUser.csID)
    return response

def businessInfo(request, bname):
    #template variables...
    URL = settings.URL
    bname =  bname.replace('_',' ')
    user = CSUser(request)
    csID = user.csUser.csID
    business = Businesses.objects.filter(businessName = bname)[0]
    lat,lng = getMap(business.businessID)
    level1Reward = Rewards.objects.filter(businessID = business.businessID, level = 1)[0]
    level2Reward = Rewards.objects.filter(businessID = business.businessID, level = 2)[0]
    introReward = Rewards.objects.filter(businessID = business.businessID, level = 0)[0]
    used,left,redeemed,recommended = user.getRewardStatistics(business)
    rID = introReward.rID
#    myRecommendation = MyRecommendations(businessID = business.businessID, recID = recid, appID = introReward.appID ,rID =introReward.rID , csID = user.csUser.csID, dateGiven = datetime.now())
#    myRecommendation.save()
    response = render_to_response('businessInfo.html', locals(),context_instance= RequestContext(request))
    return response

def recommendation(request,bname):
    #template variables...
    URL = settings.URL
    user = CSUser(request)
    csID = user.csUser.csID
    bname =  bname.replace('_',' ')
    business = Businesses.objects.filter(businessName = bname)[0]
    level1Reward = Rewards.objects.filter(businessID = business.businessID, level = 1)[0]
    level2Reward = Rewards.objects.filter(businessID = business.businessID, level = 2)[0]
    introReward = Rewards.objects.filter(businessID = business.businessID, level = 0)[0]
    rID = introReward.rID
#    myRecommendation = MyRecommendations(businessID = business.businessID, recID = recid, appID = introReward.appID ,rID =introReward.rID , csID = user.csUser.csID, dateGiven = datetime.now())
#    myRecommendation.save()
    used,left,redeemed,recommended = user.getRewardStatistics(business)
    return render_to_response('rec.html', locals(),context_instance= RequestContext(request))

def getOffer(request,recommendedBy, rid):
    #template variables ... 
    csid = request.COOKIES.get('csID', None)
    user = CardSpringUser.objects.filter(csID = csid)
    
    if not user.exists() or csid is None:
        return loginWithRec(request,recommendedBy,rid)
  
    else:
        user = CSUser(request)
        user.addRecommendationToRewards(recommendedBy,rid)
        return redirect(settings.URL+'/home')  

def newDiscoveries(request):
    #template variables...
    user = CSUser(request)
    URL = settings.URL
    
    if request.method == 'POST':
        errors = validateCard(request)
        
    cc = Cards.objects.filter(csID = user.csUser.csID)
    
    if cc:
        hasCard = True
    
    else:
        hasCard = False
    
    
    myRewards = user.myRewards
    myUserPoints = user.userPoints
    points = 0
    redeemable = {}
    for targetReward in myRewards:
#        pointValue = 0
#        for rewardTotal in myRewards:
#            if targetReward.reward.businessID == rewardTotal.reward.businessID:
#                pointValue += len(MyRewards.objects.filter(reward = rewardTotal, reccomendedBy = user.csUser.csID, used = True))  
#                
##        pointValue = len(MyRewards.objects.filter(reward = targetReward, reccomendedBy = user.csUser.csID, used = True))  
#        if targetReward.reward.pointsNeeded <= pointValue and targetReward.used == False:
#            business = Businesses.objects.filter(businessID = targetReward.reward.businessID)[0]
#            redeemable[targetReward.reward] = business

            pointValue = len(MyRewards.objects.filter(businessID = targetReward.businessID, reccomendedBy = user.csUser.csID, used = True))
            if targetReward.reward.pointsNeeded <= pointValue and targetReward.used == False:
                business = Businesses.objects.filter(businessID = targetReward.reward.businessID)[0]
                redeemable[targetReward.reward] = business

            
    return render_to_response('newdiscoveries.html', locals(),context_instance= RequestContext(request))

def contact(request):
    errors = []
    popup = False
    if request.method == 'POST':
        if not request.POST.get('name', ''):
            errors.append('Enter a name please')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
            
        if not errors:
            popup = True
            cuf = ContactUsForm(name = request.POST.get('name'), email = request.POST.get('email'), message = request.POST.get('message'))
            cuf.save()
            return render_to_response('contact.html', locals(),context_instance= RequestContext(request))
    return render_to_response('contact.html',{'errors': errors},context_instance= RequestContext(request))

@csrf_exempt    
def callback(request):
    if request.method == "POST" or request.method == "post":
        return callBack(request)
        

def accountInfo(request):
    #template variables...       
    URL = settings.URL
    user = CSUser(request)
    csid = user.csUser.csID
    FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
    redirect = 'https://www.tivly.com/home'
    CARDSPRING_APP_ID = settings.CARDSPRING_APP_ID
    
    securityToken = IDGenerator(32)
    timestamp = datetime.now()
    key = settings.CARDSPRING_APP_ID
    raw = '{'+securityToken+'}:{'+str(datetime.now())+'}:{'+csid+'}'
    hashed = hmac.new(key, raw, sha1)
    digestedHash = '0x' + hashed.hexdigest()
    return render_to_response('myaccount.html', locals(), context_instance= RequestContext(request))

def youSure(request):
    URL = settings.URL
    return render_to_response('delete.html', locals(), context_instance= RequestContext(request))


def deleteAccount(request):
    csid = request.COOKIES.get('csID')
    csu = CardSpringUser.objects.get(csID = csid)
    fbu = FBUser.objects.get(fb_id = csu.fbID)
    token = FBAccessTokens.objects.get(user = fbu)
    Fbf = FBFriends.objects.filter(user = fbu)
    myr = MyRewards.objects.filter(csID = csid)
    
    deleteAUser(csid)
    csu.delete()
   
    token.delete()
    for f in Fbf:
        f.delete()
    
    for r in myr:
        r.delete()
    
    fbu.delete()
    return redirect('google.com')

def logout(request):
    response = redirect(settings.URL)
    response.delete_cookie('csID')
    return response

def creditCardSubmission(request):
    if request.method == 'POST':
        errors = validateCard(request)
    return render_to_response('creditcard.html', locals(),context_instance= RequestContext(request))

def faq2(request):
    return render_to_response('faq2.html',context_instance= RequestContext(request))

def aboutUs(request):
    return render_to_response('aboutus.html',context_instance= RequestContext(request))

def jobs(request):
    return render_to_response('jobs.html',context_instance= RequestContext(request))

def test(request):
    return render_to_response('test.html',context_instance= RequestContext(request))


def howto(request):
    return render_to_response('howto1.html',context_instance= RequestContext(request))
        
    



