# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CardSpringUser.dateJoined'
        db.add_column('Tivly_cardspringuser', 'dateJoined',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Transaction.date'
        db.alter_column('Tivly_transaction', 'date', self.gf('django.db.models.fields.DateField')(null=True))
        # Adding field 'MyRewards.dateUsed'
        db.add_column('Tivly_myrewards', 'dateUsed',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'MyRecommendations.dateGiven'
        db.add_column('Tivly_myrecommendations', 'dateGiven',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CardSpringUser.dateJoined'
        db.delete_column('Tivly_cardspringuser', 'dateJoined')


        # User chose to not deal with backwards NULL issues for 'Transaction.date'
        raise RuntimeError("Cannot reverse this migration. 'Transaction.date' and its values cannot be restored.")
        # Deleting field 'MyRewards.dateUsed'
        db.delete_column('Tivly_myrewards', 'dateUsed')

        # Deleting field 'MyRecommendations.dateGiven'
        db.delete_column('Tivly_myrecommendations', 'dateGiven')


    models = {
        'Tivly.businesses': {
            'Meta': {'object_name': 'Businesses'},
            'businessID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'businessName': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'fridayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mondayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pictureLocation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'saturdayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sundayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'thursdayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tuesdayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'wednesdayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'zipCode': ('django.db.models.fields.IntegerField', [], {})
        },
        'Tivly.cards': {
            'Meta': {'object_name': 'Cards'},
            'cardType': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'expDate': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last4': ('django.db.models.fields.IntegerField', [], {}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'typeString': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'Tivly.cardspringuser': {
            'Meta': {'object_name': 'CardSpringUser'},
            'TwitID': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'dateJoined': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fbID': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {})
        },
        'Tivly.fbaccesstokens': {
            'Meta': {'object_name': 'FBAccessTokens'},
            'accessToken': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'date_created': ('django.db.models.fields.DateField', [], {}),
            'expiration_accessToken': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Tivly.FBUser']"})
        },
        'Tivly.fbfriends': {
            'Meta': {'object_name': 'FBFriends'},
            'friend_fb_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Tivly.FBUser']"})
        },
        'Tivly.fbuser': {
            'Meta': {'object_name': 'FBUser'},
            'date_joined': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'Tivly.myrecommendations': {
            'Meta': {'object_name': 'MyRecommendations'},
            'appID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'businessID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'dateGiven': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'recID': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'reccsID': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'})
        },
        'Tivly.myrewards': {
            'Meta': {'object_name': 'MyRewards'},
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'dateUsed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reccomendedBy': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'reward': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Tivly.Rewards']"}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'Tivly.rewards': {
            'Meta': {'object_name': 'Rewards'},
            'appID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'businessID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pointsNeeded': ('django.db.models.fields.IntegerField', [], {}),
            'rID': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'Tivly.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'appID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'businessID': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'card_token': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'store_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'Tivly.userpoints': {
            'Meta': {'object_name': 'UserPoints'},
            'businessID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'visits': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['Tivly']