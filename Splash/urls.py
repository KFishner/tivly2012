from django.conf.urls import patterns, include, url
from Splash.views import home, contact, merchants, merchantsignup, faq, aboutus, jobs
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',   
    url(r'^$', home),
    url(r'^contact/', contact),
    url(r'^merchants/', merchants),
    url(r'^merchantsignup/', merchantsignup),
    url(r'^faq/', faq),
    url(r'^aboutus/',aboutus),
    url(r'^jobs/', jobs),    
)