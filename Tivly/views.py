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
    
    CSUser = CardSpringUser(request)
    recid =request.COOKIES.get('recID', None)
    rec = MyRecommendations.objects.filter(recID = recid)
    
    if rec.exists() is not None :
        CSUser.addRecommendationToRewards(recid)

    businessList= []
    
    for reward in CSUser.myRewards:
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
    CSUser = CardSpringUser(request)
    business = Businesses.objects.filter(businessName = bname)[0]
    lat,lng = getMap(business.businessID)
    rewards0 = Rewards.objects.filter(businessID = business.businessID, pointsNeeded = 0)[0]
    used,left,redeemed,recommended = CSUser.getRewardStatistics(business)
    
    
    response = render_to_response('businessInfo.html', locals(),context_instance= RequestContext(request))
    return response

def recommendation(request,bname):
    #template variables...
    URL = settings.URL
    CSUser = CardSpringUser(request)
    bname =  bname.replace('_',' ')
    business = Businesses.objects.filter(businessName = bname)[0]
   
    rewards = Rewards.objects.filter(businessID = business.businessID)
    for reward in rewards:
        if reward.pointsNeeded == 0: 
            rewards0 = reward 
    recid = IDGenerator()
    myRecommendation = MyRecommendations(businessID = business.businessID, recID = recid, appID = rewards0.appID ,rID =rewards0.rID , csID = CSUser.csID, dateGiven = datetime.now())
    myRecommendation.save()
    
    used,left,redeemed,recommended = CSUser.getRewardStatistics(business)
    return render_to_response('rec.html', locals(),context_instance= RequestContext(request))

def getOffer(request, recid):
    #template variables ... 
    csid = request.COOKIES.get('csID', None)
    CSUser = CardSpringUser.objects.filter(csID = csid)
    
    if not CSUser.exists() or csid is None:
        return loginWithRec(request,recid)
  
    else:
        CSUser = CardSpringUser(request)
        CSUser.addRecommendationToRewards(request,CSUser,recid)
        return redirect(settings.URL+'/home')  

def newDiscoveries(request):
    #template variables...
    CSUser = CardSpringUser(request)
    URL = settings.URL
    
    if request.method == 'POST':
        errors = validateCard(request)
        
    cc = Cards.objects.filter(csID = CSUser.csID)
    
    if cc:
        hasCard = True
    
    else:
        hasCard = False
    
    
    myRewards = CSUser.myRewards
    myUserPoints = CSUser.userPoints
    
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
    return render_to_response('myaccount.html', locals(), context_instance= RequestContext(request))

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
    return render_to_response('myaccount.html', locals(),context_instance= RequestContext(request))

    
def aboutUs(request):
    return render_to_response('aboutus.html',context_instance= RequestContext(request))

def jobs(request):
    return render_to_response('jobs.html',context_instance= RequestContext(request))

        
    



