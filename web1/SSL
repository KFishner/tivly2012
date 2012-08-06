'''
Created on Aug 6, 2012

@author: bryanantigua
'''
import re

from django.conf import settings
from django.core import urlresolvers
from django.http import HttpResponse, HttpResponseRedirect


class SSLMiddleware(object):

    def process_request(self, request):
        if not any([settings.DEBUG, request.is_secure(), request.META.get("HTTP_X_FORWARDED_PROTO", "") == 'https']):
            url = request.build_absolute_uri(request.get_full_path())
            secure_url = url.replace("http://", "https://")
            return HttpResponseRedirect(secure_url)