# Create your views here.
from web1 import settings
from django.template import RequestContext
from Facebook import facebookLogin
from django.shortcuts import render_to_response
from Management import IDGenerator
from CardSpring import CreateAUser,CreateUserAppConnection
from django.shortcuts import redirect
from googlemaps import GoogleMaps
from datetime import datetime
from Tivly.models import CardSpringUser, MyRecommendations,UserPoints, Businesses, MyRewards, Rewards, ContactUsForm, Cards

import json

def login (request):       
    FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
    redirect = settings.FACEBOOK_REDIRECT_URI
    return render_to_response('login.html', locals())

def loginWithRec (request,recid):
    FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
    redirect = settings.FACEBOOK_REDIRECT_URI
    response = render_to_response('login.html', locals())
    response.set_cookie('recID',recid)
    return response

def home(request):
    URL = settings.URL
    code = request.GET.get('code', None)    
    cardspringID = request.COOKIES.get('csID',None)

    if code is not None:
        fbUser = facebookLogin(request)
        CSUser = CardSpringUser.objects.filter(fbID = fbUser.fb_id)
        if not CSUser.exists():
            cardspringID = IDGenerator()
            CSUser = CardSpringUser(csID = cardspringID, points = 0, fbID = fbUser.fb_id, dateJoined = datetime.now())
            CSUser.save()                
            CreateAUser(cardspringID)
            justCreated = True
            CSUser = CardSpringUser.objects.filter(csID = cardspringID)
    
    elif cardspringID is not None:
        CSUser = CardSpringUser.objects.filter(csID = request.COOKIES.get('csID'))
    
    else:
        cardspringID = IDGenerator()
        CSUser = CardSpringUser(csID = cardspringID, points = 0, fbID = fbUser.fb_id, dateJoined = datetime.now())
        CSUser.save()                
        CreateAUser(cardspringID)
        justCreated = True
        CSUser = CardSpringUser.objects.filter(csID = cardspringID)
    
    CSUser = CSUser[0]
    recid = request.COOKIES.get('recID', None)
    
    if recid is not None:
        rec = MyRecommendations.objects.filter(recID = recid)
        
        if rec.exists():
            rec = rec[0]
            userPoints = UserPoints.objects.filter(csID = CSUser.csID, businessID = rec.businessID)
            
            if not userPoints.exists():
                userPoints = UserPoints(csID = CSUser.csID, businessID = rec.businessID, points = 0, visits = 0)
                userPoints.save()
                setReward(CSUser.csID,request,recid)
                 
    URL = settings.URL    

    myRewards = MyRewards.objects.filter(csID = CSUser.csID)
    businessList= []
    
    for reward in myRewards:
        business = Businesses.objects.filter(businessID = reward.reward.businessID)[0]
        if business in businessList:
            continue
        else:
            businessList.append(business)
        
    allPoints = UserPoints.objects.filter(csID = CSUser.csID)

    
    response = render_to_response('myfvorites.html', locals(),context_instance= RequestContext(request))
    response.set_cookie('csID',CSUser.csID)
    return response

def businessInfo(request, bname):
    
    bname =  bname.replace('_',' ')
    business = Businesses.objects.filter(businessName = bname)[0]
    points = UserPoints.objects.filter(csID = request.COOKIES.get('csID'), businessID = business.businessID)[0]
    recommended = len(MyRecommendations.objects.filter(csID = request.COOKIES.get('csID'), businessID = business.businessID))
    
    allRewards = Rewards.objects.filter(businessID = business.businessID)
    redeemed = 0
    
    allMyRewards = MyRewards.objects.filter(csID = request.COOKIES.get('csID'))
    used = len(MyRewards.objects.filter(csID = request.COOKIES.get('csID'), used = True))
    left = len(allMyRewards) - used
    for rewardLookUp in allRewards:
        redeemed += len(MyRewards.objects.filter(reccomendedBy = request.COOKIES.get('csID'), reward = rewardLookUp))
    
    rewards = Rewards.objects.filter(businessID = business.businessID).order_by('pointsNeeded')
    rewards0 = rewards[0] 
    rewards1 = rewards[1]  
    rewards2 = rewards[2] 
    rewards3 = rewards[3] 
    
    
    lat,lng = getMap(business.businessID)
    response = render_to_response('businessInfo.html', locals(),context_instance= RequestContext(request))
    return response

