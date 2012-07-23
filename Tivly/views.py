# Create your views here.
from web1 import settings
from django.template import RequestContext
from Facebook import facebookLogin
from django.shortcuts import render_to_response
from Management import IDGenerator
from CardSpring import createAUser,createUserAppConnection, deleteAUser
from django.shortcuts import redirect
from googlemaps import GoogleMaps
from datetime import datetime
from CallBack import callBack
from Tivly.models import CardSpringUser, MyRecommendations,UserPoints, Businesses, MyRewards, Rewards, ContactUsForm, Cards, FBUser,FBFriends, FBAccessTokens

import json

def validateCard(request):
    errors = []
    number = request.POST.get('number')
    if not number:
        errors.append('Enter a correct credit card number')
    
    month = request.POST.get('month')
    if not month:
        errors.append('Enter a correct month')
    
    year = request.POST.get('year')
    if not year:
        errors.append('Enter a correct year')
    
    if not errors:
        result = json.load(request.POST.get())
        d = Cards(csID=request.COOKIES.get('csID'), token=result['token'], last4=result['last4'], expDate=result['expiration'], cardType=result['type'], typeString=result['type_string'])
        d.save()
    else:
        return errors  

def getCardSpringUser(request):
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
        CSUser = CardSpringUser.objects.filter(csID = request.COOKIES.get('csID'))
    
    else:
        cardspringID = IDGenerator()
        CSUser = CardSpringUser(csID = cardspringID, points = 0, fbID = fbUser.fb_id, dateJoined = datetime.now())
        CSUser.save()                
        createAUser(cardspringID)
        CSUser = CardSpringUser.objects.filter(csID = cardspringID)
    
    CSUser = CSUser[0]
    return CSUser

def addRecommendationToRewards(request,CSUser,recid):
    rec = MyRecommendations.objects.filter(recID = recid)  
    if rec.exists():
        rec = rec[0]
        userPoints = UserPoints.objects.filter(csID = CSUser.csID, businessID = rec.businessID)
            
        if not userPoints.exists():
            userPoints = UserPoints(csID = CSUser.csID, businessID = rec.businessID, points = 0, visits = 0)
            userPoints.save()
            setReward(CSUser.csID,request,recid)
    return

def getRewardStatistics(business,csid):
    allRewards = Rewards.objects.filter(businessID = business.businessID)
    allMyRewards = MyRewards.objects.filter(csID = csid)
    used = len(MyRewards.objects.filter(csID = csid, used = True))
    left = len(allMyRewards) - used
    redeemed = 0
    recommended = len(MyRecommendations.objects.filter(csID =csid, businessID = business.businessID))
    for rewardLookUp in allRewards:
        redeemed += len(MyRewards.objects.filter(reccomendedBy = csid, reward = rewardLookUp))
    
    return used,left,redeemed,recommended

def setReward(csid,request, recid):
    recommendation = MyRecommendations.objects.filter(recID = recid)[0]
    createUserAppConnection(csid,recommendation.appID)
    recReward = Rewards.objects.filter(appID = recommendation.appID)[0]
    myReward = MyRewards(csID = csid, reward = recReward, reccomendedBy = recommendation.csID, used = False)
    myReward.save()
    recommendation.delete()

def getMap(businessid):
    GOOGLEMAPS_API_KEY = settings.GOOGLEMAPS_API_KEY
    gmaps = GoogleMaps(GOOGLEMAPS_API_KEY)
    business = Businesses.objects.filter(businessID = businessid)[0]
    address = business.street + ' ' + business.city + ' ' + str(business.zipCode)
    lat, lng = gmaps.address_to_latlng(address)
    return lat,lng

###############################################################################################
def login (request):
    #template variables...       
    FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
    redirect = settings.FACEBOOK_REDIRECT_URI
    
    if request.method == 'POST':
        errors = validateCard(request)

    return render_to_response('signin.html', locals(),context_instance= RequestContext(request))
    

def loginWithRec (request,recid):
    #template variables...
    FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
    redirect = settings.FACEBOOK_REDIRECT_URI
    
    response = render_to_response('signin.html', locals(),context_instance= RequestContext(request))
    response.set_cookie('recID',recid)
    return response
                     
