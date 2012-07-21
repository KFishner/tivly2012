'''
Created on Jun 30, 2012

@author: bryanantigua
'''
import json
import urllib2
from urlparse import parse_qsl
from datetime import datetime
from Tivly.models import FBUser,FBAccessTokens,FBFriends
from web1 import settings
    
#facebook code for authentication...
def facebookLogin(request):         
    code = request.GET.get('code', '')    
    
    #aquire access token and expiration...
    response = urllib2.urlopen("https://graph.facebook.com/oauth/access_token?client_id="+ 
    settings.FACEBOOK_APP_ID +"&redirect_uri="+settings.FACEBOOK_REDIRECT_URI+"&client_secret="+ 
    settings.FACEBOOK_API_SECRET+"&code="+code)
    html = response.read()
    dic = dict(parse_qsl(html))
    
    #getting profile, email, and friends...
    graphUrl = 'https://graph.facebook.com/'
    accessToken = '?access_token='+dic.get('access_token')
    
    url = graphUrl + 'me' + accessToken
    response = urllib2.urlopen(url)
    profile = json.load(response)
    
    url = graphUrl + 'me/friends' + accessToken
    response = urllib2.urlopen(url)
    friends = json.load(response)['data']
    
    #if not in database add User to Database...    
    fbUser, created = FBUser.objects.get_or_create(first_name = profile["first_name"],last_name= profile["last_name"], email = profile["email"],
    gender=profile["gender"],fb_id = profile["id"],location = profile["locale"])
    atcreated = False
    if created:
        fbUser.date_joined = datetime.now()
        fbUser.save()
        
        accessToken = FBAccessTokens(accessToken = dic.get('access_token'), expiration_accessToken = dic.get('expires'), 
                                     user = fbUser, date_created =datetime.now())
        accessToken.save()
        atcreated = True
        
        for friend in friends:
            try:
                facebookFriends = FBFriends(name=friend["name"],friend_fb_id =friend["id"],user=fbUser)
                facebookFriends.save()

            except:
                continue
    
    if atcreated == False:
        FBA = FBAccessTokens.objects.filter(user = fbUser)
        if FBA.exists():
            if dic.get('access_token') != FBAccessTokens.objects.filter(user = fbUser)[0]:
                accessToken =  FBAccessTokens.objects.filter(user = fbUser)[0]
                accessToken.accessToken = dic.get('access_token')
                accessToken.expiration_accessToken = dic.get('expires')
                accessToken.save()            
    return fbUser