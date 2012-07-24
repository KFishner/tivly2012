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

class FBFriends(models.Model):
    name = models.CharField(max_length = 300)
    friend_fb_id = models.BigIntegerField()
    user = models.ForeignKey(FBUser)

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
    
class Rewards(models.Model):
    rID = models.CharField(max_length = 6)
    appID = models.CharField(max_length = 40)
    businessID = models.CharField(max_length = 40)
    description = models.CharField(max_length = 300)
    pointsNeeded = models.IntegerField()

#==================USER SPECIFIC=======================#
    
class CardSpringUser(models.Model):
    csID = models.CharField(max_length = 6)
    points = models.IntegerField()
    fbID = models.BigIntegerField(blank = True, null = True)
    TwitID = models.BigIntegerField(blank = True, null = True)
    dateJoined = models.DateField(blank = True, null = True)

    
class Cards(models.Model):
    csID = models.CharField(max_length = 6)
    token = models.CharField(max_length = 30)
    last4 = models.IntegerField()
    expDate = models.CharField(max_length =20 )
    cardType = models.CharField(max_length = 20)
    typeString = models.CharField(max_length = 20)
    
class UserPoints(models.Model):
    csID = models.CharField(max_length = 6)
    businessID = models.CharField(max_length = 40)
    points = models.IntegerField()
    visits = models.IntegerField()
    
class MyRecommendations(models.Model):
    csID = models.CharField(max_length = 6)
    appID = models.CharField(max_length = 40)
    businessID = models.CharField(max_length = 40)
    rID = models.CharField(max_length = 6)
    recID = models.CharField(max_length = 30)
    reccsID = models.CharField(max_length = 6, blank = True, null = True)
    dateGiven= models.DateField(blank = True, null = True)


class MyRewards(models.Model):
    csID = models.CharField(max_length = 6)
    reccomendedBy = models.CharField(max_length = 6)
    reward = models.ForeignKey(Rewards)
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
class ContactUsForm(models.Model):
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 60)
    message = models.CharField(max_length = 400)
    

    

     
