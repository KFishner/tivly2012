from django.conf.urls import patterns,include,url
from Tivly.views import login, privacy,userterms,merchantInfo,accountInfo,aboutUs,howto,jobs,businessDashboard,contact,deleteAccount,logout,home,callback,newDiscoveries,recommendation,businessInfo,getOffer, youSure
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
    url(r'howto/(\d{1})',howto),
    url(r'^making_a_mistake', youSure),
    url(r'^callback',csrf_exempt(callback)),
    url(r'^newdiscoveries/$', newDiscoveries),
    url(r'rec/(?P<bname>\w{0,50})/$', recommendation),
    url(r'^business/(?P<bname>\w{0,50})/$', businessInfo),
    url(r'^merchantInfo/$', merchantInfo),
    url(r'^offer/(?P<recommendedBy>\w{0,6})/(?P<rid>\w{0,6})/$', getOffer),
    url(r'^bizdash/',businessDashboard),
    url(r'^privacy/', privacy),
    url(r'^userterms/', userterms),
    )

urlpatterns += patterns('',
    url(r'^splash/', include('Splash.urls')),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

