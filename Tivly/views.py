from web1 import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from Management import IDGenerator
from CardSpringActions import deleteAUser
from dateutil import parser
from django.shortcuts import redirect
from datetime import datetime
from CallBack import callBack
from Tivly.models import MerchantInfoForm,CardSpringUser, Businesses, MyRewards, Rewards, ContactUsForm, Cards, FBUser,FBFriends, FBAccessTokens
from CreditCard import validateCard
from GMaps import getMap
from GeneralUser import User
from django.views.decorators.csrf import csrf_exempt
from hashlib import sha1
import hmac
import time
from django.utils import simplejson
import json
from django.http import HttpResponse, HttpResponseRedirect

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
        return redirect(facebookRedirect)

def loginWithRec(request,recommendedBy,rid):
    #template variables...
    pictureAvailable = True
    rID = rid
    description = Rewards.objects.filter(rID = rid)[0].description
    pictureLocation = Businesses.objects.filter(businessID = Rewards.objects.filter(rID = rid)[0].businessID)[0].pictureLocation
    businessName = Businesses.objects.filter(businessID = Rewards.objects.filter(rID = rid)[0].businessID)[0].businessName
    business = Businesses.objects.filter(businessID = Rewards.objects.filter(rID = rid)[0].businessID)[0]
    FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
    facebookRedirect = 'https://www.tivly.com/home'
    csID = recommendedBy
    if rID:
        print "rID = " + str(rID)
    else:
        rID = 0
    if csID:
        print "csID = " + str(csID)
    else:
        csID = 0
    response = render_to_response('signin.html', locals(),context_instance= RequestContext(request))
    response.set_cookie('rID',rid)

    response.set_cookie('recommendedBy',recommendedBy)
    return response
                     
def home(request):
    #template variables...
    URL = settings.URL  
    user = User(request)
    
    #This checks if a user has a registered credit card, if not it asks them if they want to add a cc at this time
    cc = Cards.objects.filter(csID = user.csUser.csID)
    if cc:
        hasCard = True  
    
    else:
        hasCard = False
    
    #check if the cookie has a new reward id, if so we add that to this users list of rewards
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
    error = False
    try:
        business = Businesses.objects.filter(businessName = bname)[0]
        user = User(request)
        csID = user.csUser.csID
        used,left,redeemed,recommended = user.getRewardStatistics(business)
        print "successfully parsed info"
    except Exception as e:
        print str(e)
        error = True

    
    lat,lng = getMap(business.businessID)
    level1Reward = Rewards.objects.filter(businessID = business.businessID, level = 1)[0]
    level2Reward = Rewards.objects.filter(businessID = business.businessID, level = 2)[0]
    introReward = Rewards.objects.filter(businessID = business.businessID, level = 0)[0]

    rID = introReward.rID
    response = render_to_response('businessInfo.html', locals(),context_instance= RequestContext(request))
    return response

def recommendation(request,bname):
    #template variables...
    URL = settings.URL
    user = User(request)
    csID = user.csUser.csID
    bname =  bname.replace('_',' ')
    business = Businesses.objects.filter(businessName = bname)[0]
    level1Reward = Rewards.objects.filter(businessID = business.businessID, level = 1)[0]
    level2Reward = Rewards.objects.filter(businessID = business.businessID, level = 2)[0]
    introReward = Rewards.objects.filter(businessID = business.businessID, level = 0)[0]
    rID = introReward.rID
    used,left,redeemed,recommended = user.getRewardStatistics(business)
    return render_to_response('rec.html', locals(),context_instance= RequestContext(request))

def getOffer(request,recommendedBy, rid):
    #template variables ... 
    csid = request.COOKIES.get('csID', None)
    user = CardSpringUser.objects.filter(csID = csid)
    
    if not user.exists() or csid is None:
        return loginWithRec(request,recommendedBy,rid)
  
    else:
        user = User(request)
        user.addRecommendationToRewards(recommendedBy,rid)
        return redirect(settings.URL+'/home')  

def newDiscoveries(request):
    #template variables...
    user = User(request)
    URL = settings.URL
    
    #This checks if a user has a registered credit card, if not it asks them if they want to add a cc at this time
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
    #After receiving a notification we, add the transaction to our DB...
    if request.method == "POST" or request.method == "post":
        return callBack(request)
        
