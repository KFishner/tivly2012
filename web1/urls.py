from django.conf.urls import patterns,include,url
from Tivly.views import login,accountInfo,aboutUs,jobs,contact,deleteAccount,home,callback,newDiscoveries,recommendation,businessInfo,getOffer, youSure, creditCardSubmission, faq2
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', login),
    url(r'^me/$', accountInfo),
    url(r'^aboutus/$', aboutUs),
    url(r'jobs/$', jobs),
    url(r'contact/$', contact),
    url(r'delete/', deleteAccount),
    url(r'^home/', home),
    url(r'^making_a_mistake', youSure),
    url(r'^callback/', callback),
    url(r'^newdiscoveries/$', newDiscoveries),
    url(r'rec/(?P<bname>\w{0,50})/$', recommendation),
    url(r'business/(?P<bname>\w{0,50})/$', businessInfo),
    url(r'offer/(?P<recid>\w{0,6})/$', getOffer),
    url(r'creditcard',creditCardSubmission),
    url(r'faq2', faq2),
)

urlpatterns = patterns('',
    url(r'^splash/', include('Splash.urls')),
)
