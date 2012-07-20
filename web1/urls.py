from django.conf.urls import patterns, include, url
from Tivly.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web1.views.home', name='home'),
    # url(r'^web1/', include('web1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^me/$', accountInfo),
    url(r'^logout/$', logout),
    url(r'^aboutUs/$', aboutUs),
    url(r'jobs/$', jobs),
    url(r'privacy/$', privacy),
    url(r'contact/$', contact),
    url(r'^$', login),
    url(r'^home/(?P<recid>\w{6})/$',homeWithRec),
    url(r'^home/', home),
    url(r'maps/(?P<businessid>\w{0,50})/$', getMap),
    url(r'^newdiscoveries/$', discoveries),
    url(r'rec/(?P<bname>\w{0,50})/$', recommendation),
    url(r'venues/(?P<bname>\w{0,50})/$', businessInfo),
    url(r'offer/(?P<recid>\w{0,6})/$', getOffer)
)