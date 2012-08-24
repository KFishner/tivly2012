# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from Splash.models import ContactUsForm,SignUpForm, MerchantSignUpForm
from web1 import settings

def home(request):
    URL = settings.URL
    FACEBOOK_API_ID = settings.FACEBOOK_APP_ID
    errors = []
    popup = False
    if request.method == 'POST':
        if not request.POST.get('name', ''):
            errors.append('Enter a name please')
        if request.POST.get('email','') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
            
        if not errors:
            popup = True
            suf = SignUpForm(name = request.POST.get('name'), email = request.POST.get('email'))
            suf.save()
            return render_to_response('splash_index.html', locals(),context_instance= RequestContext(request))
    return render_to_response('splash_index.html',locals(),context_instance= RequestContext(request))

def contact(request):
    URL = settings.URL
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
        if not request.POST.get('restaurant', ''):
            errors.append('Enter a restaurant name please')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not request.POST.get('phone', ''):
            errors.append('Enter a phone number please')
        if not request.POST.get('address', ''):
            errors.append('Enter an address please')
        if not request.POST.get('city', ''):
            errors.append('Enter a city please')
        if not request.POST.get('state', ''):
            errors.append('Enter a state please')
        if not request.POST.get('zip', ''):
            errors.append('Enter a zip code please')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
            
        if not errors:
            popup = True
            msf = MerchantSignUpForm(phone = request.POST.get('phone'),name = request.POST.get('name'),restaurantName = request.POST.get('restaurant'), city = request.POST.get('city'), state = request.POST.get('state'), street = request.POST.get('address'),zip = request.POST.get('zip'), email = request.POST.get('email'), message = request.POST.get('message'))
            msf.save()
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

    