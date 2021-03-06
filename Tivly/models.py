from django.db import models

#######################################################
######                  FACEBOOK                 ######
#######################################################

class FBUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length= 40)
    gender = models.CharField(max_length=30)
    fb_id = models.CharField(max_length = 30)
    location = models.CharField(max_length=30)
    date_joined = models.DateField(blank = True, null = True)
        
class FBAccessTokens(models.Model):
    accessToken = models.CharField(max_length=300)
    expiration_accessToken = models.CharField(max_length=30)
    user = models.ForeignKey(FBUser)
    date_created = models.DateField()

#######################################################
######                CARDSPRING                 ######
#######################################################


#=======================GENERAL=======================#
class Businesses(models.Model):
    businessID = models.CharField(max_length = 40)
    businessName = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    street = models.CharField(max_length = 30)
    zipCode = models.IntegerField()
    mondayHours = models.CharField(max_length = 20)
    tuesdayHours= models.CharField(max_length = 20)
    wednesdayHours= models.CharField(max_length = 20)
    thursdayHours= models.CharField(max_length = 20)
    fridayHours= models.CharField(max_length = 20)
    saturdayHours= models.CharField(max_length = 20)
    sundayHours= models.CharField(max_length = 20)
    description = models.CharField(max_length = 400)
    pictureLocation = models.CharField(max_length = 50)
    website = models.CharField(max_length = 50)
    #extPictureLocation = models.CharField(max_length = 80)
    
class Rewards(models.Model):
    rID = models.CharField(max_length = 6)
    appID = models.CharField(max_length = 40)
    businessID = models.CharField(max_length = 40)
    description = models.CharField(max_length = 300)
    pointsNeeded = models.IntegerField()
    level = models.IntegerField()

#==================USER SPECIFIC=======================#
    
class CardSpringUser(models.Model):
    csID = models.CharField(max_length = 6)
    points = models.IntegerField()
    fbID = models.BigIntegerField(blank = True, null = True)
    TwitID = models.BigIntegerField(blank = True, null = True)
    dateJoined = models.DateField(blank = True, null = True)
    emailed = models.BooleanField(default=False)
    
class Cards(models.Model):
    csID = models.CharField(max_length = 6)
    token = models.CharField(max_length = 30)
    last4 = models.IntegerField()
    expDate = models.CharField(max_length = 20)
#    expDate = models.CharField(maxlink _length =20 )
    cardType = models.CharField(max_length = 20)
    typeString = models.CharField(max_length = 20)
    
class MyRewards(models.Model):
    csID = models.CharField(max_length = 6)
    reccomendedBy = models.CharField(max_length = 6)
    reward = models.ForeignKey(Rewards)
    businessID = models.CharField(max_length = 40)
    used = models.BooleanField(default=False)
    dateUsed = models.DateField(blank = True, null = True)


#######################################################
######              ANALYTICS                    ######
#######################################################

class Transaction(models.Model):
    csID = models.CharField(max_length = 6)
    appID = models.CharField(max_length = 40)
    date = models.DateField()
    event_type = models.CharField(max_length = 20)
    businessID = models.CharField(max_length = 30)
    currency = models.CharField(max_length = 5)
    amount = models.IntegerField()
    card_token = models.CharField(max_length = 30)
    transaction_id = models.CharField(max_length = 30)
    store_id = models.CharField(max_length = 30) 
    date = models.DateField(blank = True, null = True)

class UniqueRewardHistory(models.Model):
    csID = models.CharField(max_length = 6)
    reccomendedBy = models.CharField(max_length = 6)
    reward = models.ForeignKey(Rewards)
    dateUsed = models.DateField(blank = True, null = True)

class RewardHistory(models.Model):
    csID = models.CharField(max_length = 6)
    reccomendedBy = models.CharField(max_length = 6)
    reward = models.ForeignKey(Rewards)
    dateUsed = models.DateField(blank = True, null = True)

class UniqueBusinessHistory(models.Model):
    csID = models.CharField(max_length = 6)
    reward = models.ForeignKey(Rewards)
    dateUsed = models.DateField(blank = True, null = True)
    businessID = models.CharField(max_length = 40)


#######################################################
######              MISC                         ######
#######################################################

class MerchantInfoForm(models.Model):
    merchantID = models.CharField(max_length = 50)
    businessName = models.CharField(max_length = 50)
    amexSES = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    zipCode = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    phoneNumber = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    signerName = models.CharField(max_length = 50)
    signerTitle = models.CharField(max_length = 50)
    date = models.DateField()
    
    
class ContactUsForm(models.Model):
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 60)
    message = models.CharField(max_length = 400)
    

    

     
