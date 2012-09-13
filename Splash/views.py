# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from Splash.models import ContactUsForm, MerchantSignUpForm
from web1 import settings
from django.core.mail import *
def home(request):
    URL = settings.URL
    FACEBOOK_API_ID = settings.FACEBOOK_APP_ID
    return render_to_response('splash_index.html',locals(),context_instance= RequestContext(request))

def contact(request):
    URL = settings.URL
    errors = []
    popup = False
    if request.method == 'POST':
        if not request.POST.get('name', ''):
            errors.append('Enter a name please')
        else:
            name = request.POST.get('name', '')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        else:
            email = request.POST.get('email')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        else:
            message = request.POST.get('message')
            
        if not errors:
            popup = True
            cuf = ContactUsForm(name = name, email = email, message = message)
            cuf.save()
            subject = "New contact us request: %s" % str(name)
            fromAddr = "newcontactus@tivly.com"
            body = "%s just contacted us. \n\nMessage:\n\n==========================\n\n%s\n\n==========================\n\n Email them at %s" % (str(name), str(message), str(email))
            kevemail = "KFishner@gmail.com"
            messages = []
            
            try:
                messages.append((subject, body, fromAddr, [kevemail.encode('ascii')]))
                messages = tuple(messages)
                #print messages
                print "sending kevin messages"  
                send_mass_mail(messages)
                print "message sent, exiting"
            except Exception as e:
                print str(e)
            return render_to_response('splash_contact.html', locals(),context_instance= RequestContext(request))
    return render_to_response('splash_contact.html',locals(),context_instance= RequestContext(request))

def merchants(request):
    URL = settings.URL
    return render_to_response('splash_merchants.html',locals(), context_instance= RequestContext(request))

def merchantsignup(request):
    URL = settings.URL
    errors = []
    popup = False
    FACEBOOK_API_ID = settings.FACEBOOK_APP_ID
    if request.method == 'POST':
        if not request.POST.get('name', ''):
            errors.append('Enter a name please')
        else:
            name = request.POST.get('name', '')
        if not request.POST.get('restaurant', ''):
            errors.append('Enter a restaurant name please')
        else:
            resname = request.POST.get('restaurant', '')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        else:
            email = request.POST.get('email', '')
        if not request.POST.get('phone', ''):
            errors.append('Enter a phone number please')
        else:
            phone = request.POST.get('phone', '')
        if not request.POST.get('address', ''):
            errors.append('Enter an address please')
        else:
            address = request.POST.get('address', '')
        if not request.POST.get('city', ''):
            errors.append('Enter a city please')
        else:
            city = request.POST.get('city', '')
        if not request.POST.get('state', ''):
            errors.append('Enter a state please')
        else:
            state = request.POST.get('state', '')
        if not request.POST.get('zip', ''):
            errors.append('Enter a zip code please')
        else:
            zipcode = request.POST.get('zip', '')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        else:
            message = request.POST.get('message', '')
            
        if not errors:
            popup = True
            try:
                msf = MerchantSignUpForm(phone = phone,name = name,restaurantName = resname, city = city, state = state, street = address,zip = zipcode, email = email, message = message)
                msf.save()
                subject = "New Merchant Info: %s" % str(resname)
                fromAddr = "newmerchant@tivly.com"
                body = "%s from %s, %s, just requested more information. Email %s at %s" % (str(resname),str(city), str(state), str(name), str(email))
                kevemail = "KFishner@gmail.com"
                messages = []
            except Exception as e:
                print str(e)
            
            try:
                messages.append((subject, body, fromAddr, [kevemail.encode('ascii')]))
                messages = tuple(messages)
                #print messages
                print "sending kevin messages"  
                send_mass_mail(messages)
                print "message sent, exiting"
            except Exception as e:
                print str(e)
            return render_to_response('splash_merchantsignup.html', locals(),context_instance= RequestContext(request))
    return render_to_response('splash_merchantsignup.html',locals(),context_instance= RequestContext(request))


def faq(request):
    URL = settings.URL
    return render_to_response('splash_faq.html',locals(),context_instance= RequestContext(request))

def aboutus(request):
    URL = settings.URL
    return render_to_response('splash_aboutus.html',locals(),context_instance= RequestContext(request))

def jobs(request):
    URL = settings.URL
    return render_to_response('splash_jobs.html',locals(),context_instance= RequestContext(request))

def privacy(request):
    URL = settings.URL
    return render_to_response('splash_privacy.html',locals(),context_instance= RequestContext(request))

def userterms(request):
    URL = settings.URL
    return render_to_response('splash_userterms.html',locals(),context_instance= RequestContext(request))

    
