from django.conf import settings

def cardspring(request):
    return { 'CARDSPRING_APP_ID': settings.CARDSPRING_APP_ID }