def recommendation(request,bname):
    URL = settings.URL
    bname =  bname.replace('_',' ')
    business = Businesses.objects.filter(businessName = bname)[0]
    rewards = Rewards.objects.filter(businessID = business.businessID)
    for reward in rewards:
        if reward.pointsNeeded == 0: 
            rewards0 = reward 
    recid = IDGenerator()
    myRecommendation = MyRecommendations(businessID = business.businessID, recID = recid, appID = rewards0.appID ,rID =rewards0.rID , csID = request.COOKIES.get('csID'), dateGiven = datetime.now())
    myRecommendation.save()
    
    recommended = len(MyRecommendations.objects.filter(csID = request.COOKIES.get('csID'), businessID = business.businessID))
    allRewards = Rewards.objects.filter(businessID = business.businessID)
    redeemed = 0
    
    for rewardLookUp in allRewards:
        redeemed += len(MyRewards.objects.filter(reccomendedBy = request.COOKIES.get('csID'), reward = rewardLookUp))
    
    myRewardsRemaining = len(MyRewards.objects.filter(csID = request.COOKIES.get('csID'),used = False))
    myRewardsUsed = len(MyRewards.objects.filter(csID = request.COOKIES.get('csID'),used = True))

    return render_to_response('rec.html', locals(),context_instance= RequestContext(request))

def getOffer(request, recid):
        
    csid = request.COOKIES.get('csID', None)
    CSUser = CardSpringUser.objects.filter(csID = csid)
    
    if not CSUser.exists() or csid is None:
        return loginWithRec(request,recid)
  
    else:
        rec = MyRecommendations.objects.filter(recID = recid)
        
        if rec.exists():
            rec =rec[0]
            userPoints = UserPoints.objects.filter(csID = csid, businessID = rec.businessID)
            
            if not userPoints.exists():
                userPoints = UserPoints(csID = csid, businessID = rec.businessID, points = 0, visits = 0)
                userPoints.save() 
        
                setReward(csid,request, recid)    
        return redirect(settings.URL+'/home')

def setReward(csid,request, recid):
    recommendation = MyRecommendations.objects.filter(recID = recid)[0]
    CreateUserAppConnection(csid,recommendation.appID)
    recReward = Rewards.objects.filter(appID = recommendation.appID)[0]
    myReward = MyRewards(csID = csid, reward = recReward, reccomendedBy = recommendation.csID, used = False)
    myReward.save()
    recommendation.delete()  
    
def logout(request):
    return render_to_response('base.html',context_instance= RequestContext(request))

def discoveries(request):
    errors = []
    URL = settings.URL
    if request.method == 'POST':
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
            exp = year+"-"+month
            result = json.load(request.POST.get())
            d = Cards(csID=request.COOKIES.get('csID'), token=result['token'], last4=result['last4'], expDate=result['expiration'], cardType=result['type'], typeString=result['type_string'])
            d.save()
            
    csid = request.COOKIES.get('csID')
    cc = Cards.objects.filter(csID = csid)
    hasCard = True
    
    if not cc:
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

def getMap(businessid):
    GOOGLEMAPS_API_KEY = settings.GOOGLEMAPS_API_KEY
    gmaps = GoogleMaps(GOOGLEMAPS_API_KEY)
    business = Businesses.objects.filter(businessID = businessid)[0]
    address = business.street + ' ' + business.city + ' ' + str(business.zipCode)
    lat, lng = gmaps.address_to_latlng(address)
    return lat,lng

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


def accountInfo(request):
    return render_to_response('base.html',context_instance= RequestContext(request))

def aboutUs(request):
    return render_to_response('aboutus.html',context_instance= RequestContext(request))

def jobs(request):
    return render_to_response('jobs.html',context_instance= RequestContext(request))

def privacy(request):
    return render_to_response('base.html',context_instance= RequestContext(request))

        
        



