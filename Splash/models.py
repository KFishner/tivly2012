from django.db import models

class SignUpForm(models.Model):
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 60)
    
class MerchantSignUpForm(models.Model):
    name = models.CharField(max_length = 40)
    restaurantName = models.CharField(max_length = 50)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 2)
    street = models.CharField(max_length = 100)
    zip = models.IntegerField()
    email = models.CharField(max_length = 60)
    phone = models.BigIntegerField()
    message = models.CharField(max_length = 400)

class ContactUsForm(models.Model):
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 60)
    message = models.CharField(max_length = 400)
    
