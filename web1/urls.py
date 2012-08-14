from django.conf.urls import patterns,include,url
from Tivly.views import login,accountInfo,aboutUs,jobs,contact,deleteAccount,logout,home,callback,newDiscoveries, test, recommendation,businessInfo,getOffer, youSure, faq2
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', login),
    url(r'^me/$', accountInfo),
    url(r'^aboutus/$', aboutUs),
    url(r'^logout/', logout),
    url(r'^jobs/$', jobs),
    url(r'^contact/$', contact),
    url(r'^delete/', deleteAccount),
    url(r'^home/', home),
    url(r'^making_a_mistake', youSure),
    url(r'^callback',csrf_exempt(callback)),
    url(r'^newdiscoveries/$', newDiscoveries),
    url(r'rec/(?P<bname>\w{0,50})/$', recommendation),
    url(r'^business/(?P<bname>\w{0,50})/$', businessInfo),
    url(r'^offer/(?P<recommendedBy>\w{0,6})/(?P<rid>\w{0,6})/$', getOffer),
    )

urlpatterns += patterns('',
    url(r'^splash/', include('Splash.urls')),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