def accountInfo(request):
    #after CS.addCard is sucessful, this adds the credit card Token to our DB...
    print "****in account info"
    print request.GET
    expiration = request.GET.get("expiration", None)
    token = request.GET.get("token", None)
    last4 = request.GET.get("last4", None)
    brand = request.GET.get("brand", None)
    print "expiration = " + str(expiration);
    print "token = " + str(token);
    print "last4 = " + str(last4);
    print "brand = " + str(brand);
    if request.method == u'GET' and expiration:
        try:
            print "*****ADDING CARD*********"
            exdate = parser.parse(request.GET['expiration'])
            print "exdate = " + str(exdate)
            cardToAdd, created = Cards.objects.get_or_create(csID = request.COOKIES.get('csID'),token = request.GET['token'], last4 = request.GET['last4'], cardType = request.GET["brand"] ,typeString = request.GET['brand_string'],
            expDate = exdate)
            if created:
                cardToAdd.save();
                print "created new card"
                json_data = json.dumps({"HTTPRESPONSE":"new"})
            else:
                print "pulled old card"
                json_data = json.dumps({"HTTPRESPONSE":"old"})
            
            print "\n***successfully added!!!***\n"
            return HttpResponse(json_data, mimetype="application/json") 
         
        except Exception as e:
            print str(e)
            json_data = json.dumps({"HTTPRESPONSE":"fail"})
            return HttpResponse(json_data, mimetype="application/json")
    
    #template variables...       
    URL = settings.URL
    user = User(request)
    csid = user.csUser.csID
    FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
    redirect = 'https://www.tivly.com/home'
    CARDSPRING_APP_ID = settings.CARDSPRING_APP_ID
    
    #these are for authentication with CardSpring JS library...
    securityToken = IDGenerator(32)
    timestamp = int(time.time())
    key = settings.CARDSPRING_APP_SECRET
    raw = securityToken +':'+str(timestamp)+':'+csid
    hashed = hmac.new(key, raw, sha1)
    digestedHash = hashed.hexdigest()
    return render_to_response('myaccount.html', locals(), context_instance= RequestContext(request))

def youSure(request):
    #double checks if you truly want to delete...
    URL = settings.URL
    return render_to_response('delete.html', locals(), context_instance= RequestContext(request))


def deleteAccount(request):
    #erases all data of said user...
    
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

def merchantInfo(request):
    errors = []
    popup = False    
    
    if request.method == 'POST':
        if not request.POST.get('merchantID', ''):
            errors.append('Enter a valid Merchant ID please')
        if not request.POST.get('businessName', ''):
            errors.append('Enter a valid business name please')
        if not request.POST.get('address', ''):
            errors.append('Enter a valid street address please')
        if not request.POST.get('zipCode', ''):
            errors.append('Enter a valid zip code please')
        if not request.POST.get('city', ''):
            errors.append('Enter a valid city please')
        if not request.POST.get('state', ''):
            errors.append('Enter a valid state please')
        if not request.POST.get('phoneNumber', ''):
            errors.append('Enter a valid phone number please')
        if not request.POST.get('email', ''):
            errors.append('Enter a valid email please')
        if not request.POST.get('signerName', ''):
            errors.append('Enter a valid name for signer please')
        if not request.POST.get('signerTitle', ''):
            errors.append('Enter a valid signer title please')
        
        if not request.POST.get('agree',False):
            errors.append('Please agree to terms of service')
        
        if not errors:
            popup = True
            if  request.POST.get('amexSES'):
                msuf = MerchantInfoForm(merchantID = request.POST.get('merchantID'),businessName = request.POST.get('businessName'),amexSES = request.POST.get('amexSES'), address = request.POST.get('address'),zipCode = request.POST.get('zipCode'),city = request.POST.get('city'),state = request.POST.get('state'),phoneNumber = request.POST.get('phoneNumber'),email = request.POST.get('email'), signerName = request.POST.get('signerName'),signerTitle = request.POST.get('signerTitle'),date= datetime.now())
            else:
                msuf = MerchantInfoForm(merchantID = request.POST.get('merchantID'),businessName = request.POST.get('businessName'), amexSES = 'none',address = request.POST.get('address'),zipCode = request.POST.get('zipCode'),city = request.POST.get('city'),state = request.POST.get('state'),phoneNumber = request.POST.get('phoneNumber'),email = request.POST.get('email'), signerName = request.POST.get('signerName'),signerTitle = request.POST.get('signerTitle'),date= datetime.now())
           
            msuf.save()
            return render_to_response('merchantInfo.html', locals(),context_instance= RequestContext(request))
    return render_to_response('merchantInfo.html',{'errors': errors},context_instance= RequestContext(request))

    
######################################################################
#####                   FLAT PAGES                               #####
######################################################################

def faq2(request):
    return render_to_response('faq2.html',context_instance= RequestContext(request))

def aboutUs(request):
    return render_to_response('aboutus.html',context_instance= RequestContext(request))

def jobs(request):
    return render_to_response('jobs.html',context_instance= RequestContext(request))

def test(request):
    return render_to_response('test.html',context_instance= RequestContext(request))


def howto(request,number):
    
    URL = settings.URL
    csid = request.COOKIES.get('csID')
    user = User(request)
    rewards = user.myRewards
    
    for reward in rewards:
        if reward.reward.level == 0:
            introReward = reward.reward
            break
        
    business = Businesses.objects.filter(businessID = introReward.businessID)[0]
    
    #these are for authentication with CardSpring JS library...
    securityToken = IDGenerator(32)
    timestamp = int(time.time())
    key = settings.CARDSPRING_APP_SECRET
    raw = securityToken +':'+str(timestamp)+':'+ csid
    hashed = hmac.new(key, raw, sha1)
    digestedHash = hashed.hexdigest()
    return render_to_response('howto'+str(number)+'.html',locals(),context_instance= RequestContext(request))

def businessDashboard(request):
    return render_to_response('bizdash.html',context_instance= RequestContext(request))
