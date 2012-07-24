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

def login (request):
    #template variables...       
    FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
    facebookRedirect = settings.FACEBOOK_REDIRECT_URI
    redirectURL = settings.URL + '/splash'

    csid = request.COOKIES.get('csID',None)
    if csid is not None:
        return redirect(redirectURL)
    else:
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
    user = CSUser(request)
    
    cc = Cards.objects.filter(csID = user.csUser.csID)
    
    if cc:
        hasCard = True
    
    else:
        hasCard = False
    recid =request.COOKIES.get('recID', None)
    rec = MyRecommendations.objects.filter(recID = recid)
    
    if rec.exists():
        user.addRecommendationToRewards(recid)

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
    bname =  bname.replace('_',' ')
    user = CSUser(request)
    business = Businesses.objects.filter(businessName = bname)[0]
    lat,lng = getMap(business.businessID)
    rewards0 = Rewards.objects.filter(businessID = business.businessID, pointsNeeded = 0)[0]
    used,left,redeemed,recommended = user.getRewardStatistics(business)
    
    
    response = render_to_response('businessInfo.html', locals(),context_instance= RequestContext(request))
    return response

def recommendation(request,bname):
    #template variables...
    URL = settings.URL
    user = CSUser(request)
    bname =  bname.replace('_',' ')
    business = Businesses.objects.filter(businessName = bname)[0]
   
    rewards = Rewards.objects.filter(businessID = business.businessID)
    for reward in rewards:
        if reward.pointsNeeded == 0: 
            rewards0 = reward 
    recid = IDGenerator()
    myRecommendation = MyRecommendations(businessID = business.businessID, recID = recid, appID = rewards0.appID ,rID =rewards0.rID , csID = user.csUser.csID, dateGiven = datetime.now())
    myRecommendation.save()
    
    used,left,redeemed,recommended = user.getRewardStatistics(business)
    return render_to_response('rec.html', locals(),context_instance= RequestContext(request))

def getOffer(request, recid):
    #template variables ... 
    csid = request.COOKIES.get('csID', None)
    user = CardSpringUser.objects.filter(csID = csid)
    
    if not user.exists() or csid is None:
        return loginWithRec(request,recid)
  
    else:
        user = CSUser(request)
        user.addRecommendationToRewards(recid)
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

        
    