def home(request):
    #template variables...
    URL = settings.URL
    
    CSUser = getCardSpringUser(request)
    recid = request.COOKIES.get('recID', None)
    
    if recid is not None:
        addRecommendationToRewards(request, CSUser, recid)
    
    myRewards = MyRewards.objects.filter(csID = CSUser.csID)
    businessList= []
    
    for reward in myRewards:
        business = Businesses.objects.filter(businessID = reward.reward.businessID)[0]
        if business in businessList:
            continue
        else:
            businessList.append(business)
    
    response = render_to_response('myfavorites.html', locals(),context_instance= RequestContext(request))
    response.set_cookie('csID',CSUser.csID)
    return response

def businessInfo(request, bname):
    #template variables...
    bname =  bname.replace('_',' ')
    csid = request.COOKIES.get('csID')
    business = Businesses.objects.filter(businessName = bname)[0]
    lat,lng = getMap(business.businessID)
    rewards0 = Rewards.objects.filter(businessID = business.businessID, pointsNeeded = 0)[0]
    used,left,redeemed,recommended = getRewardStatistics(business,csid)
    
    
    response = render_to_response('businessInfo.html', locals(),context_instance= RequestContext(request))
    return response

def recommendation(request,bname):
    #template variables...
    URL = settings.URL
    csid = request.COOKIES.get('csID')
    bname =  bname.replace('_',' ')
    business = Businesses.objects.filter(businessName = bname)[0]
   
    rewards = Rewards.objects.filter(businessID = business.businessID)
    for reward in rewards:
        if reward.pointsNeeded == 0: 
            rewards0 = reward 
    recid = IDGenerator()
    myRecommendation = MyRecommendations(businessID = business.businessID, recID = recid, appID = rewards0.appID ,rID =rewards0.rID , csID = csid, dateGiven = datetime.now())
    myRecommendation.save()
    
    used,left,redeemed,recommended = getRewardStatistics(business,csid)
    return render_to_response('rec.html', locals(),context_instance= RequestContext(request))

def getOffer(request, recid):
    #template variables ... 
    csid = request.COOKIES.get('csID', None)
    
    CSUser = CardSpringUser.objects.filter(csID = csid)
    if not CSUser.exists() or csid is None:
        return loginWithRec(request,recid)
  
    else:
        addRecommendationToRewards(request,CSUser,recid)
        return redirect(settings.URL+'/home')  

def discoveries(request):
    #template variables...
    errors = []
    csid = request.COOKIES.get('csID')
    URL = settings.URL
    
    if request.method == 'POST':
        errors = validateCard(request)
        
    cc = Cards.objects.filter(csID = csid)
    
    if cc:
        hasCard = True
    
    else:
        hasCard = False
    
    
    myRewards = MyRewards.objects.filter(csID = csid)
    myUserPoints = UserPoints.objects.filter(csID = csid)
    
    redeemable = {}
    for reward in myRewards:
        pointValue = -1
        for userPoints in myUserPoints:
            if userPoints.businessID == reward.reward.businessID:
                pointValue = userPoints.points
            
        if reward.reward.pointsNeeded <= pointValue and pointValue != -1:
            business = Businesses.objects.filter(businessID = reward.reward.businessID)[0]
            redeemable[reward.reward] = business
            
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


def callback(request):
    if request.method == "POST":
        callBack(request)
        

def accountInfo(request):
    #template variables...
    URL = settings.URL
    FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
    redirect = settings.FACEBOOK_REDIRECT_URI
    return render_to_response('myaccount.html',context_instance= RequestContext(request))

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
    deleted = True
    URL = settings.URL
    FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
    redirect = settings.FACEBOOK_REDIRECT_URI
    return render_to_response('myaccount.html',context_instance= RequestContext(request))

    
def aboutUs(request):
    return render_to_response('aboutus.html',context_instance= RequestContext(request))

def jobs(request):
    return render_to_response('jobs.html',context_instance= RequestContext(request))

        
    



