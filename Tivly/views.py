    # Create your views here.
from web1 import settings
from django.template import RequestContext
from Facebook import facebookLogin
from django.shortcuts import render_to_response
from Tivly.models import CardSpringUser, Rewards, Businesses, UserPoints, MyRewards, Cards,MyRecommendations
from Management import IDGenerator
from CardSpring import CreateAUser,CreateUserAppConnection,CreateACard
from django.http import HttpResponseRedirect
from googlemaps import GoogleMaps
import json

def login (request):       
    FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
    redirect = settings.FACEBOOK_REDIRECT_URI
    return render_to_response('login.html', locals())

def home(request):
    
    try:
        fbUser = facebookLogin(request)

        try:
            CSUser = CardSpringUser.objects.get(fbID = fbUser.fb_id)
            
        except:
            cardspringID = IDGenerator()
            CreateAUser(request,cardspringID)
            CSUser = CardSpringUser(csID = cardspringID, points = 0, fbID = fbUser.fb_id)
            CSUser.save()   
            
    except:
        CSUser = CardSpringUser(csID = request.COOKIES.get('csID'))
   
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

    response = render_to_response('index.html', locals(),context_instance= RequestContext(request))
    response.set_cookie('csID',CSUser.csID)
    return response

def businessInfo(request, bname):
    
    bname =  bname.replace('_',' ')
    business = Businesses.objects.filter(businessName = bname)[0]
    points = UserPoints.objects.filter(csID = request.COOKIES.get('csID'), businessID = business.businessID)[0]
    recommended = len(MyRecommendations.objects.filter(csID = request.COOKIES.get('csID'), businessID = business.businessID, received = True))
    redeemed =len(MyRecommendations.objects.filter(csID = request.COOKIES.get('csID'), businessID = business.businessID, redeemed = True))
    rewards = Rewards.objects.filter(businessID = business.businessID).order_by('pointsNeeded')
    rewards0 = rewards[0] 
    rewards1 = rewards[1]  
    rewards2 = rewards[2] 
    rewards3 = rewards[3] 
    
    progressBar1 = int(float(points.points) / float(rewards1.pointsNeeded) * 100)
    progressBar2 = int(float(points.points) / float(rewards2.pointsNeeded) * 100)
    progressBar3 = int(float(points.points) / float(rewards3.pointsNeeded) * 100)
 
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
    myRecommendation = MyRecommendations(businessID = business.businessID, received = False, redeemed = False, recID = recid, appID = rewards0.appID ,rID =rewards0.rID , csID = request.COOKIES.get('csID'))
    myRecommendation.save()

    return render_to_response('rec.html', locals(),context_instance= RequestContext(request))

def giveIntroOffer(request, recid):
#      
#    rewardLookUp = MyRecommendations.objects.filter(recID = recid)[0]
#    if rewardLookUp.received == False:
#           
#        try:
#            CSUser = CardSpringUser.objects.get(fbID = fbUser.fb_id)
#
#        except:
#            cardspringID = IDGenerator()
#            CreateAUser(request,cardspringID)
#            CSUser = CardSpringUser(csID = cardspringID, points = 0, fbID = fbUser.fb_id)
#            CSUser.save()  
#        
#        if rewardLookUp.csID == CSUser.csID:
#            rewardLookUp.delete()
#            return render_to_response('offer.html', locals(),context_instance= RequestContext(request))
#        rewardLookUp.received = True
#        rewardLookUp.reccsID = CSUser.csID
#        rewardLookUp.save()
#        
#        myReward = MyRewards(csID = CSUser.csID, reward = rewardLookUp )
#        CreateUserAppConnection(request,CSUser.csID,rewardLookUp.appID)
#        myReward.save()
#    
    return render_to_response('offer.html', locals(),context_instance= RequestContext(request))
    
def logout(request):
    return render_to_response('base.html',context_instance= RequestContext(request))

def discoveries(request):
    errors = []
    if request.method == 'POST':
        number = request.POST.get('number')
        if not number:
            errors.append('Enter a correct credit card number')
        month = request.POST.get('month')
        if not month:
            errors.append('Enter a correct month')
        year = request.POST.get('year')
        if not month:
            errors.append('Enter a correct year')
        exp = year+"-"+month
        response = CreateACard(request.COOKIES.get('csID'), number, exp)
        result = json.load(response)
        d = Cards(csID=request.COOKIES.get('csID'), token=result['token'], last4=result['last4'], expDate=result['expiration'], cardType=result['type'], typeString=result['type_string'])
        d.save()
        
    csid = request.COOKIES.get('csID')
    cc = Cards.objects.filter(csID = csid)
    hasCard = True
    
    if not cc:
        hasCard = False
    
    else:
        myRewards = MyRewards.objects.filter(csID = csid)
        myUserPoints = UserPoints.objects.filter(csID = csid)
        pointValue = -1
        redeemable = {}
        for reward in myRewards:
            for userPoints in myUserPoints:
                if userPoints.businessID == reward.reward.businessID:
                    pointValue = userPoints.points
                
            if reward.reward.pointsNeeded <= pointValue and pointValue != -1:
                business = Businesses.objects.filter(businessID = reward.reward.businessID)[0]
                redeemable[reward.reward] = business
    return render_to_response('discoveries.html', locals(),context_instance= RequestContext(request))

def getMap(request,businessid):
    GOOGLEMAPS_API_KEY = settings.GOOGLEMAPS_API_KEY
    gmaps = GoogleMaps(GOOGLEMAPS_API_KEY)
    business = Businesses.objects.filter(businessID = businessid)[0]
    address = business.street + ' ' + business.city + ' ' + str(business.zipCode)
    lat, lng = gmaps.address_to_latlng(address)
    
    rlat = lat + .003
    rlng = lng - .008
    return render_to_response('map.html', locals(),context_instance = RequestContext(request))

def accountInfo(request):
    return render_to_response('base.html',context_instance= RequestContext(request))

def aboutUs(request):
    return render_to_response('base.html',context_instance= RequestContext(request))

def jobs(request):
    return render_to_response('base.html',context_instance= RequestContext(request))

def privacy(request):
    return render_to_response('base.html',context_instance= RequestContext(request))

def contact(request):
    return render_to_response('base.html',context_instance= RequestContext(request))


        
        



